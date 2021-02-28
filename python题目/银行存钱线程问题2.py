from time import sleep
from threading import Thread, Lock


class Account(object):
    def __init__(self):
        self._balence = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        new_balence = self._balence + money
        sleep(0.01)
        self._balence = new_balence
        self._lock.release()

    @property
    def balence(self):
        return self._balence


class AddmoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddmoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：$%d元' % account.balence)


if __name__ == '__main__':
    main()
