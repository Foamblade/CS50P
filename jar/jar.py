class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        elif n < 1:
            raise ValueError
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self._size:
            self._size -= n
        elif n < 1:
            raise ValueError
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    try:
        jar = Jar()
        print(jar)
    except:
        raise ValueError

main()


