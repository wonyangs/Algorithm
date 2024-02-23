def word_clock(h, m):
    numbers_to_words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two",
        23: "twenty three", 24: "twenty four", 25: "twenty five",
        26: "twenty six", 27: "twenty seven", 28: "twenty eight",
        29: "twenty nine", 30: "thirty"
    }

    if m == 0:
        return f"{numbers_to_words[h]} o' clock"
    elif m <= 30:
        minute_word = "minute" if m == 1 else "minutes"
        if m == 15:
            return f"quarter past {numbers_to_words[h]}"
        elif m == 30:
            return f"half past {numbers_to_words[h]}"
        else:
            return f"{numbers_to_words[m]} {minute_word} past {numbers_to_words[h]}"
    else:
        minute_word = "minute" if (60 - m) == 1 else "minutes"
        next_hour = h + 1 if h < 12 else 1
        if m == 45:
            return f"quarter to {numbers_to_words[next_hour]}"
        else:
            return f"{numbers_to_words[60 - m]} {minute_word} to {numbers_to_words[next_hour]}"

print(word_clock(int(input()), int(input())))
