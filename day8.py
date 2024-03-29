#CAESER CIPHER
direction=input("Type 'encode' to encrypt OR Type 'decode' to decrypt\n")
text=input("Enter the message\n")
shift=int(input("Type shift number\n"))

def encode(text, shift):
    result = ""
    for i in range(len(text)):
        char_code = ord(text[i])
        shifted_code = char_code + shift
        result += chr(shifted_code)
    return result

def decode(text, shift):
    result = ""
    for i in range(len(text)):
        char_code = ord(text[i])
        shifted_code = char_code - shift
        result += chr(shifted_code)
    return result



if direction=="encode":
    print("Encrypted Message is : ",encode(text,shift))
elif direction=="decode":
    print("Decrypted Message is :",decode(text,shift))
else:
    print("error")
        
        

    
