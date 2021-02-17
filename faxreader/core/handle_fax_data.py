def split_and_type_conversion_of_content(account_number: str):
    account_numbers_as_chars = split_input_to_list(account_number)
    account_number_as_ints = check_input_and_type_conversion(account_numbers_as_chars)
    return account_number_as_ints


def split_input_to_list(account_number: str):
    account_numbers_as_chars = list(account_number)
    return account_numbers_as_chars


def check_input_and_type_conversion(account_number: list):
    for i in range(0, len(account_number)):
        try:
            account_number[i] = int(account_number[i])
        except:
            raise TypeError("Be careful!Only integers can be enter as input!")
    return account_number
