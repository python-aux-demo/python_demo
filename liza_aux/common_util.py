import logging
import time

import pandas as pd

logger = logging.getLogger(__name__)


def elapsed_from(start_time: float) -> int:
    current_time = time.time()
    elapsed = int(current_time - start_time)
    return elapsed


def remove_empty_columns(input_df: pd.DataFrame) -> pd.DataFrame:
    non_empty_columns = (~input_df.isna()).sum()
    non_empty_columns = non_empty_columns[non_empty_columns > 0]
    output_df = input_df[non_empty_columns.index.to_list()]
    return output_df
