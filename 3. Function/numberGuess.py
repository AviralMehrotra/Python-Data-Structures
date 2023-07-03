import random
GUESS= random.randint(0,100)

def check_if_correct(input):
    if input == GUESS:
        print("\n\n Great guess! You Won\n\n")
        exit()
    elif input< GUESS:
        print("\n Try something Higher!")
    else:
        print("\n Try something Lower!")


print(""" ____  __ __  ____   ____   ____     _____  _   _  ____     __  _  __ __  __  __ _____  ____ _____ 
/ (_,`|  |  || ===| (_ (_` (_ (_`   |_   _|| |_| || ===|   |  \| ||  |  ||  \/  || () )| ===|| () )
\____) \___/ |____|.__)__).__)__)     |_|  |_| |_||____|   |_|\__| \___/ |_|\/|_||_()_)|____||_|\_\ """)

# print(GUESS)

difficulty= input("\n Please enter your difficulty 'easy' or 'hard': ").lower()
if difficulty=="easy":
    i=10        
elif difficulty=="hard":
    i=5        
else: 
    print(" Invalid Response")
    exit()

for j in range(i):
    user_input= int(input(f"\n Attempt No. {j+1}\n Enter your guess (0-100): "))
    check_if_correct(user_input)

print("\n\n You ran out of guesses! Your lost! \n\n")