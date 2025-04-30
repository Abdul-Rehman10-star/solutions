"""
Opgave "multiply_numbers":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Forandre koden i funktionen multiply_numbers() sådan at den gør hvad der står i dens dokumentation.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""
# from jsonschema.benchmarks.const_vs_enum import value


def multiply_numbers(start, multiplier, upper_limit):
    """
    Beginning with the start value, this function prints the current value,
    then multiplies it with multiplier, prints the new current value etc.
    The function stops when the current value is greater than the upper limit"""
    current_value = start
    big_enough = False
    while not big_enough:
        print(current_value)

        current_value = multiplier * current_value
        big_enough = current_value > upper_limit


# number = int(input("type a starting number"))
multiply_numbers(5, 3, 1000000)