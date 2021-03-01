import faxreader.core.numbers as numbers

def read_lines_from_file(filename: str):
    with open(filename) as f:
        file_content = f.readlines()
    return file_content

def interpret_eight_segment_numbers_and_covert_to_str(line: list):
    count = 0
    final_list = ""
    for i in range(9):
        number = [line[0][0+count] + line[0][1+count] + line[0][2+count]
                + line[1][0+count] + line[1][1+count] + line[1][2+count]
                + line[2][0+count] + line[2][1+count] + line[2][2+count]]
        if count < 24:
            count += 3
        number_as_digit = transform_eight_segment_to_digit(number)
        final_list += number_as_digit
    return final_list

def transform_eight_segment_to_digit(input_number: list):
    number = numbers.numbers()
    if number.one == input_number:
        return '1'
    elif number.two == input_number:
        return '2'
    elif number.three == input_number:
        return '3'
    elif number.four == input_number:
        return '4'
    elif number.five == input_number:
        return '5'
    elif number.six == input_number:
        return '6'
    elif number.seven == input_number:
        return '7'
    elif number.eight == input_number:
        return '8'
    elif number.nine == input_number:
        return '9'
    else:
        raise TypeError("Number is not eight digit format")

