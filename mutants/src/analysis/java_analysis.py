
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
import time
import xml.etree.ElementTree as ET
import glob

from src.analysis.java_assertion_ratios import assertions_density_java, assertions_mccabe_ratio_java
from src.analysis.python_validation import CompileStatus
from src.config import Config
import subprocess


def x_run_checkstyle__mutmut_orig(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_1(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['XXjavaXX', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_2(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', 'XX-jarXX', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_3(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, 'XX-cXX', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_4(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_5(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path], stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_6(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_7(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_8(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = None

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_9(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("XXCheckstyle stdout output:XX")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_10(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("XXCheckstyle stderr output:XX")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_11(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout - result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_12(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = None

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_13(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(None)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_14(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = None

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_15(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("XXFound Checkstyle errors:XX")
            for error in errors:
                print(error)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_16(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(None)
        else:
            print("No Checkstyle issues found for this file.")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []


def x_run_checkstyle__mutmut_17(java_file_path):
    """ Run Checkstyle for a Java file and return a list of errors """
    try:
        result = subprocess.run(
            ['java', '-jar', Config._java_checkstyle_jar_path, '-c', Config._java_checkstyle_config, java_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("Checkstyle stdout output:")
            print(result.stdout)

        if result.stderr:
            print("Checkstyle stderr output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing, as errors might be in either
        output = result.stdout + result.stderr

        # Extract errors from the output
        errors = parse_checkstyle_errors(output)

        if errors:
            print("Found Checkstyle errors:")
            for error in errors:
                print(error)
        else:
            print("XXNo Checkstyle issues found for this file.XX")

        return errors

    except Exception as e:
        print(f"Error running Checkstyle: {e}")
        return []

x_run_checkstyle__mutmut_mutants = {
'x_run_checkstyle__mutmut_1': x_run_checkstyle__mutmut_1, 
    'x_run_checkstyle__mutmut_2': x_run_checkstyle__mutmut_2, 
    'x_run_checkstyle__mutmut_3': x_run_checkstyle__mutmut_3, 
    'x_run_checkstyle__mutmut_4': x_run_checkstyle__mutmut_4, 
    'x_run_checkstyle__mutmut_5': x_run_checkstyle__mutmut_5, 
    'x_run_checkstyle__mutmut_6': x_run_checkstyle__mutmut_6, 
    'x_run_checkstyle__mutmut_7': x_run_checkstyle__mutmut_7, 
    'x_run_checkstyle__mutmut_8': x_run_checkstyle__mutmut_8, 
    'x_run_checkstyle__mutmut_9': x_run_checkstyle__mutmut_9, 
    'x_run_checkstyle__mutmut_10': x_run_checkstyle__mutmut_10, 
    'x_run_checkstyle__mutmut_11': x_run_checkstyle__mutmut_11, 
    'x_run_checkstyle__mutmut_12': x_run_checkstyle__mutmut_12, 
    'x_run_checkstyle__mutmut_13': x_run_checkstyle__mutmut_13, 
    'x_run_checkstyle__mutmut_14': x_run_checkstyle__mutmut_14, 
    'x_run_checkstyle__mutmut_15': x_run_checkstyle__mutmut_15, 
    'x_run_checkstyle__mutmut_16': x_run_checkstyle__mutmut_16, 
    'x_run_checkstyle__mutmut_17': x_run_checkstyle__mutmut_17
}

def run_checkstyle(*args, **kwargs):
    result = _mutmut_trampoline(x_run_checkstyle__mutmut_orig, x_run_checkstyle__mutmut_mutants, *args, **kwargs)
    return result 

run_checkstyle.__signature__ = _mutmut_signature(x_run_checkstyle__mutmut_orig)
x_run_checkstyle__mutmut_orig.__name__ = 'x_run_checkstyle'




def x_parse_checkstyle_errors__mutmut_orig(output):
    """ Parse the Checkstyle output to extract errors """
    errors = []

    # Split the output into lines and look for lines that indicate errors
    for line in output.splitlines():
        if "error" in line.lower():
            errors.append(line.strip())

    return errors


def x_parse_checkstyle_errors__mutmut_1(output):
    """ Parse the Checkstyle output to extract errors """
    errors = None

    # Split the output into lines and look for lines that indicate errors
    for line in output.splitlines():
        if "error" in line.lower():
            errors.append(line.strip())

    return errors


def x_parse_checkstyle_errors__mutmut_2(output):
    """ Parse the Checkstyle output to extract errors """
    errors = []

    # Split the output into lines and look for lines that indicate errors
    for line in output.splitlines():
        if "XXerrorXX" in line.lower():
            errors.append(line.strip())

    return errors


def x_parse_checkstyle_errors__mutmut_3(output):
    """ Parse the Checkstyle output to extract errors """
    errors = []

    # Split the output into lines and look for lines that indicate errors
    for line in output.splitlines():
        if "error" not in line.lower():
            errors.append(line.strip())

    return errors

x_parse_checkstyle_errors__mutmut_mutants = {
'x_parse_checkstyle_errors__mutmut_1': x_parse_checkstyle_errors__mutmut_1, 
    'x_parse_checkstyle_errors__mutmut_2': x_parse_checkstyle_errors__mutmut_2, 
    'x_parse_checkstyle_errors__mutmut_3': x_parse_checkstyle_errors__mutmut_3
}

def parse_checkstyle_errors(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_checkstyle_errors__mutmut_orig, x_parse_checkstyle_errors__mutmut_mutants, *args, **kwargs)
    return result 

parse_checkstyle_errors.__signature__ = _mutmut_signature(x_parse_checkstyle_errors__mutmut_orig)
x_parse_checkstyle_errors__mutmut_orig.__name__ = 'x_parse_checkstyle_errors'




def x_run_maven_test_compile__mutmut_orig(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_1(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = True
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_2(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = None
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_3(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = True

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_4(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = None

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_5(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['XXmvnXX', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_6(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'XXtest-compileXX'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_7(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=None,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_8(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=False,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_9(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=False,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_10(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=None
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_11(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_12(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_13(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_14(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_15(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = None
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_16(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = None
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_17(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode != 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_18(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 1:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_19(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("XXTest compilation passedXX")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_20(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = None
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_21(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("XXTest compilation failedXX")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_22(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = None
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_23(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = False
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_24(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = None
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_25(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "XXTest compilation timed out.XX"
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_26(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = None
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_27(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = None
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_28(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("XXError occurred during compilation: XX", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_29(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", None)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_30(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ",)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_31(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = False
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_32(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = None
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_33(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = None
        syntax_maven_output = None

    return syntax_maven_output, syntax, timeout_occurred, error


def x_run_maven_test_compile__mutmut_34(project_dir, timeout):
    """
    Runs 'mvn test-compile' in the given project directory with the specified timeout.

    Returns a tuple: (syntax_maven_output, syntax, timeout_occurred, error)
    """
    timeout_occurred = False
    error = False

    try:
        result = subprocess.run(
            ['mvn', 'test-compile'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        syntax_maven_output = result.stdout
        print(result.stdout)
        print(result.stderr)
        if result.returncode == 0:
            print("Test compilation passed")
            syntax = CompileStatus.OK
        else:
            print("Test compilation failed")
            syntax = CompileStatus.SYNTAX_ERROR
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        syntax_maven_output = "Test compilation timed out."
        syntax = CompileStatus.EXCEPTION_OCCURRED
    except Exception as e:
        print("Error occurred during compilation: ", e)
        error = True
        syntax = CompileStatus.EXCEPTION_OCCURRED
        syntax_maven_output = ""

    return syntax_maven_output, syntax, timeout_occurred, error

x_run_maven_test_compile__mutmut_mutants = {
'x_run_maven_test_compile__mutmut_1': x_run_maven_test_compile__mutmut_1, 
    'x_run_maven_test_compile__mutmut_2': x_run_maven_test_compile__mutmut_2, 
    'x_run_maven_test_compile__mutmut_3': x_run_maven_test_compile__mutmut_3, 
    'x_run_maven_test_compile__mutmut_4': x_run_maven_test_compile__mutmut_4, 
    'x_run_maven_test_compile__mutmut_5': x_run_maven_test_compile__mutmut_5, 
    'x_run_maven_test_compile__mutmut_6': x_run_maven_test_compile__mutmut_6, 
    'x_run_maven_test_compile__mutmut_7': x_run_maven_test_compile__mutmut_7, 
    'x_run_maven_test_compile__mutmut_8': x_run_maven_test_compile__mutmut_8, 
    'x_run_maven_test_compile__mutmut_9': x_run_maven_test_compile__mutmut_9, 
    'x_run_maven_test_compile__mutmut_10': x_run_maven_test_compile__mutmut_10, 
    'x_run_maven_test_compile__mutmut_11': x_run_maven_test_compile__mutmut_11, 
    'x_run_maven_test_compile__mutmut_12': x_run_maven_test_compile__mutmut_12, 
    'x_run_maven_test_compile__mutmut_13': x_run_maven_test_compile__mutmut_13, 
    'x_run_maven_test_compile__mutmut_14': x_run_maven_test_compile__mutmut_14, 
    'x_run_maven_test_compile__mutmut_15': x_run_maven_test_compile__mutmut_15, 
    'x_run_maven_test_compile__mutmut_16': x_run_maven_test_compile__mutmut_16, 
    'x_run_maven_test_compile__mutmut_17': x_run_maven_test_compile__mutmut_17, 
    'x_run_maven_test_compile__mutmut_18': x_run_maven_test_compile__mutmut_18, 
    'x_run_maven_test_compile__mutmut_19': x_run_maven_test_compile__mutmut_19, 
    'x_run_maven_test_compile__mutmut_20': x_run_maven_test_compile__mutmut_20, 
    'x_run_maven_test_compile__mutmut_21': x_run_maven_test_compile__mutmut_21, 
    'x_run_maven_test_compile__mutmut_22': x_run_maven_test_compile__mutmut_22, 
    'x_run_maven_test_compile__mutmut_23': x_run_maven_test_compile__mutmut_23, 
    'x_run_maven_test_compile__mutmut_24': x_run_maven_test_compile__mutmut_24, 
    'x_run_maven_test_compile__mutmut_25': x_run_maven_test_compile__mutmut_25, 
    'x_run_maven_test_compile__mutmut_26': x_run_maven_test_compile__mutmut_26, 
    'x_run_maven_test_compile__mutmut_27': x_run_maven_test_compile__mutmut_27, 
    'x_run_maven_test_compile__mutmut_28': x_run_maven_test_compile__mutmut_28, 
    'x_run_maven_test_compile__mutmut_29': x_run_maven_test_compile__mutmut_29, 
    'x_run_maven_test_compile__mutmut_30': x_run_maven_test_compile__mutmut_30, 
    'x_run_maven_test_compile__mutmut_31': x_run_maven_test_compile__mutmut_31, 
    'x_run_maven_test_compile__mutmut_32': x_run_maven_test_compile__mutmut_32, 
    'x_run_maven_test_compile__mutmut_33': x_run_maven_test_compile__mutmut_33, 
    'x_run_maven_test_compile__mutmut_34': x_run_maven_test_compile__mutmut_34
}

def run_maven_test_compile(*args, **kwargs):
    result = _mutmut_trampoline(x_run_maven_test_compile__mutmut_orig, x_run_maven_test_compile__mutmut_mutants, *args, **kwargs)
    return result 

run_maven_test_compile.__signature__ = _mutmut_signature(x_run_maven_test_compile__mutmut_orig)
x_run_maven_test_compile__mutmut_orig.__name__ = 'x_run_maven_test_compile'




def x_run_maven_clean_test__mutmut_orig(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_1(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = ""
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_2(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = True
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_3(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = None
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_4(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = True
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_5(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = None
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_6(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = None
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_7(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['XXmvnXX', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_8(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'XXcleanXX', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_9(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'XXverifyXX'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_10(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=None,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_11(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=False,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_12(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=False,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_13(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=None
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_14(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_15(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_16(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_17(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_18(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = None
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_19(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = None
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_20(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = False
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_21(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = None
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_22(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "XXTest execution timed out.XX"
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_23(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = None
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_24(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("XXError occurred during test execution: XX", e)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_25(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", None)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_26(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ",)
        error = True
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_27(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = False
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_28(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = None
    end_time = time.time()
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_29(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = None
    execution_time = end_time - start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_30(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = end_time + start_time
    return test_maven_output, timeout_occurred, error, execution_time


def x_run_maven_clean_test__mutmut_31(project_dir, timeout):
    """
    Runs 'mvn clean test' in the given project directory with the specified timeout.

    Returns a tuple: (test_maven_output, timeout_occurred, error, execution_time)
    """
    test_maven_output = None
    timeout_occurred = False
    error = False
    start_time = time.time()
    try:
        result = subprocess.run(
            ['mvn', 'clean', 'verify'],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        test_maven_output = result.stdout
    except subprocess.TimeoutExpired:
        timeout_occurred = True
        test_maven_output = "Test execution timed out."
    except Exception as e:
        print("Error occurred during test execution: ", e)
        error = True
    end_time = time.time()
    execution_time = None
    return test_maven_output, timeout_occurred, error, execution_time

x_run_maven_clean_test__mutmut_mutants = {
'x_run_maven_clean_test__mutmut_1': x_run_maven_clean_test__mutmut_1, 
    'x_run_maven_clean_test__mutmut_2': x_run_maven_clean_test__mutmut_2, 
    'x_run_maven_clean_test__mutmut_3': x_run_maven_clean_test__mutmut_3, 
    'x_run_maven_clean_test__mutmut_4': x_run_maven_clean_test__mutmut_4, 
    'x_run_maven_clean_test__mutmut_5': x_run_maven_clean_test__mutmut_5, 
    'x_run_maven_clean_test__mutmut_6': x_run_maven_clean_test__mutmut_6, 
    'x_run_maven_clean_test__mutmut_7': x_run_maven_clean_test__mutmut_7, 
    'x_run_maven_clean_test__mutmut_8': x_run_maven_clean_test__mutmut_8, 
    'x_run_maven_clean_test__mutmut_9': x_run_maven_clean_test__mutmut_9, 
    'x_run_maven_clean_test__mutmut_10': x_run_maven_clean_test__mutmut_10, 
    'x_run_maven_clean_test__mutmut_11': x_run_maven_clean_test__mutmut_11, 
    'x_run_maven_clean_test__mutmut_12': x_run_maven_clean_test__mutmut_12, 
    'x_run_maven_clean_test__mutmut_13': x_run_maven_clean_test__mutmut_13, 
    'x_run_maven_clean_test__mutmut_14': x_run_maven_clean_test__mutmut_14, 
    'x_run_maven_clean_test__mutmut_15': x_run_maven_clean_test__mutmut_15, 
    'x_run_maven_clean_test__mutmut_16': x_run_maven_clean_test__mutmut_16, 
    'x_run_maven_clean_test__mutmut_17': x_run_maven_clean_test__mutmut_17, 
    'x_run_maven_clean_test__mutmut_18': x_run_maven_clean_test__mutmut_18, 
    'x_run_maven_clean_test__mutmut_19': x_run_maven_clean_test__mutmut_19, 
    'x_run_maven_clean_test__mutmut_20': x_run_maven_clean_test__mutmut_20, 
    'x_run_maven_clean_test__mutmut_21': x_run_maven_clean_test__mutmut_21, 
    'x_run_maven_clean_test__mutmut_22': x_run_maven_clean_test__mutmut_22, 
    'x_run_maven_clean_test__mutmut_23': x_run_maven_clean_test__mutmut_23, 
    'x_run_maven_clean_test__mutmut_24': x_run_maven_clean_test__mutmut_24, 
    'x_run_maven_clean_test__mutmut_25': x_run_maven_clean_test__mutmut_25, 
    'x_run_maven_clean_test__mutmut_26': x_run_maven_clean_test__mutmut_26, 
    'x_run_maven_clean_test__mutmut_27': x_run_maven_clean_test__mutmut_27, 
    'x_run_maven_clean_test__mutmut_28': x_run_maven_clean_test__mutmut_28, 
    'x_run_maven_clean_test__mutmut_29': x_run_maven_clean_test__mutmut_29, 
    'x_run_maven_clean_test__mutmut_30': x_run_maven_clean_test__mutmut_30, 
    'x_run_maven_clean_test__mutmut_31': x_run_maven_clean_test__mutmut_31
}

def run_maven_clean_test(*args, **kwargs):
    result = _mutmut_trampoline(x_run_maven_clean_test__mutmut_orig, x_run_maven_clean_test__mutmut_mutants, *args, **kwargs)
    return result 

run_maven_clean_test.__signature__ = _mutmut_signature(x_run_maven_clean_test__mutmut_orig)
x_run_maven_clean_test__mutmut_orig.__name__ = 'x_run_maven_clean_test'




def x_compute_coverage_percentage__mutmut_orig(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_1(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"XXlineXX": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_2(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "XXbranchXX": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_3(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(None, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_4(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'XXtargetXX', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_5(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'XXsiteXX', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_6(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'XXjacocoXX', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_7(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'XXjacoco.xmlXX')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_8(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join( 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_9(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = None
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_10(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(None):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_11(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(None)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_12(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = None
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_13(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = None

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_14(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"XXlineXX": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_15(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "XXbranchXX": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_16(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = None

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_17(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(None)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_18(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = None
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_19(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = None
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_20(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is not None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_21(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["XXLINEXX", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_22(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "XXBRANCHXX"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_23(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = None
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_24(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is  None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_25(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("XXcoveredXX", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_26(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 1))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_27(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = None
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_28(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("XXmissedXX", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_29(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 1))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_30(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = None
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_31(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("XXCOVERED: XX" + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_32(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " - str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_33(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(None) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_34(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) - " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_35(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + "XX MISSED: XX" + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_36(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " - str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_37(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(None))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_38(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered - missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_39(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed >= 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_40(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 1:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_41(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[None] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_42(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered * (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_43(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered - missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_44(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) / 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_45(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 101
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_46(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = None
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_47(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["XXlineXX"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_48(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage[None] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_49(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is  None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_50(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["XXbranchXX"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_51(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage[None] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_52(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is not None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_53(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None or coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_54(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["XXbranchXX"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_55(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage[None] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_56(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 101
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_57(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = None
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_58(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"XXlineXX": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_59(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "XXbranchXX": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_60(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("XXCoverage report not found.XX")
        return {"line": None, "branch": None}


def x_compute_coverage_percentage__mutmut_61(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"XXlineXX": None, "branch": None}


def x_compute_coverage_percentage__mutmut_62(project_dir, src_file_path, timeout_occurred):
    """
    Parses the JaCoCo coverage report and computes both line and branch coverage percentages.

    Returns:
        A dictionary with line and branch coverage percentages, or None if the report is not found or a timeout occurred.
    """
    if timeout_occurred:
        return {"line": None, "branch": None}

    coverage_report_path = os.path.join(project_dir, 'target', 'site', 'jacoco', 'jacoco.xml')
    if os.path.exists(coverage_report_path):
        try:
            tree = ET.parse(coverage_report_path)
            root = tree.getroot()

            # Initialize coverage metrics
            coverage = {"line": None, "branch": None}

            file_name = os.path.basename(src_file_path)
            # Find the <sourcefile> element with the specified file name
            source_file = root.find(f".//sourcefile[@name='{file_name}']")
            if source_file is None:
                print(f"File '{file_name}' not found in the coverage report.")
                return coverage

            # Extract LINE and BRANCH counters for the file
            for counter_type in ["LINE", "BRANCH"]:
                counter = source_file.find(f"./counter[@type='{counter_type}']")
                if counter is not None:
                    covered = int(counter.get("covered", 0))
                    missed = int(counter.get("missed", 0))
                    print("COVERED: " + str(covered) + " MISSED: " + str(missed))
                    if covered + missed > 0:
                        coverage[counter_type.lower()] = (covered / (covered + missed)) * 100
                else:
                    if coverage["line"] is not None and coverage["branch"] is None:
                        # case when branch coverage isn't in report because code has no branches that need covering
                        coverage["branch"] = 100
            return coverage

        except Exception as e:
            print(f"Error processing coverage report: {e}")
            return {"line": None, "branch": None}
    else:
        print("Coverage report not found.")
        return {"line": None, "XXbranchXX": None}

x_compute_coverage_percentage__mutmut_mutants = {
'x_compute_coverage_percentage__mutmut_1': x_compute_coverage_percentage__mutmut_1, 
    'x_compute_coverage_percentage__mutmut_2': x_compute_coverage_percentage__mutmut_2, 
    'x_compute_coverage_percentage__mutmut_3': x_compute_coverage_percentage__mutmut_3, 
    'x_compute_coverage_percentage__mutmut_4': x_compute_coverage_percentage__mutmut_4, 
    'x_compute_coverage_percentage__mutmut_5': x_compute_coverage_percentage__mutmut_5, 
    'x_compute_coverage_percentage__mutmut_6': x_compute_coverage_percentage__mutmut_6, 
    'x_compute_coverage_percentage__mutmut_7': x_compute_coverage_percentage__mutmut_7, 
    'x_compute_coverage_percentage__mutmut_8': x_compute_coverage_percentage__mutmut_8, 
    'x_compute_coverage_percentage__mutmut_9': x_compute_coverage_percentage__mutmut_9, 
    'x_compute_coverage_percentage__mutmut_10': x_compute_coverage_percentage__mutmut_10, 
    'x_compute_coverage_percentage__mutmut_11': x_compute_coverage_percentage__mutmut_11, 
    'x_compute_coverage_percentage__mutmut_12': x_compute_coverage_percentage__mutmut_12, 
    'x_compute_coverage_percentage__mutmut_13': x_compute_coverage_percentage__mutmut_13, 
    'x_compute_coverage_percentage__mutmut_14': x_compute_coverage_percentage__mutmut_14, 
    'x_compute_coverage_percentage__mutmut_15': x_compute_coverage_percentage__mutmut_15, 
    'x_compute_coverage_percentage__mutmut_16': x_compute_coverage_percentage__mutmut_16, 
    'x_compute_coverage_percentage__mutmut_17': x_compute_coverage_percentage__mutmut_17, 
    'x_compute_coverage_percentage__mutmut_18': x_compute_coverage_percentage__mutmut_18, 
    'x_compute_coverage_percentage__mutmut_19': x_compute_coverage_percentage__mutmut_19, 
    'x_compute_coverage_percentage__mutmut_20': x_compute_coverage_percentage__mutmut_20, 
    'x_compute_coverage_percentage__mutmut_21': x_compute_coverage_percentage__mutmut_21, 
    'x_compute_coverage_percentage__mutmut_22': x_compute_coverage_percentage__mutmut_22, 
    'x_compute_coverage_percentage__mutmut_23': x_compute_coverage_percentage__mutmut_23, 
    'x_compute_coverage_percentage__mutmut_24': x_compute_coverage_percentage__mutmut_24, 
    'x_compute_coverage_percentage__mutmut_25': x_compute_coverage_percentage__mutmut_25, 
    'x_compute_coverage_percentage__mutmut_26': x_compute_coverage_percentage__mutmut_26, 
    'x_compute_coverage_percentage__mutmut_27': x_compute_coverage_percentage__mutmut_27, 
    'x_compute_coverage_percentage__mutmut_28': x_compute_coverage_percentage__mutmut_28, 
    'x_compute_coverage_percentage__mutmut_29': x_compute_coverage_percentage__mutmut_29, 
    'x_compute_coverage_percentage__mutmut_30': x_compute_coverage_percentage__mutmut_30, 
    'x_compute_coverage_percentage__mutmut_31': x_compute_coverage_percentage__mutmut_31, 
    'x_compute_coverage_percentage__mutmut_32': x_compute_coverage_percentage__mutmut_32, 
    'x_compute_coverage_percentage__mutmut_33': x_compute_coverage_percentage__mutmut_33, 
    'x_compute_coverage_percentage__mutmut_34': x_compute_coverage_percentage__mutmut_34, 
    'x_compute_coverage_percentage__mutmut_35': x_compute_coverage_percentage__mutmut_35, 
    'x_compute_coverage_percentage__mutmut_36': x_compute_coverage_percentage__mutmut_36, 
    'x_compute_coverage_percentage__mutmut_37': x_compute_coverage_percentage__mutmut_37, 
    'x_compute_coverage_percentage__mutmut_38': x_compute_coverage_percentage__mutmut_38, 
    'x_compute_coverage_percentage__mutmut_39': x_compute_coverage_percentage__mutmut_39, 
    'x_compute_coverage_percentage__mutmut_40': x_compute_coverage_percentage__mutmut_40, 
    'x_compute_coverage_percentage__mutmut_41': x_compute_coverage_percentage__mutmut_41, 
    'x_compute_coverage_percentage__mutmut_42': x_compute_coverage_percentage__mutmut_42, 
    'x_compute_coverage_percentage__mutmut_43': x_compute_coverage_percentage__mutmut_43, 
    'x_compute_coverage_percentage__mutmut_44': x_compute_coverage_percentage__mutmut_44, 
    'x_compute_coverage_percentage__mutmut_45': x_compute_coverage_percentage__mutmut_45, 
    'x_compute_coverage_percentage__mutmut_46': x_compute_coverage_percentage__mutmut_46, 
    'x_compute_coverage_percentage__mutmut_47': x_compute_coverage_percentage__mutmut_47, 
    'x_compute_coverage_percentage__mutmut_48': x_compute_coverage_percentage__mutmut_48, 
    'x_compute_coverage_percentage__mutmut_49': x_compute_coverage_percentage__mutmut_49, 
    'x_compute_coverage_percentage__mutmut_50': x_compute_coverage_percentage__mutmut_50, 
    'x_compute_coverage_percentage__mutmut_51': x_compute_coverage_percentage__mutmut_51, 
    'x_compute_coverage_percentage__mutmut_52': x_compute_coverage_percentage__mutmut_52, 
    'x_compute_coverage_percentage__mutmut_53': x_compute_coverage_percentage__mutmut_53, 
    'x_compute_coverage_percentage__mutmut_54': x_compute_coverage_percentage__mutmut_54, 
    'x_compute_coverage_percentage__mutmut_55': x_compute_coverage_percentage__mutmut_55, 
    'x_compute_coverage_percentage__mutmut_56': x_compute_coverage_percentage__mutmut_56, 
    'x_compute_coverage_percentage__mutmut_57': x_compute_coverage_percentage__mutmut_57, 
    'x_compute_coverage_percentage__mutmut_58': x_compute_coverage_percentage__mutmut_58, 
    'x_compute_coverage_percentage__mutmut_59': x_compute_coverage_percentage__mutmut_59, 
    'x_compute_coverage_percentage__mutmut_60': x_compute_coverage_percentage__mutmut_60, 
    'x_compute_coverage_percentage__mutmut_61': x_compute_coverage_percentage__mutmut_61, 
    'x_compute_coverage_percentage__mutmut_62': x_compute_coverage_percentage__mutmut_62
}

def compute_coverage_percentage(*args, **kwargs):
    result = _mutmut_trampoline(x_compute_coverage_percentage__mutmut_orig, x_compute_coverage_percentage__mutmut_mutants, *args, **kwargs)
    return result 

compute_coverage_percentage.__signature__ = _mutmut_signature(x_compute_coverage_percentage__mutmut_orig)
x_compute_coverage_percentage__mutmut_orig.__name__ = 'x_compute_coverage_percentage'




def x_process_java_files_and_run_test_analysis__mutmut_orig(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_1(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=31
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_2(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = None
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_3(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = True
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_4(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = None
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_5(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = True
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_6(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = None
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_7(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = ""
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_8(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = ""
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_9(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(None):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_10(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith("XX.javaXX"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_11(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(None, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_12(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, None)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_13(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join( file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_14(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir,)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_15(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = None
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_16(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name != os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_17(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(None):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_18(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(None, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_19(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, None)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_20(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join( file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_21(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir,)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_22(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = None
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_23(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = None
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_24(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(None, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_25(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, None)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_26(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join( file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_27(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir,)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_28(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = None
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_29(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = None
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_30(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(None), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_31(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=False)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_32(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path),)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_33(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(None, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_34(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, None)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_35(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy( destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_36(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path,)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_37(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(None)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_38(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(None, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_39(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, None)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_40(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile( timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_41(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir,)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_42(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = None
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_43(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = None

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_44(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred and compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_45(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = None

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_46(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(None)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_47(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = None
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_48(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(None, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_49(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, None)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_50(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java( test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_51(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path,)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_52(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = None
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_53(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("XXError occurred during computation of McCabe ratio: XX", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_54(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", None)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_55(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ",)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_56(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = ""

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_57(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax == CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_58(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "XXexecution_time_secXX": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_59(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "XXline_coverage_percentXX": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_60(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "XXbranch_coverage_percentXX": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_61(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "XXtimeout_occurredXX": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_62(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "XXinternal_error_occurredXX": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_63(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "XXsyntaxXX": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_64(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "XXsyntax_maven_outputXX": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_65(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "XXassertion_densityXX": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_66(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "XXassertions_mccabe_ratioXX": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_67(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "XXruntime_errorsXX": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_68(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "XXtest_pass_rateXX": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_69(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "XXtest_maven_outputXX": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_70(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(None, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_71(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, None)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_72(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test( timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_73(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir,)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_74(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = None
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_75(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = None

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_76(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred and test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_77(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = None
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_78(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error and test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_79(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = None
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_80(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = None
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_81(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(None, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_82(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, None, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_83(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, None)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_84(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage( source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_85(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_86(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path,)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_87(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = None

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_88(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "XXexecution_time_secXX": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_89(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "XXline_coverage_percentXX": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_90(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["XXlineXX"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_91(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage[None],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_92(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "XXbranch_coverage_percentXX": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_93(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["XXbranchXX"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_94(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage[None],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_95(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "XXtimeout_occurredXX": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_96(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "XXtest_maven_outputXX": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_97(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "XXsyntax_maven_outputXX": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_98(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "XXinternal_error_occurredXX": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_99(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "XXsyntaxXX": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_100(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "XXruntime_errorsXX": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_101(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "XXtest_pass_rateXX": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_102(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "XXassertion_densityXX": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_103(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "XXassertions_mccabe_ratioXX": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(copied_file)


def x_process_java_files_and_run_test_analysis__mutmut_104(
        input_dir,
        test_input_file_path,
        src_dir=Config._java_src_dir,
        test_dir=Config._java_test_dir,
        project_dir=Config._java_project_root,
        timeout=30
):
    # Track copied files for cleanup later
    copied_files = []
    timeout_occurred = False
    error = False
    source_file_path = None
    test_file_path = None
    try:
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".java"):
                source_path = os.path.join(input_dir, file_name)
                if file_name == os.path.basename(test_input_file_path):
                    destination_path = os.path.join(test_dir, file_name)
                    test_file_path = destination_path
                else:
                    destination_path = os.path.join(src_dir, file_name)
                    source_file_path = destination_path
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(source_path, destination_path)
                copied_files.append(destination_path)

        compile_results = run_maven_test_compile(project_dir, timeout)
        syntax_maven_output, syntax, compile_timeout_occurred, compile_error = compile_results

        timeout_occurred = timeout_occurred or compile_timeout_occurred

        assertions_density = assertions_density_java(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_java(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            # Cleanup copied files
            return {
                "execution_time_sec": None,
                "line_coverage_percent": None,
                "branch_coverage_percent": None,
                "timeout_occurred": timeout_occurred,
                "internal_error_occurred": error,
                "syntax": syntax,
                "syntax_maven_output": syntax_maven_output,
                "assertion_density": assertions_density,
                "assertions_mccabe_ratio": mccabe,
                "runtime_errors": None,
                "test_pass_rate": None,
                "test_maven_output": None
            }

        # Run 'mvn clean test' using the extracted method
        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        # Update the overall timeout and error status
        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error
        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._java_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percent": coverage_percentage["line"],
            "branch_coverage_percent": coverage_percentage["branch"],
            "timeout_occurred": timeout_occurred,
            "test_maven_output": test_maven_output,
            "syntax_maven_output": syntax_maven_output,
            "internal_error_occurred": error,
            "syntax": syntax,
            "runtime_errors": runtime_errors,
            "test_pass_rate": pass_rate,
            "assertion_density": assertions_density,
            "assertions_mccabe_ratio": mccabe
        }
    finally:
        for copied_file in copied_files:
            os.remove(None)

x_process_java_files_and_run_test_analysis__mutmut_mutants = {
'x_process_java_files_and_run_test_analysis__mutmut_1': x_process_java_files_and_run_test_analysis__mutmut_1, 
    'x_process_java_files_and_run_test_analysis__mutmut_2': x_process_java_files_and_run_test_analysis__mutmut_2, 
    'x_process_java_files_and_run_test_analysis__mutmut_3': x_process_java_files_and_run_test_analysis__mutmut_3, 
    'x_process_java_files_and_run_test_analysis__mutmut_4': x_process_java_files_and_run_test_analysis__mutmut_4, 
    'x_process_java_files_and_run_test_analysis__mutmut_5': x_process_java_files_and_run_test_analysis__mutmut_5, 
    'x_process_java_files_and_run_test_analysis__mutmut_6': x_process_java_files_and_run_test_analysis__mutmut_6, 
    'x_process_java_files_and_run_test_analysis__mutmut_7': x_process_java_files_and_run_test_analysis__mutmut_7, 
    'x_process_java_files_and_run_test_analysis__mutmut_8': x_process_java_files_and_run_test_analysis__mutmut_8, 
    'x_process_java_files_and_run_test_analysis__mutmut_9': x_process_java_files_and_run_test_analysis__mutmut_9, 
    'x_process_java_files_and_run_test_analysis__mutmut_10': x_process_java_files_and_run_test_analysis__mutmut_10, 
    'x_process_java_files_and_run_test_analysis__mutmut_11': x_process_java_files_and_run_test_analysis__mutmut_11, 
    'x_process_java_files_and_run_test_analysis__mutmut_12': x_process_java_files_and_run_test_analysis__mutmut_12, 
    'x_process_java_files_and_run_test_analysis__mutmut_13': x_process_java_files_and_run_test_analysis__mutmut_13, 
    'x_process_java_files_and_run_test_analysis__mutmut_14': x_process_java_files_and_run_test_analysis__mutmut_14, 
    'x_process_java_files_and_run_test_analysis__mutmut_15': x_process_java_files_and_run_test_analysis__mutmut_15, 
    'x_process_java_files_and_run_test_analysis__mutmut_16': x_process_java_files_and_run_test_analysis__mutmut_16, 
    'x_process_java_files_and_run_test_analysis__mutmut_17': x_process_java_files_and_run_test_analysis__mutmut_17, 
    'x_process_java_files_and_run_test_analysis__mutmut_18': x_process_java_files_and_run_test_analysis__mutmut_18, 
    'x_process_java_files_and_run_test_analysis__mutmut_19': x_process_java_files_and_run_test_analysis__mutmut_19, 
    'x_process_java_files_and_run_test_analysis__mutmut_20': x_process_java_files_and_run_test_analysis__mutmut_20, 
    'x_process_java_files_and_run_test_analysis__mutmut_21': x_process_java_files_and_run_test_analysis__mutmut_21, 
    'x_process_java_files_and_run_test_analysis__mutmut_22': x_process_java_files_and_run_test_analysis__mutmut_22, 
    'x_process_java_files_and_run_test_analysis__mutmut_23': x_process_java_files_and_run_test_analysis__mutmut_23, 
    'x_process_java_files_and_run_test_analysis__mutmut_24': x_process_java_files_and_run_test_analysis__mutmut_24, 
    'x_process_java_files_and_run_test_analysis__mutmut_25': x_process_java_files_and_run_test_analysis__mutmut_25, 
    'x_process_java_files_and_run_test_analysis__mutmut_26': x_process_java_files_and_run_test_analysis__mutmut_26, 
    'x_process_java_files_and_run_test_analysis__mutmut_27': x_process_java_files_and_run_test_analysis__mutmut_27, 
    'x_process_java_files_and_run_test_analysis__mutmut_28': x_process_java_files_and_run_test_analysis__mutmut_28, 
    'x_process_java_files_and_run_test_analysis__mutmut_29': x_process_java_files_and_run_test_analysis__mutmut_29, 
    'x_process_java_files_and_run_test_analysis__mutmut_30': x_process_java_files_and_run_test_analysis__mutmut_30, 
    'x_process_java_files_and_run_test_analysis__mutmut_31': x_process_java_files_and_run_test_analysis__mutmut_31, 
    'x_process_java_files_and_run_test_analysis__mutmut_32': x_process_java_files_and_run_test_analysis__mutmut_32, 
    'x_process_java_files_and_run_test_analysis__mutmut_33': x_process_java_files_and_run_test_analysis__mutmut_33, 
    'x_process_java_files_and_run_test_analysis__mutmut_34': x_process_java_files_and_run_test_analysis__mutmut_34, 
    'x_process_java_files_and_run_test_analysis__mutmut_35': x_process_java_files_and_run_test_analysis__mutmut_35, 
    'x_process_java_files_and_run_test_analysis__mutmut_36': x_process_java_files_and_run_test_analysis__mutmut_36, 
    'x_process_java_files_and_run_test_analysis__mutmut_37': x_process_java_files_and_run_test_analysis__mutmut_37, 
    'x_process_java_files_and_run_test_analysis__mutmut_38': x_process_java_files_and_run_test_analysis__mutmut_38, 
    'x_process_java_files_and_run_test_analysis__mutmut_39': x_process_java_files_and_run_test_analysis__mutmut_39, 
    'x_process_java_files_and_run_test_analysis__mutmut_40': x_process_java_files_and_run_test_analysis__mutmut_40, 
    'x_process_java_files_and_run_test_analysis__mutmut_41': x_process_java_files_and_run_test_analysis__mutmut_41, 
    'x_process_java_files_and_run_test_analysis__mutmut_42': x_process_java_files_and_run_test_analysis__mutmut_42, 
    'x_process_java_files_and_run_test_analysis__mutmut_43': x_process_java_files_and_run_test_analysis__mutmut_43, 
    'x_process_java_files_and_run_test_analysis__mutmut_44': x_process_java_files_and_run_test_analysis__mutmut_44, 
    'x_process_java_files_and_run_test_analysis__mutmut_45': x_process_java_files_and_run_test_analysis__mutmut_45, 
    'x_process_java_files_and_run_test_analysis__mutmut_46': x_process_java_files_and_run_test_analysis__mutmut_46, 
    'x_process_java_files_and_run_test_analysis__mutmut_47': x_process_java_files_and_run_test_analysis__mutmut_47, 
    'x_process_java_files_and_run_test_analysis__mutmut_48': x_process_java_files_and_run_test_analysis__mutmut_48, 
    'x_process_java_files_and_run_test_analysis__mutmut_49': x_process_java_files_and_run_test_analysis__mutmut_49, 
    'x_process_java_files_and_run_test_analysis__mutmut_50': x_process_java_files_and_run_test_analysis__mutmut_50, 
    'x_process_java_files_and_run_test_analysis__mutmut_51': x_process_java_files_and_run_test_analysis__mutmut_51, 
    'x_process_java_files_and_run_test_analysis__mutmut_52': x_process_java_files_and_run_test_analysis__mutmut_52, 
    'x_process_java_files_and_run_test_analysis__mutmut_53': x_process_java_files_and_run_test_analysis__mutmut_53, 
    'x_process_java_files_and_run_test_analysis__mutmut_54': x_process_java_files_and_run_test_analysis__mutmut_54, 
    'x_process_java_files_and_run_test_analysis__mutmut_55': x_process_java_files_and_run_test_analysis__mutmut_55, 
    'x_process_java_files_and_run_test_analysis__mutmut_56': x_process_java_files_and_run_test_analysis__mutmut_56, 
    'x_process_java_files_and_run_test_analysis__mutmut_57': x_process_java_files_and_run_test_analysis__mutmut_57, 
    'x_process_java_files_and_run_test_analysis__mutmut_58': x_process_java_files_and_run_test_analysis__mutmut_58, 
    'x_process_java_files_and_run_test_analysis__mutmut_59': x_process_java_files_and_run_test_analysis__mutmut_59, 
    'x_process_java_files_and_run_test_analysis__mutmut_60': x_process_java_files_and_run_test_analysis__mutmut_60, 
    'x_process_java_files_and_run_test_analysis__mutmut_61': x_process_java_files_and_run_test_analysis__mutmut_61, 
    'x_process_java_files_and_run_test_analysis__mutmut_62': x_process_java_files_and_run_test_analysis__mutmut_62, 
    'x_process_java_files_and_run_test_analysis__mutmut_63': x_process_java_files_and_run_test_analysis__mutmut_63, 
    'x_process_java_files_and_run_test_analysis__mutmut_64': x_process_java_files_and_run_test_analysis__mutmut_64, 
    'x_process_java_files_and_run_test_analysis__mutmut_65': x_process_java_files_and_run_test_analysis__mutmut_65, 
    'x_process_java_files_and_run_test_analysis__mutmut_66': x_process_java_files_and_run_test_analysis__mutmut_66, 
    'x_process_java_files_and_run_test_analysis__mutmut_67': x_process_java_files_and_run_test_analysis__mutmut_67, 
    'x_process_java_files_and_run_test_analysis__mutmut_68': x_process_java_files_and_run_test_analysis__mutmut_68, 
    'x_process_java_files_and_run_test_analysis__mutmut_69': x_process_java_files_and_run_test_analysis__mutmut_69, 
    'x_process_java_files_and_run_test_analysis__mutmut_70': x_process_java_files_and_run_test_analysis__mutmut_70, 
    'x_process_java_files_and_run_test_analysis__mutmut_71': x_process_java_files_and_run_test_analysis__mutmut_71, 
    'x_process_java_files_and_run_test_analysis__mutmut_72': x_process_java_files_and_run_test_analysis__mutmut_72, 
    'x_process_java_files_and_run_test_analysis__mutmut_73': x_process_java_files_and_run_test_analysis__mutmut_73, 
    'x_process_java_files_and_run_test_analysis__mutmut_74': x_process_java_files_and_run_test_analysis__mutmut_74, 
    'x_process_java_files_and_run_test_analysis__mutmut_75': x_process_java_files_and_run_test_analysis__mutmut_75, 
    'x_process_java_files_and_run_test_analysis__mutmut_76': x_process_java_files_and_run_test_analysis__mutmut_76, 
    'x_process_java_files_and_run_test_analysis__mutmut_77': x_process_java_files_and_run_test_analysis__mutmut_77, 
    'x_process_java_files_and_run_test_analysis__mutmut_78': x_process_java_files_and_run_test_analysis__mutmut_78, 
    'x_process_java_files_and_run_test_analysis__mutmut_79': x_process_java_files_and_run_test_analysis__mutmut_79, 
    'x_process_java_files_and_run_test_analysis__mutmut_80': x_process_java_files_and_run_test_analysis__mutmut_80, 
    'x_process_java_files_and_run_test_analysis__mutmut_81': x_process_java_files_and_run_test_analysis__mutmut_81, 
    'x_process_java_files_and_run_test_analysis__mutmut_82': x_process_java_files_and_run_test_analysis__mutmut_82, 
    'x_process_java_files_and_run_test_analysis__mutmut_83': x_process_java_files_and_run_test_analysis__mutmut_83, 
    'x_process_java_files_and_run_test_analysis__mutmut_84': x_process_java_files_and_run_test_analysis__mutmut_84, 
    'x_process_java_files_and_run_test_analysis__mutmut_85': x_process_java_files_and_run_test_analysis__mutmut_85, 
    'x_process_java_files_and_run_test_analysis__mutmut_86': x_process_java_files_and_run_test_analysis__mutmut_86, 
    'x_process_java_files_and_run_test_analysis__mutmut_87': x_process_java_files_and_run_test_analysis__mutmut_87, 
    'x_process_java_files_and_run_test_analysis__mutmut_88': x_process_java_files_and_run_test_analysis__mutmut_88, 
    'x_process_java_files_and_run_test_analysis__mutmut_89': x_process_java_files_and_run_test_analysis__mutmut_89, 
    'x_process_java_files_and_run_test_analysis__mutmut_90': x_process_java_files_and_run_test_analysis__mutmut_90, 
    'x_process_java_files_and_run_test_analysis__mutmut_91': x_process_java_files_and_run_test_analysis__mutmut_91, 
    'x_process_java_files_and_run_test_analysis__mutmut_92': x_process_java_files_and_run_test_analysis__mutmut_92, 
    'x_process_java_files_and_run_test_analysis__mutmut_93': x_process_java_files_and_run_test_analysis__mutmut_93, 
    'x_process_java_files_and_run_test_analysis__mutmut_94': x_process_java_files_and_run_test_analysis__mutmut_94, 
    'x_process_java_files_and_run_test_analysis__mutmut_95': x_process_java_files_and_run_test_analysis__mutmut_95, 
    'x_process_java_files_and_run_test_analysis__mutmut_96': x_process_java_files_and_run_test_analysis__mutmut_96, 
    'x_process_java_files_and_run_test_analysis__mutmut_97': x_process_java_files_and_run_test_analysis__mutmut_97, 
    'x_process_java_files_and_run_test_analysis__mutmut_98': x_process_java_files_and_run_test_analysis__mutmut_98, 
    'x_process_java_files_and_run_test_analysis__mutmut_99': x_process_java_files_and_run_test_analysis__mutmut_99, 
    'x_process_java_files_and_run_test_analysis__mutmut_100': x_process_java_files_and_run_test_analysis__mutmut_100, 
    'x_process_java_files_and_run_test_analysis__mutmut_101': x_process_java_files_and_run_test_analysis__mutmut_101, 
    'x_process_java_files_and_run_test_analysis__mutmut_102': x_process_java_files_and_run_test_analysis__mutmut_102, 
    'x_process_java_files_and_run_test_analysis__mutmut_103': x_process_java_files_and_run_test_analysis__mutmut_103, 
    'x_process_java_files_and_run_test_analysis__mutmut_104': x_process_java_files_and_run_test_analysis__mutmut_104
}

def process_java_files_and_run_test_analysis(*args, **kwargs):
    result = _mutmut_trampoline(x_process_java_files_and_run_test_analysis__mutmut_orig, x_process_java_files_and_run_test_analysis__mutmut_mutants, *args, **kwargs)
    return result 

process_java_files_and_run_test_analysis.__signature__ = _mutmut_signature(x_process_java_files_and_run_test_analysis__mutmut_orig)
x_process_java_files_and_run_test_analysis__mutmut_orig.__name__ = 'x_process_java_files_and_run_test_analysis'




def x_parse_report_and_compute_pass_rate__mutmut_orig(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_1(test_reports):
    report_files = glob.glob(None)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_2(test_reports):
    report_files = None

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_3(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 1
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_4(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = None
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_5(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 1
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_6(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = None
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_7(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 1
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_8(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = None
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_9(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 1

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_10(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = None

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_11(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(None)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_12(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = None
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_13(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = None
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_14(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests -= int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_15(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests = int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_16(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('XXtestsXX', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_17(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 1))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_18(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures -= int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_19(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures = int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_20(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('XXfailuresXX', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_21(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 1))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_22(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped -= int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_23(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped = int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_24(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('XXskippedXX', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_25(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 1))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_26(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors -= int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_27(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors = int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_28(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('XXerrorsXX', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_29(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 1))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_30(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests + total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_31(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures + total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_32(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests + total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_33(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures + total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_34(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = None
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_35(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed * total_tests) * 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_36(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) / 100 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_37(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 101 if total_tests != 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_38(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests == 0 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_39(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = (total_passed / total_tests) * 100 if total_tests != 1 else None
    return pass_percentage, total_runtime_errors


def x_parse_report_and_compute_pass_rate__mutmut_40(test_reports):
    report_files = glob.glob(test_reports)

    total_tests = 0
    total_failures = 0
    total_skipped = 0
    total_runtime_errors = 0

    for report_file in report_files:
        tree = ET.parse(report_file)
        root = tree.getroot()
        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_skipped += int(root.attrib.get('skipped', 0))
        total_runtime_errors += int(root.attrib.get('errors', 0))


    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Skipped: {total_skipped}")
    print(f"Passed: {total_tests - total_failures - total_skipped}")

    total_passed = total_tests - total_failures - total_skipped
    pass_percentage = None
    return pass_percentage, total_runtime_errors

x_parse_report_and_compute_pass_rate__mutmut_mutants = {
'x_parse_report_and_compute_pass_rate__mutmut_1': x_parse_report_and_compute_pass_rate__mutmut_1, 
    'x_parse_report_and_compute_pass_rate__mutmut_2': x_parse_report_and_compute_pass_rate__mutmut_2, 
    'x_parse_report_and_compute_pass_rate__mutmut_3': x_parse_report_and_compute_pass_rate__mutmut_3, 
    'x_parse_report_and_compute_pass_rate__mutmut_4': x_parse_report_and_compute_pass_rate__mutmut_4, 
    'x_parse_report_and_compute_pass_rate__mutmut_5': x_parse_report_and_compute_pass_rate__mutmut_5, 
    'x_parse_report_and_compute_pass_rate__mutmut_6': x_parse_report_and_compute_pass_rate__mutmut_6, 
    'x_parse_report_and_compute_pass_rate__mutmut_7': x_parse_report_and_compute_pass_rate__mutmut_7, 
    'x_parse_report_and_compute_pass_rate__mutmut_8': x_parse_report_and_compute_pass_rate__mutmut_8, 
    'x_parse_report_and_compute_pass_rate__mutmut_9': x_parse_report_and_compute_pass_rate__mutmut_9, 
    'x_parse_report_and_compute_pass_rate__mutmut_10': x_parse_report_and_compute_pass_rate__mutmut_10, 
    'x_parse_report_and_compute_pass_rate__mutmut_11': x_parse_report_and_compute_pass_rate__mutmut_11, 
    'x_parse_report_and_compute_pass_rate__mutmut_12': x_parse_report_and_compute_pass_rate__mutmut_12, 
    'x_parse_report_and_compute_pass_rate__mutmut_13': x_parse_report_and_compute_pass_rate__mutmut_13, 
    'x_parse_report_and_compute_pass_rate__mutmut_14': x_parse_report_and_compute_pass_rate__mutmut_14, 
    'x_parse_report_and_compute_pass_rate__mutmut_15': x_parse_report_and_compute_pass_rate__mutmut_15, 
    'x_parse_report_and_compute_pass_rate__mutmut_16': x_parse_report_and_compute_pass_rate__mutmut_16, 
    'x_parse_report_and_compute_pass_rate__mutmut_17': x_parse_report_and_compute_pass_rate__mutmut_17, 
    'x_parse_report_and_compute_pass_rate__mutmut_18': x_parse_report_and_compute_pass_rate__mutmut_18, 
    'x_parse_report_and_compute_pass_rate__mutmut_19': x_parse_report_and_compute_pass_rate__mutmut_19, 
    'x_parse_report_and_compute_pass_rate__mutmut_20': x_parse_report_and_compute_pass_rate__mutmut_20, 
    'x_parse_report_and_compute_pass_rate__mutmut_21': x_parse_report_and_compute_pass_rate__mutmut_21, 
    'x_parse_report_and_compute_pass_rate__mutmut_22': x_parse_report_and_compute_pass_rate__mutmut_22, 
    'x_parse_report_and_compute_pass_rate__mutmut_23': x_parse_report_and_compute_pass_rate__mutmut_23, 
    'x_parse_report_and_compute_pass_rate__mutmut_24': x_parse_report_and_compute_pass_rate__mutmut_24, 
    'x_parse_report_and_compute_pass_rate__mutmut_25': x_parse_report_and_compute_pass_rate__mutmut_25, 
    'x_parse_report_and_compute_pass_rate__mutmut_26': x_parse_report_and_compute_pass_rate__mutmut_26, 
    'x_parse_report_and_compute_pass_rate__mutmut_27': x_parse_report_and_compute_pass_rate__mutmut_27, 
    'x_parse_report_and_compute_pass_rate__mutmut_28': x_parse_report_and_compute_pass_rate__mutmut_28, 
    'x_parse_report_and_compute_pass_rate__mutmut_29': x_parse_report_and_compute_pass_rate__mutmut_29, 
    'x_parse_report_and_compute_pass_rate__mutmut_30': x_parse_report_and_compute_pass_rate__mutmut_30, 
    'x_parse_report_and_compute_pass_rate__mutmut_31': x_parse_report_and_compute_pass_rate__mutmut_31, 
    'x_parse_report_and_compute_pass_rate__mutmut_32': x_parse_report_and_compute_pass_rate__mutmut_32, 
    'x_parse_report_and_compute_pass_rate__mutmut_33': x_parse_report_and_compute_pass_rate__mutmut_33, 
    'x_parse_report_and_compute_pass_rate__mutmut_34': x_parse_report_and_compute_pass_rate__mutmut_34, 
    'x_parse_report_and_compute_pass_rate__mutmut_35': x_parse_report_and_compute_pass_rate__mutmut_35, 
    'x_parse_report_and_compute_pass_rate__mutmut_36': x_parse_report_and_compute_pass_rate__mutmut_36, 
    'x_parse_report_and_compute_pass_rate__mutmut_37': x_parse_report_and_compute_pass_rate__mutmut_37, 
    'x_parse_report_and_compute_pass_rate__mutmut_38': x_parse_report_and_compute_pass_rate__mutmut_38, 
    'x_parse_report_and_compute_pass_rate__mutmut_39': x_parse_report_and_compute_pass_rate__mutmut_39, 
    'x_parse_report_and_compute_pass_rate__mutmut_40': x_parse_report_and_compute_pass_rate__mutmut_40
}

def parse_report_and_compute_pass_rate(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_report_and_compute_pass_rate__mutmut_orig, x_parse_report_and_compute_pass_rate__mutmut_mutants, *args, **kwargs)
    return result 

parse_report_and_compute_pass_rate.__signature__ = _mutmut_signature(x_parse_report_and_compute_pass_rate__mutmut_orig)
x_parse_report_and_compute_pass_rate__mutmut_orig.__name__ = 'x_parse_report_and_compute_pass_rate'


