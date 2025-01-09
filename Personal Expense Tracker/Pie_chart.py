class Pie_Chart:
    import matplotlib.pyplot as plt
    import numpy as np
    final = input('Do you want to see your expense(per year) and income(per year) on a pie_chart, Please type yes or no: ')
    if final == 'yes':
        cal = open('monthly_expenses.csv','r')
        num1=cal.readline()
        num2=cal.readline()
        num3=cal.readline()
        num4=cal.readline()
        num5=cal.readline()
        num6=cal.readline()
        num7=cal.readline()
        num8=cal.readline()
        num9=cal.readline()
        num10=cal.readline()
        num11=cal.readline()
        num12=cal.readline()

        cal1 = open('total_monthly_pay_for_12_month_Period.csv', 'r')
        num13=cal1.readline()

        cal2 = open('after_tax_deductions.csv', 'r')
        num14=cal2.readline()

        sum1 = float(num1)+float(num2)+float(num3)+float(num4)+float(num5)+float(num6)+float(num7)+float(num8)+float(num9)+float(num10)+float(num11)+float(num12)
        sum2 = int(sum1) + float(num13)
        sum3 = float(num14) - int(sum2) 

        y = np.array([sum2, num14])
        mylabel = [f'Expenses:{sum2}(y)', f'Income:{num14}(y)']
        mycolors = ['red', 'lightgreen']

        plt.pie(y, labels=mylabel, colors=mycolors)
        if sum2 < float(num14):
            plt.title('Your Expense is less then your income')

        if sum2 > float(num14):
            plt.title('Your Expense is greater then your income')

        plt.savefig('Expenses vs income.png') 