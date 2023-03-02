import pandas as pd
from mercury_muscle.score import MercuriTable

def test_declare_with_df():
    # fmt: off
    df = pd.DataFrame({
             'id': ['p1', 'p2', 'p3', 'p4'],
        'disease': ['d1', 'd1', 'd2', 'd2'],
            'a_L': [   0,    0,    0,    0],
            'a_R': [   0,    0,    0,    0],
            'b_L': [   1,    1,    1,    1],
            'b_R': [   1,    1,    1,    1],
    })
    # fmt: on
    mt = MercuriTable(df)