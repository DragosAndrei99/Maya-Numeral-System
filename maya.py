def base10_to_base20_maya(number):
    # definim simbolurile maya pentru numere
    maya_zero = '@'
    maya_symbols = ['', '.', '..', '...', '....', '-', '-.', '-..', '-...', '-....', '--', 
        '--.', '--..', '--...', '--....', '---', '---.', '---..', '---...', '---....']
    maya_values = [1, 20, 400, 8000, 160000, 3200000, 64000000]
    # lista pentru adaugarea rezultatelor (simboluri maya)
    result_digits = []
    initial_num= number
    # iteram prin maya_values in ordine inversa 
    for maya_value in reversed(maya_values):
        # calculam coeficientul
        quotient = number // maya_value
        if quotient == 0 and initial_num> maya_value:
            result_digits.append(maya_zero)
        # adaugam simbolul maya corespunzator la rezultatul listei
        result_digits.append(maya_symbols[quotient])
        # linia urmatoare reprezinta puterea lui 20
        result_digits.append('\n')
        # scadem din numar coeficientul inmultit cu valoarea maya
        number -= quotient * maya_value
    # adaugam listei ulimul simbol maya
    result_digits.append(maya_symbols[number])
    # returnam lista ca un string
    return ''.join(result_digits)
# exemplu 
number = 5450
maya_number = base10_to_base20_maya(number)
print(f"{number} in Maya base 20 is \n{maya_number}")