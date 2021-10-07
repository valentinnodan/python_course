class Importer:
    def __init__(self, functions=None):
        self.functions = functions if functions else []

    def default_import(self, module, globals):
        Importer.import_functions(module, self.functions, globals)

    @staticmethod
    def import_functions(module, functions, globals):
        for function in functions:
            Importer.import_function(module, function, globals)

    @staticmethod
    def import_function(module, function_name, globals):
        if isinstance(function_name, tuple) or isinstance(function_name, list):
            globals[function_name[1]] = module.__dict__[function_name[0]]
        else:
            globals[function_name] = module.__dict__[function_name]
