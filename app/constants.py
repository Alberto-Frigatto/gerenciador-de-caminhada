from enum import StrEnum


WALKING_LIST_DIRECTORY = 'data'
WALKING_LIST_FILE_NAME = 'walking_list.csv'
CSV_SEPARATOR = ';'


class WalkingListColumns(StrEnum):
    DATE = 'Data'
    DISTANCE = 'Distância'
    DURATION = 'Duração'
