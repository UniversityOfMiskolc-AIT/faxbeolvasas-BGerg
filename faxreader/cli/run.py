from faxreader.cli.cli_parser import parse
from faxreader.core.handle_fax_data import split_and_type_conversion_of_content


def handle(args):
    account_number = split_and_type_conversion_of_content(args.account_number)


if __name__ == "__main__":
    handle(parse())
