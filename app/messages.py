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
