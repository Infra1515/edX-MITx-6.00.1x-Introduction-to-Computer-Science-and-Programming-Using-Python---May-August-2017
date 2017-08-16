
# balance = 320000999999999
# original_balance = balance
# annualInterestRate = 0.2
# minFixed = 0
#
# while balance >= 0:
#     balance = original_balance
#     minFixed += 10
#     for i in range(12):
#         balance -= minFixed
#         balance += balance * annualInterestRate//12
# # I got +10 i swapped line 328 and 329
# # interest rate is calculated after paying the fixed task
#
#
# print(minFixed)


balance = 320000
annualInterestRate = 0.2
initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0

while abs(balance) >= epsilon:
    balance = initBalance

    for i in range(12):
        balance -= minPay
        balance += monthlyInterestRate * balance

    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high+low)/2.0
minPay = round(minPay,2)
print('Lowest payment:',minPay)
