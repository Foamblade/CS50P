from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.256.255") == False
    assert validate("255.255.0") == False
    assert validate("1.2.3.4.5") == False
