import os
from dotenv import load_dotenv
from dagster import asset

from helper import utils
from helper.database import DatabaseManager
from helper.utils import is_convertible_to_int
from helper.time_utils import Time
import sys
import pandas as pd

load_dotenv()
db = DatabaseManager()
if not db.is_connected():
    sys.exit(1)


@asset
def itemPropertiesReader() -> None:
    is_debugging_str = os.getenv('DEBUG', 'False')
    is_debugging: bool = is_debugging_str.lower() in ['true']

    filenames: list[str] = utils.extract_file_names()

    if not isinstance(filenames, list):
        raise ValueError(f"expected a list, but got {type(filenames).__name__}")

    time = Time(is_debugging)
    for filename in filenames:
        time.start()
        time.setMessage(f'\"{filename}\" preparation start')
        time.print()
        df = pd.read_csv(f'./archive/{filename}.csv')
        df['value'] = df['value'].apply(lambda x: int(x) * 10 if is_convertible_to_int(x) else x)
        data_dict = df.to_dict(orient='records')
        time.setMessage('end of data preparation')
        time.end()
        try:
            db.insertMany(data_dict, "item_properties")
            time.setMessage('item properties inserted in')
            time.end()
        except Exception as e:
            print(f'error occurred during insert data from {filenames}: {e}')


itemPropertiesReader()
