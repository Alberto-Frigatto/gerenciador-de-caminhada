import os
from .constants import (
    WALKING_LIST_DIRECTORY,
    WALKING_LIST_FILE_PATH,
    WalkingListColumns,
    CSV_SEPARATOR
)


def walking_list_file_exist() -> bool:
    return os.path.exists(WALKING_LIST_FILE_PATH)


def create_walking_list_file() -> None:
    os.makedirs(
        os.path.join('./', WALKING_LIST_DIRECTORY),
        exist_ok=True
    )

    with open(
        WALKING_LIST_FILE_PATH,
        'w',
        encoding='UTF-8'
    ) as walking_list_file:
        columns = (f'{WalkingListColumns.DATE}{CSV_SEPARATOR}'
                   f'{WalkingListColumns.DISTANCE}{CSV_SEPARATOR}'
                   f'{WalkingListColumns.DURATION}{CSV_SEPARATOR}\n')

        walking_list_file.write(columns)
