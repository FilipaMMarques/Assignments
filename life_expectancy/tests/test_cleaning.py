"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import main
from . import OUTPUT_DIR


def test_main(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
   
    pt_life_expectancy_actual = main()
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual.head(5), pt_life_expectancy_expected
    )
