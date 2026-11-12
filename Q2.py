# Q2 - OTP Verification

correct_otp = "1234"
attempts = 0

print("OTP Verification Using While Loop")

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry. Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP Verified Successfully!")
        break

    else:
        print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")


print("\nOTP Verification Using For Loop")

for attempt in range(3):
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry. Try again.")
        continue

    if otp == correct_otp:
        print("OTP Verified Successfully!")
        break

    print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")


# Demonstration of pass
if attempts == 0:
    pass