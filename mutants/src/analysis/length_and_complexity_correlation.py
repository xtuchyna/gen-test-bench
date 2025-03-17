
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
import tempfile

import pandas as pd
from scipy.stats import mannwhitneyu, spearmanr

from src.config import Config
from src.analysis.python_assertion_ratios import compute_complexity


def x_analyze_correlations__mutmut_orig():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_1():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "XXfiltered_Python_stats_gpt_4o_2024_08_06.csvXX"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_2():
    gpt = None
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_3():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "XXfiltered_Python_stats_gemini_1_5_pro_002.csvXX"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_4():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = None
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_5():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "XXfiltered_Python_stats_deepseek_coder.csvXX"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_6():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = None
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_7():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "XXcombined_stats.csvXX"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_8():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = None

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_9():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"XXgpt_4o_2024_08_06XX": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_10():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "XXgemini_1_5_pro_002XX": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_11():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "XXdeepseek_coderXX": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_12():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = None
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_13():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("XXPython, XX" + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_14():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " - model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_15():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model - ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_16():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + "XX:XX")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_17():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['XXpassed_compilation_and_runtimeXX'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_18():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data[None] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_19():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['XXcompilation_statusXX'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_20():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data[None] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_21():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] != 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_22():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'XXCompileStatus.OKXX') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_23():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') | (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_24():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['XXruntime_errors_countXX'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_25():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data[None] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_26():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] != 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_27():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 1)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_28():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = None

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_29():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['XXpassed_compilation_and_runtimeXX'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_30():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data[None] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_31():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] != True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_32():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_33():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[None]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_34():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["XXcode_lengthXX"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_35():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True][None]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_36():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = None
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_37():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['XXpassed_compilation_and_runtimeXX'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_38():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data[None] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_39():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] != False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_40():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_41():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[None]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_42():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["XXcode_lengthXX"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_43():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False][None]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_44():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = None
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_45():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(None, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_46():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, None, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_47():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='XXtwo-sidedXX')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_48():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu( nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_49():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_50():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths,)
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_51():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = None
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_52():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("XXMann-Whitney U statistic:XX", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_53():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", None)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_54():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:",)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_55():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("XXp-value:XX", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_56():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", None)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_57():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:",)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_58():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value <= 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_59():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 1.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_60():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("XXStatistically significant difference between True and False groups.XX")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_61():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("XXNo statistically significant difference between True and False groups.XX")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_62():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["XXtask_nameXX", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_63():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "XXlanguage_nameXX", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_64():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "XXline_countXX", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_65():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "XXcodeXX"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_66():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[None], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_67():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], None, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_68():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["XXtask_nameXX", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_69():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "XXlanguage_nameXX"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_70():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="XXinnerXX")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_71():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_72():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_73():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"],)

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_74():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = None

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_75():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["XXllm_modelXX"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_76():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df[None] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_77():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] != model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_78():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[None]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_79():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = None

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_80():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "XXline_countXX",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_81():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "XXcodeXX",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_82():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "XXcompilation_status_scoreXX",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_83():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "XXruntime_errors_scoreXX",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_84():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "XXexecution_time_scoreXX",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_85():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "XXline_coverage_scoreXX",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_86():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "XXbranch_coverage_scoreXX",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_87():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "XXassertions_mccabe_ratio_scoreXX",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_88():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "XXassertions_density_scoreXX",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_89():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "XXwarnings_count_scoreXX"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_90():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = None

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_91():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[None]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_92():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = None

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_93():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col  in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_94():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["XXline_countXX", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_95():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "XXcodeXX"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_96():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = None
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_97():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[None].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_98():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=2)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_99():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = None

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_100():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["XXline_countXX"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_101():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df[None], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_102():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], None)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_103():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"],)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_104():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = None

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_105():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("XXSpearman correlation:XX", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_106():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", None)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_107():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:",)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_108():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("XXP-value:XX", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_109():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", None)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_110():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:",)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_111():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value <= 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_112():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 1.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_113():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("XXThere is a statistically significant monotonic relationship.XX")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_114():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("XXNo statistically significant monotonic relationship.XX")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_115():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["XXcodeXX"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_116():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df[None].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_117():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(None)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_118():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = None

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_119():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("XXPython, XX" + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_120():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " - model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_121():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model - ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_122():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + "XX, relationship between complexity and total score:XX")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_123():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(None, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_124():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, None)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_125():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr( total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_126():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity,)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_127():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = None
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_128():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("XXSpearman correlation:XX", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_129():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", None)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_130():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:",)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_131():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("XXP-value:XX", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_132():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", None)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_133():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:",)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_134():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value <= 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_135():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 1.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_136():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("XXThere is a statistically significant monotonic relationship.XX")
        else:
            print("No statistically significant monotonic relationship.")
        print()
        print()


def x_analyze_correlations__mutmut_137():
    gpt = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gpt_4o_2024_08_06.csv"))
    gemini = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_gemini_1_5_pro_002.csv"))
    deepseek = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "filtered_Python_stats_deepseek_coder.csv"))
    combined_stats = pd.read_csv(os.path.join(Config.get_stats_input_dir(), "combined_stats.csv"))

    models_data = {"gpt_4o_2024_08_06": gpt, "gemini_1_5_pro_002": gemini, "deepseek_coder": deepseek}
    for model, model_data in models_data.items():
        print("Python, " + model + ":")
        model_data['passed_compilation_and_runtime'] = (model_data['compilation_status'] == 'CompileStatus.OK') & (
                model_data['runtime_errors_count'] == 0)

        executable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == True]["code_length"]
        nonexecutable_code_lengths = model_data[model_data['passed_compilation_and_runtime'] == False]["code_length"]
        stat, p_value = mannwhitneyu(executable_code_lengths, nonexecutable_code_lengths, alternative='two-sided')
        print("Mann-Whitney U statistic:", stat)
        print("p-value:", p_value)

        if p_value < 0.05:
            print("Statistically significant difference between True and False groups.")
        else:
            print("No statistically significant difference between True and False groups.")

        # Perform inner join on 'task_name' and 'language_name'
        merged_df = pd.merge(model_data[["task_name", "language_name", "line_count", "code"]], combined_stats, on=["task_name", "language_name"], how="inner")

        # Filter rows where 'llm_model' == llm_model_value
        filtered_df = merged_df[merged_df["llm_model"] == model]

        # Select the specified columns
        columns_to_select = [
            "line_count",
            "code",
            "compilation_status_score",
            "runtime_errors_score",
            "execution_time_score",
            "line_coverage_score",
            "branch_coverage_score",
            "assertions_mccabe_ratio_score",
            "assertions_density_score",
            "warnings_count_score"
        ]

        result_df = filtered_df[columns_to_select]

        score_columns = [col for col in columns_to_select if col not in ["line_count", "code"]]
        total_score = result_df[score_columns].sum(axis=1)

        # Compute Spearman correlation
        corr, p_value = spearmanr(result_df["line_count"], total_score)

        print("Spearman correlation:", corr)
        print("P-value:", p_value)

        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("No statistically significant monotonic relationship.")

        complexity = result_df["code"].apply(get_complexity_from_code)

        print()
        print()
        print("Python, " + model + ", relationship between complexity and total score:")
        corr, p_value = spearmanr(complexity, total_score)
        print("Spearman correlation:", corr)
        print("P-value:", p_value)
        if p_value < 0.05:
            print("There is a statistically significant monotonic relationship.")
        else:
            print("XXNo statistically significant monotonic relationship.XX")
        print()
        print()

