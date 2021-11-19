from abc import abstractmethod
import random
import unittest

import filecmp
import os
import sys

import shutil
import string

from common.test_runner import run_tests
from itertools import chain


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


class FileMachine:
    def __init__(self):
        self.dir = os.path.join(os.path.dirname(
            os.path.join(os.getcwd(), sys.argv[0])), "tmp")
        if (os.path.isdir(self.dir)):
            shutil.rmtree(self.dir)
        os.makedirs(self.dir)
        self.input = os.path.join(self.dir, "input")
        open(self.input, 'a', encoding="utf-8").close()
        self.output = self.dir + "/output"
        open(self.output, 'a', encoding="utf-8").close()
        self.gold_output = os.path.join(self.dir, "gold_output")
        open(self.gold_output, 'a', encoding="utf-8").close()

    def check_equality(self):
        res = filecmp.cmp(self.output, self.gold_output)
        if not res:
            print("Actual:")
            with open(self.output, "r", encoding="utf-8") as f:
                print(f.read())
            print("Expected:")
            with open(self.gold_output, "r", encoding="utf-8") as f:
                print(f.read())
            assert filecmp.cmp(self.output, self.gold_output)

    def remove(self):
        shutil.rmtree(self.dir)


def norm(x):
    return x.isalpha() and x.lower().isalpha() and ("a" + x).lower() == "a" + x.lower() and (x + "a").lower() == x.lower() + "a" and ("a" + x + "a").lower() == "a" + x.lower() + "a"


small = [i for i in chain(char_range('a', 'z'), char_range('а', 'я'))]
big = list(filter(lambda x: norm(x), [i for i in chain(char_range(
    'A', 'Z'), char_range('А', 'Я'), char_range("\u0000", "\uffff"))]))


def randword():
    word = []
    length = random.randrange(5, 40)
    for _ in range(length):
        start = small
        if random.randint(0, 10) == 0:
            start = big
        word.append(random.choice(start))
    if (random.randint(0, 40) == 0):
        word.insert(3, '-')
    if (word[-1] == 's'):
        if (random.randint(0, 40) == 0):
            word.insert(-1, "'")
    return "".join(word)


def separator():
    whitespaces = string.whitespace
    if (random.randrange(0, 30) == 0):
        return random.choice(whitespaces) + random.choice(string.punctuation) + random.choice(whitespaces)
    if (random.randrange(0, 5) == 0):
        return random.choice(string.punctuation) + random.choice(whitespaces)
    return random.choice(whitespaces)


def gen_answer(fm: FileMachine, n_words: int, n_ind_words: int, hard: bool = False):
    stats = [[randword()] for _ in range(n_ind_words)]

    for i in range(n_words):
        wn = random.randrange(0, n_ind_words)
        stats[wn].append(i + 1)

    stats_new = sorted(filter(lambda x: len(x) > 1, stats), key=lambda x: x[1])
    with open(fm.gold_output, "w", encoding="utf-8") as f:
        for word in stats_new:
            f.write(word[0].lower())
            f.write(" ")
            f.write(str(len(word[1:])))
            if hard:
                f.write(" ")
                f.write(" ".join(list(map(str, word[1:]))))
            f.write("\n")

    file = ["" for i in range(n_words)]

    for word in stats_new:
        for a in word[1:]:
            file[a - 1] = word[0]

    with open(fm.input, "w", encoding="utf-8") as f:
        if len(file) == 0:
            return
        f.write(file[0])
        for i in range(1, len(file)):
            f.write(separator())
            f.write(file[i])


class TestBase(unittest.TestCase):

    @abstractmethod
    def hard(self):
        pass

    def base(self, n, m):
        fm = FileMachine()
        gen_answer(fm, n, m, self.hard())
        collector(fm.input, fm.output)
        fm.check_equality()
        fm.remove()

    def test_0(self):
        self.base(0, 0)

    def test_spaces(self):
        fm = FileMachine()
        with open(fm.input, "w", encoding="utf-8") as f:
            for i in range(100):
                f.write(string.whitespace)
        fm.check_equality()
        fm.remove()

    def test_1(self):
        self.base(6, 3)

    def test_2(self):
        self.base(60, 1)

    def test_3(self):
        self.base(60, 40)

    def test_4(self):
        self.base(60, 40)

    def test_5(self):
        self.base(600, 40)

    def test_6(self):
        self.base(600, 400)

    def test_small(self):
        for i in range(100):
            self.base(60, 40)

    def test_max(self):
        for i in range(100):
            self.base(600, 400)
    
    def test_maximum(self):
        for i in range(10):
            self.base(6000, 4000)


class CollectorTestCase(TestBase):

    @abstractmethod
    def hard(self):
        return False


class CollectorTestCaseHard(TestBase):

    @abstractmethod
    def hard(self):
        return True


def easy_tests(module):
    run_tests(module, globals(), ['collector'], [CollectorTestCase])


def hard_tests(module):
    run_tests(module, globals(), ['collector'], [CollectorTestCaseHard])
