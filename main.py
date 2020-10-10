import runpy


def main():
    appy_package = runpy.run_module(mod_name="appy", init_globals=globals())
    appy_package['message'].script_path(__file__)
    appy_package['main']()


if __name__ == "__main__":
    main()
