
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


import javalang
import lizard
from src.analysis.loc_analysis import get_sloc


def x_is_assertion_method__mutmut_orig(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_1(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'XXassertEqualsXX', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_2(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'XXassertNotEqualsXX', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_3(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'XXassertTrueXX', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_4(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'XXassertFalseXX',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_5(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'XXassertNullXX', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_6(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'XXassertNotNullXX', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_7(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'XXassertSameXX', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_8(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'XXassertNotSameXX',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_9(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'XXassertArrayEqualsXX', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_10(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'XXassertThrowsXX', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_11(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'XXassertDoesNotThrowXX', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_12(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'XXfailXX',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_13(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'XXassertThatXX', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_14(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'XXverifyXX', 'check'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_15(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'XXcheckXX'
    ]
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_16(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = None
    return method_name.startswith('assert') or method_name in assertion_methods


def x_is_assertion_method__mutmut_17(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('XXassertXX') or method_name in assertion_methods


def x_is_assertion_method__mutmut_18(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') or method_name not in assertion_methods


def x_is_assertion_method__mutmut_19(method_name):
    # List of common assertion methods in testing frameworks
    assertion_methods = [
        'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
        'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
        'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
        'assertThat', 'verify', 'check'
    ]
    return method_name.startswith('assert') and method_name in assertion_methods

x_is_assertion_method__mutmut_mutants = {
'x_is_assertion_method__mutmut_1': x_is_assertion_method__mutmut_1, 
    'x_is_assertion_method__mutmut_2': x_is_assertion_method__mutmut_2, 
    'x_is_assertion_method__mutmut_3': x_is_assertion_method__mutmut_3, 
    'x_is_assertion_method__mutmut_4': x_is_assertion_method__mutmut_4, 
    'x_is_assertion_method__mutmut_5': x_is_assertion_method__mutmut_5, 
    'x_is_assertion_method__mutmut_6': x_is_assertion_method__mutmut_6, 
    'x_is_assertion_method__mutmut_7': x_is_assertion_method__mutmut_7, 
    'x_is_assertion_method__mutmut_8': x_is_assertion_method__mutmut_8, 
    'x_is_assertion_method__mutmut_9': x_is_assertion_method__mutmut_9, 
    'x_is_assertion_method__mutmut_10': x_is_assertion_method__mutmut_10, 
    'x_is_assertion_method__mutmut_11': x_is_assertion_method__mutmut_11, 
    'x_is_assertion_method__mutmut_12': x_is_assertion_method__mutmut_12, 
    'x_is_assertion_method__mutmut_13': x_is_assertion_method__mutmut_13, 
    'x_is_assertion_method__mutmut_14': x_is_assertion_method__mutmut_14, 
    'x_is_assertion_method__mutmut_15': x_is_assertion_method__mutmut_15, 
    'x_is_assertion_method__mutmut_16': x_is_assertion_method__mutmut_16, 
    'x_is_assertion_method__mutmut_17': x_is_assertion_method__mutmut_17, 
    'x_is_assertion_method__mutmut_18': x_is_assertion_method__mutmut_18, 
    'x_is_assertion_method__mutmut_19': x_is_assertion_method__mutmut_19
}

def is_assertion_method(*args, **kwargs):
    result = _mutmut_trampoline(x_is_assertion_method__mutmut_orig, x_is_assertion_method__mutmut_mutants, *args, **kwargs)
    return result 

is_assertion_method.__signature__ = _mutmut_signature(x_is_assertion_method__mutmut_orig)
x_is_assertion_method__mutmut_orig.__name__ = 'x_is_assertion_method'



def x_count_assertions_in_file__mutmut_orig(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_1(file_path):
    count = 1
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_2(file_path):
    count = None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_3(file_path):
    count = 0
    try:
        with open(None, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_4(file_path):
    count = 0
    try:
        with open(file_path, 'XXrXX', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_5(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='XXutf-8XX') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_6(file_path):
    count = 0
    try:
        with open( 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_7(file_path):
    count = 0
    try:
        with open(file_path, 'r',) as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_8(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = None
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_9(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(None)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_10(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = None
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_11(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 1

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_12(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count -= 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_13(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count = 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_14(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 2

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_15(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = None
            if is_assertion_method(method_name):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_16(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(None):
                count += 1

    return count

def x_count_assertions_in_file__mutmut_17(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count -= 1

    return count

def x_count_assertions_in_file__mutmut_18(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count = 1

    return count

def x_count_assertions_in_file__mutmut_19(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = javalang.parse.parse(code)
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")
        return 0

    # Walk through the AST nodes
    for path, node in tree:
        # Count built-in 'assert' statements
        if isinstance(node, javalang.parser.tree.AssertStatement):
            count += 1

        # Count method calls that are assertions
        elif isinstance(node, javalang.parser.tree.MethodInvocation):
            method_name = node.member
            if is_assertion_method(method_name):
                count += 2

    return count

x_count_assertions_in_file__mutmut_mutants = {
'x_count_assertions_in_file__mutmut_1': x_count_assertions_in_file__mutmut_1, 
    'x_count_assertions_in_file__mutmut_2': x_count_assertions_in_file__mutmut_2, 
    'x_count_assertions_in_file__mutmut_3': x_count_assertions_in_file__mutmut_3, 
    'x_count_assertions_in_file__mutmut_4': x_count_assertions_in_file__mutmut_4, 
    'x_count_assertions_in_file__mutmut_5': x_count_assertions_in_file__mutmut_5, 
    'x_count_assertions_in_file__mutmut_6': x_count_assertions_in_file__mutmut_6, 
    'x_count_assertions_in_file__mutmut_7': x_count_assertions_in_file__mutmut_7, 
    'x_count_assertions_in_file__mutmut_8': x_count_assertions_in_file__mutmut_8, 
    'x_count_assertions_in_file__mutmut_9': x_count_assertions_in_file__mutmut_9, 
    'x_count_assertions_in_file__mutmut_10': x_count_assertions_in_file__mutmut_10, 
    'x_count_assertions_in_file__mutmut_11': x_count_assertions_in_file__mutmut_11, 
    'x_count_assertions_in_file__mutmut_12': x_count_assertions_in_file__mutmut_12, 
    'x_count_assertions_in_file__mutmut_13': x_count_assertions_in_file__mutmut_13, 
    'x_count_assertions_in_file__mutmut_14': x_count_assertions_in_file__mutmut_14, 
    'x_count_assertions_in_file__mutmut_15': x_count_assertions_in_file__mutmut_15, 
    'x_count_assertions_in_file__mutmut_16': x_count_assertions_in_file__mutmut_16, 
    'x_count_assertions_in_file__mutmut_17': x_count_assertions_in_file__mutmut_17, 
    'x_count_assertions_in_file__mutmut_18': x_count_assertions_in_file__mutmut_18, 
    'x_count_assertions_in_file__mutmut_19': x_count_assertions_in_file__mutmut_19
}

def count_assertions_in_file(*args, **kwargs):
    result = _mutmut_trampoline(x_count_assertions_in_file__mutmut_orig, x_count_assertions_in_file__mutmut_mutants, *args, **kwargs)
    return result 

count_assertions_in_file.__signature__ = _mutmut_signature(x_count_assertions_in_file__mutmut_orig)
x_count_assertions_in_file__mutmut_orig.__name__ = 'x_count_assertions_in_file'




def x_assertions_density_java__mutmut_orig(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if (sloc != 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_1(file_path):
    assertions_count = count_assertions_in_file(None)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if (sloc != 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_2(file_path):
    assertions_count = None
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if (sloc != 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_3(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(None)
    return round(assertions_count / sloc, 2) if (sloc != 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_4(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = None
    return round(assertions_count / sloc, 2) if (sloc != 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_5(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count * sloc, 2) if (sloc != 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_6(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 3) if (sloc != 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_7(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if (sloc == 0 and sloc is not None) else None


def x_assertions_density_java__mutmut_8(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if (sloc != 1 and sloc is not None) else None


def x_assertions_density_java__mutmut_9(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if (sloc != 0 and sloc is  None) else None


def x_assertions_density_java__mutmut_10(file_path):
    assertions_count = count_assertions_in_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if (sloc != 0 or sloc is not None) else None

x_assertions_density_java__mutmut_mutants = {
'x_assertions_density_java__mutmut_1': x_assertions_density_java__mutmut_1, 
    'x_assertions_density_java__mutmut_2': x_assertions_density_java__mutmut_2, 
    'x_assertions_density_java__mutmut_3': x_assertions_density_java__mutmut_3, 
    'x_assertions_density_java__mutmut_4': x_assertions_density_java__mutmut_4, 
    'x_assertions_density_java__mutmut_5': x_assertions_density_java__mutmut_5, 
    'x_assertions_density_java__mutmut_6': x_assertions_density_java__mutmut_6, 
    'x_assertions_density_java__mutmut_7': x_assertions_density_java__mutmut_7, 
    'x_assertions_density_java__mutmut_8': x_assertions_density_java__mutmut_8, 
    'x_assertions_density_java__mutmut_9': x_assertions_density_java__mutmut_9, 
    'x_assertions_density_java__mutmut_10': x_assertions_density_java__mutmut_10
}

def assertions_density_java(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_density_java__mutmut_orig, x_assertions_density_java__mutmut_mutants, *args, **kwargs)
    return result 

assertions_density_java.__signature__ = _mutmut_signature(x_assertions_density_java__mutmut_orig)
x_assertions_density_java__mutmut_orig.__name__ = 'x_assertions_density_java'




def x_assertions_mccabe_ratio_java__mutmut_orig(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_1(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(None)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_2(code_file_path, test_file_path):
    assertions_count = None
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_3(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(None)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_4(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = None
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_5(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = None
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_6(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("XXAssertions: XX", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_7(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", None)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_8(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ",)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_9(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("XXComplexity: XX", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_10(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", None)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_11(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ",)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_12(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count * complexity) if (complexity != 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_13(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity == 0 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_14(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 1 and complexity is not None) else None


def x_assertions_mccabe_ratio_java__mutmut_15(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 and complexity is  None) else None


def x_assertions_mccabe_ratio_java__mutmut_16(code_file_path, test_file_path):
    assertions_count = count_assertions_in_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if (complexity != 0 or complexity is not None) else None

x_assertions_mccabe_ratio_java__mutmut_mutants = {
'x_assertions_mccabe_ratio_java__mutmut_1': x_assertions_mccabe_ratio_java__mutmut_1, 
    'x_assertions_mccabe_ratio_java__mutmut_2': x_assertions_mccabe_ratio_java__mutmut_2, 
    'x_assertions_mccabe_ratio_java__mutmut_3': x_assertions_mccabe_ratio_java__mutmut_3, 
    'x_assertions_mccabe_ratio_java__mutmut_4': x_assertions_mccabe_ratio_java__mutmut_4, 
    'x_assertions_mccabe_ratio_java__mutmut_5': x_assertions_mccabe_ratio_java__mutmut_5, 
    'x_assertions_mccabe_ratio_java__mutmut_6': x_assertions_mccabe_ratio_java__mutmut_6, 
    'x_assertions_mccabe_ratio_java__mutmut_7': x_assertions_mccabe_ratio_java__mutmut_7, 
    'x_assertions_mccabe_ratio_java__mutmut_8': x_assertions_mccabe_ratio_java__mutmut_8, 
    'x_assertions_mccabe_ratio_java__mutmut_9': x_assertions_mccabe_ratio_java__mutmut_9, 
    'x_assertions_mccabe_ratio_java__mutmut_10': x_assertions_mccabe_ratio_java__mutmut_10, 
    'x_assertions_mccabe_ratio_java__mutmut_11': x_assertions_mccabe_ratio_java__mutmut_11, 
    'x_assertions_mccabe_ratio_java__mutmut_12': x_assertions_mccabe_ratio_java__mutmut_12, 
    'x_assertions_mccabe_ratio_java__mutmut_13': x_assertions_mccabe_ratio_java__mutmut_13, 
    'x_assertions_mccabe_ratio_java__mutmut_14': x_assertions_mccabe_ratio_java__mutmut_14, 
    'x_assertions_mccabe_ratio_java__mutmut_15': x_assertions_mccabe_ratio_java__mutmut_15, 
    'x_assertions_mccabe_ratio_java__mutmut_16': x_assertions_mccabe_ratio_java__mutmut_16
}

def assertions_mccabe_ratio_java(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_mccabe_ratio_java__mutmut_orig, x_assertions_mccabe_ratio_java__mutmut_mutants, *args, **kwargs)
    return result 

assertions_mccabe_ratio_java.__signature__ = _mutmut_signature(x_assertions_mccabe_ratio_java__mutmut_orig)
x_assertions_mccabe_ratio_java__mutmut_orig.__name__ = 'x_assertions_mccabe_ratio_java'


