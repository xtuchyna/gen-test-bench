
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


import lizard
from pygments import lex
from pygments.lexers.go import GoLexer
from pygments.token import Token

from src.analysis.loc_analysis import get_sloc


# List of common assertion methods in Go
go_assertion_methods = [
    # Standard library testing functions
    'Error', 'Errorf', 'Fatal', 'Fatalf', 'Fail', 'FailNow',
    # Third-party libraries like testify
    'Equal', 'NotEqual', 'Nil', 'NotNil', 'Contains',
    # Gomega and other libraries
    'Expect', 'Should', 'ShouldNot', 'BeTrue', 'BeFalse', 'MatchError',
    'HaveOccurred', 'Succeed',
]


def x_count_assertions_in_go_file__mutmut_orig(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_1(file_path):
    count = 1
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_2(file_path):
    count = None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_3(file_path):
    count = 0
    try:
        with open(None, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_4(file_path):
    count = 0
    try:
        with open(file_path, 'XXrXX', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_5(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='XXutf-8XX') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_6(file_path):
    count = 0
    try:
        with open( 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_7(file_path):
    count = 0
    try:
        with open(file_path, 'r',) as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_8(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = None
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_9(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(None, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_10(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex( GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_11(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = None
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_12(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(None)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_13(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = None
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_14(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 1
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_15(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = None
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_16(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i <= len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_17(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[None]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_18(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = None
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_19(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type != Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_20(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value not in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_21(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other or token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_22(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i - 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_23(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 2
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_24(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = None
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_25(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j <= len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_26(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[None][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_27(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][1] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_28(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][None] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_29(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] not in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_30(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) or tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_31(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j -= 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_32(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j = 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_33(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 2
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_34(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j <= len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_35(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[None][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_36(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][2] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_37(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][None] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_38(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] != '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_39(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == 'XX(XX':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_40(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) or tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_41(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count -= 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_42(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count = 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_43(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 2
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_44(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = None  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_45(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i -= 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_46(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i = 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_go_file__mutmut_47(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, GoLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name.Other and token_value in go_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 2
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

x_count_assertions_in_go_file__mutmut_mutants = {
'x_count_assertions_in_go_file__mutmut_1': x_count_assertions_in_go_file__mutmut_1, 
    'x_count_assertions_in_go_file__mutmut_2': x_count_assertions_in_go_file__mutmut_2, 
    'x_count_assertions_in_go_file__mutmut_3': x_count_assertions_in_go_file__mutmut_3, 
    'x_count_assertions_in_go_file__mutmut_4': x_count_assertions_in_go_file__mutmut_4, 
    'x_count_assertions_in_go_file__mutmut_5': x_count_assertions_in_go_file__mutmut_5, 
    'x_count_assertions_in_go_file__mutmut_6': x_count_assertions_in_go_file__mutmut_6, 
    'x_count_assertions_in_go_file__mutmut_7': x_count_assertions_in_go_file__mutmut_7, 
    'x_count_assertions_in_go_file__mutmut_8': x_count_assertions_in_go_file__mutmut_8, 
    'x_count_assertions_in_go_file__mutmut_9': x_count_assertions_in_go_file__mutmut_9, 
    'x_count_assertions_in_go_file__mutmut_10': x_count_assertions_in_go_file__mutmut_10, 
    'x_count_assertions_in_go_file__mutmut_11': x_count_assertions_in_go_file__mutmut_11, 
    'x_count_assertions_in_go_file__mutmut_12': x_count_assertions_in_go_file__mutmut_12, 
    'x_count_assertions_in_go_file__mutmut_13': x_count_assertions_in_go_file__mutmut_13, 
    'x_count_assertions_in_go_file__mutmut_14': x_count_assertions_in_go_file__mutmut_14, 
    'x_count_assertions_in_go_file__mutmut_15': x_count_assertions_in_go_file__mutmut_15, 
    'x_count_assertions_in_go_file__mutmut_16': x_count_assertions_in_go_file__mutmut_16, 
    'x_count_assertions_in_go_file__mutmut_17': x_count_assertions_in_go_file__mutmut_17, 
    'x_count_assertions_in_go_file__mutmut_18': x_count_assertions_in_go_file__mutmut_18, 
    'x_count_assertions_in_go_file__mutmut_19': x_count_assertions_in_go_file__mutmut_19, 
    'x_count_assertions_in_go_file__mutmut_20': x_count_assertions_in_go_file__mutmut_20, 
    'x_count_assertions_in_go_file__mutmut_21': x_count_assertions_in_go_file__mutmut_21, 
    'x_count_assertions_in_go_file__mutmut_22': x_count_assertions_in_go_file__mutmut_22, 
    'x_count_assertions_in_go_file__mutmut_23': x_count_assertions_in_go_file__mutmut_23, 
    'x_count_assertions_in_go_file__mutmut_24': x_count_assertions_in_go_file__mutmut_24, 
    'x_count_assertions_in_go_file__mutmut_25': x_count_assertions_in_go_file__mutmut_25, 
    'x_count_assertions_in_go_file__mutmut_26': x_count_assertions_in_go_file__mutmut_26, 
    'x_count_assertions_in_go_file__mutmut_27': x_count_assertions_in_go_file__mutmut_27, 
    'x_count_assertions_in_go_file__mutmut_28': x_count_assertions_in_go_file__mutmut_28, 
    'x_count_assertions_in_go_file__mutmut_29': x_count_assertions_in_go_file__mutmut_29, 
    'x_count_assertions_in_go_file__mutmut_30': x_count_assertions_in_go_file__mutmut_30, 
    'x_count_assertions_in_go_file__mutmut_31': x_count_assertions_in_go_file__mutmut_31, 
    'x_count_assertions_in_go_file__mutmut_32': x_count_assertions_in_go_file__mutmut_32, 
    'x_count_assertions_in_go_file__mutmut_33': x_count_assertions_in_go_file__mutmut_33, 
    'x_count_assertions_in_go_file__mutmut_34': x_count_assertions_in_go_file__mutmut_34, 
    'x_count_assertions_in_go_file__mutmut_35': x_count_assertions_in_go_file__mutmut_35, 
    'x_count_assertions_in_go_file__mutmut_36': x_count_assertions_in_go_file__mutmut_36, 
    'x_count_assertions_in_go_file__mutmut_37': x_count_assertions_in_go_file__mutmut_37, 
    'x_count_assertions_in_go_file__mutmut_38': x_count_assertions_in_go_file__mutmut_38, 
    'x_count_assertions_in_go_file__mutmut_39': x_count_assertions_in_go_file__mutmut_39, 
    'x_count_assertions_in_go_file__mutmut_40': x_count_assertions_in_go_file__mutmut_40, 
    'x_count_assertions_in_go_file__mutmut_41': x_count_assertions_in_go_file__mutmut_41, 
    'x_count_assertions_in_go_file__mutmut_42': x_count_assertions_in_go_file__mutmut_42, 
    'x_count_assertions_in_go_file__mutmut_43': x_count_assertions_in_go_file__mutmut_43, 
    'x_count_assertions_in_go_file__mutmut_44': x_count_assertions_in_go_file__mutmut_44, 
    'x_count_assertions_in_go_file__mutmut_45': x_count_assertions_in_go_file__mutmut_45, 
    'x_count_assertions_in_go_file__mutmut_46': x_count_assertions_in_go_file__mutmut_46, 
    'x_count_assertions_in_go_file__mutmut_47': x_count_assertions_in_go_file__mutmut_47
}

def count_assertions_in_go_file(*args, **kwargs):
    result = _mutmut_trampoline(x_count_assertions_in_go_file__mutmut_orig, x_count_assertions_in_go_file__mutmut_mutants, *args, **kwargs)
    return result 

count_assertions_in_go_file.__signature__ = _mutmut_signature(x_count_assertions_in_go_file__mutmut_orig)
x_count_assertions_in_go_file__mutmut_orig.__name__ = 'x_count_assertions_in_go_file'




def x_assertions_mccabe_ratio_go__mutmut_orig(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_1(go_file, test_file):
    result = lizard.analyze_file(None)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_2(go_file, test_file):
    result = None
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_3(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = None
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_4(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(None)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_5(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = None

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_6(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("XXAssertion count: XX", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_7(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", None)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_8(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ",)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_9(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("XXComplexity number: XX", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_10(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", None)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_11(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ",)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_12(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count * complexity_number, 2) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_13(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 3) if complexity_number != 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_14(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number == 0 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_15(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = round(assertion_count / complexity_number, 2) if complexity_number != 1 else None
    return mccabe_ratio


def x_assertions_mccabe_ratio_go__mutmut_16(go_file, test_file):
    result = lizard.analyze_file(go_file)
    complexity_number = sum([f.cyclomatic_complexity for f in result.function_list])
    assertion_count = count_assertions_in_go_file(test_file)

    print("Assertion count: ", assertion_count)
    print("Complexity number: ", complexity_number)
    mccabe_ratio = None
    return mccabe_ratio

x_assertions_mccabe_ratio_go__mutmut_mutants = {
'x_assertions_mccabe_ratio_go__mutmut_1': x_assertions_mccabe_ratio_go__mutmut_1, 
    'x_assertions_mccabe_ratio_go__mutmut_2': x_assertions_mccabe_ratio_go__mutmut_2, 
    'x_assertions_mccabe_ratio_go__mutmut_3': x_assertions_mccabe_ratio_go__mutmut_3, 
    'x_assertions_mccabe_ratio_go__mutmut_4': x_assertions_mccabe_ratio_go__mutmut_4, 
    'x_assertions_mccabe_ratio_go__mutmut_5': x_assertions_mccabe_ratio_go__mutmut_5, 
    'x_assertions_mccabe_ratio_go__mutmut_6': x_assertions_mccabe_ratio_go__mutmut_6, 
    'x_assertions_mccabe_ratio_go__mutmut_7': x_assertions_mccabe_ratio_go__mutmut_7, 
    'x_assertions_mccabe_ratio_go__mutmut_8': x_assertions_mccabe_ratio_go__mutmut_8, 
    'x_assertions_mccabe_ratio_go__mutmut_9': x_assertions_mccabe_ratio_go__mutmut_9, 
    'x_assertions_mccabe_ratio_go__mutmut_10': x_assertions_mccabe_ratio_go__mutmut_10, 
    'x_assertions_mccabe_ratio_go__mutmut_11': x_assertions_mccabe_ratio_go__mutmut_11, 
    'x_assertions_mccabe_ratio_go__mutmut_12': x_assertions_mccabe_ratio_go__mutmut_12, 
    'x_assertions_mccabe_ratio_go__mutmut_13': x_assertions_mccabe_ratio_go__mutmut_13, 
    'x_assertions_mccabe_ratio_go__mutmut_14': x_assertions_mccabe_ratio_go__mutmut_14, 
    'x_assertions_mccabe_ratio_go__mutmut_15': x_assertions_mccabe_ratio_go__mutmut_15, 
    'x_assertions_mccabe_ratio_go__mutmut_16': x_assertions_mccabe_ratio_go__mutmut_16
}

def assertions_mccabe_ratio_go(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_mccabe_ratio_go__mutmut_orig, x_assertions_mccabe_ratio_go__mutmut_mutants, *args, **kwargs)
    return result 

assertions_mccabe_ratio_go.__signature__ = _mutmut_signature(x_assertions_mccabe_ratio_go__mutmut_orig)
x_assertions_mccabe_ratio_go__mutmut_orig.__name__ = 'x_assertions_mccabe_ratio_go'




def x_assertions_density_go__mutmut_orig(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_1(test_file):
    assertions_count = count_assertions_in_go_file(None)
    sloc = get_sloc(test_file)
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_2(test_file):
    assertions_count = None
    sloc = get_sloc(test_file)
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_3(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(None)
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_4(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = None
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_5(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("XXSLOC:XX", sloc)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_6(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("SLOC:", None)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_7(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("SLOC:",)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_8(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("SLOC:", sloc)
    return round(assertions_count * sloc, 2) if sloc != 0 else None


def x_assertions_density_go__mutmut_9(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 3) if sloc != 0 else None


def x_assertions_density_go__mutmut_10(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 2) if sloc == 0 else None


def x_assertions_density_go__mutmut_11(test_file):
    assertions_count = count_assertions_in_go_file(test_file)
    sloc = get_sloc(test_file)
    print("SLOC:", sloc)
    return round(assertions_count / sloc, 2) if sloc != 1 else None

x_assertions_density_go__mutmut_mutants = {
'x_assertions_density_go__mutmut_1': x_assertions_density_go__mutmut_1, 
    'x_assertions_density_go__mutmut_2': x_assertions_density_go__mutmut_2, 
    'x_assertions_density_go__mutmut_3': x_assertions_density_go__mutmut_3, 
    'x_assertions_density_go__mutmut_4': x_assertions_density_go__mutmut_4, 
    'x_assertions_density_go__mutmut_5': x_assertions_density_go__mutmut_5, 
    'x_assertions_density_go__mutmut_6': x_assertions_density_go__mutmut_6, 
    'x_assertions_density_go__mutmut_7': x_assertions_density_go__mutmut_7, 
    'x_assertions_density_go__mutmut_8': x_assertions_density_go__mutmut_8, 
    'x_assertions_density_go__mutmut_9': x_assertions_density_go__mutmut_9, 
    'x_assertions_density_go__mutmut_10': x_assertions_density_go__mutmut_10, 
    'x_assertions_density_go__mutmut_11': x_assertions_density_go__mutmut_11
}

def assertions_density_go(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_density_go__mutmut_orig, x_assertions_density_go__mutmut_mutants, *args, **kwargs)
    return result 

assertions_density_go.__signature__ = _mutmut_signature(x_assertions_density_go__mutmut_orig)
x_assertions_density_go__mutmut_orig.__name__ = 'x_assertions_density_go'


