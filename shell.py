from lib.interpreter import run
import sys


def main(run_test=None):
    keep_run = True
    while keep_run:
        if run_test != None:
            keep_run = False
            text = run_test
        else:
            text = input('Persatuan> ')

        if text == "keluar":
            break
        if text.strip() == '':
            continue
        _, error = run('<stdin>', text)

        if error:
            print(error.as_string())


if __name__ == '__main__':
    if len(sys.argv) != 1:
        main(sys.argv[1])
    else:
        main()
