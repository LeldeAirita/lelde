import random

computer_number = random.randint(1, 100)
user_guess = input('Uzmini skaitli starp 1 un 100:')

if user_guess == computer_number:
    print('Precīzi, tu uzminēji!')
elif user_guess < computer_number:
    print('Vairāk')   
elif user_guess > computer_number:
    print('Mazāk')  
else:
    print('Notika kļūda!') 

    import random

computer_number = random.randint(1, 100)
continue_game = True
user_guesses = []

while(True):
    user_guess = int(input('Uzmini skaitli starp 1 un 100: '))
    user_guesses.append(user_guess)

    if user_guess == computer_number:
        print('Precīzi, tu uzminēji!')
        break
    elif user_guess < computer_number:
        print('Vairāk')
    elif user_guess > computer_number:
        print('Mazāk')
    else:
        print('Notika kļūda!')

print('Game over!')
