from enum import Enum


WALKING_LIST_DIRECTORY = 'data'
WALKING_LIST_FILE_NAME = 'walking_list.csv'
CSV_SEPARATOR = ';'


class WalkingListColumns(Enum):
    DATE = 'Data'
    DISTANCE = 'Distãncia'
    DURATION = 'Duração'
