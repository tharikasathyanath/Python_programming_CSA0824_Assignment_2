# Q3 - Vehicle Registration Validator

def normalise(text):
    text = text.upper()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[0:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if not reg[4:-4].isalpha():
        return False

    if len(reg[4:-4]) not in (1, 2):
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_number(reg):
    if is_valid(reg):
        return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]
    else:
        return "INVALID"


numbers = [
    "tn 09 ab 1234",
    "TN-09-AB-1234",
    "Tn09Ab1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB"
]

for number in numbers:
    reg = normalise(number)

    if is_valid(reg):
        print(number, "->", reg, "->", format_number(reg))
    else:
        print(number, "->", reg, "-> INVALID")