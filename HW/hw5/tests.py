import random
import unittest

from common.test_runner import run_tests


class DefaultDictTestCase(unittest.TestCase):
    def test_int(self):
        s = 'mississippi'
        d = mydefaultdict(int)
        for k in s:
            d[k] += 1
        self.assertEqual(sorted(d.items()), [('i', 4), ('m', 1), ('p', 2), ('s', 4)])

    def test_list(self):
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        d = mydefaultdict(list)
        for k, v in s:
            d[k].append(v)

        self.assertEqual(sorted(d.items()), [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])])

    def test_set(self):
        s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
        d = mydefaultdict(set)
        for k, v in s:
            d[k].add(v)

        self.assertEqual(sorted(d.items()), [('blue', {2, 4}), ('red', {1, 3})])

    def test_custom(self):
        def constant_factory(value):
            return lambda: value
        d = mydefaultdict(constant_factory('the market'))
        d.update(name='John', action='ran')
        self.assertEqual('%(name)s %(action)s to %(object)s' % d, 'John ran to the market')

    def test_constructor1(self):
        d = mydefaultdict(str, short='dict', long='dictionary')
        self.assertEqual('%(short)s %(long)s' % d, 'dict dictionary')

    def test_constructor2(self):
        d = mydefaultdict(str, {'short':'dict', 'long':'dictionary'})
        self.assertEqual('%(short)s %(long)s' % d, 'dict dictionary')
        d = mydefaultdict(str, [('short', 'dict'), ('long', 'dictionary')])
        self.assertEqual('%(short)s %(long)s' % d, 'dict dictionary')

def easy_tests(module):
    run_tests(module, globals(), ['mydefaultdict'], [DefaultDictTestCase])


def hard_tests(module):
    easy_tests(module)
