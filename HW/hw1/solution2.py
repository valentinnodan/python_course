


cur_input = int(input())
counter1 = 0 
counter2 = 0
while cur_input != 0:
    if (cur_input > 0) :
        counter1 += cur_input
    else:
        counter2 += cur_input

    cur_input = int(input())

print(counter1 + counter2, counter1, counter2)