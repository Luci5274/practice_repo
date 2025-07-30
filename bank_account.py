class BankAccount:
    def __init__(self, name, starting_balance=0):
        self.balance = starting_balance
        self.name = name
        self.transactions = []

    def deposit(self, d_amount):
        if d_amount > 0:
            oldbal = self.balance
            self.balance += d_amount
            newbal = self.balance
            self.transactions.append({
                'action': 'deposit',
                'old_balance': oldbal,
                'new_balance': newbal
            })
            print(f'current balance: {oldbal}')
            print(f'your new balance after deposit is {newbal}')
            return True
        else:
            print('error, amount must be positive')
            return False

    def withdraw(self, wd_amount):
        if wd_amount <= 0:
            print('Error: Withdrawal amount must be greater than zero.')
            return False
        elif wd_amount > self.balance:
            print('Error: Insufficient balance.')
            return False
        else:
            oldbal = self.balance
            self.balance -= wd_amount
            newbal = self.balance
            self.transactions.append({
                'action': 'withdrawal',
                'old_balance': oldbal,
                'new_balance': newbal
            })
            print(f'Withdrawal successful! New balance: {self.balance}')
            return True

    def get_balance(self):
        print(f'balance: {self.balance}')
        return self.balance

    def get_info(self):
        print(f'name: {self.name}')
        print(f'balance: {self.balance}')
        return self.name, self.balance

    def get_trans(self):
        for x , transaction in enumerate(self.transactions, start=1):
            print(f'{x}, {transaction["action"].capitalize()}:${transaction["old_balance"]}'
                  f'-> ${transaction["new_balance"]}')
