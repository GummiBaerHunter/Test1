# Caesar Cipher Encrypt
def caesar_cipher_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    print(result)
    return result


# Caesar Cipher Decrypt
def caesar_cipher_decrypt(text, shift):
    # To decrypt, we reverse the shift by using -shift
    return caesar_cipher_encrypt(text, -shift)

# Example usage
encrypted = caesar_cipher_encrypt(input('Bitte gib ein Text ein:'),int(input("Bitte gib ein Key:")))
print("Encrypted:", encrypted)

#decrypted = caesar_cipher_decrypt(input,encrypted,input-3)
#print("Decrypted:", decrypted)

