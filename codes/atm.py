atm_pin=int(input('enter ayour pin: '))
fixed_pin=2003
menu=['withdraw','balanace enquiry','fast cash']
if fixed_pin==atm_pin:
    print(menu)
    select=input('select the menu: ')
    if select=='withdraw':
        amount=int(input('enter the amount: '))
        if amount>0:
            print('collect your cash')
        else:
            print('amount not available')
    elif select=='balance enquiry':
        print('your available amount is: ')
    elif select=='fast cash':
        amount=int(input('enter the amount: '))
        if amount>0:
            print('collect your cash')
        else:
            print('amount not available')
else:
    print('your enetered pin wrong')
        
