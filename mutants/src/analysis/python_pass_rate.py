
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


import re
import os
import shutil
import subprocess
import time
import json
import tempfile

from src.analysis.python_coverage_computation import get_coverage


def x_run_tests__mutmut_orig(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_1(test_file, timeout=31):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_2(test_file, timeout=30):
    original_dir = None
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_3(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(None, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_4(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "XX../../..XX")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_5(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join( "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_6(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = None
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_7(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(None, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_8(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(None))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_9(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join( os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_10(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = None

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_11(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(None, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_12(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, None)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_13(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2( temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_14(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file,)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_15(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(None)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_16(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = None
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_17(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(None):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_18(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith("XX.pyXX") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_19(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and  file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_20(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("XXtestXX"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_21(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") or not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_22(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(None, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_23(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, None)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_24(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join( file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_25(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir,)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_26(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = None
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_27(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(None, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_28(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, None)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_29(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2( temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_30(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path,)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_31(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(None)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_32(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["XXpytestXX", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_33(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "XX--tb=shortXX", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_34(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "XX-qXX", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_35(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "XX--json-reportXX"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_36(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = None
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_37(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_38(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_39(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_40(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_41(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = None

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_42(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = None

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_43(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is not None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_44(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() + start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_45(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time >= timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_46(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, False

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_47(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() + start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_48(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = None
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_49(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = None

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_50(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(None)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_51(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = None
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_52(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(None, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_53(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=False)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_54(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage( branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_55(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path,)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_56(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = None

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_57(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("XXLine coverage: XX", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_58(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", None)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_59(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ",)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_60(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("XXBranch coverage: XX", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_61(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", None)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_62(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ",)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_63(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 1

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_64(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = None

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_65(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("XXSTDOUT:XX")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_66(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("XXSTDERR:XX")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_67(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"XX(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+XX", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_68(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = None

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_69(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = None
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_70(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error == "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_71(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "XXAssertionErrorXX":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_72(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors -= 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_73(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors = 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_74(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 2

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_75(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("XXRuntime errors: XX", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_76(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", None)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_77(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ",)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_78(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = 'XX.report.jsonXX'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_79(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = None  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_80(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(None):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_81(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(None, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_82(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'XXrXX') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_83(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open( 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_84(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(None)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_85(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = None
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_86(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["XXsummaryXX"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_87(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report[None].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_88(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("XXtotalXX", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_89(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = None
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_90(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["XXsummaryXX"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_91(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report[None].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_92(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("XXpassedXX", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_93(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = None
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_94(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["XXsummaryXX"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_95(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report[None].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_96(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("XXfailedXX", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_97(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = None
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_98(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is not None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_99(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is not None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_100(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None and passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_101(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = ""
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_102(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests * total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_103(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) / 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_104(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 101 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_105(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests >= 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_106(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 1 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_107(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 1

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_108(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = None

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_109(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'XXtotal_testsXX': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_110(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is  None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_111(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'XXpassed_testsXX': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_112(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'XXfailed_testsXX': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_113(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'XXpass_percentageXX': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_114(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(None, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_115(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 3) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_116(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round( 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_117(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is  None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_118(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'XXexecution_timeXX': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_119(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'XXruntime_errorsXX': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_120(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'XXtimeoutXX': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_121(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': True,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_122(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'XXbranch_coverageXX': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_123(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'XXline_coverageXX': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_124(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = None
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_125(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("XXResult: XX", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_126(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", None)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_127(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ",)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_128(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, True
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_129(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("XXTest report not found.XX")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_130(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, True
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_131(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("XXError occurred: XX", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_132(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", None)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_133(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ",)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_134(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(None)
        shutil.rmtree(temp_dir)


def x_run_tests__mutmut_135(test_file, timeout=30):
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp(dir=os.path.abspath(os.path.join(original_dir, "../../..")))
    temp_file_path = os.path.join(temp_dir, os.path.basename(test_file))

    try:
        # Copy the test file to the temporary directory
        shutil.copy2(test_file, temp_file_path)
        current_dir = os.path.dirname(test_file)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and not file_name.startswith("test"):
                source_path = os.path.join(current_dir, file_name)
                shutil.copy2(source_path, temp_dir)

        # Change to the temporary directory
        os.chdir(temp_dir)

        # Run pytest in the copied test file with subprocess
        args = ["pytest", temp_file_path, "--tb=short", "-q", "--json-report"]
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        start_time = time.time()

        # Wait for the process to complete or terminate it if it exceeds the timeout
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.terminate()
                print(f"Test execution exceeded {timeout} seconds and was terminated.")
                return None, True

        exec_time = time.time() - start_time
        stdout, stderr = process.communicate()

        line_coverage = get_coverage(temp_file_path)
        branch_coverage = get_coverage(temp_file_path, branch=True)

        print("Line coverage: ", line_coverage)
        print("Branch coverage: ", branch_coverage)

        runtime_errors = 0

        print("STDOUT:")
        print(stdout.decode())
        print("STDERR:")
        print(stderr.decode())

        # Regex pattern for runtime errors (excluding AssertionError)
        runtime_error_pattern = re.compile(
            r"(?<=Traceback \(most recent call last\):\n).*?\n(\w+Error): .+", re.DOTALL
        )

        # Parse stdout and stderr for runtime errors
        for output in (stdout, stderr):
            matches = runtime_error_pattern.findall(output.decode())
            for error in matches:
                if error != "AssertionError":  # Explicitly exclude AssertionError
                    runtime_errors += 1

        print("Runtime errors: ", runtime_errors)
        # Parse the pytest json report if available
        json_report_path = '.report.json'  # This is the default pytest json-report output file
        if os.path.exists(json_report_path):
            with open(json_report_path, 'r') as json_file:
                test_report = json.load(json_file)
                total_tests = test_report["summary"].get("total", None)
                passed_tests = test_report["summary"].get("passed", None)
                failed_tests = test_report["summary"].get("failed", None)
                if total_tests is None or passed_tests is None:
                    pass_percentage = None
                else:
                    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                result = {
                    'total_tests': total_tests if total_tests is not None else None,
                    'passed_tests': passed_tests,
                    'failed_tests': failed_tests,
                    'pass_percentage': round(pass_percentage, 2) if pass_percentage is not None else None,
                    'execution_time': exec_time,
                    'runtime_errors': runtime_errors,
                    'timeout': False,
                    'branch_coverage': branch_coverage,
                    'line_coverage': line_coverage
                }
                print("Result: ", result)

                return result, False
        else:
            print("Test report not found.")
            return None, False
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        os.chdir(original_dir)
        shutil.rmtree(None)

x_run_tests__mutmut_mutants = {
'x_run_tests__mutmut_1': x_run_tests__mutmut_1, 
    'x_run_tests__mutmut_2': x_run_tests__mutmut_2, 
    'x_run_tests__mutmut_3': x_run_tests__mutmut_3, 
    'x_run_tests__mutmut_4': x_run_tests__mutmut_4, 
    'x_run_tests__mutmut_5': x_run_tests__mutmut_5, 
    'x_run_tests__mutmut_6': x_run_tests__mutmut_6, 
    'x_run_tests__mutmut_7': x_run_tests__mutmut_7, 
    'x_run_tests__mutmut_8': x_run_tests__mutmut_8, 
    'x_run_tests__mutmut_9': x_run_tests__mutmut_9, 
    'x_run_tests__mutmut_10': x_run_tests__mutmut_10, 
    'x_run_tests__mutmut_11': x_run_tests__mutmut_11, 
    'x_run_tests__mutmut_12': x_run_tests__mutmut_12, 
    'x_run_tests__mutmut_13': x_run_tests__mutmut_13, 
    'x_run_tests__mutmut_14': x_run_tests__mutmut_14, 
    'x_run_tests__mutmut_15': x_run_tests__mutmut_15, 
    'x_run_tests__mutmut_16': x_run_tests__mutmut_16, 
    'x_run_tests__mutmut_17': x_run_tests__mutmut_17, 
    'x_run_tests__mutmut_18': x_run_tests__mutmut_18, 
    'x_run_tests__mutmut_19': x_run_tests__mutmut_19, 
    'x_run_tests__mutmut_20': x_run_tests__mutmut_20, 
    'x_run_tests__mutmut_21': x_run_tests__mutmut_21, 
    'x_run_tests__mutmut_22': x_run_tests__mutmut_22, 
    'x_run_tests__mutmut_23': x_run_tests__mutmut_23, 
    'x_run_tests__mutmut_24': x_run_tests__mutmut_24, 
    'x_run_tests__mutmut_25': x_run_tests__mutmut_25, 
    'x_run_tests__mutmut_26': x_run_tests__mutmut_26, 
    'x_run_tests__mutmut_27': x_run_tests__mutmut_27, 
    'x_run_tests__mutmut_28': x_run_tests__mutmut_28, 
    'x_run_tests__mutmut_29': x_run_tests__mutmut_29, 
    'x_run_tests__mutmut_30': x_run_tests__mutmut_30, 
    'x_run_tests__mutmut_31': x_run_tests__mutmut_31, 
    'x_run_tests__mutmut_32': x_run_tests__mutmut_32, 
    'x_run_tests__mutmut_33': x_run_tests__mutmut_33, 
    'x_run_tests__mutmut_34': x_run_tests__mutmut_34, 
    'x_run_tests__mutmut_35': x_run_tests__mutmut_35, 
    'x_run_tests__mutmut_36': x_run_tests__mutmut_36, 
    'x_run_tests__mutmut_37': x_run_tests__mutmut_37, 
    'x_run_tests__mutmut_38': x_run_tests__mutmut_38, 
    'x_run_tests__mutmut_39': x_run_tests__mutmut_39, 
    'x_run_tests__mutmut_40': x_run_tests__mutmut_40, 
    'x_run_tests__mutmut_41': x_run_tests__mutmut_41, 
    'x_run_tests__mutmut_42': x_run_tests__mutmut_42, 
    'x_run_tests__mutmut_43': x_run_tests__mutmut_43, 
    'x_run_tests__mutmut_44': x_run_tests__mutmut_44, 
    'x_run_tests__mutmut_45': x_run_tests__mutmut_45, 
    'x_run_tests__mutmut_46': x_run_tests__mutmut_46, 
    'x_run_tests__mutmut_47': x_run_tests__mutmut_47, 
    'x_run_tests__mutmut_48': x_run_tests__mutmut_48, 
    'x_run_tests__mutmut_49': x_run_tests__mutmut_49, 
    'x_run_tests__mutmut_50': x_run_tests__mutmut_50, 
    'x_run_tests__mutmut_51': x_run_tests__mutmut_51, 
    'x_run_tests__mutmut_52': x_run_tests__mutmut_52, 
    'x_run_tests__mutmut_53': x_run_tests__mutmut_53, 
    'x_run_tests__mutmut_54': x_run_tests__mutmut_54, 
    'x_run_tests__mutmut_55': x_run_tests__mutmut_55, 
    'x_run_tests__mutmut_56': x_run_tests__mutmut_56, 
    'x_run_tests__mutmut_57': x_run_tests__mutmut_57, 
    'x_run_tests__mutmut_58': x_run_tests__mutmut_58, 
    'x_run_tests__mutmut_59': x_run_tests__mutmut_59, 
    'x_run_tests__mutmut_60': x_run_tests__mutmut_60, 
    'x_run_tests__mutmut_61': x_run_tests__mutmut_61, 
    'x_run_tests__mutmut_62': x_run_tests__mutmut_62, 
    'x_run_tests__mutmut_63': x_run_tests__mutmut_63, 
    'x_run_tests__mutmut_64': x_run_tests__mutmut_64, 
    'x_run_tests__mutmut_65': x_run_tests__mutmut_65, 
    'x_run_tests__mutmut_66': x_run_tests__mutmut_66, 
    'x_run_tests__mutmut_67': x_run_tests__mutmut_67, 
    'x_run_tests__mutmut_68': x_run_tests__mutmut_68, 
    'x_run_tests__mutmut_69': x_run_tests__mutmut_69, 
    'x_run_tests__mutmut_70': x_run_tests__mutmut_70, 
    'x_run_tests__mutmut_71': x_run_tests__mutmut_71, 
    'x_run_tests__mutmut_72': x_run_tests__mutmut_72, 
    'x_run_tests__mutmut_73': x_run_tests__mutmut_73, 
    'x_run_tests__mutmut_74': x_run_tests__mutmut_74, 
    'x_run_tests__mutmut_75': x_run_tests__mutmut_75, 
    'x_run_tests__mutmut_76': x_run_tests__mutmut_76, 
    'x_run_tests__mutmut_77': x_run_tests__mutmut_77, 
    'x_run_tests__mutmut_78': x_run_tests__mutmut_78, 
    'x_run_tests__mutmut_79': x_run_tests__mutmut_79, 
    'x_run_tests__mutmut_80': x_run_tests__mutmut_80, 
    'x_run_tests__mutmut_81': x_run_tests__mutmut_81, 
    'x_run_tests__mutmut_82': x_run_tests__mutmut_82, 
    'x_run_tests__mutmut_83': x_run_tests__mutmut_83, 
    'x_run_tests__mutmut_84': x_run_tests__mutmut_84, 
    'x_run_tests__mutmut_85': x_run_tests__mutmut_85, 
    'x_run_tests__mutmut_86': x_run_tests__mutmut_86, 
    'x_run_tests__mutmut_87': x_run_tests__mutmut_87, 
    'x_run_tests__mutmut_88': x_run_tests__mutmut_88, 
    'x_run_tests__mutmut_89': x_run_tests__mutmut_89, 
    'x_run_tests__mutmut_90': x_run_tests__mutmut_90, 
    'x_run_tests__mutmut_91': x_run_tests__mutmut_91, 
    'x_run_tests__mutmut_92': x_run_tests__mutmut_92, 
    'x_run_tests__mutmut_93': x_run_tests__mutmut_93, 
    'x_run_tests__mutmut_94': x_run_tests__mutmut_94, 
    'x_run_tests__mutmut_95': x_run_tests__mutmut_95, 
    'x_run_tests__mutmut_96': x_run_tests__mutmut_96, 
    'x_run_tests__mutmut_97': x_run_tests__mutmut_97, 
    'x_run_tests__mutmut_98': x_run_tests__mutmut_98, 
    'x_run_tests__mutmut_99': x_run_tests__mutmut_99, 
    'x_run_tests__mutmut_100': x_run_tests__mutmut_100, 
    'x_run_tests__mutmut_101': x_run_tests__mutmut_101, 
    'x_run_tests__mutmut_102': x_run_tests__mutmut_102, 
    'x_run_tests__mutmut_103': x_run_tests__mutmut_103, 
    'x_run_tests__mutmut_104': x_run_tests__mutmut_104, 
    'x_run_tests__mutmut_105': x_run_tests__mutmut_105, 
    'x_run_tests__mutmut_106': x_run_tests__mutmut_106, 
    'x_run_tests__mutmut_107': x_run_tests__mutmut_107, 
    'x_run_tests__mutmut_108': x_run_tests__mutmut_108, 
    'x_run_tests__mutmut_109': x_run_tests__mutmut_109, 
    'x_run_tests__mutmut_110': x_run_tests__mutmut_110, 
    'x_run_tests__mutmut_111': x_run_tests__mutmut_111, 
    'x_run_tests__mutmut_112': x_run_tests__mutmut_112, 
    'x_run_tests__mutmut_113': x_run_tests__mutmut_113, 
    'x_run_tests__mutmut_114': x_run_tests__mutmut_114, 
    'x_run_tests__mutmut_115': x_run_tests__mutmut_115, 
    'x_run_tests__mutmut_116': x_run_tests__mutmut_116, 
    'x_run_tests__mutmut_117': x_run_tests__mutmut_117, 
    'x_run_tests__mutmut_118': x_run_tests__mutmut_118, 
    'x_run_tests__mutmut_119': x_run_tests__mutmut_119, 
    'x_run_tests__mutmut_120': x_run_tests__mutmut_120, 
    'x_run_tests__mutmut_121': x_run_tests__mutmut_121, 
    'x_run_tests__mutmut_122': x_run_tests__mutmut_122, 
    'x_run_tests__mutmut_123': x_run_tests__mutmut_123, 
    'x_run_tests__mutmut_124': x_run_tests__mutmut_124, 
    'x_run_tests__mutmut_125': x_run_tests__mutmut_125, 
    'x_run_tests__mutmut_126': x_run_tests__mutmut_126, 
    'x_run_tests__mutmut_127': x_run_tests__mutmut_127, 
    'x_run_tests__mutmut_128': x_run_tests__mutmut_128, 
    'x_run_tests__mutmut_129': x_run_tests__mutmut_129, 
    'x_run_tests__mutmut_130': x_run_tests__mutmut_130, 
    'x_run_tests__mutmut_131': x_run_tests__mutmut_131, 
    'x_run_tests__mutmut_132': x_run_tests__mutmut_132, 
    'x_run_tests__mutmut_133': x_run_tests__mutmut_133, 
    'x_run_tests__mutmut_134': x_run_tests__mutmut_134, 
    'x_run_tests__mutmut_135': x_run_tests__mutmut_135
}

def run_tests(*args, **kwargs):
    result = _mutmut_trampoline(x_run_tests__mutmut_orig, x_run_tests__mutmut_mutants, *args, **kwargs)
    return result 

run_tests.__signature__ = _mutmut_signature(x_run_tests__mutmut_orig)
x_run_tests__mutmut_orig.__name__ = 'x_run_tests'





