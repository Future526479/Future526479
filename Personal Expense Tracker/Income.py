class Income_before_deduction_and_after_tax_deduction:
    Gross_income = float(input('What is you Gross monthly income before deductions: '))
    months = 12
    full_amount = Gross_income*months
    per_annum = open('Annum_payment.csv', 'w')
    per_annum.write(str(full_amount))

    if full_amount < 237100:
        # 0 to 237,100
        tax1 = 0.18
        tax1_payment = full_amount*tax1
        money_after_tax1 = full_amount-tax1_payment
        after_tax1_deductions = open('after_tax_deductions.csv', 'w')
        after_tax1_deductions.write(str(money_after_tax1))

    if full_amount >= 237101 <= 370500:
        # 237,101 to 370,500
        tax2 = 0.26
        added_to_tax2 = 42678
        tax2_payment = full_amount*tax2
        money_after_tax2 = full_amount-tax2_payment-added_to_tax2
        after_tax2_deductions = open('after_tax_deductions.csv', 'w')
        after_tax2_deductions.write(str(money_after_tax2))


    # 370,501 to 512,800
    if full_amount >=370501 <=512800:
        tax3 = 0.31
        added_to_tax3 = 77362
        tax3_payment = full_amount*tax3
        money_after_tax3 = full_amount-tax3_payment-added_to_tax3
        after_tax3_deductions = open('after_tax_deductions.csv', 'w')
        after_tax3_deductions.write(str(money_after_tax3))



    # 512,801 to 673,000
    if full_amount >=512801 <=673000:
        tax4 = 0.36
        added_to_tax4 = 121475
        tax4_payment = full_amount*tax4
        money_after_tax4 = full_amount-tax4_payment-added_to_tax4
        after_tax4_deductions = open('after_tax_deductions.csv', 'w')
        after_tax4_deductions.write(str(money_after_tax4))


    # 673,001 to 857,900
    if full_amount >=673001 <=857900:
        tax5 = 0.39
        added_to_tax5 = 179147
        tax5_payment = full_amount*tax5
        money_after_tax5 = full_amount-tax5_payment-added_to_tax5
        after_tax5_deductions = open('after_tax_deductions.csv', 'w')
        after_tax5_deductions.write(str(money_after_tax5))


    # 857,901 to 1,817,000
    if full_amount >=857901 <=1817000:
        tax6 = 0.41
        added_to_tax6 = 251258
        tax6_payment = full_amount*tax6
        money_after_tax6 = full_amount-tax6_payment-added_to_tax6
        after_tax6_deductions = open('after_tax_deductions.csv', 'w')
        after_tax6_deductions.write(str(money_after_tax6))

    # 1,817,001 and above
    if full_amount > 1817001:
        tax7 = 0.45
        added_to_tax7 = 644489
        tax7_payment = full_amount*tax7
        money_after_tax7 = full_amount-tax7_payment-added_to_tax7
        after_tax7_deductions = open('after_tax_deductions.csv', 'w')
        after_tax7_deductions.write(str(money_after_tax7))