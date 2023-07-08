class FizzBuzz():
    def Print(self, number):
        """
            Return fizzBuzz si multiple de 3 et 5
            fizz si multiple de 3
            buzz si mulmtiple de 5
            le nombre le cas echeant

            :param number: le nombre
            :return: le nombre ou fizs/buzz
            >>> fizzBuzz=FizzBuzz() 
            >>> fizzBuzz.Print(1)
            1
            >>> fizzBuzz.Print(3)
            'Fizz'
            >>> fizzBuzz.Print(5)
            'Buzz'
            >>> fizzBuzz.Print(15)
            'FizzBuzz'
        """
        if (number % 3 == 0 and number % 5 == 0):
            return "FizzBuzz"
        if (number % 3 == 0):
            return "Fizz"
        if (number % 5 == 0):
            return "Buzz"
        return number
