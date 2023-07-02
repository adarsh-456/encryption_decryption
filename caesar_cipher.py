alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo="""


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
process="yes"
mapped = {}
while process=="yes" :
    
    direction =input("Type encode to incrypt, Type decode to decrypt:\n")
    
    text=input("type your mesage:\n").lower()

    shift=input("type the shift number:\n")
    
    mapped[text]=shift
    print(mapped)
    shift=int(shift)
    shift=shift % 26      

    def caesar(start_text, shift_amount, cipher_direction):
        end_text=""
        if cipher_direction=="decode":
            shift_amount*= -1
        for letter in start_text:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position = (position + shift_amount)%len(alphabet)
                end_text +=alphabet[new_position]
            else:
                end_text+=letter
        print(f"Here's the result :{end_text}")             
          
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)       
    process=input("If you want continue the process of Type 'yes' or if you want you exit type 'no' :\n")
    
        
