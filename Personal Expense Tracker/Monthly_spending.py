class Money_Spent_Every_Month:
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    # Jan
    Jan = float(input('How much in total did you spent in the month Jan: '))
    # Feb
    Feb = float(input('How much in total did you spent in the month Feb: '))
    # Mar
    Mar = float(input('How much in total did you spent in the month Mar: '))
    # Apr
    Apr = float(input('How much in total did you spent in the month Apr: '))
    # May
    May = float(input('How much in total did you spent in the month May: '))
    # Jun
    Jun = float(input('How much in total did you spent in the month Jun: '))
    # Jul
    Jul = float(input('How much in total did you spent in the month Jul: '))
    # Aug
    Aug = float(input('How much in total did you spent in the month Aug: '))
    # Sep
    Sep = float(input('How much in total did you spent in the month Sep: '))
    # Oct
    Oct = float(input('How much in total did you spent in the month Oct: '))
    # Nov
    Nov = float(input('How much in total did you spent in the month Nov: '))
    # Dec
    Dec = float(input('How much in total did you spent in the month Dec: '))

    months = {
        'Jan':[Jan],
        'Feb':[Feb],
        'Mar':[Mar],
        'Apr':[Apr],
        'May':[May],
        'Jun':[Jun],
        'Jul':[Jul],
        'Aug':[Aug],
        'Sep':[Sep],
        'Oct':[Oct],
        'Nov':[Nov],
        'Dec':[Dec]
    }
    df_months = pd.DataFrame(months)
    a = open('Monthly_spending.csv', 'a')
    a.write(str(df_months))

    p = open('monthly_expenses.csv','a')
    p.write(str(f'{Jan}\n{Feb}\n{Mar}\n{Apr}\n{May}\n{Jun}\n{Jul}\n{Aug}\n{Sep}\n{Oct}\n{Nov}\n{Dec}'))

    y = np.array([Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec])
    mylabel = [f'Jan:{Jan}',f'Feb:{Feb}',f'Mar:{Mar}',f'Apr:{Apr}',f'May:{May}',f'Jun:{Jun}',f'Jul:{Jul}',f'Aug:{Aug}',f'Sep:{Sep}',f'Oct:{Oct}',f'Nov:{Nov}',f'Dec:{Dec}']
    myexplode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    plt.pie(y, labels=mylabel, explode = myexplode)
    plt.savefig('Monthly spending.png')
