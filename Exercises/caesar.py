def main():
    try:
        key = int(input("enter a key: "))
    except:
        print("input must be valid non-negative number")
        return None
    
    if key < 0:
        print("input must be non-negative number")
        return None
    plaintext = input("Plaintext: ")
    n = len(plaintext)
    chiphertext = []
    for i in range(n):
        if plaintext[i].isalpha():
            base = "A" if plaintext[i].isupper() else "a"
            temp_value = ord(plaintext[i]) - ord(base)
            shift_value = temp_value + key
            value_after_rotate = shift_value % 26
            ascii_value = value_after_rotate + ord(base)
            letter = chr(ascii_value)
            chiphertext.append(letter)
            
        else:
            chiphertext.append(plaintext[i])
    
    str_chiphertext = "".join(i for i in chiphertext)
    print(str_chiphertext)

       
main()