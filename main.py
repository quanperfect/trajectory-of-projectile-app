import sys
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

import subprocess

from enums import yes_no
from file_controller.write_inputdata_to_file import write_inputdata_to_file
from file_controller.read_outputdata_from_file import read_outputdata_from_file
from my_logger.logger import log_message_debug
import default_values

class PhysicsProject(QtWidgets.QMainWindow):
    def __init__(self):
        super(PhysicsProject, self).__init__()
        self.show()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.analytical_solution = default_values.analytical_solution
        self.account_air_resistance = default_values.account_for_air_resistance

    def init_UI(self):
        self.setWindowTitle("CS II Project")
        self.setWindowIcon(QIcon('cs-II.ico'))

        self.ui.air_resistance_YES.clicked.connect(self.account_air_resistance_handle_radio_button)
        self.ui.air_resistance_NO.clicked.connect(self.account_air_resistance_handle_radio_button)
        self.ui.analyt_YES.clicked.connect(self.analytical_handle_radio_button)
        self.ui.analyt_NO.clicked.connect(self.analytical_handle_radio_button)
        self.ui.reset_to_default.clicked.connect(self.reset_values_to_default)
        self.ui.display_graph.clicked.connect(self.compute_and_display_projectile_graph)

        self.reset_values_to_default()

    def reset_values_to_default(self):
        log_message_debug("Defaulting all values...")
        self.ui.mass_text_field.setText(f"{default_values.mass}")
        self.ui.headsurf_text_field.setText(f"{default_values.head_surface}")
        self.ui.air_resistance_text_field.setText(f"{default_values.air_resistance_coefficient}")
        self.ui.init_vel_text_field.setText(f"{default_values.initial_velocity}")
        self.ui.can_angle_text_field.setText(f"{default_values.cannon_angle}")
        self.ui.time_step_text_field.setText(f"{default_values.time_step}")
        log_message_debug("UI values successfully defaulted\n")

    def account_air_resistance_handle_radio_button(self):
        sender = self.sender()
        hide = False
        if sender == self.ui.air_resistance_YES:
            self.account_air_resistance = yes_no.YES
            hide = False
        elif sender == self.ui.air_resistance_NO:
            self.account_air_resistance = yes_no.NO
            hide = True

        # show/hide all related to air resistance parameters
        self.ui.mass_text.setHidden(hide)
        self.ui.mass_text_field.setHidden(hide)
        self.ui.m_letter.setHidden(hide)
        self.ui.kg_unit.setHidden(hide)

        self.ui.head_surface.setHidden(hide)
        self.ui.headsurf_text_field.setHidden(hide)
        self.ui.A_letter.setHidden(hide)
        self.ui.m2_unit.setHidden(hide)

        self.ui.air_resistance_coef.setHidden(hide)
        self.ui.air_resistance_text_field.setHidden(hide)
        self.ui.Cd_letter.setHidden(hide)

        log_message_debug(f"Handling account for air resistance yes/no radio buttion, new value: {self.account_air_resistance.value}\n")
    def analytical_handle_radio_button(self):
        sender = self.sender()
        if sender == self.ui.analyt_YES:
            self.analytical_solution = yes_no.YES
        elif sender == self.ui.analyt_NO:
            self.analytical_solution = yes_no.NO

        log_message_debug(f"Handling analytical solution yes/no radio buttion, new value: {self.analytical_solution.value}\n")

    def compute_and_display_projectile_graph(self):
        plt.close()
        log_message_debug("Compute and display projectile graph called")
        mass = float(self.ui.mass_text_field.text())
        head_surface = float(self.ui.headsurf_text_field.text())
        air_resistance_coefficient = float(self.ui.air_resistance_text_field.text())
        initial_velocity = float(self.ui.init_vel_text_field.text())
        cannon_angle = float(self.ui.can_angle_text_field.text())
        time_step = float(self.ui.time_step_text_field.text())
        write_inputdata_to_file(mass, head_surface, air_resistance_coefficient, initial_velocity, cannon_angle, time_step,
                                self.account_air_resistance.value, self.analytical_solution.value)
        log_message_debug("Data was written to input.txt")
        command = 'cd C_code && gcc -o computator computator.c && .\computator'
        subprocess.call(command, shell=True)
        log_message_debug("computator.c finished execution")


        x_coord, y_coord, analytical_x_coord, analytical_y_coord = read_outputdata_from_file(self.analytical_solution)
        log_message_debug("Data was read from output.txt that was created by computer.c")

        log_message_debug("Starting to create plot figure...")
        fig = plt.figure('Trajectory of the projectile')
        plt.clf()

        numerical_solution_label = 'Numerical solution\n(with air resistance)'
        if air_resistance_coefficient == 0 or mass == 0 or head_surface == 0 or self.account_air_resistance == yes_no.NO:
            numerical_solution_label = 'Numerical solution\n(no air resistance)'
        plt.plot(x_coord, y_coord, label=numerical_solution_label, color="red")

        if self.analytical_solution == yes_no.YES:
            numerical_solution_label = 'Analytical solution\n(no air resistance)'
            plt.plot(analytical_x_coord, analytical_y_coord, label=numerical_solution_label, color="blue")

        plt.xlabel("x", fontsize=40)
        plt.ylabel("y", fontsize=40)
        plt.title("Trajectory of the projectile", fontsize=40)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0), prop={'size': 10})

        plt.xlim(left=0)
        plt.ylim(bottom=0)

        plt.gcf().subplots_adjust(bottom=0.15)
        plt.tight_layout()
        mng = plt.get_current_fig_manager()
        mng.window.showMaximized()
        plt.show()
        log_message_debug("Plot (graph) displayed\n")



app = QtWidgets.QApplication([])
application = PhysicsProject()
app.exec_()

sys.exit(app.exec())
