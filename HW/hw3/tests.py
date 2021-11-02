from abc import abstractmethod
import random
import unittest

import filecmp
import os
import sys

import shutil

from common.test_runner import run_tests


class FileMachine:
    def __init__(self):
        self.dir = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0])) + "/tmp"
        if (os.path.isdir(self.dir)):
            shutil.rmtree(self.dir)
        os.makedirs(self.dir)
        self.input = self.dir + "/input"
        open(self.input, 'a', encoding="utf-8").close()
        self.output = self.dir + "/output"
        open(self.output, 'a', encoding="utf-8").close()
        self.gold_output = self.dir + "/gold_output"
        open(self.gold_output, 'a', encoding="utf-8").close()

    def check_equality(self):
        assert filecmp.cmp(self.output, self.gold_output)

    def remove(self):
        shutil.rmtree(self.dir)


def randword():
    word = []
    length = random.randrange(4, 12)
    for _ in range(length):
        start = 'a'
        if random.randint(0, 10) == 0:
            start = 'A'
        word.append(chr(ord(start) + random.randrange(0, 26)))
    if (random.randint(0, 40) == 0):
        word.insert(3, '-')
    return "".join(word)

whitespaces = [" ", " ", " ", "\n", "\t"]

arr_sep_right = ",:;.!?"

arr_sep_both = "-–"


def separator():
    if (random.randrange(0, 30) == 0):
        return random.choice(whitespaces) + random.choice(arr_sep_both) + random.choice(whitespaces)
    if (random.randrange(0, 5) == 0):
        return random.choice(arr_sep_right) + random.choice(whitespaces)
    return random.choice(whitespaces)


def gen_answer(fm: FileMachine, n_words: int, n_ind_words: int, hard: bool = False):
    stats = [[randword()] for _ in range(n_ind_words)]

    for i in range(n_words):
        wn = random.randrange(0, n_ind_words)
        stats[wn].append(i + 1)

    stats_new=sorted(filter(lambda x: len(x) > 1, stats), key=lambda x: x[1])
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

    def test_1(self):
        self.base(6, 3)

    def test_2(self):
        self.base(60, 1)

    def test_3(self):
        self.base(60, 40)

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
