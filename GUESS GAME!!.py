secret_number = 7

user_permission = input('do you want to play our game?\n Please type (Y/N): ').lower()
guess_count = 0
guess_limit = 3
if user_permission == 'y'  :
    while guess_count < guess_limit :
        guess_number = int(input('Try to guess our number: '))
        guess_count += 1
        if guess_number == secret_number:
            print('Thats correct')
            exit()
        elif (guess_number - secret_number) == 1:
            print('you ar close to the number by 1 number')
    else :
        print('sorry you lost!!')

else :
    print('please come back next time')