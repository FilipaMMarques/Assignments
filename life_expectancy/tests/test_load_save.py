"""Tests for the cleaning module"""
import pandas as pd
import pytest

from life_expectancy.cleaning import main
from life_expectancy.load_save import save_data
from . import OUTPUT_DIR


def test_save_data_csv(

    monkeypatch : pytest.MonkeyPatch,
    pt_life_expectancy_expected) -> None :

    """Patch save_csv method, testing load_data_csv function."""

    def _mockreturn_save_csv(*args, **kwargs) -> str :

        """Result to receive when mock."""

        return "DataFrame saved to csv file."

    monkeypatch.setattr(

        pt_life_expectancy_expected,

        "to_csv",

        _mockreturn_save_csv)

    assert save_data(pt_life_expectancy_expected) == "DataFrame saved to csv file."