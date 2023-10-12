num = input("Enter a number: ")

while num:
    try:
        if num == "Hello":
            raise TypeError
        num = int(num)
        num = 10 / num
        print(f"10 divided by your number is: {num}")
    except ValueError:
        print(f"{num} is not a number.")
    except ZeroDivisionError:
        print("Please don't divide by 0")
    except:
        print("A thing happened...")
    num = input("Enter a number: ")