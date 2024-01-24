class Category:

  def __init__(self,cat):
    self.ledger = []
    self.category = cat

  def __str__(self):
    build_str = '*'*((30-len(self.category)) // 2)
    print_item = build_str+str(self.category)+build_str
    print_item = print_item if len(print_item) == 30 else print_item+'*'
    for el in self.ledger:
      two_decimals = str("% .2f" %el['amount'])
      desc = el['description']
      desc = desc if len(desc) < 23 else desc[:23]
      white_space = ' '*(30 - (len(desc) + len(two_decimals)))
      print_item = print_item+f'\n{desc}{white_space}{two_decimals}'
    return print_item + f'\nTotal: {self.get_balance()}'

  def deposit(self, amount, description = ""):
    self.ledger.append({'amount':amount,'description':description})

  def withdraw(self,amount,description = ""):
    if self.check_funds(amount):
      self.ledger.append({'amount':-1*float(amount),'description':description})
      return True
    return False

  def get_balance(self):
    total = 0
    for el in self.ledger:
      total += float(el['amount'])
    return total

  def transfer(self,amount,category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {category.category}')
      category.deposit(amount, f'Transfer from {self.category}')
      return True
    return False

  def check_funds(self,amount):
    if self.get_balance() >= amount:
      return True
    return False


# print(create_spend_chart([food, clothing, auto]))
def create_spend_chart(arr):
  total_spent = 0
  dict = {}
  for el in arr:
    cat_spent = 0
    for x in el.ledger:
      if x['amount'] < 0:
        cat_spent += abs(x['amount'])*100
    dict[f'{el.category}'] = "% .2f"%(cat_spent/100)
    total_spent += cat_spent/100
  chart = 'Percentage spent by category'
  for el in range(10,-1,-1):
    yval = str(el*10)
    while len(yval) < 3:
      yval = " " + yval
    chart += f'\n{yval}|'
    for x in dict.values():
      percent = ((float(x)/total_spent)*100) //1
      if percent >= el*10:
        chart += ' o '
      else:
        chart += '   '
    chart += ' '
  chart += '\n    ' + '---'*len(arr)+'-'
  dict_keys = sorted(list(dict.keys()),key=len,reverse=True)
  longest = len(dict_keys[0])
  str_arr = list(dict.keys())
  for index in range(len(str_arr)):
    el = str_arr[index]
    while len(el) < longest:
      el += ' '
    str_arr[index] = el
  for i in range(longest):
    chart += f'\n     {str_arr[0][i]}  {str_arr[1][i]}  {str_arr[2][i]}  '
  return (chart)





