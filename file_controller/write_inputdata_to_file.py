from my_logger.logger import log_message_debug

def write_inputdata_to_file(mass, head_surface, air_resistance_coefficient, initial_velocity, cannon_angle, time_step, account_air_resistance_yes_no, analytical_solution_yes_no):
    with open('computational_files_io/input.txt', 'w', encoding='utf=8') as f:
        log_message_debug("[FILE_CONTROLLER / WRITE_INPUT] - input.txt opened, writing to it...")
        f.write("# - FILE GENERATED AUTOMATICALLY THROUGH APPLICATION - #\n")
        f.write("# - - - - - - - - - - - - - - - - - - - - - - - - - - #\n")
        f.write(f"{mass}\n")
        f.write(f"{head_surface}\n")
        f.write(f"{air_resistance_coefficient}\n")
        f.write(f"{initial_velocity}\n")
        f.write(f"{cannon_angle}\n")
        f.write(f"{time_step}\n")
        f.write(f"{account_air_resistance_yes_no}\n")
        f.write(f"{analytical_solution_yes_no}\n")
        f.write(str("# - - - - - - - - - - - - - - - - - - - - - - - - - - #\n"))