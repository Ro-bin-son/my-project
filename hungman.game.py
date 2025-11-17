# --- helper methods for prize logic (place inside MainWindow) ---

def _safe_int(self, widget_text, default=0):
    try:
        return int(str(widget_text).replace(",", "").replace("+", "").strip() or default)
    except Exception:
        return default

def _safe_float(self, widget_text, default=0.0):
    try:
        return float(str(widget_text).replace(",", "").replace("+", "").strip() or default)
    except Exception:
        return default

def _read_cards(self):
    return [
        self.button1.text().strip(),
        self.button2.text().strip(),
        self.button3.text().strip(),
        self.button4.text().strip(),
        self.button5.text().strip(),
        self.button6.text().strip(),
    ]

def _all_cards_equal(self, cards):
    # returns (True, value) if all equal (and non-empty), else (False, None)
    if not cards or any(c == "" for c in cards):
        return False, None
    first = cards[0]
    if all(c == first for c in cards):
        return True, first
    return False, None

def _any_upper_or_lower_match(self, cards):
    # True if either first three equal OR last three equal (partial matches)
    return (cards[0] == cards[1] == cards[2] and cards[0] != "") or \
           (cards[3] == cards[4] == cards[5] and cards[3] != "")

def _format_prize_text(self, value):
    # Always format with sign when positive (you said "always show +")
    if value < 0:
        return f"{value:.2f}"
    else:
        return f"+{value:.2f}"

def _apply_prize_style(self, value):
    # Centralized UI styling (one place)
    color = "red" if value < 0 else "black" if value == 0 else "blue"
    self.prize_button.setStyleSheet(
        f"background-color: white; font-size: 22px; color: {color}; border-radius: 10px;"
    )

# --- refactored prize_determinant ---
def prize_determinant(self):
    """
    Read the current UI state (cards, counts, current prize),
    compute the new prize value according to rules, update UI.
    """
    try:
        # READ (single responsibility: gather inputs)
        cards = self._read_cards()
        matchedL = self._safe_int(self.num_of_matched_buttonsL.text(), 0)
        matchedU = self._safe_int(self.num_of_matched_buttons.text(), 0)
        all_matched_count = self._safe_int(self.all_matched_button.text(), 0)
        current_prize = self._safe_float(self.prize_button.text(), 0.0)

        all_equal, val = self._all_cards_equal(cards)

        # DECIDE (single responsibility: compute prize change)
        new_prize = current_prize  # default: no change

        if all_equal:
            # all 6 equal -> special handling by card value
            if val in ("1", "2", "3", "4"):
                bonus = (matchedL + (matchedU + 1))
                # Example: different multipliers per card value (these were in your logic)
                multipliers = {"1": 0.008, "3": 0.007, "2": 0.005, "4": 0.009}
                m = multipliers.get(val, 0.0)
                new_prize = (current_prize + bonus + (250 if val == "4" else 0)) * m
            elif val == "5":
                # your intentional behavior: sets prize to zero
                new_prize = 0.0
            elif val == "6":
                # double the current prize (your intentional behavior)
                new_prize = current_prize + current_prize
        elif self._any_upper_or_lower_match(cards) and not all_equal:
            # partial match (either top 3 or bottom 3)
            prize_value = self._safe_float(self.prize_button.text(), 0.0)
            top_card = cards[0]  # use top card as rule source
            if top_card in ("1", "3"):
                new_prize = prize_value - 3
            elif top_card == "6":
                new_prize = prize_value + 1
            elif top_card == "2":
                new_prize = prize_value + 0.01
            else:
                new_prize = prize_value  # no change for other values

        # If you want to enforce a minimum or zero-out late-game negative:
        # if self.remaining_attempts_button.text().strip() == "0" and new_prize < 0:
        #     new_prize = 0.0

        # APPLY (single responsibility: update UI)
        self.prize_button.setText(self._format_prize_text(new_prize))
        self._apply_prize_style(new_prize)

    except Exception as e:
        # Single place for logging errors
        print("prize_determinant error:", e)
