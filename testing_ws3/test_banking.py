import pytest
from banking import Account, MoneyTransfer

@pytest.fixture
def accounts():
    account1 = Account("Acc1", 1000)
    account2 = Account("Acc2", 500)
    return account1, account2

def test_depositAcc1(accounts):
    account = accounts[0]
    account.deposit(500)
    # test pass
    assert account.balance == 1500
    # test fail
    # assert account.balance == 2000
def test_depositAcc2(accounts):
    account = accounts[1]
    account.deposit(500)
    # test pass
    assert account.balance == 1000
    # test fail
    # assert account.balance == 2000

def test_withdraw1(accounts):
    account = accounts[0]
    account.withdraw(500)
    # test pass
    assert account.balance == 500
    # test fail
    # assert account.balance == 2000

def test_withdraw2(accounts):
    account = accounts[1]
    account.withdraw(500)
    # test pass
    assert account.balance == 0
    # test fail
    # assert account.balance == 2000

def test_insufficient_withdraw1(accounts):
    account = accounts[0]
    with pytest.raises(ValueError):
        # test pass
        account.withdraw(5000)
        # test fail
        # account.withdraw(1)
def test_insufficient_withdraw2(accounts):
    account = accounts[1]
    with pytest.raises(ValueError):
        # test pass
        account.withdraw(5000)
        # test fail
        # account.withdraw(1)

def test_transfer(accounts):
    sender, receiver = accounts
    MoneyTransfer.transfer(sender, receiver, 200)
    # test pass
    assert sender.balance == 800
    # test pass
    assert receiver.balance == 700
    # test fail
    # assert sender.balance == 900
    # test fail
    # assert receiver.balance == 900