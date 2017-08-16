# Write a program to calculate the credit card balance after one year if a person
# only pays the minimum monthly payment required by the credit card company each month


balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
minMonthPay = balance * monthlyPaymentRate
balance -= minMonthPay
# print('minMonthPay - start', minMonthPay)
# print('Balance - start', balance)
for i in range(12):
    # print('Balance top of loop', balance)
    balance = balance + annualInterestRate/12.0 * balance
    # print('Balance after adding interest', balance)
    minMonthPay = balance * monthlyPaymentRate
    # print('new minMonthPay with interest', minMonthPay)
    # print('Remaining balance:{0:.2f}'.format(balance))
    if i == 11:
        break
    balance -= minMonthPay
    # print('end of loop', i)
print('Remaining balance:{0:.2f}'.format(balance))
