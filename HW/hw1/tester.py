
import sys
import subprocess
import random


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
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def main(number):
    try:
        if (len(sys.argv) != 3):
            print("Not enought arguments")
            return
        
        python_script = sys.argv[1]
        version = sys.argv[2]
        if not check_int(version) or not int(version) in {1,2,3}:
            print("Version shound be {1 for easy, 2 for medium, 3 for hard}")
            return
        version = int(version)

        process = subprocess.Popen(["python3", python_script],
                            stdin =subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)

        length = random.randint(2, 50)

        resultPlus = 0
        resultMin = 0

        for _ in range(length):
            thing = genarator_plus_minus(version)
            if (check_int(thing)):
                val = int(thing)
                if (val > 0) :
                    resultPlus+=val
                else:
                    resultMin+=val
            process.stdin.write(thing + "\n")
        process.stdin.write("0\n")
        process.stdin.close()
        errors=process.stderr.readlines()
        for error in errors:
            print(error)
        answer = process.stdout.readline()
        if (version in {1}):
            res = answer.split()[0]
            assert int(res) == resultPlus + resultMin
        else:
            res, plus, minus = answer.split()
            assert int(res) == resultPlus + resultMin
            assert int(plus) == resultPlus
            assert int(minus) == resultMin
        print(f"success {number}")
    except:
        print(f"test failed: {number}")

if __name__ == "__main__":
    for i in range(10):
        main(i + 1)