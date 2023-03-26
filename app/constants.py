import os
from enum import StrEnum


WALKING_LIST_DIRECTORY = 'data'
WALKING_LIST_FILE_NAME = 'walking_list.csv'
WALKING_LIST_FILE_PATH = os.path.join(
    WALKING_LIST_DIRECTORY, WALKING_LIST_FILE_NAME
)
CSV_SEPARATOR = ';'


class WalkingListColumns(StrEnum):
    DATE = 'Data'
    DISTANCE = 'Distância'
    DURATION = 'Duração'
