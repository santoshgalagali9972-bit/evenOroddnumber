from even_or_odd import evenandodd

def test_even():
    assert evenandodd(10) == "The number is even"

def test_odd():
    assert evenandodd(7) == "The number is odd"

def test_zero():
    assert evenandodd(0) == "The number is even"