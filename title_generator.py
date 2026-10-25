import os
import subprocess
import argparse

PADDING = 2


def main():
    parser = argparse.ArgumentParser(description="title generator for the readme")
    parser.add_argument("name", help="my name dingus")
    args = parser.parse_args()

    width = os.get_terminal_size().columns
    separator = " " * PADDING + "@" * (width - PADDING * 2)
    res = subprocess.run(
        ["figlet", "-c", "-w", str(width), "-f", "a2", args.name],
        capture_output=True, text=True, check=True,
    )

    print(separator + "\n")
    print(res.stdout)
    print(separator)


if __name__ == "__main__":
    main()
else:
    print("cant be ran as a module")
