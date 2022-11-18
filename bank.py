print('Welcome To Rakshith Bank Of India')
restart = 'y'
chances = 3
balance = 100000.55
while chances >= 0 :
    pin = int (input('please enter your 4 digit pin:'))
    if pin == (5798) :
        print ('you entered pin correctly\n')
        while restart not in ('n','N','no','NO'):
            print ('please press 1 for your balance\n')
            print ('please press 2 make a withdraw\n')
            print ('please press 3 to credit money \n')
            print ('please press 4 to return card\n')
            option = int(input('what is option would you like to choose?'))
            if option == 1 :
                print('Your Balance is ', balance , '\n' )
                input ('would you like to go back ?')
                if ('n','N','no','NO'):
                    print('Thank You')
                    break
            elif option == 2:

                withdrawl = float(input('How much money would you like to withdraw? \n A$100/A$200/A$$500'))
                if withdrawl in [100,200,500]:
                    balance = balance - withdrawl
                    print('\nYour Balance is Now ', balance)
                    input('would you like to go back ?')
                    if  ('n', 'N', 'no', 'NO'):
                        print('Thank You')
                        break
            elif option == 3:
                pay_in = float(input('How Much Would You Like To pay in ?'))
                balance = balance + pay_in
                print('\nYour Balance is Now ', balance)
                input('would you like to go back ?')
                if  ('n', 'N', 'no', 'NO'):
                    print('Thank You')
                    break
            elif option  == 4:

                print("please don't forget to take the card.....\n")
                print(' THANKS FOR VISITING')
                break
            else:
                 print('please choose a correct option ')

    elif pin!=('5798'):
        print('incorrect pin')
        chances = chances - 1
        if chances == 0 :
            print ('\n No More Tries')
            break

