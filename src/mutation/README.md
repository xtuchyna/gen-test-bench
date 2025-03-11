## Mutation Testing (MT)

Given language L and set of generated tests S, the procedure for MT is following:
    - Get the S_L
    - Get the T_P as a passing test result set from S_L
    - Run MT(T_P) and make an Observation (see Obervation section)


## Observation

MT(T_Pi; T_Pi in T_P) = F_i

F_i is True if test Failed
        False otherwise

Observation metric should then contain sum of all these Fs.
A statistic on all the failed Fs can be made, including switched operators that were the cause of the Failure.

## Goal

Make F dataset given L is Python

## Generated tests dataset
Rewrite data folder followingly:
Replace main implementation file name with just `implementation.py`
Replace generated file tests names with just `test_<model_name>.py`


## F dataset
index
generated test (python code)
F status (T or False)
Mutation change (list of operators changed OR changed python code)

## Mutation Selection

### Sampling
For start

### Clustering
For advancement
