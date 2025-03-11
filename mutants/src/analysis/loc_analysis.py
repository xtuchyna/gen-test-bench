
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


from pygount import analysis


def x_get_sloc__mutmut_orig(file):
    result = analysis.SourceAnalysis.from_file(file, file, encoding="utf8")
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_1(file):
    result = analysis.SourceAnalysis.from_file(None, file, encoding="utf8")
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_2(file):
    result = analysis.SourceAnalysis.from_file(file, None, encoding="utf8")
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_3(file):
    result = analysis.SourceAnalysis.from_file(file, file, encoding="XXutf8XX")
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_4(file):
    result = analysis.SourceAnalysis.from_file( file, encoding="utf8")
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_5(file):
    result = analysis.SourceAnalysis.from_file(file, encoding="utf8")
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_6(file):
    result = analysis.SourceAnalysis.from_file(file, file,)
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_7(file):
    result = None
    if result is None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_8(file):
    result = analysis.SourceAnalysis.from_file(file, file, encoding="utf8")
    if result is not None or not result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_9(file):
    result = analysis.SourceAnalysis.from_file(file, file, encoding="utf8")
    if result is None or  result.is_countable:
        return None
    return result.code_count


def x_get_sloc__mutmut_10(file):
    result = analysis.SourceAnalysis.from_file(file, file, encoding="utf8")
    if result is None and not result.is_countable:
        return None
    return result.code_count

x_get_sloc__mutmut_mutants = {
'x_get_sloc__mutmut_1': x_get_sloc__mutmut_1, 
    'x_get_sloc__mutmut_2': x_get_sloc__mutmut_2, 
    'x_get_sloc__mutmut_3': x_get_sloc__mutmut_3, 
    'x_get_sloc__mutmut_4': x_get_sloc__mutmut_4, 
    'x_get_sloc__mutmut_5': x_get_sloc__mutmut_5, 
    'x_get_sloc__mutmut_6': x_get_sloc__mutmut_6, 
    'x_get_sloc__mutmut_7': x_get_sloc__mutmut_7, 
    'x_get_sloc__mutmut_8': x_get_sloc__mutmut_8, 
    'x_get_sloc__mutmut_9': x_get_sloc__mutmut_9, 
    'x_get_sloc__mutmut_10': x_get_sloc__mutmut_10
}

def get_sloc(*args, **kwargs):
    result = _mutmut_trampoline(x_get_sloc__mutmut_orig, x_get_sloc__mutmut_mutants, *args, **kwargs)
    return result 

get_sloc.__signature__ = _mutmut_signature(x_get_sloc__mutmut_orig)
x_get_sloc__mutmut_orig.__name__ = 'x_get_sloc'


