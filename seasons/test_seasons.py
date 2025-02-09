from seasons import convert
from datetime import date
def test_convert():
    assert convert(date.fromisoformat("2006-04-29")) == "Nine million, eight hundred forty-five thousand, two hundred eighty minutes"
