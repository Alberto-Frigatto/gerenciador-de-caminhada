import app.dao
from colorama import Fore


class App:
    def __init__(self) -> None:
        self._create_walking_list_file_if_not_exists()
        self.OPTIONS = [
            (1, self.view_walks),
            (2, self.create_walk),
            (3, self.mean_walking_time),
            (4, self.walking_time_std),
            (5, self.total_mileage),
            (6, self.mean_monthly_mileage),
            (7, self.mean_monthly_mileage_plot),
            (8, self.walking_time_plot),
            (9, self.exit)
        ]

    def _create_walking_list_file_if_not_exists(self) -> None:
        if not app.dao.walking_list_file_exist():
            app.dao.create_walking_list_file()

    def view_walks(self):
        pass

    def create_walk(self):
        pass

    def mean_walking_time(self):
        pass

    def walking_time_std(self):
        pass

    def total_mileage(self):
        pass

    def mean_monthly_mileage(self):
        pass

    def mean_monthly_mileage_plot(self):
        pass

    def walking_time_plot(self):
        pass

    def exit(self):
        pass
