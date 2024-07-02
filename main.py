#task-01 implement Caesar Cipher encryption and decryption using python program

#function encryption
def encryption(plaintext,s):
    res = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        #  uppercase characters
        if (char.isupper()):
            res += chr((ord(char) + s - 65) % 26 + 65)

        # lowercase characters
        else:
            res += chr((ord(char) + s - 97) % 26 + 97)

    return res

#function decryption
def decryption(ciphertext,s):
    res = ""

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        #  uppercase characters
        if (char.isupper()):
            res += chr((ord(char) - s - 65) % 26 + 65)

        # lowercase characters
        else:
            res += chr((ord(char) - s - 97) % 26 + 97)

    return res
c=int(input("num of counter:"))
while c!=0:
    chose=str(input("Enter Type enc or dec : "))
    if chose == "enc":
        Message = str(input("Enter PlainText:"))
        shift_num = int(input("Enter Shift num:"))
        print("CipherText is : " + encryption(Message, shift_num))
    elif chose=="dec":
        Message = str(input("Enter cipherText:"))
        shift_num = int(input("Enter Shift num:"))
        print("PlainText is : " + decryption(Message, shift_num))
    else:
        break
    c=c-1