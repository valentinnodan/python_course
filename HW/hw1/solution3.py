


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()




cur_input = input()
counter1 = 0
counter2 = 0
while not (check_int(cur_input) and int(cur_input) == 0):
    if (check_int(cur_input)):
        cur_input = int(cur_input)
        if (cur_input > 0) :
            counter1 += cur_input
        else:
            counter2 += cur_input

    cur_input = input()

print(counter1 + counter2, counter1, counter2)