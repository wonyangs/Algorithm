def min_distance_to_type_password(start_char):
    password = "ILOVEYONSEI"
    current_index = ord(start_char) - ord('A') + 1
    
    total_distance = 0
    for char in password:
        target_index = ord(char) - ord('A') + 1
        total_distance += abs(target_index - current_index)
        current_index = target_index
    
    return total_distance

print(min_distance_to_type_password(input()))
