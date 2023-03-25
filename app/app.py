import app.dao
import app.messages
from colorama import Fore
import os


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

    def welcome(self) -> None:
        os.system('cls')
        app.messages.welcome()

    def options_menu(self) -> None:
        menu = (
            f'{Fore.YELLOW}1{Fore.RESET} - Visualizar caminhadas\n'
            f'{Fore.YELLOW}2{Fore.RESET} - Cadastrar caminhada\n'
            f'{Fore.YELLOW}3{Fore.RESET} - Tempo médio das caminhadas\n'
            f'{Fore.YELLOW}4{Fore.RESET} - Desvio médio dos tempos das caminhadas\n'
            f'{Fore.YELLOW}5{Fore.RESET} - Quilometragem total\n'
            f'{Fore.YELLOW}6{Fore.RESET} - Quilometragem média mensal\n'
            f'{Fore.YELLOW}7{Fore.RESET} - Gráfico da quilometragem média mensal\n'
            f'{Fore.YELLOW}8{Fore.RESET} - Gráfico dos tempos das caminhadas\n'
            f'{Fore.YELLOW}9{Fore.RESET} - Sair\n'
        )
        print(menu)

    def get_valid_user_option(self) -> int:
        while True:
            try:
                user_input = int(input('Selecione uma opção: '))

                if user_input not in range(1, len(self.OPTIONS) + 1):
                    raise ValueError

            except ValueError:
                os.system('cls')
                app.messages.invalid_option()
                self.options_menu()

            else:
                return user_input

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
