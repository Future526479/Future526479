class Monthly_Payment:
    # Months
    monthly_payment = input('How many expenses (from 1 to 10) are required from you to be paid for(Monthly), besides tax: ')
    if monthly_payment == '1':
        Day = input('Date(Pay day): ')
        Name = input('Name: ')
        Money_1 = float(float(input('Amount: ')))
        full_price = Money_1 * 12
        print(full_price)

        total = open('total_monthly_pay_for_12_month_Period.csv', 'a')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day {Day}: Description {Name}: Amount {Money_1}'))

    if monthly_payment == '2':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))
        full_price = (Money1+Money2)*12
        print(full_price)

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}'))

    if monthly_payment == '3':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}'))

    if monthly_payment == '4':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))

        Day4 = input('Date(Pay day): ')
        Name4 = input('Name: ')
        Money4 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3+Money4)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}\n'))
        Monthly.write(str(f'Day: {Day4}; Description: {Name4}; Amount: {Money4}'))

    if monthly_payment == '5':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))

        Day4 = input('Date(Pay day): ')
        Name4 = input('Name: ')
        Money4 = float(input('Amount: '))

        Day5 = input('Date(Pay day): ')
        Name5 = input('Name: ')
        Money5 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3+Money4+Money5)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}\n'))
        Monthly.write(str(f'Day: {Day4}; Description: {Name4}; Amount: {Money4}\n'))
        Monthly.write(str(f'Day: {Day5}; Description: {Name5}; Amount: {Money5}'))

    if monthly_payment == '6':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))

        Day4 = input('Date(Pay day): ')
        Name4 = input('Name: ')
        Money4 = float(input('Amount: '))

        Day5 = input('Date(Pay day): ')
        Name5 = input('Name: ')
        Money5 = float(input('Amount: '))

        Day6 = input('Date(Pay day): ')
        Name6 = input('Name: ')
        Money6 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3+Money4+Money5+Money6)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}\n'))
        Monthly.write(str(f'Day: {Day4}; Description: {Name4}; Amount: {Money4}\n'))
        Monthly.write(str(f'Day: {Day5}; Description: {Name5}; Amount: {Money5}\n'))
        Monthly.write(str(f'Day: {Day6}; Description: {Name6}; Amount: {Money6}'))

    if monthly_payment == '7':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))

        Day4 = input('Date(Pay day): ')
        Name4 = input('Name: ')
        Money4 = float(input('Amount: '))

        Day5 = input('Date(Pay day): ')
        Name5 = input('Name: ')
        Money5 = float(input('Amount: '))

        Day6 = input('Date(Pay day): ')
        Name6 = input('Name: ')
        Money6 = float(input('Amount: '))

        Day7 = input('Date(Pay day): ')
        Name7 = input('Name: ')
        Money7 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3+Money4+Money5+Money6+Money7)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}\n'))
        Monthly.write(str(f'Day: {Day4}; Description: {Name4}; Amount: {Money4}\n'))
        Monthly.write(str(f'Day: {Day5}; Description: {Name5}; Amount: {Money5}\n'))
        Monthly.write(str(f'Day: {Day6}; Description: {Name6}; Amount: {Money6}\n'))
        Monthly.write(str(f'Day: {Day7}; Description: {Name7}; Amount: {Money7}'))

    if monthly_payment == '8':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))

        Day4 = input('Date(Pay day): ')
        Name4 = input('Name: ')
        Money4 = float(input('Amount: '))

        Day5 = input('Date(Pay day): ')
        Name5 = input('Name: ')
        Money5 = float(input('Amount: '))

        Day6 = input('Date(Pay day): ')
        Name6 = input('Name: ')
        Money6 = float(input('Amount: '))

        Day7 = input('Date(Pay day): ')
        Name7 = input('Name: ')
        Money7 = float(input('Amount: '))

        Day8 = input('Date(Pay day): ')
        Name8 = input('Name: ')
        Money8 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3+Money4+Money5+Money6+Money7+Money8)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}\n'))
        Monthly.write(str(f'Day: {Day4}; Description: {Name4}; Amount: {Money4}\n'))
        Monthly.write(str(f'Day: {Day5}; Description: {Name5}; Amount: {Money5}\n'))
        Monthly.write(str(f'Day: {Day6}; Description: {Name6}; Amount: {Money6}\n'))
        Monthly.write(str(f'Day: {Day7}; Description: {Name7}; Amount: {Money7}\n'))
        Monthly.write(str(f'Day: {Day8}; Description: {Name8}; Amount: {Money8}'))

    if monthly_payment == '9':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))

        Day4 = input('Date(Pay day): ')
        Name4 = input('Name: ')
        Money4 = float(input('Amount: '))

        Day5 = input('Date(Pay day): ')
        Name5 = input('Name: ')
        Money5 = float(input('Amount: '))

        Day6 = input('Date(Pay day): ')
        Name6 = input('Name: ')
        Money6 = float(input('Amount: '))

        Day7 = input('Date(Pay day): ')
        Name7 = input('Name: ')
        Money7 = float(input('Amount: '))

        Day8 = input('Date(Pay day): ')
        Name8 = input('Name: ')
        Money8 = float(input('Amount: '))

        Day9 = input('Date(Pay day): ')
        Name9 = input('Name: ')
        Money9 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3+Money4+Money5+Money6+Money7+Money8+Money9)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}\n'))
        Monthly.write(str(f'Day: {Day4}; Description: {Name4}; Amount: {Money4}\n'))
        Monthly.write(str(f'Day: {Day5}; Description: {Name5}; Amount: {Money5}\n'))
        Monthly.write(str(f'Day: {Day6}; Description: {Name6}; Amount: {Money6}\n'))
        Monthly.write(str(f'Day: {Day7}; Description: {Name7}; Amount: {Money7}\n'))
        Monthly.write(str(f'Day: {Day8}; Description: {Name8}; Amount: {Money8}\n'))
        Monthly.write(str(f'Day: {Day9}; Description: {Name9}; Amount: {Money9}'))

    if monthly_payment == '10':
        Day1 = input('Date(Pay day): ')
        Name1 = input('Name: ')
        Money1 = float(input('Amount: '))

        Day2 = input('Date(Pay day): ')
        Name2 = input('Name: ')
        Money2 = float(input('Amount: '))

        Day3 = input('Date(Pay day): ')
        Name3 = input('Name: ')
        Money3 = float(input('Amount: '))

        Day4 = input('Date(Pay day): ')
        Name4 = input('Name: ')
        Money4 = float(input('Amount: '))

        Day5 = input('Date(Pay day): ')
        Name5 = input('Name: ')
        Money5 = float(input('Amount: '))

        Day6 = input('Date(Pay day): ')
        Name6 = input('Name: ')
        Money6 = float(input('Amount: '))
        
        Day7 = input('Date(Pay day): ')
        Name7 = input('Name: ')
        Money7 = float(input('Amount: '))

        Day8 = input('Date(Pay day): ')
        Name8 = input('Name: ')
        Money8 = float(input('Amount: '))

        Day9 = input('Date(Pay day): ')
        Name9 = input('Name: ')
        Money9 = float(input('Amount: '))

        Day10 = input('Date(Pay day): ')
        Name10 = input('Name: ')
        Money10 = float(input('Amount: '))
        full_price = (Money1+Money2+Money3+Money4+Money5+Money6+Money7+Money8+Money9+Money10)*12

        total = open('total_monthly_pay_for_12_month_Period.csv', 'w')
        total.write(str(full_price))

        Monthly = open('Monthly_required_payment.csv', 'a')
        Monthly.write(str(f'Day: {Day1}; Description: {Name1}; Amount: {Money1}\n'))
        Monthly.write(str(f'Day: {Day2}; Description: {Name2}; Amount: {Money2}\n'))
        Monthly.write(str(f'Day: {Day3}; Description: {Name3}; Amount: {Money3}\n'))
        Monthly.write(str(f'Day: {Day4}; Description: {Name4}; Amount: {Money4}\n'))
        Monthly.write(str(f'Day: {Day5}; Description: {Name5}; Amount: {Money5}\n'))
        Monthly.write(str(f'Day: {Day6}; Description: {Name6}; Amount: {Money6}\n'))
        Monthly.write(str(f'Day: {Day7}; Description: {Name7}; Amount: {Money7}\n'))
        Monthly.write(str(f'Day: {Day8}; Description: {Name8}; Amount: {Money8}\n'))
        Monthly.write(str(f'Day: {Day9}; Description: {Name9}; Amount: {Money9}\n'))
        Monthly.write(str(f'Day: {Day10}; Description: {Name10}; Amount: {Money10}'))
