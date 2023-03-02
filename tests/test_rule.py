import pytest
import numpy as np
import pandas as pd

from mercury_muscle.score import MercuriTable
from mercury_muscle.rule import RuleEvaluator

@pytest.fixture
def example_mt():
    # fmt: off
    return MercuriTable(pd.DataFrame({
             'id': [  'p1',   'p2', 'p3', 'p4', 'p5', 'p6'],
        'disease': [  'd1',   'd1', 'd1', 'd2', 'd2', 'd2'],
            'a_R': [np.nan,      0,    0,    1,    1,    2],
            'b_R': [     0,      0,    1,    1,    2,    3],
            'c_R': [     0, np.nan,    1,    2,    2,    3],
    }))
    # fmt: on

@pytest.fixture
def example_ruleevaluator_equal(example_mt):
    re = RuleEvaluator(example_mt, target='d1')
    re.add_rule('a==b')
    re.add_rule('a==c')
    re.add_rule('b==c')
    return re

@pytest.fixture
def example_ruleevaluator_greater(example_mt):
    re = RuleEvaluator(example_mt, target='d1')
    re.add_rule('a>b')
    re.add_rule('a>c')
    re.add_rule('b>c')
    return re

@pytest.fixture
def example_ruleevaluator_greater_equal(example_mt):
    re = RuleEvaluator(example_mt, target='d1')
    re.add_rule('a>=b')
    re.add_rule('a>=c')
    re.add_rule('b>=c')
    return re

@pytest.fixture
def example_ruleevaluator_smaller(example_mt):
    re = RuleEvaluator(example_mt, target='d1')
    re.add_rule('a<b')
    re.add_rule('a<c')
    re.add_rule('b<c')
    return re

@pytest.fixture
def example_ruleevaluator_smaller_equal(example_mt):
    re = RuleEvaluator(example_mt, target='d1')
    re.add_rule('a<=b')
    re.add_rule('a<=c')
    re.add_rule('b<=c')
    return re

@pytest.fixture
def example_ruleevaluator_subset(example_mt):
    re = RuleEvaluator(example_mt, target='d1')
    re.add_rule('a==0->a==b')
    re.add_rule('a==0->a==c')
    re.add_rule('a==0->b==c')
    return re

# Totals

def test_totals_equal_total(example_ruleevaluator_equal):
    example_ruleevaluator_equal.evaluate_totals(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_equal.totals_df['True']) == [2, 0, 4]
    assert list(example_ruleevaluator_equal.totals_df['False']) == [3, 4, 1]
    assert    list(example_ruleevaluator_equal.totals_df['NA']) == [1, 2, 1]
    # fmt: on

def test_totals_greater_total(example_ruleevaluator_greater):
    example_ruleevaluator_greater.evaluate_totals(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_greater.totals_df['True']) == [0, 0, 0]
    assert list(example_ruleevaluator_greater.totals_df['False']) == [5, 4, 5]
    assert    list(example_ruleevaluator_greater.totals_df['NA']) == [1, 2, 1]
    # fmt: on

def test_totals_greater_equal_total(example_ruleevaluator_greater_equal):
    example_ruleevaluator_greater_equal.evaluate_totals(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_greater_equal.totals_df['True']) == [2, 0, 4]
    assert list(example_ruleevaluator_greater_equal.totals_df['False']) == [3, 4, 1]
    assert    list(example_ruleevaluator_greater_equal.totals_df['NA']) == [1, 2, 1]
    # fmt: on

def test_totals_smaller_total(example_ruleevaluator_smaller):
    example_ruleevaluator_smaller.evaluate_totals(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_smaller.totals_df['True']) == [3, 4, 1]
    assert list(example_ruleevaluator_smaller.totals_df['False']) == [2, 0, 4]
    assert    list(example_ruleevaluator_smaller.totals_df['NA']) == [1, 2, 1]
    # fmt: on

def test_totals_smaller_equal_total(example_ruleevaluator_smaller_equal):
    example_ruleevaluator_smaller_equal.evaluate_totals(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_smaller_equal.totals_df['True']) == [5, 4, 5]
    assert list(example_ruleevaluator_smaller_equal.totals_df['False']) == [0, 0, 0]
    assert    list(example_ruleevaluator_smaller_equal.totals_df['NA']) == [1, 2, 1]
    # fmt: on

def test_totals_subset_total(example_ruleevaluator_subset):
    example_ruleevaluator_subset.evaluate_totals(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_subset.totals_df['True']) == [1, 0, 1]
    assert list(example_ruleevaluator_subset.totals_df['False']) == [1, 1, 0]
    assert    list(example_ruleevaluator_subset.totals_df['NA']) == [1, 2, 2]
    # fmt: on

# CMs

def test_totals_equal_cm(example_ruleevaluator_equal):
    example_ruleevaluator_equal.evaluate_cm(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_equal.cm_df['tp']) == [1, 0, 2]
    assert  list(example_ruleevaluator_equal.cm_df['fp']) == [1, 0, 2]
    assert  list(example_ruleevaluator_equal.cm_df['tn']) == [2, 3, 1]
    assert  list(example_ruleevaluator_equal.cm_df['fn']) == [1, 1, 0]
    assert list(example_ruleevaluator_equal.cm_df['nan']) == [1, 2, 1]
    # fmt: on

def test_totals_subset_cm(example_ruleevaluator_subset):
    example_ruleevaluator_subset.evaluate_cm(side='R')
    # fmt: off
    assert  list(example_ruleevaluator_subset.cm_df['tp']) == [1, 0, 1]
    assert  list(example_ruleevaluator_subset.cm_df['fp']) == [0, 0, 0]
    assert  list(example_ruleevaluator_subset.cm_df['tn']) == [0, 0, 0]
    assert  list(example_ruleevaluator_subset.cm_df['fn']) == [1, 1, 0]
    assert list(example_ruleevaluator_subset.cm_df['nan']) == [1, 2, 2]
    # fmt: on


# fmt: off
{
     'id': [  'p1',   'p2', 'p3', 'p4', 'p5', 'p6'],
'disease': [  'd1',   'd1', 'd1', 'd2', 'd2', 'd2'],
    'a_R': [np.nan,      0,    0,    1,    1,    2],
    'b_R': [     0,      0,    1,    1,    2,    3],
    'c_R': [     0, np.nan,    1,    2,    2,    3],
}
# fmt: on