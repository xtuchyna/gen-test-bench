
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

from src.analysis.java_analysis import run_maven_test_compile, run_maven_clean_test, compute_coverage_percentage, \
    parse_report_and_compute_pass_rate
from src.analysis.kotlin_assertion_ratios import assertions_density_kotlin, assertions_mccabe_ratio_kotlin
from src.analysis.python_validation import CompileStatus
from src.config import Config


def x_run_ktlint__mutmut_orig(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_1(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['XXjavaXX', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_2(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', 'XX-jarXX', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_3(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_4(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path], stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_5(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_6(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_7(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = None

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_8(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("XXktlint.jar output:XX")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_9(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("XXktlint.jar error output:XX")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_10(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout - result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_11(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = None
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_12(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(None)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_13(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = None

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_14(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("XXFound ktlint.jar warnings:XX")
            for error in warnings:
                print(error)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_15(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(None)
        else:
            print("No ktlint.jar issues found for this file.")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []


def x_run_ktlint__mutmut_16(kotlin_file_path):
    """Run ktlint for a Kotlin file and return a list of style errors."""
    try:
        result = subprocess.run(
            ['java', '-jar', Config.get_ktlint_path(), kotlin_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if result.stdout:
            print("ktlint.jar output:")
            print(result.stdout)

        if result.stderr:
            print("ktlint.jar error output:")
            print(result.stderr)

        # Combine both stdout and stderr for processing
        output = result.stdout + result.stderr
        warnings = parse_ktlint_output(output)

        if warnings:
            print("Found ktlint.jar warnings:")
            for error in warnings:
                print(error)
        else:
            print("XXNo ktlint.jar issues found for this file.XX")

        return warnings

    except Exception as e:
        print(f"Error running ktlint.jar: {e}")
        return []

x_run_ktlint__mutmut_mutants = {
'x_run_ktlint__mutmut_1': x_run_ktlint__mutmut_1, 
    'x_run_ktlint__mutmut_2': x_run_ktlint__mutmut_2, 
    'x_run_ktlint__mutmut_3': x_run_ktlint__mutmut_3, 
    'x_run_ktlint__mutmut_4': x_run_ktlint__mutmut_4, 
    'x_run_ktlint__mutmut_5': x_run_ktlint__mutmut_5, 
    'x_run_ktlint__mutmut_6': x_run_ktlint__mutmut_6, 
    'x_run_ktlint__mutmut_7': x_run_ktlint__mutmut_7, 
    'x_run_ktlint__mutmut_8': x_run_ktlint__mutmut_8, 
    'x_run_ktlint__mutmut_9': x_run_ktlint__mutmut_9, 
    'x_run_ktlint__mutmut_10': x_run_ktlint__mutmut_10, 
    'x_run_ktlint__mutmut_11': x_run_ktlint__mutmut_11, 
    'x_run_ktlint__mutmut_12': x_run_ktlint__mutmut_12, 
    'x_run_ktlint__mutmut_13': x_run_ktlint__mutmut_13, 
    'x_run_ktlint__mutmut_14': x_run_ktlint__mutmut_14, 
    'x_run_ktlint__mutmut_15': x_run_ktlint__mutmut_15, 
    'x_run_ktlint__mutmut_16': x_run_ktlint__mutmut_16
}

def run_ktlint(*args, **kwargs):
    result = _mutmut_trampoline(x_run_ktlint__mutmut_orig, x_run_ktlint__mutmut_mutants, *args, **kwargs)
    return result 

run_ktlint.__signature__ = _mutmut_signature(x_run_ktlint__mutmut_orig)
x_run_ktlint__mutmut_orig.__name__ = 'x_run_ktlint'




import re
from collections import defaultdict


def x_parse_ktlint_output__mutmut_orig(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_1(output):
    # Initialize result structures
    errors = None
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_2(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(None)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_3(output):
    # Initialize result structures
    errors = []
    rule_summary = None

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_4(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'XX^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$XX')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_5(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = None
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_6(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'XX^\s*(.+?): (\d+)$XX')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_7(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = None

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_8(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("XX\nXX")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_9(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = None
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_10(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = False

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_11(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = None

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_12(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "XXSummary error countXX" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_13(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" not in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_14(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = True  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_15(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = None  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_16(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            break

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_17(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(None)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_18(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = None
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_19(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = None
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_20(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "XXfile_pathXX": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_21(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "XXlineXX": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_22(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(None),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_23(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "XXcolumnXX": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_24(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(None),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_25(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "XXmessageXX": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_26(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "XXruleXX": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_27(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(None)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_28(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = None
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_29(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = None
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_30(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[None] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_31(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(None)

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_32(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = None

    return {
        "errors": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_33(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "XXerrorsXX": errors,
        "rule_summary": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_34(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "XXrule_summaryXX": dict(rule_summary)
    }


def x_parse_ktlint_output__mutmut_35(output):
    # Initialize result structures
    errors = []
    rule_summary = defaultdict(int)

    # Regex patterns
    error_pattern = re.compile(r'^(.*?):(\d+):(\d+): (.+?) \((.+?)\)$')
    summary_pattern = re.compile(r'^\s*(.+?): (\d+)$')

    lines = output.split("\n")
    parsing_errors = True

    for line in lines:
        if "Summary error count" in line:
            parsing_errors = False  # Start parsing the summary section
            continue

        if parsing_errors:
            match = error_pattern.match(line)
            if match:
                file_path, line_no, col_no, message, rule = match.groups()
                errors.append({
                    "file_path": file_path,
                    "line": int(line_no),
                    "column": int(col_no),
                    "message": message,
                    "rule": rule
                })
        else:
            match = summary_pattern.match(line)
            if match:
                rule, count = match.groups()
                rule_summary[rule] = int(count)

    return {
        "errors": errors,
        "rule_summary": dict(None)
    }

x_parse_ktlint_output__mutmut_mutants = {
'x_parse_ktlint_output__mutmut_1': x_parse_ktlint_output__mutmut_1, 
    'x_parse_ktlint_output__mutmut_2': x_parse_ktlint_output__mutmut_2, 
    'x_parse_ktlint_output__mutmut_3': x_parse_ktlint_output__mutmut_3, 
    'x_parse_ktlint_output__mutmut_4': x_parse_ktlint_output__mutmut_4, 
    'x_parse_ktlint_output__mutmut_5': x_parse_ktlint_output__mutmut_5, 
    'x_parse_ktlint_output__mutmut_6': x_parse_ktlint_output__mutmut_6, 
    'x_parse_ktlint_output__mutmut_7': x_parse_ktlint_output__mutmut_7, 
    'x_parse_ktlint_output__mutmut_8': x_parse_ktlint_output__mutmut_8, 
    'x_parse_ktlint_output__mutmut_9': x_parse_ktlint_output__mutmut_9, 
    'x_parse_ktlint_output__mutmut_10': x_parse_ktlint_output__mutmut_10, 
    'x_parse_ktlint_output__mutmut_11': x_parse_ktlint_output__mutmut_11, 
    'x_parse_ktlint_output__mutmut_12': x_parse_ktlint_output__mutmut_12, 
    'x_parse_ktlint_output__mutmut_13': x_parse_ktlint_output__mutmut_13, 
    'x_parse_ktlint_output__mutmut_14': x_parse_ktlint_output__mutmut_14, 
    'x_parse_ktlint_output__mutmut_15': x_parse_ktlint_output__mutmut_15, 
    'x_parse_ktlint_output__mutmut_16': x_parse_ktlint_output__mutmut_16, 
    'x_parse_ktlint_output__mutmut_17': x_parse_ktlint_output__mutmut_17, 
    'x_parse_ktlint_output__mutmut_18': x_parse_ktlint_output__mutmut_18, 
    'x_parse_ktlint_output__mutmut_19': x_parse_ktlint_output__mutmut_19, 
    'x_parse_ktlint_output__mutmut_20': x_parse_ktlint_output__mutmut_20, 
    'x_parse_ktlint_output__mutmut_21': x_parse_ktlint_output__mutmut_21, 
    'x_parse_ktlint_output__mutmut_22': x_parse_ktlint_output__mutmut_22, 
    'x_parse_ktlint_output__mutmut_23': x_parse_ktlint_output__mutmut_23, 
    'x_parse_ktlint_output__mutmut_24': x_parse_ktlint_output__mutmut_24, 
    'x_parse_ktlint_output__mutmut_25': x_parse_ktlint_output__mutmut_25, 
    'x_parse_ktlint_output__mutmut_26': x_parse_ktlint_output__mutmut_26, 
    'x_parse_ktlint_output__mutmut_27': x_parse_ktlint_output__mutmut_27, 
    'x_parse_ktlint_output__mutmut_28': x_parse_ktlint_output__mutmut_28, 
    'x_parse_ktlint_output__mutmut_29': x_parse_ktlint_output__mutmut_29, 
    'x_parse_ktlint_output__mutmut_30': x_parse_ktlint_output__mutmut_30, 
    'x_parse_ktlint_output__mutmut_31': x_parse_ktlint_output__mutmut_31, 
    'x_parse_ktlint_output__mutmut_32': x_parse_ktlint_output__mutmut_32, 
    'x_parse_ktlint_output__mutmut_33': x_parse_ktlint_output__mutmut_33, 
    'x_parse_ktlint_output__mutmut_34': x_parse_ktlint_output__mutmut_34, 
    'x_parse_ktlint_output__mutmut_35': x_parse_ktlint_output__mutmut_35
}

def parse_ktlint_output(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_ktlint_output__mutmut_orig, x_parse_ktlint_output__mutmut_mutants, *args, **kwargs)
    return result 

parse_ktlint_output.__signature__ = _mutmut_signature(x_parse_ktlint_output__mutmut_orig)
x_parse_ktlint_output__mutmut_orig.__name__ = 'x_parse_ktlint_output'




def x_get_code_file_path__mutmut_orig(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_1(test_file_path):
    dir = os.path.dirname(None)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_2(test_file_path):
    dir = None
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_3(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(None):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_4(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith("XX.ktXX") and not file_name.endswith("Test.kt"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_5(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and  file_name.endswith("Test.kt"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_6(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("XXTest.ktXX"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_7(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") or not file_name.endswith("Test.kt"):
            return os.path.join(dir, file_name)
    return None


def x_get_code_file_path__mutmut_8(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join(None, file_name)
    return None


def x_get_code_file_path__mutmut_9(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join(dir, None)
    return None


def x_get_code_file_path__mutmut_10(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join( file_name)
    return None


def x_get_code_file_path__mutmut_11(test_file_path):
    dir = os.path.dirname(test_file_path)
    for file_name in os.listdir(dir):
        if file_name.endswith(".kt") and not file_name.endswith("Test.kt"):
            return os.path.join(dir,)
    return None

x_get_code_file_path__mutmut_mutants = {
'x_get_code_file_path__mutmut_1': x_get_code_file_path__mutmut_1, 
    'x_get_code_file_path__mutmut_2': x_get_code_file_path__mutmut_2, 
    'x_get_code_file_path__mutmut_3': x_get_code_file_path__mutmut_3, 
    'x_get_code_file_path__mutmut_4': x_get_code_file_path__mutmut_4, 
    'x_get_code_file_path__mutmut_5': x_get_code_file_path__mutmut_5, 
    'x_get_code_file_path__mutmut_6': x_get_code_file_path__mutmut_6, 
    'x_get_code_file_path__mutmut_7': x_get_code_file_path__mutmut_7, 
    'x_get_code_file_path__mutmut_8': x_get_code_file_path__mutmut_8, 
    'x_get_code_file_path__mutmut_9': x_get_code_file_path__mutmut_9, 
    'x_get_code_file_path__mutmut_10': x_get_code_file_path__mutmut_10, 
    'x_get_code_file_path__mutmut_11': x_get_code_file_path__mutmut_11
}

def get_code_file_path(*args, **kwargs):
    result = _mutmut_trampoline(x_get_code_file_path__mutmut_orig, x_get_code_file_path__mutmut_mutants, *args, **kwargs)
    return result 

get_code_file_path.__signature__ = _mutmut_signature(x_get_code_file_path__mutmut_orig)
x_get_code_file_path__mutmut_orig.__name__ = 'x_get_code_file_path'




def x_analyze_kotlin_tests__mutmut_orig(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_1(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_2(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_3(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_4(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_5(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_6(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_7(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_8(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_9(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_10(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith("XX.ktXX"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_11(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_12(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_13(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_14(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_15(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_16(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_17(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_18(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_19(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_20(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_21(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_22(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_23(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_24(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_25(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_26(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_27(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_28(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_29(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_30(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_31(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_32(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_33(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_34(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_35(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_36(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_37(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_38(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_39(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_40(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_41(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_42(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_43(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_44(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_45(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_46(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(None)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_47(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_48(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(None, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_49(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, None)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_50(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin( test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_51(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path,)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_52(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = None
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_53(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("XXError occurred during computation of McCabe ratio: XX", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_54(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", None)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_55(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ",)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_56(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = ""

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_57(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax == CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_58(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "XXexecution_time_secXX": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_59(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "XXline_coverage_percentageXX": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_60(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "XXbranch_coverage_percentageXX": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_61(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_62(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_63(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_64(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_65(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_66(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_67(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_68(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_69(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_70(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(None, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_71(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, None)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_72(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test( timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_73(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir,)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_74(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = None
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_75(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = None

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_76(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred and test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_77(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = None
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_78(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error and test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_79(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = None

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_80(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = None
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_81(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(None, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_82(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, None, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_83(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, None)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_84(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage( source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_85(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_86(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path,)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_87(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = None

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_88(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "XXexecution_time_secXX": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_89(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "XXline_coverage_percentageXX": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_90(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["XXlineXX"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_91(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage[None],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_92(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "XXbranch_coverage_percentageXX": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_93(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["XXbranchXX"],
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


def x_analyze_kotlin_tests__mutmut_94(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage[None],
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


def x_analyze_kotlin_tests__mutmut_95(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_96(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_97(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_98(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_99(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_100(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_101(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_102(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_103(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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


def x_analyze_kotlin_tests__mutmut_104(
        input_dir,
        test_input_file_path,
        src_dir=Config.get_kotlin_src_dir(),
        test_dir=Config.get_kotlin_test_dir(),
        project_dir=Config.get_kotlin_project_root(),
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
            if file_name.endswith(".kt"):
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

        assertions_density = assertions_density_kotlin(test_file_path)
        try:
            mccabe = assertions_mccabe_ratio_kotlin(source_file_path, test_file_path)
        except Exception as e:
            print("Error occurred during computation of McCabe ratio: ", e)
            mccabe = None

        if syntax != CompileStatus.OK:
            return {
                "execution_time_sec": None,
                "line_coverage_percentage": None,
                "branch_coverage_percentage": None,
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

        test_results = run_maven_clean_test(project_dir, timeout)
        test_maven_output, test_timeout_occurred, test_error, execution_time = test_results

        timeout_occurred = timeout_occurred or test_timeout_occurred
        error = error or test_error

        pass_rate, runtime_errors = parse_report_and_compute_pass_rate(Config._kotlin_test_reports)
        coverage_percentage = compute_coverage_percentage(project_dir, source_file_path, timeout_occurred)

        return {
            "execution_time_sec": execution_time,
            "line_coverage_percentage": coverage_percentage["line"],
            "branch_coverage_percentage": coverage_percentage["branch"],
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

x_analyze_kotlin_tests__mutmut_mutants = {
'x_analyze_kotlin_tests__mutmut_1': x_analyze_kotlin_tests__mutmut_1, 
    'x_analyze_kotlin_tests__mutmut_2': x_analyze_kotlin_tests__mutmut_2, 
    'x_analyze_kotlin_tests__mutmut_3': x_analyze_kotlin_tests__mutmut_3, 
    'x_analyze_kotlin_tests__mutmut_4': x_analyze_kotlin_tests__mutmut_4, 
    'x_analyze_kotlin_tests__mutmut_5': x_analyze_kotlin_tests__mutmut_5, 
    'x_analyze_kotlin_tests__mutmut_6': x_analyze_kotlin_tests__mutmut_6, 
    'x_analyze_kotlin_tests__mutmut_7': x_analyze_kotlin_tests__mutmut_7, 
    'x_analyze_kotlin_tests__mutmut_8': x_analyze_kotlin_tests__mutmut_8, 
    'x_analyze_kotlin_tests__mutmut_9': x_analyze_kotlin_tests__mutmut_9, 
    'x_analyze_kotlin_tests__mutmut_10': x_analyze_kotlin_tests__mutmut_10, 
    'x_analyze_kotlin_tests__mutmut_11': x_analyze_kotlin_tests__mutmut_11, 
    'x_analyze_kotlin_tests__mutmut_12': x_analyze_kotlin_tests__mutmut_12, 
    'x_analyze_kotlin_tests__mutmut_13': x_analyze_kotlin_tests__mutmut_13, 
    'x_analyze_kotlin_tests__mutmut_14': x_analyze_kotlin_tests__mutmut_14, 
    'x_analyze_kotlin_tests__mutmut_15': x_analyze_kotlin_tests__mutmut_15, 
    'x_analyze_kotlin_tests__mutmut_16': x_analyze_kotlin_tests__mutmut_16, 
    'x_analyze_kotlin_tests__mutmut_17': x_analyze_kotlin_tests__mutmut_17, 
    'x_analyze_kotlin_tests__mutmut_18': x_analyze_kotlin_tests__mutmut_18, 
    'x_analyze_kotlin_tests__mutmut_19': x_analyze_kotlin_tests__mutmut_19, 
    'x_analyze_kotlin_tests__mutmut_20': x_analyze_kotlin_tests__mutmut_20, 
    'x_analyze_kotlin_tests__mutmut_21': x_analyze_kotlin_tests__mutmut_21, 
    'x_analyze_kotlin_tests__mutmut_22': x_analyze_kotlin_tests__mutmut_22, 
    'x_analyze_kotlin_tests__mutmut_23': x_analyze_kotlin_tests__mutmut_23, 
    'x_analyze_kotlin_tests__mutmut_24': x_analyze_kotlin_tests__mutmut_24, 
    'x_analyze_kotlin_tests__mutmut_25': x_analyze_kotlin_tests__mutmut_25, 
    'x_analyze_kotlin_tests__mutmut_26': x_analyze_kotlin_tests__mutmut_26, 
    'x_analyze_kotlin_tests__mutmut_27': x_analyze_kotlin_tests__mutmut_27, 
    'x_analyze_kotlin_tests__mutmut_28': x_analyze_kotlin_tests__mutmut_28, 
    'x_analyze_kotlin_tests__mutmut_29': x_analyze_kotlin_tests__mutmut_29, 
    'x_analyze_kotlin_tests__mutmut_30': x_analyze_kotlin_tests__mutmut_30, 
    'x_analyze_kotlin_tests__mutmut_31': x_analyze_kotlin_tests__mutmut_31, 
    'x_analyze_kotlin_tests__mutmut_32': x_analyze_kotlin_tests__mutmut_32, 
    'x_analyze_kotlin_tests__mutmut_33': x_analyze_kotlin_tests__mutmut_33, 
    'x_analyze_kotlin_tests__mutmut_34': x_analyze_kotlin_tests__mutmut_34, 
    'x_analyze_kotlin_tests__mutmut_35': x_analyze_kotlin_tests__mutmut_35, 
    'x_analyze_kotlin_tests__mutmut_36': x_analyze_kotlin_tests__mutmut_36, 
    'x_analyze_kotlin_tests__mutmut_37': x_analyze_kotlin_tests__mutmut_37, 
    'x_analyze_kotlin_tests__mutmut_38': x_analyze_kotlin_tests__mutmut_38, 
    'x_analyze_kotlin_tests__mutmut_39': x_analyze_kotlin_tests__mutmut_39, 
    'x_analyze_kotlin_tests__mutmut_40': x_analyze_kotlin_tests__mutmut_40, 
    'x_analyze_kotlin_tests__mutmut_41': x_analyze_kotlin_tests__mutmut_41, 
    'x_analyze_kotlin_tests__mutmut_42': x_analyze_kotlin_tests__mutmut_42, 
    'x_analyze_kotlin_tests__mutmut_43': x_analyze_kotlin_tests__mutmut_43, 
    'x_analyze_kotlin_tests__mutmut_44': x_analyze_kotlin_tests__mutmut_44, 
    'x_analyze_kotlin_tests__mutmut_45': x_analyze_kotlin_tests__mutmut_45, 
    'x_analyze_kotlin_tests__mutmut_46': x_analyze_kotlin_tests__mutmut_46, 
    'x_analyze_kotlin_tests__mutmut_47': x_analyze_kotlin_tests__mutmut_47, 
    'x_analyze_kotlin_tests__mutmut_48': x_analyze_kotlin_tests__mutmut_48, 
    'x_analyze_kotlin_tests__mutmut_49': x_analyze_kotlin_tests__mutmut_49, 
    'x_analyze_kotlin_tests__mutmut_50': x_analyze_kotlin_tests__mutmut_50, 
    'x_analyze_kotlin_tests__mutmut_51': x_analyze_kotlin_tests__mutmut_51, 
    'x_analyze_kotlin_tests__mutmut_52': x_analyze_kotlin_tests__mutmut_52, 
    'x_analyze_kotlin_tests__mutmut_53': x_analyze_kotlin_tests__mutmut_53, 
    'x_analyze_kotlin_tests__mutmut_54': x_analyze_kotlin_tests__mutmut_54, 
    'x_analyze_kotlin_tests__mutmut_55': x_analyze_kotlin_tests__mutmut_55, 
    'x_analyze_kotlin_tests__mutmut_56': x_analyze_kotlin_tests__mutmut_56, 
    'x_analyze_kotlin_tests__mutmut_57': x_analyze_kotlin_tests__mutmut_57, 
    'x_analyze_kotlin_tests__mutmut_58': x_analyze_kotlin_tests__mutmut_58, 
    'x_analyze_kotlin_tests__mutmut_59': x_analyze_kotlin_tests__mutmut_59, 
    'x_analyze_kotlin_tests__mutmut_60': x_analyze_kotlin_tests__mutmut_60, 
    'x_analyze_kotlin_tests__mutmut_61': x_analyze_kotlin_tests__mutmut_61, 
    'x_analyze_kotlin_tests__mutmut_62': x_analyze_kotlin_tests__mutmut_62, 
    'x_analyze_kotlin_tests__mutmut_63': x_analyze_kotlin_tests__mutmut_63, 
    'x_analyze_kotlin_tests__mutmut_64': x_analyze_kotlin_tests__mutmut_64, 
    'x_analyze_kotlin_tests__mutmut_65': x_analyze_kotlin_tests__mutmut_65, 
    'x_analyze_kotlin_tests__mutmut_66': x_analyze_kotlin_tests__mutmut_66, 
    'x_analyze_kotlin_tests__mutmut_67': x_analyze_kotlin_tests__mutmut_67, 
    'x_analyze_kotlin_tests__mutmut_68': x_analyze_kotlin_tests__mutmut_68, 
    'x_analyze_kotlin_tests__mutmut_69': x_analyze_kotlin_tests__mutmut_69, 
    'x_analyze_kotlin_tests__mutmut_70': x_analyze_kotlin_tests__mutmut_70, 
    'x_analyze_kotlin_tests__mutmut_71': x_analyze_kotlin_tests__mutmut_71, 
    'x_analyze_kotlin_tests__mutmut_72': x_analyze_kotlin_tests__mutmut_72, 
    'x_analyze_kotlin_tests__mutmut_73': x_analyze_kotlin_tests__mutmut_73, 
    'x_analyze_kotlin_tests__mutmut_74': x_analyze_kotlin_tests__mutmut_74, 
    'x_analyze_kotlin_tests__mutmut_75': x_analyze_kotlin_tests__mutmut_75, 
    'x_analyze_kotlin_tests__mutmut_76': x_analyze_kotlin_tests__mutmut_76, 
    'x_analyze_kotlin_tests__mutmut_77': x_analyze_kotlin_tests__mutmut_77, 
    'x_analyze_kotlin_tests__mutmut_78': x_analyze_kotlin_tests__mutmut_78, 
    'x_analyze_kotlin_tests__mutmut_79': x_analyze_kotlin_tests__mutmut_79, 
    'x_analyze_kotlin_tests__mutmut_80': x_analyze_kotlin_tests__mutmut_80, 
    'x_analyze_kotlin_tests__mutmut_81': x_analyze_kotlin_tests__mutmut_81, 
    'x_analyze_kotlin_tests__mutmut_82': x_analyze_kotlin_tests__mutmut_82, 
    'x_analyze_kotlin_tests__mutmut_83': x_analyze_kotlin_tests__mutmut_83, 
    'x_analyze_kotlin_tests__mutmut_84': x_analyze_kotlin_tests__mutmut_84, 
    'x_analyze_kotlin_tests__mutmut_85': x_analyze_kotlin_tests__mutmut_85, 
    'x_analyze_kotlin_tests__mutmut_86': x_analyze_kotlin_tests__mutmut_86, 
    'x_analyze_kotlin_tests__mutmut_87': x_analyze_kotlin_tests__mutmut_87, 
    'x_analyze_kotlin_tests__mutmut_88': x_analyze_kotlin_tests__mutmut_88, 
    'x_analyze_kotlin_tests__mutmut_89': x_analyze_kotlin_tests__mutmut_89, 
    'x_analyze_kotlin_tests__mutmut_90': x_analyze_kotlin_tests__mutmut_90, 
    'x_analyze_kotlin_tests__mutmut_91': x_analyze_kotlin_tests__mutmut_91, 
    'x_analyze_kotlin_tests__mutmut_92': x_analyze_kotlin_tests__mutmut_92, 
    'x_analyze_kotlin_tests__mutmut_93': x_analyze_kotlin_tests__mutmut_93, 
    'x_analyze_kotlin_tests__mutmut_94': x_analyze_kotlin_tests__mutmut_94, 
    'x_analyze_kotlin_tests__mutmut_95': x_analyze_kotlin_tests__mutmut_95, 
    'x_analyze_kotlin_tests__mutmut_96': x_analyze_kotlin_tests__mutmut_96, 
    'x_analyze_kotlin_tests__mutmut_97': x_analyze_kotlin_tests__mutmut_97, 
    'x_analyze_kotlin_tests__mutmut_98': x_analyze_kotlin_tests__mutmut_98, 
    'x_analyze_kotlin_tests__mutmut_99': x_analyze_kotlin_tests__mutmut_99, 
    'x_analyze_kotlin_tests__mutmut_100': x_analyze_kotlin_tests__mutmut_100, 
    'x_analyze_kotlin_tests__mutmut_101': x_analyze_kotlin_tests__mutmut_101, 
    'x_analyze_kotlin_tests__mutmut_102': x_analyze_kotlin_tests__mutmut_102, 
    'x_analyze_kotlin_tests__mutmut_103': x_analyze_kotlin_tests__mutmut_103, 
    'x_analyze_kotlin_tests__mutmut_104': x_analyze_kotlin_tests__mutmut_104
}

def analyze_kotlin_tests(*args, **kwargs):
    result = _mutmut_trampoline(x_analyze_kotlin_tests__mutmut_orig, x_analyze_kotlin_tests__mutmut_mutants, *args, **kwargs)
    return result 

analyze_kotlin_tests.__signature__ = _mutmut_signature(x_analyze_kotlin_tests__mutmut_orig)
x_analyze_kotlin_tests__mutmut_orig.__name__ = 'x_analyze_kotlin_tests'


