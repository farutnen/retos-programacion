# escribe un programa que, 
# dado un número, compruebe y muestre si es 
# primo, fibonacci y par.
# Ejemplos: " del 0 al 10"
#-con el 1, nos dirá: "1 no es primo, no es fibonacci y es impar"
#-con el 2, nos dirá: "2 es primo, es fibonacci y es par"
#-con el 3, nos dirá: "3 es primo, no es fibonacci y es impar"
#-con el 5, nos dirá:
#-con el 7, nos dirá: "7 es primo, no esfibonacci y es impar"



import math


def check_prime_fibonacci_even(number):

        result= f"{number} "
        
        #primo
        if number > 1:
            for index in range(2, number):
                if number % index == 0:
                    result += "no es primo, "
                    break
            else:
                result += "es primo, "
        
        else:
            result += "no es primo, "
        
        #fibonacci
        result += "es fibonacci " if number > 0 and (is_perfect_square (5 * number * number + 4) or is_perfect_square(5 * number * number - 4)) else "no es fibonacci, "
        
        #par
        # if(numer % 2 == 0)es par
        result += "y es par" if number %2 == 0 else "y es impar"
        
        print (result)

def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number
    
check_prime_fibonacci_even(6)
check_prime_fibonacci_even(2)
check_prime_fibonacci_even(0)
check_prime_fibonacci_even(5)
check_prime_fibonacci_even(7)