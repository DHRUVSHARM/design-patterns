from abc import ABC
from enum import Enum

# SUMMARY
# 

class BankAccount:
    # lowest we can go
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        # initial balance
        self.balance = balance

    def deposit(self, amount):
        # deposit action , it is trivial and mostly should always succeed ( at least in our simple impl)
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')

    def withdraw(self, amount):
        # just ensuring that we do not go over the overdraft limit before making the op
        # NOTE : THE FLAG BEING RETURNED IS USEFUL TO DETERMINE THE SUCCESS / FAIL OF THIS OP
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            # can do 
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            return True
        # cannot do 
        return False

    def __str__(self):
        # balance repr 
        return f'Balance = {self.balance}'


# for recording the commands that is one level higher (interface)
# this is useful gives users an expected baseline when trying to develop 
# commands further
class Command(ABC):

    def __init__(self):
        # implicit failure assume when a command is initialized
        self.command = False

    # invoke
    def invoke(self):
        pass
    # undo
    def undo(self):
        pass

# bank account command is a type of command that will implement the command interface above
class BankAccountCommand(Command):
    def __init__(self, account, action, amount):
        super().__init__()
        self.amount = amount
        self.action = action
        self.account = account
    

    # actions 
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            # set success
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        # only continue with undo if the cmd actually suceeded 
        if not self.success:
            return
        # strictly speaking this is not correct
        # (you don't undo a deposit by withdrawing)
        # but it works for this demo, so...
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == '__main__':
    ba = BankAccount()
    # create bank account command 
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    # call the command to invoke 
    cmd.invoke()
    # deposit print statement after the deposit
    print('After $100 deposit:', ba)

    # imp, using a command gives the ability to rollback the state is bound to the command, so in 
    # this simple implementation this should be easy 
    cmd.undo()
    print('$100 deposit undone:', ba)

    # something like this will fail so it is important in the undo to ensure the command succeeds 
    # which is maintained using the success memeber in our implementation
    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    illegal_cmd.invoke()
    print('After impossible withdrawal:', ba)
    # undo will not have an effect
    illegal_cmd.undo()
    print('After undo:', ba)


