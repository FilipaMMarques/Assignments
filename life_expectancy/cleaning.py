"""cleaning data"""
import argparse
import os
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent / 'data'

def clean_data(
    reg="PT",
    data= DATA_PATH
    ):
    """cleaning data"""
    df=pd.read_csv(
        os.path.join( data , "eu_life_expectancy_raw.tsv"),
        sep="\t|,",
        engine='python'
    )

    df.rename(columns={"geo\\time":"region"},inplace=True)
    df_unpivot = pd.melt(df, id_vars=['unit',"sex", "age", "region"], var_name='year')
    df_unpivot["year"]=df_unpivot["year"].astype(int)
    df_unpivot.value.unique()
    df_unpivot=df_unpivot[df_unpivot.value!=': ']
    df_unpivot=df_unpivot[df_unpivot.value!=':']
    df_unpivot['value'] = df_unpivot['value'].map(lambda x: x.lstrip('').rstrip(' epb'))
    df_unpivot=df_unpivot[df_unpivot['region']==reg]
    df_unpivot["value"]=df_unpivot["value"].astype(float)

    df_unpivot.to_csv(
        os.path.join(data, "pt_life_expectancy.csv"),
        index=False
    )
    return df_unpivot

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region", type=str, default="PT")

    args = parser.parse_args()
    print(args.region)
    clean_data(reg=args.region)
