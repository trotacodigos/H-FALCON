import pandas as pd

def sent_per_min(df):
    assert 'time' in df.columns, "Wrong format"
    
    # remove outliers
    df = df[df.time < 10000]
    
    mps = df.groupby('domain')['time'].mean() / 60 # min per sent
    return 1 / mps

