'''This code implements a Caesar cipher encryption and decryption program that takes user inputs for the choice 
(encrypt or decrypt), secret message, and shift key. 
It repeatedly executes the cipher based on user inputs until the user chooses to stop running the program.'''

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

running = True


def caesarCipher(text, key, choice):
    if choice == "0":
        key *= -1
    output = ""
    x = len(text)
    for i in range(0, x):
        if text[i] in alphabets:
            idx = alphabets.index(text[i])
            output += alphabets[idx+key]
        else:
            output += text[i]
    print(f"The secret message is: {output}")


# def encrypt(text, key):
#     output=""
#     x= len(text)
#     for i in range(0, x):
#         if text[i] == " ":
#             output+= " "
#         else:
#             idx= alphabets.index(text[i])
#             output+=alphabets[idx+key]
#     return output
# def decrypt(text, key):
#     output=""
#     x= len(text)
#     for i in range(0, x):
#         if text[i] == " ":
#             output+= " "
#         else:
#             idx= alphabets.index(text[i])
#             output+=alphabets[idx-key]
#     return output
# def startProcess(choice, text, key):
    # if choice == "1":
    #     encrypt(text, key)
    # else:
    #     decrypt(text, key)
    #        pass
while running:
    choice = input(
        "Enter your choice whether you want to encrypt(1) or decrypt(0): ")
    text = input("\nEnter your secret message: ").lower()
    key = int(input("\nEnter your shift key: "))
    if key >= 26:
        key %= 26
    caesarCipher(text, key, choice)
    again = input("\nRun again? ").lower()
    if again == "no":
        running = False
    elif again == "yes":
        continue
    else:
        print("I could not understand...\n")
