import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download Speed in Mbps: ", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload Speed in Mbps: ", up_speed)

    ping = test.results.ping
    print("Ping: ", ping)
Speed_Test()
while True:
        try:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            operant = input("Which operation do you want to perform? (+, -, * or /): ")
            if operant == "+" or operant == "-" or operant == "*" or operant == "/":
                if operant == "+":
                    num3 = num1 + num2
                    print("The sum is:", num3)
                if operant == "-":
                    num3 = num1 - num2
                    print("The subtraction is:", num3)
                if operant == "*":
                    num3 = num1 * num2
                    print("The multiplication is:", num3)
                if operant == "/":
                    num3 = num1 / num2
                    print("The division is:", num3)

            break
        except ValueError:
            print("That's not a number")
        except ZeroDivisionError:
            print("You can't divide by zero you IDIOT.🙄")


