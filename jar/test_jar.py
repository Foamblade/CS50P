from jar import Jar

def test_init():
    jar = Jar()
    assert jar._capacity == 12
    jar2 = Jar(5)
    assert jar2._capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar._size == 7
    jar.deposit(5)
    assert jar._size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(5)
    assert jar._size == 2
    jar.withdraw(2)
    assert jar._size == 0
