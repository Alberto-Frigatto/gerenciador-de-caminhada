import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from .walk import Walk


current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, '..')
sys.path.append(root_dir)

from app.constants import (
    CSV_SEPARATOR,
    WALKING_LIST_FILE_PATH,
    WalkingListColumns
)


plt.rc('figure', figsize=(10, 6))


class WalkingList:
    def __init__(self) -> None:
        self._df_walking_list = pd.read_csv(
            WALKING_LIST_FILE_PATH,
            sep=CSV_SEPARATOR,
            encoding='UTF-8'
        )
        self._df_walking_list.rename_axis(
            'Índice',
            axis='columns',
            inplace=True
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

    def delete_walk(self, walk_index: int) -> None:
        self._df_walking_list.drop(walk_index, inplace=True)
        self._df_walking_list.index = range(
            len(self._df_walking_list)
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
        mins_decimal = round(float(mins), 2)
        seconds = round((mins_decimal - int(mins_decimal))*100, 2)

        if seconds not in range(61):
            correction = .4

            mins_correct = mins_decimal + correction
            return round(mins_correct, 2)

        return mins_decimal

    def total_mileage(self) -> float:
        return round(
            self._df_walking_list[WalkingListColumns.DISTANCE].sum(),
            2
        )

    def total_monthly_mileage(self) -> pd.DataFrame:
        df_total_monthly_mileage = pd.DataFrame(
            columns=['Mês', 'Km']
        )

        for month in range(1, 13):
            month = str(month).zfill(2)
            total = self._df_walking_list[self._df_walking_list[
                WalkingListColumns.DATE].str.match(
                    '^(\d{2}/' + month + '/\d{4})$'
                )][WalkingListColumns.DISTANCE].sum()
            rounded_total = round(total, 2)

            df_total_monthly_mileage.loc[len(df_total_monthly_mileage)] = \
                {'Mês': month, 'Km': rounded_total}

        month_with_empty_mileage = df_total_monthly_mileage['Km'] == 0
        df_total_monthly_mileage = \
            df_total_monthly_mileage[~month_with_empty_mileage]

        df_total_monthly_mileage.index = range(
            len(df_total_monthly_mileage)
        )

        return df_total_monthly_mileage

    def total_monthly_mileage_plot(self) -> None:
        df_total_monthly_miliage = self.total_monthly_mileage()

        plot = df_total_monthly_miliage.plot.bar('Mês', 'Km', grid=True)

        plot.set_title('Quilometragem total mensal')
        plot.set_xlabel('Mês')
        plot.set_ylabel('Distância (Km)')

        plt.show()

    def walking_time_plot(self) -> None:
        plt.plot(
            self._df_walking_list[WalkingListColumns.DATE],
            self._df_walking_list[WalkingListColumns.DURATION],
            marker='o',
            markersize=7
        )
        plt.title('Tempos das caminhadas')
        plt.grid(True, linestyle=':', color='gray')
        plt.xlabel('Data')
        plt.ylabel('Duração (min)')

        plt.show()

    @property
    def walks(self) -> pd.DataFrame:
        return self._df_walking_list

    @property
    def index(self) -> list[int]:
        return self._df_walking_list.index
