principal = float(input('Enter the inital principal balance: '))
rate = float(input('Enter the intrest rate: '))
year = int(input('Enter the amount of years that interest will be calculated for: '))
amount = principal
c_year = 1

for i in range (year):
    amount = amount * (1 + rate/100)
    amount = round(amount,2)
    print(f'Year {c_year} amount: ${amount}')
    c_year += 1