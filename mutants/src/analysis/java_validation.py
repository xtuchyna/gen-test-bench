
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


from src.helpers import convert_to_java_filename
from src.analysis.python_validation import CompileStatus
import subprocess
import os


def x_validate_java_code__mutmut_orig(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_1(java_code):
    try:
        name = convert_to_java_filename("XXTemp.javaXX", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_2(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "XXXX", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_3(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=None)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_4(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "",)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_5(java_code):
    try:
        name = None
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_6(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("XX/data/javaSetup/src/main/java/org/example/packageXX", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_7(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", None)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_8(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package",)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_9(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = None
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_10(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(None, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_11(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "XXwXX") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_12(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open( "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_13(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(None)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_14(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['XXjavacXX', temp_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_15(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=False, text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_16(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=False)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_17(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], text=True)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_18(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True,)

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_19(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = None

        if result.returncode == 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_20(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode != 0:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_java_code__mutmut_21(java_code):
    try:
        name = convert_to_java_filename("Temp.java", "", data=java_code)
        temp_file_path = os.path.join("/data/javaSetup/src/main/java/org/example/package", name)
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(java_code)

        # Run javac to check for syntax errors
        result = subprocess.run(['javac', temp_file_path], capture_output=True, text=True)

        if result.returncode == 1:
            return CompileStatus.OK
        else:
            # Syntax errors occurred
            print(f"Syntax error:\n{result.stderr}")
            return CompileStatus.SYNTAX_ERROR

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Exception occurred: {e}")
        return CompileStatus.EXCEPTION_OCCURRED

x_validate_java_code__mutmut_mutants = {
'x_validate_java_code__mutmut_1': x_validate_java_code__mutmut_1, 
    'x_validate_java_code__mutmut_2': x_validate_java_code__mutmut_2, 
    'x_validate_java_code__mutmut_3': x_validate_java_code__mutmut_3, 
    'x_validate_java_code__mutmut_4': x_validate_java_code__mutmut_4, 
    'x_validate_java_code__mutmut_5': x_validate_java_code__mutmut_5, 
    'x_validate_java_code__mutmut_6': x_validate_java_code__mutmut_6, 
    'x_validate_java_code__mutmut_7': x_validate_java_code__mutmut_7, 
    'x_validate_java_code__mutmut_8': x_validate_java_code__mutmut_8, 
    'x_validate_java_code__mutmut_9': x_validate_java_code__mutmut_9, 
    'x_validate_java_code__mutmut_10': x_validate_java_code__mutmut_10, 
    'x_validate_java_code__mutmut_11': x_validate_java_code__mutmut_11, 
    'x_validate_java_code__mutmut_12': x_validate_java_code__mutmut_12, 
    'x_validate_java_code__mutmut_13': x_validate_java_code__mutmut_13, 
    'x_validate_java_code__mutmut_14': x_validate_java_code__mutmut_14, 
    'x_validate_java_code__mutmut_15': x_validate_java_code__mutmut_15, 
    'x_validate_java_code__mutmut_16': x_validate_java_code__mutmut_16, 
    'x_validate_java_code__mutmut_17': x_validate_java_code__mutmut_17, 
    'x_validate_java_code__mutmut_18': x_validate_java_code__mutmut_18, 
    'x_validate_java_code__mutmut_19': x_validate_java_code__mutmut_19, 
    'x_validate_java_code__mutmut_20': x_validate_java_code__mutmut_20, 
    'x_validate_java_code__mutmut_21': x_validate_java_code__mutmut_21
}

def validate_java_code(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_java_code__mutmut_orig, x_validate_java_code__mutmut_mutants, *args, **kwargs)
    return result 

validate_java_code.__signature__ = _mutmut_signature(x_validate_java_code__mutmut_orig)
x_validate_java_code__mutmut_orig.__name__ = 'x_validate_java_code'


