''' TIP CALCULATOR PROJECT
If the bill was $150,00 split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 '''

loop = True

while loop:
    print('---------- TIP CALCULATOR ----------')
    print('Welcome!')
    print('1 - Calculate tip')
    print('2 - Exit')
    print('Choose an option')
    choice = int(input('What do you want to do? '))

    if(choice == 1):
        bill = float(input('What was the total of the bill? '))
        tip = int(input('What percentage tip would you like to give? '))
        peopleAmount = int(input('How many people to slipt the bill? '))

        if(tip <= bill):
            totalTip = bill * (tip / 100)
            tipPerPerson = totalTip / peopleAmount
            totalBillPerPerson = (totalTip + bill) / peopleAmount

            print('----------- FINAL RESULT -----------')
            print('The total of the tip is ${:.2f}'.format(totalTip))
            print('The total of the tip per person is ${:.2f}'.format(tipPerPerson))
            print('Each person should pay a total of ${:.2f}'.format(totalBillPerPerson))
            input('Press anywhere to continue...')
        else:
            print('The total of the tip cannot be bigger than the total of the bill')
            input('Press anywhere to continue...')

    elif choice == 2:
        loop = False
        print('Exiting...')
    else:
        print('This option is not available. Choose one of the options displayed to continue. ')
        input('Press anywhere to continue...')