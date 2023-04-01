def maya_sum(num1, num2):
    maya_symbols = []
    maya_sum_symbols = []
    maya_result = []
    # adaugam toate simolurile intr-o singura lista
    if len(num1) >= len (num2):
        highest_num = num1
    else:
        highest_num = num2
    # calculam care nr are mai multe poztii si in functie de acesta, cream o lista cu toate simbolurile
    # lista are pozitii grupate 2 cate 2
    for i in range(len(highest_num)):
        if i < len(num1):
            maya_symbols.append(num1[i])
            pass
        if i < len(num2):
            maya_symbols.append(num2[i])
            pass
    # vom crea o lista ce va alatura simbolurile tinand cont de pozitii ( 2 pozitii din lista devin 1 singura pozitie)
    j=0
    while j < len(maya_symbols):
        if j+1 < len(maya_symbols):
            maya_sum_symbols.append(maya_symbols[j] + maya_symbols[j+1])
            j += 2
        else:
            maya_sum_symbols.append(maya_symbols[j])
            j+=1

    # simplificarea 
    for i in range(len(maya_sum_symbols)):
        dots = 0
        bars = 0
        for symbol in maya_sum_symbols[i]:
            if symbol == '.':
                dots+= 1
            if symbol == '-':
                bars += 1
        # calculam cate puncte si bare au ramas si cate au fost transformate conform regulilor
        carry_over_bars = dots // 5
        carry_over_dots = bars // 4
        dots_remaining = dots % 5
        bars_remaining = bars % 4
        # adaugam pe fiecare pozitie rezultatul corespunzator
        maya_result.append(make_number(dots_remaining, bars_remaining + carry_over_bars))
        # adaugam ce ne-a ramas de la pozitia inferioara , pe pozitia superioara
        if i + 1 < len(maya_sum_symbols):
            # daca avem pozitie, concatenam
            maya_sum_symbols[i+1] += make_number(carry_over_dots)
        else:
            # daca nu avem pozitie, facem append ( push )
            maya_sum_symbols.append(make_number(carry_over_dots))

    # print(maya_sum_symbols)
    print(maya_result)

    return

def make_number(dots, bars=0):
    number = ''
    for i in range(bars):
        number += '-'
    for i in range(dots):
        number += '.'

    return number

# exemplu 5052 + 2798 = 7850
num1 = ['--..', '--..', '--..'] # 5052
num2 = ['---...', '---....', '-.'] # 2798
maya_sum(num1, num2)

# rezultatul ar trebui sa fie urmatorul:
# result = ['--', '--..', '---....'] # 7850
