def bit_operations(A, B):
    int_A = int(A, 2)
    int_B = int(B, 2)
    
    and_result = int_A & int_B
    or_result = int_A | int_B
    xor_result = int_A ^ int_B
    not_A_result = ~int_A & ((1 << len(A)) - 1)
    not_B_result = ~int_B & ((1 << len(B)) - 1)
    
    and_result_str = f"{and_result:0{len(A)}b}"
    or_result_str = f"{or_result:0{len(A)}b}"
    xor_result_str = f"{xor_result:0{len(A)}b}"
    not_A_result_str = f"{not_A_result:0{len(A)}b}"
    not_B_result_str = f"{not_B_result:0{len(B)}b}"
    
    print(and_result_str)
    print(or_result_str)
    print(xor_result_str)
    print(not_A_result_str)
    print(not_B_result_str)


A = input().strip()
B = input().strip()
bit_operations(A, B)
