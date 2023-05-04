"""cleaning data"""
import argparse
import os
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent / 'data'

def load_data(
    data= DATA_PATH,
    file_name="eu_life_expectancy_raw.tsv"
    ):
    """load data"""
    df=pd.read_csv(
        os.path.join( data , file_name),
        sep="\t|,",
        engine='python'
    )
    return df

def clean_data(
    data,
    reg="PT"
    ):
    """cleaning data"""
    data.rename(columns={"geo\\time":"region"},inplace=True)
    df_unpivot = pd.melt(data, id_vars=['unit',"sex", "age", "region"], var_name='year')
    df_unpivot["year"]=df_unpivot["year"].astype(int)
    df_unpivot.value.unique()
    df_unpivot=df_unpivot[df_unpivot.value!=': ']
    df_unpivot=df_unpivot[df_unpivot.value!=':']
    df_unpivot['value'] = df_unpivot['value'].map(lambda x: x.lstrip('').rstrip(' epb'))
    df_unpivot=df_unpivot[df_unpivot['region']==reg]
    df_unpivot["value"]=df_unpivot["value"].astype(float)
    return df_unpivot


def save_data(
    data_frame,
    data_path=DATA_PATH,
    file_name="pt_life_expectancy.csv"
    ):
    """load data"""
    data_frame.to_csv(
        os.path.join(data_path, file_name),
        index=False
    )
    return "thatS all folks"


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
    return "thatS all folks"


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region", type=str, default="PT")

    args = parser.parse_args()
    print(args.region)
    main(reg=args.region)
