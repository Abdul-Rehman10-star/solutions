"""
Opgave "sequence2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv en funktion med navnet "sequence2".
Scroll ned for at finde det sted i denne fil, hvor du skal skrive funktionen ind.

Del 1:
    Funktionen sequence2 skal have to parameter: "min_value" og "max_value".
    Funktionen skal udskrive heltal fra min_value op til og med maxvalue.

    Eksempel: Når du kalder sequence2(3, 5), printes 3 4 5.


Del 2:
    Dupliker hele funktionskoden. (Du kan med fordel marker hele
    funktionen og derefter taste CTRL+D.)
    Kald funktionen i duplikatet sequence3.
    Tilføj en tredje parameter "step_size" til sequence3.
    Funktionen skal udskrive heltal fra min_value op til og med maxvalue.
    Den skal dog ikke udskrive hver tal. Der skal være et mellemrum med
    størrelsen step_size mellem de udskrevne tal.

    Eksempel: Når du kalder sequence3(3, 18, 4), printes 3 7 11 15.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""


#  Write your function below this line:
def sequence2(min_value, max_value):
    for tooth in range(min_value, max_value + 1):
        print(tooth)

def sequence3(min_value, max_value, step_size):
    for tooth in range(min_value, max_value, step_size):
        print(tooth)

# Here starts the main program. Call your function here:
sequence3(3, 18, 4)