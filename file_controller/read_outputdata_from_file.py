from enums import yes_no
from my_logger.logger import log_message_debug

def check_if_number_is_real(text):
    try:
        value = float(text)
        return True
    except ValueError:
        return False


def read_outputdata_from_file(analytical_solution_state_yes_no):
    with open('computational_files_io/output.txt', 'r', encoding='utf=8') as f:
        log_message_debug("[FILE_CONTROLLER / READ_OUTPUT] - output.txt opened, reading from it...")

        x_coord, y_coord = [], []
        analytical_x_coord, analytical_y_coord = [], []

        for line in f:
            splitted_line = line.strip().split()

            if analytical_solution_state_yes_no == yes_no.YES:
                if (check_if_number_is_real(splitted_line[0]) and check_if_number_is_real(splitted_line[1]) and
                        check_if_number_is_real(splitted_line[3]) and check_if_number_is_real(splitted_line[4])):
                    x_coord.append(float(splitted_line[0]))
                    y_coord.append(float(splitted_line[1]))
                    analytical_x_coord.append(float(splitted_line[3]))
                    analytical_y_coord.append(float(splitted_line[4]))
            else:
                if check_if_number_is_real(splitted_line[0]) and check_if_number_is_real(splitted_line[1]):
                    x_coord.append(float(splitted_line[0]))
                    y_coord.append(float(splitted_line[1]))

    return x_coord, y_coord, analytical_x_coord, analytical_y_coord