x_analyze_correlations__mutmut_mutants = {
'x_analyze_correlations__mutmut_1': x_analyze_correlations__mutmut_1, 
    'x_analyze_correlations__mutmut_2': x_analyze_correlations__mutmut_2, 
    'x_analyze_correlations__mutmut_3': x_analyze_correlations__mutmut_3, 
    'x_analyze_correlations__mutmut_4': x_analyze_correlations__mutmut_4, 
    'x_analyze_correlations__mutmut_5': x_analyze_correlations__mutmut_5, 
    'x_analyze_correlations__mutmut_6': x_analyze_correlations__mutmut_6, 
    'x_analyze_correlations__mutmut_7': x_analyze_correlations__mutmut_7, 
    'x_analyze_correlations__mutmut_8': x_analyze_correlations__mutmut_8, 
    'x_analyze_correlations__mutmut_9': x_analyze_correlations__mutmut_9, 
    'x_analyze_correlations__mutmut_10': x_analyze_correlations__mutmut_10, 
    'x_analyze_correlations__mutmut_11': x_analyze_correlations__mutmut_11, 
    'x_analyze_correlations__mutmut_12': x_analyze_correlations__mutmut_12, 
    'x_analyze_correlations__mutmut_13': x_analyze_correlations__mutmut_13, 
    'x_analyze_correlations__mutmut_14': x_analyze_correlations__mutmut_14, 
    'x_analyze_correlations__mutmut_15': x_analyze_correlations__mutmut_15, 
    'x_analyze_correlations__mutmut_16': x_analyze_correlations__mutmut_16, 
    'x_analyze_correlations__mutmut_17': x_analyze_correlations__mutmut_17, 
    'x_analyze_correlations__mutmut_18': x_analyze_correlations__mutmut_18, 
    'x_analyze_correlations__mutmut_19': x_analyze_correlations__mutmut_19, 
    'x_analyze_correlations__mutmut_20': x_analyze_correlations__mutmut_20, 
    'x_analyze_correlations__mutmut_21': x_analyze_correlations__mutmut_21, 
    'x_analyze_correlations__mutmut_22': x_analyze_correlations__mutmut_22, 
    'x_analyze_correlations__mutmut_23': x_analyze_correlations__mutmut_23, 
    'x_analyze_correlations__mutmut_24': x_analyze_correlations__mutmut_24, 
    'x_analyze_correlations__mutmut_25': x_analyze_correlations__mutmut_25, 
    'x_analyze_correlations__mutmut_26': x_analyze_correlations__mutmut_26, 
    'x_analyze_correlations__mutmut_27': x_analyze_correlations__mutmut_27, 
    'x_analyze_correlations__mutmut_28': x_analyze_correlations__mutmut_28, 
    'x_analyze_correlations__mutmut_29': x_analyze_correlations__mutmut_29, 
    'x_analyze_correlations__mutmut_30': x_analyze_correlations__mutmut_30, 
    'x_analyze_correlations__mutmut_31': x_analyze_correlations__mutmut_31, 
    'x_analyze_correlations__mutmut_32': x_analyze_correlations__mutmut_32, 
    'x_analyze_correlations__mutmut_33': x_analyze_correlations__mutmut_33, 
    'x_analyze_correlations__mutmut_34': x_analyze_correlations__mutmut_34, 
    'x_analyze_correlations__mutmut_35': x_analyze_correlations__mutmut_35, 
    'x_analyze_correlations__mutmut_36': x_analyze_correlations__mutmut_36, 
    'x_analyze_correlations__mutmut_37': x_analyze_correlations__mutmut_37, 
    'x_analyze_correlations__mutmut_38': x_analyze_correlations__mutmut_38, 
    'x_analyze_correlations__mutmut_39': x_analyze_correlations__mutmut_39, 
    'x_analyze_correlations__mutmut_40': x_analyze_correlations__mutmut_40, 
    'x_analyze_correlations__mutmut_41': x_analyze_correlations__mutmut_41, 
    'x_analyze_correlations__mutmut_42': x_analyze_correlations__mutmut_42, 
    'x_analyze_correlations__mutmut_43': x_analyze_correlations__mutmut_43, 
    'x_analyze_correlations__mutmut_44': x_analyze_correlations__mutmut_44, 
    'x_analyze_correlations__mutmut_45': x_analyze_correlations__mutmut_45, 
    'x_analyze_correlations__mutmut_46': x_analyze_correlations__mutmut_46, 
    'x_analyze_correlations__mutmut_47': x_analyze_correlations__mutmut_47, 
    'x_analyze_correlations__mutmut_48': x_analyze_correlations__mutmut_48, 
    'x_analyze_correlations__mutmut_49': x_analyze_correlations__mutmut_49, 
    'x_analyze_correlations__mutmut_50': x_analyze_correlations__mutmut_50, 
    'x_analyze_correlations__mutmut_51': x_analyze_correlations__mutmut_51, 
    'x_analyze_correlations__mutmut_52': x_analyze_correlations__mutmut_52, 
    'x_analyze_correlations__mutmut_53': x_analyze_correlations__mutmut_53, 
    'x_analyze_correlations__mutmut_54': x_analyze_correlations__mutmut_54, 
    'x_analyze_correlations__mutmut_55': x_analyze_correlations__mutmut_55, 
    'x_analyze_correlations__mutmut_56': x_analyze_correlations__mutmut_56, 
    'x_analyze_correlations__mutmut_57': x_analyze_correlations__mutmut_57, 
    'x_analyze_correlations__mutmut_58': x_analyze_correlations__mutmut_58, 
    'x_analyze_correlations__mutmut_59': x_analyze_correlations__mutmut_59, 
    'x_analyze_correlations__mutmut_60': x_analyze_correlations__mutmut_60, 
    'x_analyze_correlations__mutmut_61': x_analyze_correlations__mutmut_61, 
    'x_analyze_correlations__mutmut_62': x_analyze_correlations__mutmut_62, 
    'x_analyze_correlations__mutmut_63': x_analyze_correlations__mutmut_63, 
    'x_analyze_correlations__mutmut_64': x_analyze_correlations__mutmut_64, 
    'x_analyze_correlations__mutmut_65': x_analyze_correlations__mutmut_65, 
    'x_analyze_correlations__mutmut_66': x_analyze_correlations__mutmut_66, 
    'x_analyze_correlations__mutmut_67': x_analyze_correlations__mutmut_67, 
    'x_analyze_correlations__mutmut_68': x_analyze_correlations__mutmut_68, 
    'x_analyze_correlations__mutmut_69': x_analyze_correlations__mutmut_69, 
    'x_analyze_correlations__mutmut_70': x_analyze_correlations__mutmut_70, 
    'x_analyze_correlations__mutmut_71': x_analyze_correlations__mutmut_71, 
    'x_analyze_correlations__mutmut_72': x_analyze_correlations__mutmut_72, 
    'x_analyze_correlations__mutmut_73': x_analyze_correlations__mutmut_73, 
    'x_analyze_correlations__mutmut_74': x_analyze_correlations__mutmut_74, 
    'x_analyze_correlations__mutmut_75': x_analyze_correlations__mutmut_75, 
    'x_analyze_correlations__mutmut_76': x_analyze_correlations__mutmut_76, 
    'x_analyze_correlations__mutmut_77': x_analyze_correlations__mutmut_77, 
    'x_analyze_correlations__mutmut_78': x_analyze_correlations__mutmut_78, 
    'x_analyze_correlations__mutmut_79': x_analyze_correlations__mutmut_79, 
    'x_analyze_correlations__mutmut_80': x_analyze_correlations__mutmut_80, 
    'x_analyze_correlations__mutmut_81': x_analyze_correlations__mutmut_81, 
    'x_analyze_correlations__mutmut_82': x_analyze_correlations__mutmut_82, 
    'x_analyze_correlations__mutmut_83': x_analyze_correlations__mutmut_83, 
    'x_analyze_correlations__mutmut_84': x_analyze_correlations__mutmut_84, 
    'x_analyze_correlations__mutmut_85': x_analyze_correlations__mutmut_85, 
    'x_analyze_correlations__mutmut_86': x_analyze_correlations__mutmut_86, 
    'x_analyze_correlations__mutmut_87': x_analyze_correlations__mutmut_87, 
    'x_analyze_correlations__mutmut_88': x_analyze_correlations__mutmut_88, 
    'x_analyze_correlations__mutmut_89': x_analyze_correlations__mutmut_89, 
    'x_analyze_correlations__mutmut_90': x_analyze_correlations__mutmut_90, 
    'x_analyze_correlations__mutmut_91': x_analyze_correlations__mutmut_91, 
    'x_analyze_correlations__mutmut_92': x_analyze_correlations__mutmut_92, 
    'x_analyze_correlations__mutmut_93': x_analyze_correlations__mutmut_93, 
    'x_analyze_correlations__mutmut_94': x_analyze_correlations__mutmut_94, 
    'x_analyze_correlations__mutmut_95': x_analyze_correlations__mutmut_95, 
    'x_analyze_correlations__mutmut_96': x_analyze_correlations__mutmut_96, 
    'x_analyze_correlations__mutmut_97': x_analyze_correlations__mutmut_97, 
    'x_analyze_correlations__mutmut_98': x_analyze_correlations__mutmut_98, 
    'x_analyze_correlations__mutmut_99': x_analyze_correlations__mutmut_99, 
    'x_analyze_correlations__mutmut_100': x_analyze_correlations__mutmut_100, 
    'x_analyze_correlations__mutmut_101': x_analyze_correlations__mutmut_101, 
    'x_analyze_correlations__mutmut_102': x_analyze_correlations__mutmut_102, 
    'x_analyze_correlations__mutmut_103': x_analyze_correlations__mutmut_103, 
    'x_analyze_correlations__mutmut_104': x_analyze_correlations__mutmut_104, 
    'x_analyze_correlations__mutmut_105': x_analyze_correlations__mutmut_105, 
    'x_analyze_correlations__mutmut_106': x_analyze_correlations__mutmut_106, 
    'x_analyze_correlations__mutmut_107': x_analyze_correlations__mutmut_107, 
    'x_analyze_correlations__mutmut_108': x_analyze_correlations__mutmut_108, 
    'x_analyze_correlations__mutmut_109': x_analyze_correlations__mutmut_109, 
    'x_analyze_correlations__mutmut_110': x_analyze_correlations__mutmut_110, 
    'x_analyze_correlations__mutmut_111': x_analyze_correlations__mutmut_111, 
    'x_analyze_correlations__mutmut_112': x_analyze_correlations__mutmut_112, 
    'x_analyze_correlations__mutmut_113': x_analyze_correlations__mutmut_113, 
    'x_analyze_correlations__mutmut_114': x_analyze_correlations__mutmut_114, 
    'x_analyze_correlations__mutmut_115': x_analyze_correlations__mutmut_115, 
    'x_analyze_correlations__mutmut_116': x_analyze_correlations__mutmut_116, 
    'x_analyze_correlations__mutmut_117': x_analyze_correlations__mutmut_117, 
    'x_analyze_correlations__mutmut_118': x_analyze_correlations__mutmut_118, 
    'x_analyze_correlations__mutmut_119': x_analyze_correlations__mutmut_119, 
    'x_analyze_correlations__mutmut_120': x_analyze_correlations__mutmut_120, 
    'x_analyze_correlations__mutmut_121': x_analyze_correlations__mutmut_121, 
    'x_analyze_correlations__mutmut_122': x_analyze_correlations__mutmut_122, 
    'x_analyze_correlations__mutmut_123': x_analyze_correlations__mutmut_123, 
    'x_analyze_correlations__mutmut_124': x_analyze_correlations__mutmut_124, 
    'x_analyze_correlations__mutmut_125': x_analyze_correlations__mutmut_125, 
    'x_analyze_correlations__mutmut_126': x_analyze_correlations__mutmut_126, 
    'x_analyze_correlations__mutmut_127': x_analyze_correlations__mutmut_127, 
    'x_analyze_correlations__mutmut_128': x_analyze_correlations__mutmut_128, 
    'x_analyze_correlations__mutmut_129': x_analyze_correlations__mutmut_129, 
    'x_analyze_correlations__mutmut_130': x_analyze_correlations__mutmut_130, 
    'x_analyze_correlations__mutmut_131': x_analyze_correlations__mutmut_131, 
    'x_analyze_correlations__mutmut_132': x_analyze_correlations__mutmut_132, 
    'x_analyze_correlations__mutmut_133': x_analyze_correlations__mutmut_133, 
    'x_analyze_correlations__mutmut_134': x_analyze_correlations__mutmut_134, 
    'x_analyze_correlations__mutmut_135': x_analyze_correlations__mutmut_135, 
    'x_analyze_correlations__mutmut_136': x_analyze_correlations__mutmut_136, 
    'x_analyze_correlations__mutmut_137': x_analyze_correlations__mutmut_137
}

