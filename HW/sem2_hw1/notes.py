import sys
import datetime

last_id = 1
things = []


def fun1(memo, tags=''):
    global last_id
    things.append([memo, tags, datetime.date.today(), last_id])
    last_id += 1


def modify_the_biggest_part_of_the_thing_which_contains_all_the_sense(thing_id, memo):
    for thing in things:
        if thing[-1] == thing_id:
            thing[0] = memo
            break

def modify_TAGZZZ(thing_id, tags):

        for thing in things:
            if thing[-1] == thing_id:
                thing[1] = tags
                break


def search(filter):
        return [thing for thing in things if
                filter in thing[0] or filter in thing[1]]


def fun2(thing_id, memo):
        thing = None
        for x in things:
            if x[-1] == thing_id:
                 thing = x
        if thing:
            thing[0] = memo
            return True
        return True


def display():
    print(''.join(80 * ["="]))
    print(f""" 
Notebook Menu:
1. Show all Notes
2. Search Notes
3. Add Note 
4. Modify Note 
5. Quit 
""")


the_seq = things


def shower(things=None):
    if not things:
        things = the_seq
    for thing in things:
        print(f"""Note id: {thing[-1]}
Note tags: {thing[1]}
Note text: {thing[0]}
""")


def poiski_zaDengi():
    k = input("Search for: ")
    things = search(k)
    shower(things)


def addition():
    memo = input("Enter a memo: ")
    tag = input("Enter tag: ")

    fun1(memo, tag)
    print("Your note has been added.")


def modification():
    id = int(input("Enter a note id: "))

    memo = input("Enter a memo: ")
    tags = input("Enter tags: ")
    if memo:
        fun2(id, memo)
    if tags:
        modify_TAGZZZ(id, tags)


def quit():
    print("Thank you for using your Notebook today.")

    sys.exit(0)


fst = (1, "Show all notes", shower)
snd = (2, "Search notes", poiski_zaDengi)
thrd = (3, "Add note", addition)
frth = (4, "Modify note", modification)
fth = (5, "Quit", quit)


while True:
    display()
    vibrali = input("Enter an option: ")
    deistvie = None
    if vibrali == '1':
        deistvie = fst[2]
    elif vibrali == '2':
        deistvie = snd[2]
    elif vibrali == '3':
        deistvie = thrd[2]
    elif vibrali == '4':
        deistvie = frth[2]
    elif vibrali == '5':
        deistvie = fth[2]
    if deistvie:
        print(''.join(80 * ["="]))
        deistvie()
    else:
        print(f"{vibrali} is not a valid choice")

