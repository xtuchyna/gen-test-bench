
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
from pygments.lexers.jvm import KotlinLexer
from pygments.token import Token

from src.analysis.loc_analysis import get_sloc

kotlin_assertion_methods = [
    # JUnit assertions
    'assertEquals', 'assertNotEquals', 'assertTrue', 'assertFalse',
    'assertNull', 'assertNotNull', 'assertSame', 'assertNotSame',
    'assertArrayEquals', 'assertThrows', 'assertDoesNotThrow', 'fail',
    # kotlin.test assertions
    'assertContentEquals', 'assertFailsWith', 'assertFails',
    # Kotest assertions
    'shouldBe', 'shouldNotBe', 'shouldContain', 'shouldNotContain',
    'shouldThrow', 'shouldNotThrow', 'shouldStartWith', 'shouldEndWith',
    'shouldBeEmpty', 'shouldNotBeEmpty', 'shouldHaveSize',
    # Built-in 'assert' function
    'assert',
]


def x_count_assertions_in_kotlin_file__mutmut_orig(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_1(file_path):
    count = 1
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_2(file_path):
    count = None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_3(file_path):
    count = 0
    try:
        with open(None, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_4(file_path):
    count = 0
    try:
        with open(file_path, 'XXrXX', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_5(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='XXutf-8XX') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_6(file_path):
    count = 0
    try:
        with open( 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_7(file_path):
    count = 0
    try:
        with open(file_path, 'r',) as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_8(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = None
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_9(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(None, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_10(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex( KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_11(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = None
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_12(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(None)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_13(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = None
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_14(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 1
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_15(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = None
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_16(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i <= len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_17(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[None]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_18(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = None
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_19(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type != Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_20(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value not in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_21(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name or token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_22(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i - 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_23(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 2
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_24(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = None
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_25(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j <= len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_26(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[None][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_27(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][1] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_28(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][None] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_29(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] not in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_30(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) or tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_31(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j -= 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_32(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j = 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_33(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 2
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_34(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j <= len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_35(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[None][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_36(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][2] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_37(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][None] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_38(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] != '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_39(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == 'XX(XX':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_40(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) or tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_41(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count -= 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_42(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count = 1
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_43(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 2
                    i = j  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_44(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = None  # Move to the next token after '('
            i += 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_45(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i -= 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_46(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i = 1
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def x_count_assertions_in_kotlin_file__mutmut_47(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tokens = lex(code, KotlinLexer())
        tokens_list = list(tokens)
        i = 0
        while i < len(tokens_list):
            token_type, token_value = tokens_list[i]
            if token_type == Token.Name and token_value in kotlin_assertion_methods:
                j = i + 1
                while j < len(tokens_list) and tokens_list[j][0] in (
                Token.Text, Token.Comment.Single, Token.Comment.Multiline):
                    j += 1
                if j < len(tokens_list) and tokens_list[j][1] == '(':
                    count += 1
                    i = j  # Move to the next token after '('
            i += 2
        return count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

x_count_assertions_in_kotlin_file__mutmut_mutants = {
'x_count_assertions_in_kotlin_file__mutmut_1': x_count_assertions_in_kotlin_file__mutmut_1, 
    'x_count_assertions_in_kotlin_file__mutmut_2': x_count_assertions_in_kotlin_file__mutmut_2, 
    'x_count_assertions_in_kotlin_file__mutmut_3': x_count_assertions_in_kotlin_file__mutmut_3, 
    'x_count_assertions_in_kotlin_file__mutmut_4': x_count_assertions_in_kotlin_file__mutmut_4, 
    'x_count_assertions_in_kotlin_file__mutmut_5': x_count_assertions_in_kotlin_file__mutmut_5, 
    'x_count_assertions_in_kotlin_file__mutmut_6': x_count_assertions_in_kotlin_file__mutmut_6, 
    'x_count_assertions_in_kotlin_file__mutmut_7': x_count_assertions_in_kotlin_file__mutmut_7, 
    'x_count_assertions_in_kotlin_file__mutmut_8': x_count_assertions_in_kotlin_file__mutmut_8, 
    'x_count_assertions_in_kotlin_file__mutmut_9': x_count_assertions_in_kotlin_file__mutmut_9, 
    'x_count_assertions_in_kotlin_file__mutmut_10': x_count_assertions_in_kotlin_file__mutmut_10, 
    'x_count_assertions_in_kotlin_file__mutmut_11': x_count_assertions_in_kotlin_file__mutmut_11, 
    'x_count_assertions_in_kotlin_file__mutmut_12': x_count_assertions_in_kotlin_file__mutmut_12, 
    'x_count_assertions_in_kotlin_file__mutmut_13': x_count_assertions_in_kotlin_file__mutmut_13, 
    'x_count_assertions_in_kotlin_file__mutmut_14': x_count_assertions_in_kotlin_file__mutmut_14, 
    'x_count_assertions_in_kotlin_file__mutmut_15': x_count_assertions_in_kotlin_file__mutmut_15, 
    'x_count_assertions_in_kotlin_file__mutmut_16': x_count_assertions_in_kotlin_file__mutmut_16, 
    'x_count_assertions_in_kotlin_file__mutmut_17': x_count_assertions_in_kotlin_file__mutmut_17, 
    'x_count_assertions_in_kotlin_file__mutmut_18': x_count_assertions_in_kotlin_file__mutmut_18, 
    'x_count_assertions_in_kotlin_file__mutmut_19': x_count_assertions_in_kotlin_file__mutmut_19, 
    'x_count_assertions_in_kotlin_file__mutmut_20': x_count_assertions_in_kotlin_file__mutmut_20, 
    'x_count_assertions_in_kotlin_file__mutmut_21': x_count_assertions_in_kotlin_file__mutmut_21, 
    'x_count_assertions_in_kotlin_file__mutmut_22': x_count_assertions_in_kotlin_file__mutmut_22, 
    'x_count_assertions_in_kotlin_file__mutmut_23': x_count_assertions_in_kotlin_file__mutmut_23, 
    'x_count_assertions_in_kotlin_file__mutmut_24': x_count_assertions_in_kotlin_file__mutmut_24, 
    'x_count_assertions_in_kotlin_file__mutmut_25': x_count_assertions_in_kotlin_file__mutmut_25, 
    'x_count_assertions_in_kotlin_file__mutmut_26': x_count_assertions_in_kotlin_file__mutmut_26, 
    'x_count_assertions_in_kotlin_file__mutmut_27': x_count_assertions_in_kotlin_file__mutmut_27, 
    'x_count_assertions_in_kotlin_file__mutmut_28': x_count_assertions_in_kotlin_file__mutmut_28, 
    'x_count_assertions_in_kotlin_file__mutmut_29': x_count_assertions_in_kotlin_file__mutmut_29, 
    'x_count_assertions_in_kotlin_file__mutmut_30': x_count_assertions_in_kotlin_file__mutmut_30, 
    'x_count_assertions_in_kotlin_file__mutmut_31': x_count_assertions_in_kotlin_file__mutmut_31, 
    'x_count_assertions_in_kotlin_file__mutmut_32': x_count_assertions_in_kotlin_file__mutmut_32, 
    'x_count_assertions_in_kotlin_file__mutmut_33': x_count_assertions_in_kotlin_file__mutmut_33, 
    'x_count_assertions_in_kotlin_file__mutmut_34': x_count_assertions_in_kotlin_file__mutmut_34, 
    'x_count_assertions_in_kotlin_file__mutmut_35': x_count_assertions_in_kotlin_file__mutmut_35, 
    'x_count_assertions_in_kotlin_file__mutmut_36': x_count_assertions_in_kotlin_file__mutmut_36, 
    'x_count_assertions_in_kotlin_file__mutmut_37': x_count_assertions_in_kotlin_file__mutmut_37, 
    'x_count_assertions_in_kotlin_file__mutmut_38': x_count_assertions_in_kotlin_file__mutmut_38, 
    'x_count_assertions_in_kotlin_file__mutmut_39': x_count_assertions_in_kotlin_file__mutmut_39, 
    'x_count_assertions_in_kotlin_file__mutmut_40': x_count_assertions_in_kotlin_file__mutmut_40, 
    'x_count_assertions_in_kotlin_file__mutmut_41': x_count_assertions_in_kotlin_file__mutmut_41, 
    'x_count_assertions_in_kotlin_file__mutmut_42': x_count_assertions_in_kotlin_file__mutmut_42, 
    'x_count_assertions_in_kotlin_file__mutmut_43': x_count_assertions_in_kotlin_file__mutmut_43, 
    'x_count_assertions_in_kotlin_file__mutmut_44': x_count_assertions_in_kotlin_file__mutmut_44, 
    'x_count_assertions_in_kotlin_file__mutmut_45': x_count_assertions_in_kotlin_file__mutmut_45, 
    'x_count_assertions_in_kotlin_file__mutmut_46': x_count_assertions_in_kotlin_file__mutmut_46, 
    'x_count_assertions_in_kotlin_file__mutmut_47': x_count_assertions_in_kotlin_file__mutmut_47
}

def count_assertions_in_kotlin_file(*args, **kwargs):
    result = _mutmut_trampoline(x_count_assertions_in_kotlin_file__mutmut_orig, x_count_assertions_in_kotlin_file__mutmut_mutants, *args, **kwargs)
    return result 

count_assertions_in_kotlin_file.__signature__ = _mutmut_signature(x_count_assertions_in_kotlin_file__mutmut_orig)
x_count_assertions_in_kotlin_file__mutmut_orig.__name__ = 'x_count_assertions_in_kotlin_file'




def x_assertions_mccabe_ratio_kotlin__mutmut_orig(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_1(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(None)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_2(code_file_path, test_file_path):
    assertions_count = None
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_3(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(None)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_4(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = None
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_5(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = None
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_6(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("XXAssertions: XX", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_7(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", None)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_8(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ",)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_9(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("XXComplexity: XX", complexity)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_10(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", None)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_11(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ",)
    return round(assertions_count / complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_12(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count * complexity) if complexity != 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_13(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity == 0 else None


def x_assertions_mccabe_ratio_kotlin__mutmut_14(code_file_path, test_file_path):
    assertions_count = count_assertions_in_kotlin_file(test_file_path)
    result = lizard.analyze_file(code_file_path)
    complexity = sum([f.cyclomatic_complexity for f in result.function_list])
    print("Assertions: ", assertions_count)
    print("Complexity: ", complexity)
    return round(assertions_count / complexity) if complexity != 1 else None

x_assertions_mccabe_ratio_kotlin__mutmut_mutants = {
'x_assertions_mccabe_ratio_kotlin__mutmut_1': x_assertions_mccabe_ratio_kotlin__mutmut_1, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_2': x_assertions_mccabe_ratio_kotlin__mutmut_2, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_3': x_assertions_mccabe_ratio_kotlin__mutmut_3, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_4': x_assertions_mccabe_ratio_kotlin__mutmut_4, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_5': x_assertions_mccabe_ratio_kotlin__mutmut_5, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_6': x_assertions_mccabe_ratio_kotlin__mutmut_6, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_7': x_assertions_mccabe_ratio_kotlin__mutmut_7, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_8': x_assertions_mccabe_ratio_kotlin__mutmut_8, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_9': x_assertions_mccabe_ratio_kotlin__mutmut_9, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_10': x_assertions_mccabe_ratio_kotlin__mutmut_10, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_11': x_assertions_mccabe_ratio_kotlin__mutmut_11, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_12': x_assertions_mccabe_ratio_kotlin__mutmut_12, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_13': x_assertions_mccabe_ratio_kotlin__mutmut_13, 
    'x_assertions_mccabe_ratio_kotlin__mutmut_14': x_assertions_mccabe_ratio_kotlin__mutmut_14
}

def assertions_mccabe_ratio_kotlin(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_mccabe_ratio_kotlin__mutmut_orig, x_assertions_mccabe_ratio_kotlin__mutmut_mutants, *args, **kwargs)
    return result 

assertions_mccabe_ratio_kotlin.__signature__ = _mutmut_signature(x_assertions_mccabe_ratio_kotlin__mutmut_orig)
x_assertions_mccabe_ratio_kotlin__mutmut_orig.__name__ = 'x_assertions_mccabe_ratio_kotlin'




def x_assertions_density_kotlin__mutmut_orig(file_path):
    assertions_count = count_assertions_in_kotlin_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_kotlin__mutmut_1(file_path):
    assertions_count = count_assertions_in_kotlin_file(None)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_kotlin__mutmut_2(file_path):
    assertions_count = None
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_kotlin__mutmut_3(file_path):
    assertions_count = count_assertions_in_kotlin_file(file_path)
    sloc = get_sloc(None)
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_kotlin__mutmut_4(file_path):
    assertions_count = count_assertions_in_kotlin_file(file_path)
    sloc = None
    return round(assertions_count / sloc, 2) if sloc != 0 else None


def x_assertions_density_kotlin__mutmut_5(file_path):
    assertions_count = count_assertions_in_kotlin_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count * sloc, 2) if sloc != 0 else None


def x_assertions_density_kotlin__mutmut_6(file_path):
    assertions_count = count_assertions_in_kotlin_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 3) if sloc != 0 else None


def x_assertions_density_kotlin__mutmut_7(file_path):
    assertions_count = count_assertions_in_kotlin_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if sloc == 0 else None


def x_assertions_density_kotlin__mutmut_8(file_path):
    assertions_count = count_assertions_in_kotlin_file(file_path)
    sloc = get_sloc(file_path)
    return round(assertions_count / sloc, 2) if sloc != 1 else None

x_assertions_density_kotlin__mutmut_mutants = {
'x_assertions_density_kotlin__mutmut_1': x_assertions_density_kotlin__mutmut_1, 
    'x_assertions_density_kotlin__mutmut_2': x_assertions_density_kotlin__mutmut_2, 
    'x_assertions_density_kotlin__mutmut_3': x_assertions_density_kotlin__mutmut_3, 
    'x_assertions_density_kotlin__mutmut_4': x_assertions_density_kotlin__mutmut_4, 
    'x_assertions_density_kotlin__mutmut_5': x_assertions_density_kotlin__mutmut_5, 
    'x_assertions_density_kotlin__mutmut_6': x_assertions_density_kotlin__mutmut_6, 
    'x_assertions_density_kotlin__mutmut_7': x_assertions_density_kotlin__mutmut_7, 
    'x_assertions_density_kotlin__mutmut_8': x_assertions_density_kotlin__mutmut_8
}

def assertions_density_kotlin(*args, **kwargs):
    result = _mutmut_trampoline(x_assertions_density_kotlin__mutmut_orig, x_assertions_density_kotlin__mutmut_mutants, *args, **kwargs)
    return result 

assertions_density_kotlin.__signature__ = _mutmut_signature(x_assertions_density_kotlin__mutmut_orig)
x_assertions_density_kotlin__mutmut_orig.__name__ = 'x_assertions_density_kotlin'