def analyze_correlations(*args, **kwargs):
    result = _mutmut_trampoline(x_analyze_correlations__mutmut_orig, x_analyze_correlations__mutmut_mutants, *args, **kwargs)
    return result 

analyze_correlations.__signature__ = _mutmut_signature(x_analyze_correlations__mutmut_orig)
x_analyze_correlations__mutmut_orig.__name__ = 'x_analyze_correlations'




def x_get_complexity_from_code__mutmut_orig(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_1(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='XXwXX', suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_2(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix="XX.pyXX", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_3(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=True) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_4(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile( suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_5(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_6(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py",) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_7(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(None)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_8(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = None

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_9(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(None)
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_10(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = None
    finally:
        # Remove the temporary file after computation
        os.remove(temp_file_path)

    return complexity


def x_get_complexity_from_code__mutmut_11(code_snippet: str) -> float:
    # Create a named temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix=".py", delete=False) as tmp_file:
        # Write the code snippet into the temp file
        tmp_file.write(code_snippet)
        temp_file_path = tmp_file.name

    try:
        # Compute the complexity using the provided function
        complexity = compute_complexity(temp_file_path)
    finally:
        # Remove the temporary file after computation
        os.remove(None)

    return complexity

x_get_complexity_from_code__mutmut_mutants = {
'x_get_complexity_from_code__mutmut_1': x_get_complexity_from_code__mutmut_1, 
    'x_get_complexity_from_code__mutmut_2': x_get_complexity_from_code__mutmut_2, 
    'x_get_complexity_from_code__mutmut_3': x_get_complexity_from_code__mutmut_3, 
    'x_get_complexity_from_code__mutmut_4': x_get_complexity_from_code__mutmut_4, 
    'x_get_complexity_from_code__mutmut_5': x_get_complexity_from_code__mutmut_5, 
    'x_get_complexity_from_code__mutmut_6': x_get_complexity_from_code__mutmut_6, 
    'x_get_complexity_from_code__mutmut_7': x_get_complexity_from_code__mutmut_7, 
    'x_get_complexity_from_code__mutmut_8': x_get_complexity_from_code__mutmut_8, 
    'x_get_complexity_from_code__mutmut_9': x_get_complexity_from_code__mutmut_9, 
    'x_get_complexity_from_code__mutmut_10': x_get_complexity_from_code__mutmut_10, 
    'x_get_complexity_from_code__mutmut_11': x_get_complexity_from_code__mutmut_11
}

def get_complexity_from_code(*args, **kwargs):
    result = _mutmut_trampoline(x_get_complexity_from_code__mutmut_orig, x_get_complexity_from_code__mutmut_mutants, *args, **kwargs)
    return result 

get_complexity_from_code.__signature__ = _mutmut_signature(x_get_complexity_from_code__mutmut_orig)
x_get_complexity_from_code__mutmut_orig.__name__ = 'x_get_complexity_from_code'


