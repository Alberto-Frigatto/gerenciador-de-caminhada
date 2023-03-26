from colorama import Fore


def welcome() -> None:
    message = ('********************************\n'
               f'|     {Fore.YELLOW}Bem vindo ao programa{Fore.RESET}     |\n'
               '********************************\n')

    print(message)


def end() -> None:
    message = f'{Fore.YELLOW}Fim do programa{Fore.RESET}'

    print(message)


def invalid_option() -> None:
    message = f'{Fore.RED}Opção inválida{Fore.RESET}\n'

    print(message)


def no_walks() -> None:
    message = f'{Fore.YELLOW}Sem caminhadas{Fore.RESET}\n'

    print(message)

def walk_created() -> None:
    message = f'{Fore.GREEN}Caminhada cadastrada{Fore.RESET}\n'

    print(message)
