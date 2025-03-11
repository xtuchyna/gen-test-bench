
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


import os
import shutil
import subprocess
import tempfile

from src.analysis.python_validation import CompileStatus
from src.config import Config


def x_validate_go_code_with_build__mutmut_orig(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_1(go_code):
    try:
        base_temp_dir = None
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_2(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(None, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_3(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=False)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_4(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs( exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_5(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir,)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_6(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=None)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_7(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = None

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_8(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = None

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_9(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(None)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_10(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'XXtemp.goXX'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_11(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = None
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_12(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(None, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_13(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'XXxXX') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_14(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open( 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_15(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(None)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_16(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory("XX.XX")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_17(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("XXException occurred during validation:XX", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_18(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", None, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_19(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_20(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(None)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_21(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(None)
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_22(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("XXException occurred during validation:XX", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_23(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:", None)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_code_with_build__mutmut_24(go_code):
    try:
        base_temp_dir = Config.get_go_input_dir()
        os.makedirs(base_temp_dir, exist_ok=True)
        temp_dir = tempfile.mkdtemp(dir=base_temp_dir)

        original_cwd = os.getcwd()

        try:
            os.chdir(temp_dir)

            go_file_name = 'temp.go'
            with open(go_file_name, 'x') as f:
                f.write(go_code)

            # Run validation on the temp directory
            return validate_go_directory(".")
        except Exception as e:
            print("Exception occurred during validation:", e, e.__traceback__)
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("Exception occurred during validation:",)
        return CompileStatus.EXCEPTION_OCCURRED

x_validate_go_code_with_build__mutmut_mutants = {
'x_validate_go_code_with_build__mutmut_1': x_validate_go_code_with_build__mutmut_1, 
    'x_validate_go_code_with_build__mutmut_2': x_validate_go_code_with_build__mutmut_2, 
    'x_validate_go_code_with_build__mutmut_3': x_validate_go_code_with_build__mutmut_3, 
    'x_validate_go_code_with_build__mutmut_4': x_validate_go_code_with_build__mutmut_4, 
    'x_validate_go_code_with_build__mutmut_5': x_validate_go_code_with_build__mutmut_5, 
    'x_validate_go_code_with_build__mutmut_6': x_validate_go_code_with_build__mutmut_6, 
    'x_validate_go_code_with_build__mutmut_7': x_validate_go_code_with_build__mutmut_7, 
    'x_validate_go_code_with_build__mutmut_8': x_validate_go_code_with_build__mutmut_8, 
    'x_validate_go_code_with_build__mutmut_9': x_validate_go_code_with_build__mutmut_9, 
    'x_validate_go_code_with_build__mutmut_10': x_validate_go_code_with_build__mutmut_10, 
    'x_validate_go_code_with_build__mutmut_11': x_validate_go_code_with_build__mutmut_11, 
    'x_validate_go_code_with_build__mutmut_12': x_validate_go_code_with_build__mutmut_12, 
    'x_validate_go_code_with_build__mutmut_13': x_validate_go_code_with_build__mutmut_13, 
    'x_validate_go_code_with_build__mutmut_14': x_validate_go_code_with_build__mutmut_14, 
    'x_validate_go_code_with_build__mutmut_15': x_validate_go_code_with_build__mutmut_15, 
    'x_validate_go_code_with_build__mutmut_16': x_validate_go_code_with_build__mutmut_16, 
    'x_validate_go_code_with_build__mutmut_17': x_validate_go_code_with_build__mutmut_17, 
    'x_validate_go_code_with_build__mutmut_18': x_validate_go_code_with_build__mutmut_18, 
    'x_validate_go_code_with_build__mutmut_19': x_validate_go_code_with_build__mutmut_19, 
    'x_validate_go_code_with_build__mutmut_20': x_validate_go_code_with_build__mutmut_20, 
    'x_validate_go_code_with_build__mutmut_21': x_validate_go_code_with_build__mutmut_21, 
    'x_validate_go_code_with_build__mutmut_22': x_validate_go_code_with_build__mutmut_22, 
    'x_validate_go_code_with_build__mutmut_23': x_validate_go_code_with_build__mutmut_23, 
    'x_validate_go_code_with_build__mutmut_24': x_validate_go_code_with_build__mutmut_24
}

def validate_go_code_with_build(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_go_code_with_build__mutmut_orig, x_validate_go_code_with_build__mutmut_mutants, *args, **kwargs)
    return result 

validate_go_code_with_build.__signature__ = _mutmut_signature(x_validate_go_code_with_build__mutmut_orig)
x_validate_go_code_with_build__mutmut_orig.__name__ = 'x_validate_go_code_with_build'




def x_validate_go_directory__mutmut_orig(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_1(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['XXgoXX', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_2(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'XXbuildXX'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_3(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_4(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_5(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_6(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_7(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = None

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_8(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode != 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_9(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 1:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_10(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("XXGo code is syntactically valid.XX")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_11(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['XXgoXX', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_12(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'XXvetXX'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_13(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_14(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_15(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_16(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_17(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = None

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_18(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode != 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_19(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 1:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_20(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("XXGo code passed 'go vet' checks.XX")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_21(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("XXGo code has 'go vet' warnings/errors:XX")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_22(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("XXGo code has syntax errors:XX")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_23(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("XXException occurred during validation:XX", e)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_24(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:", None)
        return CompileStatus.EXCEPTION_OCCURRED


def x_validate_go_directory__mutmut_25(temp_dir):
    try:
        # Run 'go build' in the temp directory to validate syntax
        result_build = subprocess.run(
            ['go', 'build'],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result_build.returncode == 0:
            print("Go code is syntactically valid.")

            # Run 'go vet' in the temp directory to check for issues
            result_vet = subprocess.run(
                ['go', 'vet'],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result_vet.returncode == 0:
                print("Go code passed 'go vet' checks.")
                return CompileStatus.OK
            else:
                print("Go code has 'go vet' warnings/errors:")
                print(result_vet.stderr.decode())
                return CompileStatus.SYNTAX_ERROR
        else:
            print("Go code has syntax errors:")
            print(result_build.stderr.decode())
            return CompileStatus.SYNTAX_ERROR
    except Exception as e:
        print("Exception occurred during validation:",)
        return CompileStatus.EXCEPTION_OCCURRED

x_validate_go_directory__mutmut_mutants = {
'x_validate_go_directory__mutmut_1': x_validate_go_directory__mutmut_1, 
    'x_validate_go_directory__mutmut_2': x_validate_go_directory__mutmut_2, 
    'x_validate_go_directory__mutmut_3': x_validate_go_directory__mutmut_3, 
    'x_validate_go_directory__mutmut_4': x_validate_go_directory__mutmut_4, 
    'x_validate_go_directory__mutmut_5': x_validate_go_directory__mutmut_5, 
    'x_validate_go_directory__mutmut_6': x_validate_go_directory__mutmut_6, 
    'x_validate_go_directory__mutmut_7': x_validate_go_directory__mutmut_7, 
    'x_validate_go_directory__mutmut_8': x_validate_go_directory__mutmut_8, 
    'x_validate_go_directory__mutmut_9': x_validate_go_directory__mutmut_9, 
    'x_validate_go_directory__mutmut_10': x_validate_go_directory__mutmut_10, 
    'x_validate_go_directory__mutmut_11': x_validate_go_directory__mutmut_11, 
    'x_validate_go_directory__mutmut_12': x_validate_go_directory__mutmut_12, 
    'x_validate_go_directory__mutmut_13': x_validate_go_directory__mutmut_13, 
    'x_validate_go_directory__mutmut_14': x_validate_go_directory__mutmut_14, 
    'x_validate_go_directory__mutmut_15': x_validate_go_directory__mutmut_15, 
    'x_validate_go_directory__mutmut_16': x_validate_go_directory__mutmut_16, 
    'x_validate_go_directory__mutmut_17': x_validate_go_directory__mutmut_17, 
    'x_validate_go_directory__mutmut_18': x_validate_go_directory__mutmut_18, 
    'x_validate_go_directory__mutmut_19': x_validate_go_directory__mutmut_19, 
    'x_validate_go_directory__mutmut_20': x_validate_go_directory__mutmut_20, 
    'x_validate_go_directory__mutmut_21': x_validate_go_directory__mutmut_21, 
    'x_validate_go_directory__mutmut_22': x_validate_go_directory__mutmut_22, 
    'x_validate_go_directory__mutmut_23': x_validate_go_directory__mutmut_23, 
    'x_validate_go_directory__mutmut_24': x_validate_go_directory__mutmut_24, 
    'x_validate_go_directory__mutmut_25': x_validate_go_directory__mutmut_25
}

def validate_go_directory(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_go_directory__mutmut_orig, x_validate_go_directory__mutmut_mutants, *args, **kwargs)
    return result 

validate_go_directory.__signature__ = _mutmut_signature(x_validate_go_directory__mutmut_orig)
x_validate_go_directory__mutmut_orig.__name__ = 'x_validate_go_directory'


