from app import App
import os


def main() -> None:
    app = App()

    app.welcome()

    while True:
        app.options_menu()
        option_selected = app.get_valid_user_option()

        os.system('cls')

        app.execute_option(option_selected)

        if option_selected == app.exit_option:
            break

    app.end()


if __name__ == '__main__':
    main()
