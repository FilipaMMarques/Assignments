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

def save_data(
    data_frame,
    data_path=DATA_PATH,
    file_name="pt_life_expectancy.csv"
    ):
    """save data"""
    
    return data_frame.to_csv(
        os.path.join(data_path, file_name),
        index=False
    )

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region", type=str, default="PT")

    args = parser.parse_args()
    print(args.region)
    main(reg=args.region)
