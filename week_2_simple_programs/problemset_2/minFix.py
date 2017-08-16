# program that calculates the minimum fixed monthly payment
#needed in order pay off a credit card balance within 12 months.

balance = 4773
original_balance = balance
annualInterestRate = 0.2
minFixed = 0
# i = 0

while balance >= 0:
    balance = original_balance
    minFixed += 10
    for i in range(12):
        balance -= minFixed
        balance += balance * annualInterestRate//12
        # I got +10 because I  swapped line 14 and 15
        # interest rate is calculated after paying the fixed task



# # odd tuples
#
# def oddTuples(tup):
#
#     only_odd = ()
#
#     for i in range(len(tup)):
#         if i % 2 == 0:
#             only_odd += (tup[i],)
#     return only_odd
# s = ('I', 'am', 'a', 'test', 'tuple')
# print(oddTuples(s))
