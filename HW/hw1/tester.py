
import sys
import subprocess
import random
import sys


python_script = None
version = None
i = 0


def check_0(val):
    if (int(val) == 0):
        return '1'
    return val


def generator(version):
    if (version == 1 or version == 2):
        return check_0(str(random.randint(-100000000000, 100000000000)))
    elif (version == 3):
        if random.randint(0, 100000000000) % 2 == 0:
            return check_0(str(random.randint(-100000000000, 100000000000)))
        else:
            string = ""
            length = random.randint(4, 16)
            for _ in range(length):
                string += (chr(ord('a') + random.randint(0, 25)))
            return string


def genarator_plus_minus(version):
    res = generator(version)
    val = random.randint(0, 100000000000)
    if (not res.startswith("-")) and val % 10 == 0:
        res = "+" + res
    return res


def check_int(s):
    try:
        int(s)
        return 1
    except:
        return 0


def write(arr, stdin):
    for elem in arr:
        stdin.write(elem + "\n")
    stdin.write("0\n")
    stdin.close()


def launch(python_script):
    return subprocess.Popen([sys.executable, python_script],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)


def gen_random():
    things = []
    length = random.randint(2, 50)
    for _ in range(length):
        thing = genarator_plus_minus(version)
        things.append(thing)
    return things


def solve(things):
    resultPlus = 0
    resultMinus = 0
    for thing in things:
        if (check_int(thing)):
            val = int(thing)
            if (val > 0):
                resultPlus += val
            else:
                resultMinus += val
    return resultPlus, resultMinus


def checkAns(resultPlus, resultMinus, stdout):
    answer = stdout.readline()
    if (version in {1}):
        res = answer.split()[0]
        assert int(res) == resultPlus + resultMinus
    else:
        res, plus, minus = answer.split()
        assert int(res) == resultPlus + resultMinus
        assert int(plus) == resultPlus
        assert int(minus) == resultMinus


def main(gen):
    global i
    i += 1
    try:
        process = launch(python_script)

        things = gen()

        resultPlus, resultMinus = solve(things)

        write(things, process.stdin)

        errors = process.stderr.readlines()
        for error in errors:
            print(error)

        checkAns(resultPlus, resultMinus, process.stdout)

        print(f"success {i}")
    except:
        print(f"test failed: {i}")


def args_check():
    global python_script, version

    if (len(sys.argv) != 3):
        print("Not enought arguments")
        return

    python_script = sys.argv[1]
    version = sys.argv[2]
    if not check_int(version) or not int(version) in {1, 2, 3}:
        print("Version shound be {1 for easy, 2 for medium, 3 for hard}")
        return
    version = int(version)


if __name__ == "__main__":

    args_check()

    for i in range(10):
        main(gen_random)
    if version in {3}:
        main(lambda: ["-111111k111111", "+1111111111111"])
        main(lambda: ["-111111k111111", "+1111111111111"])
        main(lambda: ["-111111111111", "+1111111111111"])
        main(lambda: ["-111111-111111", "+111111+1111111"])
        main(lambda: ["-111111-111111", "+111111-1111111"])
        main(lambda: ["-111111+111111", "+111111-1111111"])
        main(lambda: ["-111111+111111", "+111111+1111111"])
        main(lambda: ["my", "name", "is", "jeff"])
        main(lambda: ["-111111111111", "++1111111111111"])
        main(lambda: ["-11111111111l", "+1111111111111l"])
        main(lambda: ["10", "0x10"])
        main(lambda: [""])
        main(lambda: ["12", "34", "", "-12", "-34"])
        print("Advanced:")
        main(lambda: [" 12 ", " 34 ", "   ", " -12 ", " -34 "])
        main(lambda: [" 12 ", " 34 ", "   ", " - 12 ", " -34 "])
        main(lambda: [" 12 ", " 34 ", "   ", " 12- ", " -34 "])
        main(lambda: [" 12 ", " 34 ", "   ", " 12  -  0", " -34 "])
        main(lambda: [" 1 2 ", " 34 ", "   ", " 12  -  0", " -34 "])
        main(lambda: [" --12 ", " 34 ", "   ", " -34 "])
        main(lambda: [" ++12 ", " 34 ", "   ", " -34 "])
        main(lambda: [" -+12 ", " 34 ", "   ", " -34 "])
        main(lambda: [" +-12 ", " 34 ", "   ", " -34 "])
        main(lambda: [" 1+2 ", " 34 ", "   ", " -34 "])
        main(lambda: [" 12+ ", " 34 ", "   ", " -34 "])
