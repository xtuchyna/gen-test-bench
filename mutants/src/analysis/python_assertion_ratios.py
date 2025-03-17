
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


import ast
import lizard
from src.analysis.loc_analysis import get_sloc


class AssertCounter(ast.NodeVisitor):
    def xǁAssertCounterǁ__init____mutmut_orig(self):
        self.count = 0
    def xǁAssertCounterǁ__init____mutmut_1(self):
        self.count = 1
    def xǁAssertCounterǁ__init____mutmut_2(self):
        self.count = None

    xǁAssertCounterǁ__init____mutmut_mutants = {
    'xǁAssertCounterǁ__init____mutmut_1': xǁAssertCounterǁ__init____mutmut_1, 
        'xǁAssertCounterǁ__init____mutmut_2': xǁAssertCounterǁ__init____mutmut_2
    }

    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssertCounterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁAssertCounterǁ__init____mutmut_mutants"), *args, **kwargs)
        return result 

    __init__.__signature__ = _mutmut_signature(xǁAssertCounterǁ__init____mutmut_orig)
    xǁAssertCounterǁ__init____mutmut_orig.__name__ = 'xǁAssertCounterǁ__init__'



    def xǁAssertCounterǁvisit_Assert__mutmut_orig(self, node):
        self.count += 1
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Assert__mutmut_1(self, node):
        self.count -= 1
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Assert__mutmut_2(self, node):
        self.count = 1
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Assert__mutmut_3(self, node):
        self.count += 2
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Assert__mutmut_4(self, node):
        self.count += 1
        self.generic_visit(None)

    xǁAssertCounterǁvisit_Assert__mutmut_mutants = {
    'xǁAssertCounterǁvisit_Assert__mutmut_1': xǁAssertCounterǁvisit_Assert__mutmut_1, 
        'xǁAssertCounterǁvisit_Assert__mutmut_2': xǁAssertCounterǁvisit_Assert__mutmut_2, 
        'xǁAssertCounterǁvisit_Assert__mutmut_3': xǁAssertCounterǁvisit_Assert__mutmut_3, 
        'xǁAssertCounterǁvisit_Assert__mutmut_4': xǁAssertCounterǁvisit_Assert__mutmut_4
    }

    def visit_Assert(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssertCounterǁvisit_Assert__mutmut_orig"), object.__getattribute__(self, "xǁAssertCounterǁvisit_Assert__mutmut_mutants"), *args, **kwargs)
        return result 

    visit_Assert.__signature__ = _mutmut_signature(xǁAssertCounterǁvisit_Assert__mutmut_orig)
    xǁAssertCounterǁvisit_Assert__mutmut_orig.__name__ = 'xǁAssertCounterǁvisit_Assert'



    def xǁAssertCounterǁvisit_Call__mutmut_orig(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.attr.startswith('assert'):
                self.count += 1
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Call__mutmut_1(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.attr.startswith('XXassertXX'):
                self.count += 1
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Call__mutmut_2(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.attr.startswith('assert'):
                self.count -= 1
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Call__mutmut_3(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.attr.startswith('assert'):
                self.count = 1
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Call__mutmut_4(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.attr.startswith('assert'):
                self.count += 2
        self.generic_visit(node)

    def xǁAssertCounterǁvisit_Call__mutmut_5(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.attr.startswith('assert'):
                self.count += 1
        self.generic_visit(None)

    xǁAssertCounterǁvisit_Call__mutmut_mutants = {
    'xǁAssertCounterǁvisit_Call__mutmut_1': xǁAssertCounterǁvisit_Call__mutmut_1, 
        'xǁAssertCounterǁvisit_Call__mutmut_2': xǁAssertCounterǁvisit_Call__mutmut_2, 
        'xǁAssertCounterǁvisit_Call__mutmut_3': xǁAssertCounterǁvisit_Call__mutmut_3, 
        'xǁAssertCounterǁvisit_Call__mutmut_4': xǁAssertCounterǁvisit_Call__mutmut_4, 
        'xǁAssertCounterǁvisit_Call__mutmut_5': xǁAssertCounterǁvisit_Call__mutmut_5
    }

    def visit_Call(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAssertCounterǁvisit_Call__mutmut_orig"), object.__getattribute__(self, "xǁAssertCounterǁvisit_Call__mutmut_mutants"), *args, **kwargs)
        return result 

    visit_Call.__signature__ = _mutmut_signature(xǁAssertCounterǁvisit_Call__mutmut_orig)
    xǁAssertCounterǁvisit_Call__mutmut_orig.__name__ = 'xǁAssertCounterǁvisit_Call'




def x_count_assertions_in_python_file__mutmut_orig(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_1(filename):
    with open(None, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_2(filename):
    with open(filename, 'XXrXX', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_3(filename):
    with open(filename, 'r', encoding='XXutf-8XX') as f:
        tree = ast.parse(f.read(), filename)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_4(filename):
    with open( 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_5(filename):
    with open(filename, 'r',) as f:
        tree = ast.parse(f.read(), filename)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_6(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), None)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_7(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(),)
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_8(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tree = None
    counter = AssertCounter()
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_9(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename)
    counter = None
    counter.visit(tree)
    return counter.count


def x_count_assertions_in_python_file__mutmut_10(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename)
    counter = AssertCounter()
    counter.visit(None)
    return counter.count

x_count_assertions_in_python_file__mutmut_mutants = {
'x_count_assertions_in_python_file__mutmut_1': x_count_assertions_in_python_file__mutmut_1, 
    'x_count_assertions_in_python_file__mutmut_2': x_count_assertions_in_python_file__mutmut_2, 
    'x_count_assertions_in_python_file__mutmut_3': x_count_assertions_in_python_file__mutmut_3, 
    'x_count_assertions_in_python_file__mutmut_4': x_count_assertions_in_python_file__mutmut_4, 
    'x_count_assertions_in_python_file__mutmut_5': x_count_assertions_in_python_file__mutmut_5, 
    'x_count_assertions_in_python_file__mutmut_6': x_count_assertions_in_python_file__mutmut_6, 
    'x_count_assertions_in_python_file__mutmut_7': x_count_assertions_in_python_file__mutmut_7, 
    'x_count_assertions_in_python_file__mutmut_8': x_count_assertions_in_python_file__mutmut_8, 
    'x_count_assertions_in_python_file__mutmut_9': x_count_assertions_in_python_file__mutmut_9, 
    'x_count_assertions_in_python_file__mutmut_10': x_count_assertions_in_python_file__mutmut_10
}

def count_assertions_in_python_file(*args, **kwargs):
    result = _mutmut_trampoline(x_count_assertions_in_python_file__mutmut_orig, x_count_assertions_in_python_file__mutmut_mutants, *args, **kwargs)
    return result 

count_assertions_in_python_file.__signature__ = _mutmut_signature(x_count_assertions_in_python_file__mutmut_orig)
x_count_assertions_in_python_file__mutmut_orig.__name__ = 'x_count_assertions_in_python_file'




def x_compute_complexity__mutmut_orig(codepath):
    result = lizard.analyze_file(codepath)
    return sum([f.cyclomatic_complexity for f in result.function_list])


def x_compute_complexity__mutmut_1(codepath):
    result = lizard.analyze_file(None)
    return sum([f.cyclomatic_complexity for f in result.function_list])


def x_compute_complexity__mutmut_2(codepath):
    result = None
    return sum([f.cyclomatic_complexity for f in result.function_list])

x_compute_complexity__mutmut_mutants = {
'x_compute_complexity__mutmut_1': x_compute_complexity__mutmut_1, 
    'x_compute_complexity__mutmut_2': x_compute_complexity__mutmut_2
}

def compute_complexity(*args, **kwargs):
    result = _mutmut_trampoline(x_compute_complexity__mutmut_orig, x_compute_complexity__mutmut_mutants, *args, **kwargs)
    return result 

compute_complexity.__signature__ = _mutmut_signature(x_compute_complexity__mutmut_orig)
x_compute_complexity__mutmut_orig.__name__ = 'x_compute_complexity'




def x_assertions_mccabe_ratio_python__mutmut_orig(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_1(codepath, testpath):
    complexity = compute_complexity(None)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_2(codepath, testpath):
    complexity = None

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_3(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(None)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_4(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = None
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_5(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("XXAssertions: XX", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_6(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", None)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_7(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ",)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_8(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("XXComplexity: XX", complexity)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_9(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", None)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_10(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ",)
    return round(assertions_count / complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_11(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count * complexity, 2) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_12(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 3) if complexity != 0 else None


def x_assertions_mccabe_ratio_python__mutmut_13(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity == 0 else None


def x_assertions_mccabe_ratio_python__mutmut_14(codepath, testpath):
    complexity = compute_complexity(codepath)

    assertions_count = count_assertions_in_python_file(testpath)
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity, 2) if complexity != 1 else None

x_assertions_mccabe_ratio_python__mutmut_mutants = {
'x_assertions_mccabe_ratio_python__mutmut_1': x_assertions_mccabe_ratio_python__mutmut_1, 
    'x_assertions_mccabe_ratio_python__mutmut_2': x_assertions_mccabe_ratio_python__mutmut_2, 
    'x_assertions_mccabe_ratio_python__mutmut_3': x_assertions_mccabe_ratio_python__mutmut_3, 
    'x_assertions_mccabe_ratio_python__mutmut_4': x_assertions_mccabe_ratio_python__mutmut_4, 
    'x_assertions_mccabe_ratio_python__mutmut_5': x_assertions_mccabe_ratio_python__mutmut_5, 
    'x_assertions_mccabe_ratio_python__mutmut_6': x_assertions_mccabe_ratio_python__mutmut_6, 
    'x_assertions_mccabe_ratio_python__mutmut_7': x_assertions_mccabe_ratio_python__mutmut_7, 
    'x_assertions_mccabe_ratio_python__mutmut_8': x_assertions_mccabe_ratio_python__mutmut_8, 
    'x_assertions_mccabe_ratio_python__mutmut_9': x_assertions_mccabe_ratio_python__mutmut_9, 
    'x_assertions_mccabe_ratio_python__mutmut_10': x_assertions_mccabe_ratio_python__mutmut_10, 
    'x_assertions_mccabe_ratio_python__mutmut_11': x_assertions_mccabe_ratio_python__mutmut_11, 
    'x_assertions_mccabe_ratio_python__mutmut_12': x_assertions_mccabe_ratio_python__mutmut_12, 
    'x_assertions_mccabe_ratio_python__mutmut_13': x_assertions_mccabe_ratio_python__mutmut_13, 
    'x_assertions_mccabe_ratio_python__mutmut_14': x_assertions_mccabe_ratio_python__mutmut_14
}

def assertions_mccabe_ratio_python(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_mccabe_ratio_python__mutmut_orig, x_assertions_mccabe_ratio_python__mutmut_mutants, *args, **kwargs)
    return result 

assertions_mccabe_ratio_python.__signature__ = _mutmut_signature(x_assertions_mccabe_ratio_python__mutmut_orig)
x_assertions_mccabe_ratio_python__mutmut_orig.__name__ = 'x_assertions_mccabe_ratio_python'




def x_assertions_density_python__mutmut_orig(filepath):
    assertions_count = count_assertions_in_python_file(filepath)
    sloc = get_sloc(filepath)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_python__mutmut_1(filepath):
    assertions_count = count_assertions_in_python_file(None)
    sloc = get_sloc(filepath)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_python__mutmut_2(filepath):
    assertions_count = None
    sloc = get_sloc(filepath)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_python__mutmut_3(filepath):
    assertions_count = count_assertions_in_python_file(filepath)
    sloc = get_sloc(None)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_python__mutmut_4(filepath):
    assertions_count = count_assertions_in_python_file(filepath)
    sloc = None
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_python__mutmut_5(filepath):
    assertions_count = count_assertions_in_python_file(filepath)
    sloc = get_sloc(filepath)
    return round(assertions_count * sloc, 2) if sloc != 0 else None


def x_assertions_density_python__mutmut_6(filepath):
    assertions_count = count_assertions_in_python_file(filepath)
    sloc = get_sloc(filepath)
    return round(assertions_count / sloc, 3) if sloc != 0 else None


def x_assertions_density_python__mutmut_7(filepath):
    assertions_count = count_assertions_in_python_file(filepath)
    sloc = get_sloc(filepath)
    return round(assertions_count / sloc, 2) if sloc == 0 else None


def x_assertions_density_python__mutmut_8(filepath):
    assertions_count = count_assertions_in_python_file(filepath)
    sloc = get_sloc(filepath)
    return round(assertions_count / sloc, 2) if sloc != 1 else None

x_assertions_density_python__mutmut_mutants = {
'x_assertions_density_python__mutmut_1': x_assertions_density_python__mutmut_1, 
    'x_assertions_density_python__mutmut_2': x_assertions_density_python__mutmut_2, 
    'x_assertions_density_python__mutmut_3': x_assertions_density_python__mutmut_3, 
    'x_assertions_density_python__mutmut_4': x_assertions_density_python__mutmut_4, 
    'x_assertions_density_python__mutmut_5': x_assertions_density_python__mutmut_5, 
    'x_assertions_density_python__mutmut_6': x_assertions_density_python__mutmut_6, 
    'x_assertions_density_python__mutmut_7': x_assertions_density_python__mutmut_7, 
    'x_assertions_density_python__mutmut_8': x_assertions_density_python__mutmut_8
}

def assertions_density_python(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_density_python__mutmut_orig, x_assertions_density_python__mutmut_mutants, *args, **kwargs)
    return result 

assertions_density_python.__signature__ = _mutmut_signature(x_assertions_density_python__mutmut_orig)
x_assertions_density_python__mutmut_orig.__name__ = 'x_assertions_density_python'


