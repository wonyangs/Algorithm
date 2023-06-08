while True:
    try:
        name = input()
        corrected_name = ""
        for char in name:
            if char == 'i':
                corrected_name += 'e'
            elif char == 'e':
                corrected_name += 'i'
            elif char == 'I':
                corrected_name += 'E'
            elif char == 'E':
                corrected_name += 'I'
            else:
                corrected_name += char
        print(corrected_name)
    except EOFError:
        break
