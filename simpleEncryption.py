message = "I am a secret message"
encryptedMessage = ""
decryptedMessage = ""
decryptionKey = 10


for letter in message:
    encryptedMessage += chr(ord(letter)+decryptionKey)


for letter in encryptedMessage:
    decryptedMessage += chr(ord(letter)-decryptionKey)

print("Original message:     " + message + "\n")
print("Encrypted message:    " + encryptedMessage + "\n")
print("Decrypted message:    " + decryptedMessage + "\n")