from bs4 import BeautifulSoup
from functools import partial
import pandas as pd
import glob

from .utils.logtime import timed, logger
from .utils.config import OUTPUT_PATH


@timed
def _query_html(soup: BeautifulSoup, field: str) -> pd.Series:
    """
    Finds all instances of single query field e.g. Author, Title etc.
    (becomes column in DF)

    Parameters
    ----------
    soup : BeautifulSoup
        BeautifulSoup html parsed object
    field: str
        Desired search field text e.g. Publisher_year

    Returns
    -------
    field_values : pd.Series
        pd.Series of all desired field values comprising of future DF column
    """
    # find all spans conatining query field
    all_text = soup.find_all(string=field)
    parents = [text.find_parents("span") for text in all_text]

    # post-process parent tags to extract desired field text
    field_values = []
    for tag in parents:
        raw_text = tag[0].get_text().split("\xa0")
        value = [*filter(lambda x: x.strip() is not "", raw_text)][1].strip()
        field_values.append(value)
    return pd.Series(field_values)


@timed
def _file2df(file_path: str) -> pd.DataFrame:
    """
    Converts single html file to DataFrame with shape(n, 4)
    Columns Names:
                    Title,
                    Author,
                    Pub_Info,
                    Description
    Parameters
    ----------
    file_path : str
        single html file path

    Returns
    -------
    df : pd.DataFrame
        Cleaned-up output dataframe with shape (n, 4)
    """
    soup = BeautifulSoup(open(file_path), "html.parser")
    _do_query = partial(_query_html, soup)

    columns = ["Title", "Author", "Pub_Info", "Description"]
    text_queries = ["Title", "Author - personal", "Publisher/year ", "Physical descr."]

    df_values = {}
    for column, query in zip(columns, text_queries):
        df_values[column] = _do_query(query)
    return pd.DataFrame(df_values)


@timed
def _files2df(path: str):
    """
    Converts multiple html files to DataFrame with shape(n, 4)
    Columns Names:
                    Title,
                    Author,
                    Pub_Info,
                    Description
    Parameters
    ----------
    path : str
        root dir path for html files

    Returns
    -------
    df : pd.DataFrame
        Cleaned-up output dataframe with shape (n, 4) as csv file
    """

    files = glob.glob(f"{path}*.html")
    return pd.concat([_file2df(file) for file in files])


@timed
def files2csv(path: str):
    """
    Converts multiple html files to CSV with shape(n, 4)
    Columns Names:
                    Title,
                    Author,
                    Pub_Info,
                    Description
    Parameters
    ----------
    path : str
        root dir path for html files

    Returns
    -------
    df.to_csv:
        Cleaned-up output dataframe with shape (n, 4) as csv file
    """

    df = _files2df(path)
    print(df.head(n=5))
    logger.info("saving to ./output/results.csv")
    df.to_csv(f"{OUTPUT_PATH}results.csv", index=False)
