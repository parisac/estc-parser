import pandas as pd
from pandas._testing import assert_frame_equal

from estc_parser import __version__
from estc_parser.parser import _file2df, _files2df


INPUT_PATH = "./tests/sample_input"
EXPECTED_PATH = "./tests/sample_expected"


def test_version():
    assert __version__ == "0.1.0"


def test_file2df():
    # test that the serialized version of this frame matches the frame creation
    df_actual = _file2df(f"{INPUT_PATH}/file1.html")
    df_expected = pd.read_pickle(f"{EXPECTED_PATH}/file1_df.pkl")
    assert df_actual.shape == (199, 4)
    assert_frame_equal(df_actual, df_expected)


def test_files2df():
    # test that the serialized version of this frame matches the frame created of all files
    df_actual = _files2df(f"{INPUT_PATH}/")
    df_expected = pd.read_pickle(f"{EXPECTED_PATH}/allfiles_df.pkl")
    assert df_actual.shape == (597, 4)
    assert_frame_equal(df_actual, df_expected)
