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

    def __len__(self) -> int:
        return len(self._df_walking_list)

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

    def mean_walking_time(self) -> float:
        mean_time = self._df_walking_list[WalkingListColumns.DURATION] \
            .mean()

        return self._correct_mins_if_wrong(mean_time)

    def walking_time_std(self) -> float:
        std_time = self._df_walking_list[WalkingListColumns.DURATION] \
            .std(ddof=0)

        return self._correct_mins_if_wrong(std_time)

    def _correct_mins_if_wrong(self, mins) -> float:
        mins_decimal = round(mins, 2)
        seconds = round(mins_decimal - int(mins_decimal), 2)*100

        if seconds not in range(61):
            correction = .4

            mins_correct = mins_decimal + correction
            return mins_correct

        return mins_decimal

    def total_mileage(self) -> float:
        return self._df_walking_list[WalkingListColumns.DISTANCE].sum()

    @property
    def walks(self) -> pd.DataFrame:
        return self._df_walking_list
