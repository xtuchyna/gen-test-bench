
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


import json
import os.path
import signal
import subprocess
import threading
import time
import pytest


def x_run_pytest_with_timeout__mutmut_orig(filename, timeout=60):
    def run():
        pytest.main([filename, '--tb=short'])

    thread = threading.Thread(target=run)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        raise TimeoutError("Test execution exceeded the time limit of 60 seconds")


def x_run_pytest_with_timeout__mutmut_1(filename, timeout=61):
    def run():
        pytest.main([filename, '--tb=short'])

    thread = threading.Thread(target=run)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        raise TimeoutError("Test execution exceeded the time limit of 60 seconds")


def x_run_pytest_with_timeout__mutmut_2(filename, timeout=60):
    def run():
        pytest.main([filename, 'XX--tb=shortXX'])

    thread = threading.Thread(target=run)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        raise TimeoutError("Test execution exceeded the time limit of 60 seconds")


def x_run_pytest_with_timeout__mutmut_3(filename, timeout=60):
    def run():
        pytest.main([filename, '--tb=short'])

    thread = threading.Thread(target=None)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        raise TimeoutError("Test execution exceeded the time limit of 60 seconds")


def x_run_pytest_with_timeout__mutmut_4(filename, timeout=60):
    def run():
        pytest.main([filename, '--tb=short'])

    thread = None
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        raise TimeoutError("Test execution exceeded the time limit of 60 seconds")


def x_run_pytest_with_timeout__mutmut_5(filename, timeout=60):
    def run():
        pytest.main([filename, '--tb=short'])

    thread = threading.Thread(target=run)
    thread.start()
    thread.join(None)
    if thread.is_alive():
        raise TimeoutError("Test execution exceeded the time limit of 60 seconds")


def x_run_pytest_with_timeout__mutmut_6(filename, timeout=60):
    def run():
        pytest.main([filename, '--tb=short'])

    thread = threading.Thread(target=run)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        raise TimeoutError("XXTest execution exceeded the time limit of 60 secondsXX")

x_run_pytest_with_timeout__mutmut_mutants = {
'x_run_pytest_with_timeout__mutmut_1': x_run_pytest_with_timeout__mutmut_1, 
    'x_run_pytest_with_timeout__mutmut_2': x_run_pytest_with_timeout__mutmut_2, 
    'x_run_pytest_with_timeout__mutmut_3': x_run_pytest_with_timeout__mutmut_3, 
    'x_run_pytest_with_timeout__mutmut_4': x_run_pytest_with_timeout__mutmut_4, 
    'x_run_pytest_with_timeout__mutmut_5': x_run_pytest_with_timeout__mutmut_5, 
    'x_run_pytest_with_timeout__mutmut_6': x_run_pytest_with_timeout__mutmut_6
}

def run_pytest_with_timeout(*args, **kwargs):
    result = _mutmut_trampoline(x_run_pytest_with_timeout__mutmut_orig, x_run_pytest_with_timeout__mutmut_mutants, *args, **kwargs)
    return result 

run_pytest_with_timeout.__signature__ = _mutmut_signature(x_run_pytest_with_timeout__mutmut_orig)
x_run_pytest_with_timeout__mutmut_orig.__name__ = 'x_run_pytest_with_timeout'




def x_timeout_handler__mutmut_orig(a, b):
    raise Exception("Timeout")


def x_timeout_handler__mutmut_1(a, b):
    raise Exception("XXTimeoutXX")

x_timeout_handler__mutmut_mutants = {
'x_timeout_handler__mutmut_1': x_timeout_handler__mutmut_1
}

def timeout_handler(*args, **kwargs):
    result = _mutmut_trampoline(x_timeout_handler__mutmut_orig, x_timeout_handler__mutmut_mutants, *args, **kwargs)
    return result 

timeout_handler.__signature__ = _mutmut_signature(x_timeout_handler__mutmut_orig)
x_timeout_handler__mutmut_orig.__name__ = 'x_timeout_handler'




@pytest.mark.timeout(30, signal)  # Optional timeout for individual tests
def get_coverage(filename, branch=False):
    directory = os.path.dirname(filename)

    if branch:
        args = ["pytest", directory, "--tb=short", "--timeout=30", "--timeout-method=signal",
                "--cov", directory, "--cov-report=json:./coverage.json", "--cov-branch", filename]
    else:
        args = ["pytest", directory, "--tb=short", "--timeout=30", "--timeout-method=signal",
                "--cov", directory, "--cov-report=json:./coverage.json", filename]

    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    start_time = time.time()

    # Wait for the process to complete or terminate it if it exceeds the timeout
    while process.poll() is None:
        if time.time() - start_time > 30:
            # Kill the process if the timeout is exceeded
            process.terminate()  # Kill all processes in the group
            print(f"Test execution exceeded {30} seconds and was terminated.")
            return None

    # Collect stdout and stderr after the process completes
    stdout, stderr = process.communicate()

    # Print the output of pytest
    print(stdout.decode())
    print(stderr.decode())

    # Parse the coverage JSON report
    json_report_path = 'coverage.json'
    if os.path.exists(json_report_path):
        with open(json_report_path, 'r') as json_file:
            coverage_data = json.load(json_file)
            # Extract the overall coverage percentage
            coverage_percentage = round(coverage_data['totals']['percent_covered'], 2)
            return coverage_percentage
    else:
        print("Coverage report not found.")
        return None
