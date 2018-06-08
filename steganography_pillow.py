from PIL import Image
import base64

im = Image.open('anonymous.png')

msg = input("Message: ")
x = int(input("X axis placement: "))
y = int(input ("Y axis placement: "))

encryptedMessage = base64.b64encode(str.encode(msg))


# if you want to work with it
image = im.load()


iterator = 0

for letter in encryptedMessage:
    if not type(int(letter)):
        image[x, y + iterator] = (ord(letter), ord(letter), ord(letter))
        print("x:", x, "y:", y + iterator)
    else:
        image[x, y + iterator] = (letter, letter, letter)
        print("x:", x, "y:", y + iterator)

    iterator = iterator + 1

im.save("anonymous.png", "png")
im.show()
