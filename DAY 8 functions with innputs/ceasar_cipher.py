import string

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabets = list(string.ascii_lowercase)

direction = input("Type encode to encrpt and decode to decrypt\n")
text = input("Type you message.....\n").lower()
shift = int(input("Type the shift number: \n"))


def encrypt(text):
    encrypted_message = ""

    for i in text:
        position = alphabets.index(i)
        new_position = (position + shift) %len(alphabets)
        new_char = alphabets[new_position]
        encrypted_message += new_char

    return encrypted_message    

result = encrypt(text)


def decrypt(text):
    decrypted_message = ""

    for i in text:
        position = alphabets.index(i)
        new_position = (position - shift)%len(alphabets)
        new_char = alphabets[new_position]
        decrypted_message += new_char

    return decrypted_message  

result2 = decrypt(text)

if direction == "encode":
    print(result)
elif direction == "decode":
    print(result2)
else:
    print("choose either to encode or decode")


