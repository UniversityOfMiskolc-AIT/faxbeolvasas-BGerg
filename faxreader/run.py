from faxreader.cli.cli_parser import parse
from faxreader.core.handle_data import read_lines_from_file, get_digit, checksum


def handle(args):
    lines = read_lines_from_file("valid.txt")
    final_list = []
    for index in range(1, 10):
        digit = get_digit(index, lines)
        final_list.append(digit)
    print("".join(final_list))
    checksum(final_list)


if __name__ == "__main__":
    handle(parse())
