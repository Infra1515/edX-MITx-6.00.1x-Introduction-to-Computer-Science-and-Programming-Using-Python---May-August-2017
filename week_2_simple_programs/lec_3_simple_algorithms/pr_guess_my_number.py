low_guess = 0
high_guess = 100
ans = (low_guess + high_guess) // 2
usr = None
print('Please think of a number between 0 and 100!')
while usr != 'c':

    print('Is your secret number', ans, '?')
    print("Enter 'h' to indicate the guess is too high.",end =' ')
    print("Enter 'l' to indicate the guess is too low.", end=" ")
    print("Enter 'c' to indicate I guessed correctly.", end = " ")
    usr = input()

    if usr == 'l':
        low_guess = ans
    elif usr == 'h':
        high_guess = ans
    elif usr == 'c':
        print('Game over. Your secret number was:', ans)
    else:
        print('Sorry, I did not understand your input.')

    ans = (high_guess + low_guess) // 2
