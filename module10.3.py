from threading import Thread, Lock


class BankAccount:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def deposit(self, amount):  # пополнение
        self.amount += amount
        print(f'Deposited {amount}, new balance is {self.amount}')

    def withdraw(self, amount):  # снятие
        self.amount -= amount
        print(f'Withdraw {amount}, new balance is {self.amount}')


def deposit_task(account, amount):  # пополнение счета на сумму
    for _ in range(5):
        with lock:
            account.deposit(amount)


def withdraw_task(account, amount):  # снятие со счета суммы
    for _ in range(5):
        with lock:
            account.withdraw(amount)

lock = Lock()

account = BankAccount(1234, 1000)

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
