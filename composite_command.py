# Composite Command a.k.a. Macro
# also: Composite design pattern ;)
# WE WILL REUSE FROM THE COMMAND MODULE WE WROTE 

import unittest
from abc import ABC, abstractmethod
from enum import Enum
from command import BankAccount , Command , BankAccountCommand


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        # list of commands
        super().__init__()
        for i in items:
            self.append(i)

    # serially apply the commands
    def invoke(self):
        for x in self:
            x.invoke()

    # in reverse serial order negate the commands applied 
    def undo(self):
        for x in reversed(self):
            x.undo()

# sort of a tree like commmand 
class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            BankAccountCommand(from_acct,
                               BankAccountCommand.Action.WITHDRAW,
                               amount),
            BankAccountCommand(to_acct,
                               BankAccountCommand.Action.DEPOSIT,
                               amount)])

    def invoke(self):
        # running mutation of states of ok , the final state of ok is what is assigned to the success of the entire command
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
                # invoke and set state only if all commands until this point succeeded 
            else:
                # at this point we know that the previous command failed and ok is false, so all subsequent commands
                # are marked as failed  
                cmd.success = False
        # final success of this special composite command is set based on the ok value
        self.success = ok



# tests
class TestSuite(unittest.TestCase):
    
    def test_composite_deposit(self):
        # this will simulate 2 commands on the same bank account
        # but applied using the composite command interface
        ba = BankAccount()
        deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 1000)
        deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 1000)
        composite = CompositeBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        print(ba)
        composite.undo()
        print(ba)

    def test_transfer_fail(self):
        # transfer fail test
        # simple apporach here where we use the composite command to aggregate 2 actions on SEPRATE bank accounts
        # in some order 
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        # composite isn't so good because of failure
        # amount = 100  # try 1000: no transactions should happen
        # fail since there is no way to tie the success of the first command wc to the second one unlike previous case
        amount = 1000
        wc = BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
        dc = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)

        transfer = CompositeBankAccountCommand([wc, dc])

        transfer.invoke()
        print('ba1:', ba1, 'ba2:', ba2)  # end up in incorrect state
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)

    def test_better_transfer(self):
        # test with better approach 
        # since the invoke will fail subsequent commands we will get correct state
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print('ba1:', ba1, 'ba2:', ba2)
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)
        print(transfer.success)


if __name__ == '__main__':
    unittest.main()