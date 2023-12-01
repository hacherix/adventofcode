import re

def main():
    with open("2023/day_one.input") as input_file:
        input_content = input_file.read()

    digits = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for digit_sr, digit_num in digits.items():
        input_content = re.sub(digit_sr, digit_sr + digit_num + digit_sr, input_content)

    digits_numbers = "|".join(digits.values())

    res = sum([int(values[0] + values[-1])
               for values in [re.findall(rf"{digits_numbers}", word)
                              for word in input_content.split()]])

    print(res)


if __name__ == "__main__":
    # 56397
    # 55701
    main()
