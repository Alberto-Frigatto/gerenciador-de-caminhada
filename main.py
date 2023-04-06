from app import App


def main() -> None:
    app = App()

    app.welcome()

    while True:
        app.options_menu()
        option_selected = app.get_valid_user_option()

        app.clear_screen()

        app.execute_option(option_selected)

        if option_selected == app.exit_option:
            break

    app.end()


if __name__ == '__main__':
    main()
