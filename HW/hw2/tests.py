import random
import unittest

from common.TestRunner import run_tests


class AckermannTestCase(unittest.TestCase):
    def test_ackermann_numbers(self):
        ackermann_numbers = [(0, 0, 1), (3, 3, 61), (1, 1, 3), (1, 2, 4), (0, 5, 6), (4, 0, 13), (2, 2, 7), (2, 3, 9),
                             (3, 2, 29), (3, 5, 253), (3, 6, 509)]
        for (m, n, res) in ackermann_numbers:
            with self.subTest(m=m, n=n):
                self.assertEqual(ackermann(m, n), res)


class CounterTestCase(unittest.TestCase):
    def counter_test(self, counter, init, range_size):
        for i in range(init, init + range_size):
            self.assertEqual(counter(), i)

    def test_simple_counter(self):
        counter = generate_counter(0)
        self.assertEqual(counter(), 1)
        self.assertEqual(counter(), 2)
        self.assertEqual(counter(), 3)

    def test_simple_counter_with_init_value(self):
        counter = generate_counter(10)
        self.assertEqual(counter(), 11)
        self.assertEqual(counter(), 12)
        self.assertEqual(counter(), 13)

    def test_count_with_init_value(self):
        counter = generate_counter(5)
        self.counter_test(counter, 6, 100)

    def test_counter_start_with_negative_value(self):
        counter = generate_counter(-42)
        self.counter_test(counter, -41, 100)

    def test_create_two_counters(self):
        counter1 = generate_counter(0)
        counter2 = generate_counter(10)
        self.assertEqual(counter1(), 1)
        self.assertEqual(counter1(), 2)

    def test_two_counters(self):
        counter1 = generate_counter(0)
        counter2 = generate_counter(0)
        self.assertEqual(counter1(), 1)
        self.assertEqual(counter1(), 2)
        self.assertEqual(counter2(), 1)
        self.assertEqual(counter1(), 3)
        self.assertEqual(counter1(), 4)
        self.assertEqual(counter2(), 2)
        self.assertEqual(counter2(), 3)

    def test_1000_counters(self):
        init_values = [random.randint(0, 1000) for _ in range(1000)]
        counters = map(generate_counter, init_values)
        for i in range(1, 1000):
            for j, counter in enumerate(counters):
                self.assertEqual(counter(), init_values[j] + i)


class SumTestCase(unittest.TestCase):
    def test_simple_sum(self):
        self.assertEqual(infinitely_called_sum(1)(), 1)

    def test_positive_sum(self):
        self.assertEqual(infinitely_called_sum(1)(2)(8)(), 11)

    def test_sum_with_negative_number(self):
        self.assertEqual(infinitely_called_sum(-5)(), -5)
        self.assertEqual(infinitely_called_sum(1)(2)(8)(-5)(), 6)

    def test_empty_sum(self):
        self.assertEqual(infinitely_called_sum(), 0)

    def test_sum_with_zero_number(self):
        self.assertEqual(infinitely_called_sum(2)(5)(0)(), 7)
        self.assertEqual(infinitely_called_sum(2)(0)(5)(), 7)

    def test_sum_of_zero_numbers(self):
        self.assertEqual(infinitely_called_sum(0)(0)(0)(), 0)

    def test_two_sum(self):
        sum1 = infinitely_called_sum(0)(4)
        sum2 = infinitely_called_sum(4)(5)
        sum1 = sum1(10)
        sum2 = sum2(-5)(8)(15)
        self.assertEqual(sum2(), 27)
        self.assertEqual(sum1(10)(), 24)

    def test_random_sum(self):
        for _ in range(10):
            real_sum = random.randint(-1000, 10000)
            summer = infinitely_called_sum(real_sum)
            for _ in range(100000):
                random_number = random.randint(-2 ** 64, 2 ** 64)
                real_sum += random_number
                summer = summer(random_number)

            self.assertEqual(summer(), real_sum)


def mul(a, b, c):
    return a * b * c


def strange_varargs_sum(a, b, *args):
    return a + b + sum(args)


class PartialApplyTestCase(unittest.TestCase):
    def test_simple_apply(self):
        mul_part = part(mul, 1)
        self.assertEqual(mul_part(2, 3), 6)
        mul_part = part(mul, 1, 2)
        self.assertEqual(mul_part(10), 20)
        mul_part = part(mul, 1, 2, 4)
        self.assertEqual(mul_part(), 8)

    def test_apply_varargs_sum(self):
        sum_part = part(strange_varargs_sum, 1, 2, 3, 4)
        self.assertEqual(sum_part(), 10)

    def test_apply_varargs_sum_twice(self):
        sum_part = part(strange_varargs_sum, 1, 2, 3, 4)
        sum_part = part(sum_part, 5, 6, 7, 8)
        self.assertEqual(sum_part(), 36)

    def test_apply_varargs_sum_twice_and_give_finally_params(self):
        sum_part = part(strange_varargs_sum, 1, 2, 3, 4)
        sum_part = part(sum_part, 5, 6, 7, 8)
        self.assertEqual(sum_part(42, -37), 41)

    def test_reuse_apply_function(self):
        sum_part = part(strange_varargs_sum, 1)
        sum_part = part(sum_part, 2)
        self.assertEqual(sum_part(), 3)
        self.assertEqual(sum_part(3), 6)
        self.assertEqual(sum_part(7), 10)


def easy_tests(module):
    run_tests(module, globals(), ['ackermann', 'generate_counter'], [AckermannTestCase, CounterTestCase])


def hard_tests(module):
    run_tests(module, globals(), ['ackermann', 'generate_counter', ('sum', 'infinitely_called_sum'), 'part'],
              [AckermannTestCase, CounterTestCase, SumTestCase, PartialApplyTestCase])
