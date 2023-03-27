from abc import ABCMeta
from colorama import Fore


class WalkError(Exception, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WalkDateError(WalkError):
    MESSAGE = f'{Fore.RED}Data inválida{Fore.RESET}\n'

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class WalkDistanceError(WalkError):
    MESSAGE = f'{Fore.RED}Distância inválida{Fore.RESET}\n'

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class WalkDurationError(WalkError):
    MESSAGE = f'{Fore.RED}Duração inválida{Fore.RESET}\n'

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)
