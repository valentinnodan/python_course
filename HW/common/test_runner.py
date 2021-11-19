import unittest
from pathlib import Path
import importlib.util

from common.importer import Importer

TEST_DIR_OVERRIDES = {}


def find_first_exist_dir(dirs, prefix='.', error_message='existing directory not found'):
    exist_dirs = [Path.cwd() / prefix / d for d in dirs if d and (Path.cwd() / prefix / d).is_dir()]
    if len(exist_dirs) == 0:
        raise ValueError(error_message)

    return exist_dirs[0].resolve()


def import_by_path(module, path):
    spec = importlib.util.spec_from_file_location(module, path)
    import_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(import_module)
    return import_module


class TestRunner:
    def __init__(self, hw_number, difficulty, src_dir='.', main_file='__init__.py', dir_overrides=None):
        self.hw_number = hw_number
        self.difficulty = difficulty
        self.dir_overrides = dir_overrides if dir_overrides is not None else TEST_DIR_OVERRIDES

        self.test_dir = self.get_test_src_dir()
        self.src_dir = find_first_exist_dir([src_dir],
                                            error_message=f'directory {(Path.cwd() / src_dir).resolve()} dont exist')
        self.src_main_file = self.src_dir / main_file

        self.hw_module = import_by_path("hw_code", self.src_main_file)
        self.test_module = import_by_path("hw_test_code", self.test_dir / 'tests.py')

    def get_test_src_dir(self):
        return find_first_exist_dir(self._get_default_dir_names(), prefix='HW' if Path.cwd().parts[-1] != 'HW' else '.',
                                    error_message=f'directory with test sources for hw {self.hw_number} not found')

    def _get_default_dir_names(self):
        hw = self.hw_number
        return [self.dir_overrides.get(hw), f'hw{hw}', f'HW{hw}']

    def run(self):
        print(f"Run hw {self.hw_number} {self.difficulty} for {self.src_main_file}")
        if self.difficulty == "hard":
            self.test_module.hard_tests(self.hw_module)
        else:
            self.test_module.easy_tests(self.hw_module)


def run_tests(module, globals, import_functions, test_causes):
    importer = Importer(import_functions)
    importer.default_import(module, globals)

    test_load = unittest.TestLoader()
    suites = [test_load.loadTestsFromTestCase(test_cause) for test_cause in test_causes]

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unittest.TestSuite(suites))
