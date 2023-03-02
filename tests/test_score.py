import pandas as pd
from mercury_muscle.score import MercuriTable

def test_declare_with_df():
    # fmt: off
    df = pd.DataFrame({
             'id': ['p1', 'p2', 'p3'],
        'disease': ['d1', 'd2', 'd3'],
           'm1_L': [   0,    1,    2],
           'm1_R': [   0,    1,    2],
    })
    # fmt: on
    mt = MercuriTable(df)