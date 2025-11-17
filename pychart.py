def users(self):
    try:
        total_users = int(self.total_users_button.text().replace(",", "").strip() or 0)
        users_remaining = int(self.users_remaining_button.text().replace(",", "").strip() or 0)
        prize_text = float(self.prize_button.text().replace(",", "").replace("+", "").strip() or 0)

        # ✅ Read all 6 card values
        cards = [
            self.button1.text().strip(),
            self.button2.text().strip(),
            self.button3.text().strip(),
            self.button4.text().strip(),
            self.button5.text().strip(),
            self.button6.text().strip()
        ]

        # ✅ Initialize users_remaining properly
        if users_remaining == 0:
            users_remaining = total_users

        # ✅ Stop when no users left
        if users_remaining <= 0:
            print("🚫 All users finished. No more deductions.")
            return

        # ✅ If all cards = 5 or 6 → no cashout
        if all(c == "5" for c in cards) or all(c == "6" for c in cards):
            print("😶 No player cashed out.")
            return
        # ✅ Pick random users to cash out
        users_cashed_out = random.randint(1, max(1, users_remaining // 2))
        remaining_users = max(0, users_remaining - users_cashed_out)
        # ✅ Update UI
        if prize_text >= 1:
            print(f"💨 {users_cashed_out} users cashed out. {remaining_users} remaining.")
            self.users_remaining_button.setText(f"{remaining_users:,}")

    except Exception as e:
        print("Users() error:", e)
