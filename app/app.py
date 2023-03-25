import app.dao


class App:
    def __init__(self) -> None:
        self._create_walking_list_file_if_not_exists()

    def _create_walking_list_file_if_not_exists(self) -> None:
        if not app.dao.walking_list_file_exist():
            app.dao.create_walking_list_file()
