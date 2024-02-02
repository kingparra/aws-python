import pandas as pd
# pytest is needed for fixtures, even thought it isn't explicitly used
import pytest

# import pytest fixtures
from tests.sample_data import sample_data
from tests.sample_data import renamed_sample_data
from tests.sample_data import sample_merge_result

# import functions for modifying frames
from csv_merge.merge import rename_columns, reorder_columns
from csv_merge.merge import merge


def test_rename_columns(sample_data, renamed_sample_data):
    renamed = [rename_columns(df) for df in sample_data]
    for df1, df2 in zip(renamed, renamed_sample_data):
        assert df1.equals(df2)


def test_merge_frames_size(sample_data, sample_merge_result):
    merged = merge([reorder_columns(rename_columns(df)) for df in sample_data])
    assert merged.shape == sample_merge_result.shape


def test_merge_content(sample_data, sample_merge_result):
    merged = merge([reorder_columns(rename_columns(df)) for df in sample_data])
    assert merged.equals(sample_merge_result)
