from main import * 

def test_should_return_samemnumber_when_it_is_not_mumltiple_of_three_or_five():
    fizzBuzz = FizzBuzz()
    number=1
    value=fizzBuzz.Print(number)
    assert 1==value

def test_should_return_fizz_when_number_it_is_mumltiple_of_three():
    fizzBuzz = FizzBuzz()
    number=3
    value=fizzBuzz.Print(number)
    assert "Fizz"==value

def test_should_return_Buzz_when_number_it_is_mumltiple_of_five():
    fizzBuzz = FizzBuzz()
    number=5
    value=fizzBuzz.Print(number)
    assert "Buzz"==value

def test_should_return_FizzBuzz_when_number_it_is_mumltiple_of_five_and_three():
    fizzBuzz = FizzBuzz()
    number=15
    value=fizzBuzz.Print(number)
    assert "FizzBuzz"==value
