import os
import sys
import pandas as pd
from .walk import Walk


current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, '..')
sys.path.append(root_dir)

from app.constants import (
    CSV_SEPARATOR,
    WALKING_LIST_FILE_PATH,
    WalkingListColumns
)


class WalkingList:
    def __init__(self) -> None:
        self._df_walking_list = pd.read_csv(
            WALKING_LIST_FILE_PATH,
            sep=CSV_SEPARATOR,
            encoding='UTF-8'
        )

    def add_walk(self, walk: Walk) -> None:
        self._df_walking_list.loc[len(self._df_walking_list)] = {
            WalkingListColumns.DATE: walk.date,
            WalkingListColumns.DISTANCE: walk.distance,
            WalkingListColumns.DURATION: walk.duration
        }

    def save(self) -> None:
        self._df_walking_list.to_csv(
            WALKING_LIST_FILE_PATH,
            sep=CSV_SEPARATOR,
            index=False
        )
