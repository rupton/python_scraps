from fizzbuzz import fizzbuzz


def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(12) == "Fizz"

def test_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(20) == "Buzz"
    assert fizzbuzz(35) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"


def test_negative():
    assert fizzbuzz(-3) == "You must provide a positive integer"

def test_non_int():
    assert fizzbuzz('hello') == "Input must be an integer"
    assert fizzbuzz('three') == "Input must be an integer"

def test_float():
    assert fizzbuzz(1.254)  == "1"


