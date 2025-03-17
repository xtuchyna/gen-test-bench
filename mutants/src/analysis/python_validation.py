
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


from enum import Enum

from src.helpers import is_not_blank


class CompileStatus(Enum):
    OK = 1
    SYNTAX_ERROR = 2
    EXCEPTION_OCCURRED = 3
    EMPTY = 4


def x_check_syntax_file__mutmut_orig(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_1(filepath) -> CompileStatus:
    try:
        with open(None, 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_2(filepath) -> CompileStatus:
    try:
        with open(filepath, 'XXrXX') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_3(filepath) -> CompileStatus:
    try:
        with open( 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_4(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = None
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_5(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if  is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_6(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if not is_not_blank(None):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_7(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(None, filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_8(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, None, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_9(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, filepath, 'XXexecXX')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_10(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile( filepath, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_file__mutmut_11(filepath) -> CompileStatus:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
            if not is_not_blank(source_code):
                return CompileStatus.EMPTY
            compile(source_code, 'exec')
            print(f"{filepath} is syntactically correct.")
            return CompileStatus.OK
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED

x_check_syntax_file__mutmut_mutants = {
'x_check_syntax_file__mutmut_1': x_check_syntax_file__mutmut_1, 
    'x_check_syntax_file__mutmut_2': x_check_syntax_file__mutmut_2, 
    'x_check_syntax_file__mutmut_3': x_check_syntax_file__mutmut_3, 
    'x_check_syntax_file__mutmut_4': x_check_syntax_file__mutmut_4, 
    'x_check_syntax_file__mutmut_5': x_check_syntax_file__mutmut_5, 
    'x_check_syntax_file__mutmut_6': x_check_syntax_file__mutmut_6, 
    'x_check_syntax_file__mutmut_7': x_check_syntax_file__mutmut_7, 
    'x_check_syntax_file__mutmut_8': x_check_syntax_file__mutmut_8, 
    'x_check_syntax_file__mutmut_9': x_check_syntax_file__mutmut_9, 
    'x_check_syntax_file__mutmut_10': x_check_syntax_file__mutmut_10, 
    'x_check_syntax_file__mutmut_11': x_check_syntax_file__mutmut_11
}

def check_syntax_file(*args, **kwargs):
    result = _mutmut_trampoline(x_check_syntax_file__mutmut_orig, x_check_syntax_file__mutmut_mutants, *args, **kwargs)
    return result 

check_syntax_file.__signature__ = _mutmut_signature(x_check_syntax_file__mutmut_orig)
x_check_syntax_file__mutmut_orig.__name__ = 'x_check_syntax_file'




def x_check_syntax_string__mutmut_orig(code_string) -> CompileStatus:
    try:
        compile(code_string, '<string>', 'exec')
        return CompileStatus.OK
    except SyntaxError as e:
        print(e)
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_string__mutmut_1(code_string) -> CompileStatus:
    try:
        compile(None, '<string>', 'exec')
        return CompileStatus.OK
    except SyntaxError as e:
        print(e)
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_string__mutmut_2(code_string) -> CompileStatus:
    try:
        compile(code_string, 'XX<string>XX', 'exec')
        return CompileStatus.OK
    except SyntaxError as e:
        print(e)
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_string__mutmut_3(code_string) -> CompileStatus:
    try:
        compile(code_string, '<string>', 'XXexecXX')
        return CompileStatus.OK
    except SyntaxError as e:
        print(e)
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_string__mutmut_4(code_string) -> CompileStatus:
    try:
        compile( '<string>', 'exec')
        return CompileStatus.OK
    except SyntaxError as e:
        print(e)
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_check_syntax_string__mutmut_5(code_string) -> CompileStatus:
    try:
        compile(code_string, '<string>', 'exec')
        return CompileStatus.OK
    except SyntaxError as e:
        print(None)
        return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print(f"An error occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED

x_check_syntax_string__mutmut_mutants = {
'x_check_syntax_string__mutmut_1': x_check_syntax_string__mutmut_1, 
    'x_check_syntax_string__mutmut_2': x_check_syntax_string__mutmut_2, 
    'x_check_syntax_string__mutmut_3': x_check_syntax_string__mutmut_3, 
    'x_check_syntax_string__mutmut_4': x_check_syntax_string__mutmut_4, 
    'x_check_syntax_string__mutmut_5': x_check_syntax_string__mutmut_5
}

def check_syntax_string(*args, **kwargs):
    result = _mutmut_trampoline(x_check_syntax_string__mutmut_orig, x_check_syntax_string__mutmut_mutants, *args, **kwargs)
    return result 

check_syntax_string.__signature__ = _mutmut_signature(x_check_syntax_string__mutmut_orig)
x_check_syntax_string__mutmut_orig.__name__ = 'x_check_syntax_string'


