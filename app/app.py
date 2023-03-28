import app.dao
import app.messages
from colorama import Fore
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, '..')
sys.path.append(root_dir)

from walk import (
    Walk,
    WalkingList
)

from walk.exceptions import WalkError


class App:
    def __init__(self) -> None:
        self._create_walking_list_file_if_not_exists()
        self._walking_list = WalkingList()
        self.OPTIONS = [
            (1, self.view_walks),
            (2, self.create_walk),
            (3, self.delete_walk),
            (4, self.mean_walking_time),
            (5, self.walking_time_std),
            (6, self.total_mileage),
            (7, self.total_monthly_mileage),
            (8, self.total_monthly_mileage_plot),
            (9, self.walking_time_plot),
            (10, self.exit)
        ]

    def _create_walking_list_file_if_not_exists(self) -> None:
        if not app.dao.walking_list_file_exist():
            app.dao.create_walking_list_file()

    def welcome(self) -> None:
        os.system('cls')
        app.messages.welcome()

    def end(self) -> None:
        os.system('cls')
        app.messages.end()

    def options_menu(self) -> None:
        menu = (
            f'{Fore.YELLOW}1{Fore.RESET} - Visualizar caminhadas\n'
            f'{Fore.YELLOW}2{Fore.RESET} - Cadastrar caminhada\n'
            f'{Fore.YELLOW}3{Fore.RESET} - Excluir caminhada\n'
            f'{Fore.YELLOW}4{Fore.RESET} - Tempo médio das caminhadas\n'
            f'{Fore.YELLOW}5{Fore.RESET} - Desvio padrão dos tempos das caminhadas\n'
            f'{Fore.YELLOW}6{Fore.RESET} - Quilometragem total\n'
            f'{Fore.YELLOW}7{Fore.RESET} - Quilometragem total mensal\n'
            f'{Fore.YELLOW}8{Fore.RESET} - Gráfico da quilometragem total mensal\n'
            f'{Fore.YELLOW}9{Fore.RESET} - Gráfico dos tempos das caminhadas\n'
            f'{Fore.YELLOW}10{Fore.RESET} - Sair\n'
        )
        print(menu)

    def get_valid_user_option(self) -> int:
        while True:
            try:
                user_input = int(input('Selecione uma opção: '))
                print()

                if user_input not in range(1, len(self.OPTIONS) + 1):
                    raise ValueError

            except ValueError:
                os.system('cls')
                app.messages.invalid_option()
                self.options_menu()

            else:
                return user_input

    def execute_option(self, option_selected: int) -> None:
        for option_index, option in self.OPTIONS:
            if option_selected == option_index:
                option()

    def view_walks(self) -> None:
        print(
            f'{self._walking_list.walks}\n'
        ) if len(self._walking_list) \
            else app.messages.no_walks()

    def create_walk(self) -> None:
        while True:
            date = input('Informe a data da caminhada (dd/mm/aaaa): ')
            distance = input('Informe a distância percorrida (Km): ')
            duration = input('Informe a duração da caminhada (min): ')

            try:
                walk = Walk(date, distance, duration)
            except WalkError as walk_error:
                os.system('cls')
                print(walk_error)
            else:
                if self._confirm_walk_creation():
                    self._walking_list.add_walk(walk)
                    self._walking_list.save()
                    app.messages.walk_created()
                else:
                    print()

                break

    def _confirm_walk_creation(self) -> bool:
        while True:
            user_input = input(
                f'Deseja criar a caminhada? {Fore.YELLOW}(s/n){Fore.RESET}: '
            ).lower()

            if user_input not in ['s', 'n']:
                app.messages.invalid_option()
                continue

            return True if user_input == 's' else False

    def delete_walk(self) -> None:
        if len(self._walking_list):
            self.view_walks()
            walk_to_be_deleted = self.get_walk_to_be_deleted()

            if self._confirm_delete_walk():
                self._walking_list.delete_walk(walk_to_be_deleted)
                self._walking_list.save()
                app.messages.walk_deleted()
        else:
            app.messages.no_walks()

    def get_walk_to_be_deleted(self) -> int:
        while True:
            try:
                user_input = input(
                    'Digite o índice da caminhada a ser deletada: '
                )
                walk_index = int(user_input)

                if walk_index not in list(self._walking_list.index):
                    raise ValueError()
            except ValueError:
                app.messages.non_existent_walk(user_input)
            else:
                return walk_index

    def _confirm_delete_walk(self) -> None:
        while True:
            user_input = input(
                f'Deseja deletar a caminhada? {Fore.YELLOW}(s/n){Fore.RESET}: '
            ).lower()

            if user_input not in ['s', 'n']:
                app.messages.invalid_option()
                continue

            return True if user_input == 's' else False

    def mean_walking_time(self) -> None:
        print(
            (f'Seu tempo médio é: {Fore.YELLOW}'
             f'{self._walking_list.mean_walking_time()}min\n'
             f'{Fore.RESET}')
        ) if len(self._walking_list) \
            else app.messages.no_walks()

    def walking_time_std(self) -> None:
        print(
            (f'O desvio padrão dos tempos é: {Fore.YELLOW}'
             f'{self._walking_list.walking_time_std()}min\n'
             f'{Fore.RESET}')
        ) if len(self._walking_list) \
            else app.messages.no_walks()

    def total_mileage(self) -> None:
        print(
            (f'Sua quilometragem total é: {Fore.YELLOW}'
             f'{self._walking_list.total_mileage()}km\n'
             f'{Fore.RESET}')
        ) if len(self._walking_list) \
            else app.messages.no_walks()

    def total_monthly_mileage(self) -> None:
        print(
            (f'Quilometragem total mensal\n\n'
             f'{self._walking_list.total_monthly_mileage()}\n')
        ) if len(self._walking_list) \
            else app.messages.no_walks()

    def total_monthly_mileage_plot(self) -> None:
        self._walking_list.total_monthly_mileage_plot() \
            if len(self._walking_list) \
            else app.messages.no_walks()

    def walking_time_plot(self) -> None:
        self._walking_list.walking_time_plot() if len(self._walking_list) \
            else app.messages.no_walks()

    def exit(self) -> None:
        self._walking_list.save()
        app.messages.walking_list_saved()

    @property
    def exit_option(self) -> int:
        return self.OPTIONS[-1][0]
