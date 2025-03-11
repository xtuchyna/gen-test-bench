
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


import subprocess

from src.analysis.python_validation import CompileStatus


def x_validate_kotlin_code__mutmut_orig(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_1(kotlin_code, kotlin_file='XXtemp.ktXX'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_2(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(None, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_3(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'XXwXX') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_4(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open( 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_5(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(None)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_6(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['XXkotlincXX', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_7(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, 'XX-dXX', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_8(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'XXoutXX'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_9(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'], stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_10(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE,)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_11(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = None

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_12(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode != 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_13(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 1:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_14(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("XXKotlin code is valid.XX")
        return CompileStatus.OK
    else:
        print("Kotlin code has errors:")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR


def x_validate_kotlin_code__mutmut_15(kotlin_code, kotlin_file='temp.kt'):
    # Write the Kotlin code to a temporary file
    with open(kotlin_file, 'w') as f:
        f.write(kotlin_code)

    # Run the Kotlin compiler to validate the code
    result = subprocess.run(['kotlinc', kotlin_file, '-d', 'out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if there are compilation errors
    if result.returncode == 0:
        print("Kotlin code is valid.")
        return CompileStatus.OK
    else:
        print("XXKotlin code has errors:XX")
        print(result.stderr.decode())
        return CompileStatus.SYNTAX_ERROR

x_validate_kotlin_code__mutmut_mutants = {
'x_validate_kotlin_code__mutmut_1': x_validate_kotlin_code__mutmut_1, 
    'x_validate_kotlin_code__mutmut_2': x_validate_kotlin_code__mutmut_2, 
    'x_validate_kotlin_code__mutmut_3': x_validate_kotlin_code__mutmut_3, 
    'x_validate_kotlin_code__mutmut_4': x_validate_kotlin_code__mutmut_4, 
    'x_validate_kotlin_code__mutmut_5': x_validate_kotlin_code__mutmut_5, 
    'x_validate_kotlin_code__mutmut_6': x_validate_kotlin_code__mutmut_6, 
    'x_validate_kotlin_code__mutmut_7': x_validate_kotlin_code__mutmut_7, 
    'x_validate_kotlin_code__mutmut_8': x_validate_kotlin_code__mutmut_8, 
    'x_validate_kotlin_code__mutmut_9': x_validate_kotlin_code__mutmut_9, 
    'x_validate_kotlin_code__mutmut_10': x_validate_kotlin_code__mutmut_10, 
    'x_validate_kotlin_code__mutmut_11': x_validate_kotlin_code__mutmut_11, 
    'x_validate_kotlin_code__mutmut_12': x_validate_kotlin_code__mutmut_12, 
    'x_validate_kotlin_code__mutmut_13': x_validate_kotlin_code__mutmut_13, 
    'x_validate_kotlin_code__mutmut_14': x_validate_kotlin_code__mutmut_14, 
    'x_validate_kotlin_code__mutmut_15': x_validate_kotlin_code__mutmut_15
}

def validate_kotlin_code(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_kotlin_code__mutmut_orig, x_validate_kotlin_code__mutmut_mutants, *args, **kwargs)
    return result 

validate_kotlin_code.__signature__ = _mutmut_signature(x_validate_kotlin_code__mutmut_orig)
x_validate_kotlin_code__mutmut_orig.__name__ = 'x_validate_kotlin_code'


