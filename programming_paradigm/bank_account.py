class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional initial balance (default is 0).
        """
        self._account_balance = initial_balance  # Private attribute to enforce encapsulation

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        :param amount: The amount to deposit (must be positive).
        """
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds are available.
        :param amount: The amount to withdraw (must be positive).
        :return: True if withdrawal is successful, False if insufficient funds.
        """
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                return True
            else:
                return False
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")
