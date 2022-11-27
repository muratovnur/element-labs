def addToBankAccount(bank, amount):
  bank += amount
  return bank

def substractFromBankAccount(bank, amount):
  bank -= amount
  return bank

def moneyConversion(bank, fromCurrency, toCurrency):
  if fromCurrency == 'USD' and toCurrency == 'KZT':
    bank *= 470
  elif fromCurrency == 'KZT' and toCurrency == 'USD':
    bank /= 470
  return bank
  
print(addToBankAccount(0, 500))
print(substractFromBankAccount(500, 200))
print(moneyConversion(300, 'USD', 'KZT'))
print(moneyConversion(470, 'KZT', 'USD'))
