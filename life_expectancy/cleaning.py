"""cleaning data"""
import argparse
import os
from pathlib import Path
import pandas as pd
from life_expectancy.load_save import load_data, save_data

DATA_PATH = Path(__file__).parent / 'data'

def clean_data(
    data,
    reg="PT"
    ):
    """cleaning data"""
    data.rename(columns={"geo\\time":"region"},inplace=True)
    df_unpivot = pd.melt(data, id_vars=['unit',"sex", "age", "region"], var_name='year')
    df_unpivot["year"]=df_unpivot["year"].astype('int64')
    df_unpivot.value.unique()
    df_unpivot=df_unpivot[df_unpivot.value!=': ']
    df_unpivot=df_unpivot[df_unpivot.value!=':']
    df_unpivot['value'] = df_unpivot['value'].map(lambda x: x.lstrip('').rstrip(' epb'))
    df_unpivot=df_unpivot[df_unpivot['region']==reg]
    df_unpivot["value"]=df_unpivot["value"].astype(float)
    return df_unpivot


def main(
    data_path= DATA_PATH,
    file_name="eu_life_expectancy_raw.tsv",
    reg="PT",
    output_name="pt_life_expectancy.csv"
    ):
    """data cleaning process"""
    data_frame=load_data(data_path,file_name)
    cleaning_df=clean_data(data_frame,reg)
    save_data(cleaning_df,data_path,output_name)
    return cleaning_df.reset_index(drop=True)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region", type=str, default="PT")

    args = parser.parse_args()
    print(args.region)
    main(reg=args.region)
