# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cs_II_uidCFMnH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt, QCoreApplication, QMetaObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QLineEdit, QPushButton, QRadioButton, QButtonGroup

from enums import yes_no
import default_values
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(591, 854)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: #204E9D")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 831, 111))
        self.frame.setStyleSheet(u"background: #222222")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.subject_name = QLabel(self.frame)
        self.subject_name.setObjectName(u"subject_name")
        self.subject_name.setGeometry(QRect(164, 0, 271, 71))
        font = QFont()
        font.setFamily(u"Bebas Neue Pro")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.subject_name.setFont(font)
        self.subject_name.setStyleSheet(u"color: white")
        self.subject_name.setTextFormat(Qt.RichText)
        self.subject_name.setAlignment(Qt.AlignCenter)
        self.project_name = QLabel(self.frame)
        self.project_name.setObjectName(u"project_name")
        self.project_name.setGeometry(QRect(162, 60, 271, 41))
        font1 = QFont()
        font1.setFamily(u"Bebas Neue Pro Light")
        font1.setPointSize(26)
        self.project_name.setFont(font1)
        self.project_name.setStyleSheet(u"color: white")
        self.project_name.setAlignment(Qt.AlignCenter)
        self.mass_text_field = QLineEdit(self.centralwidget)
        self.mass_text_field.setObjectName(u"mass_text_field")
        self.mass_text_field.setGeometry(QRect(40, 210, 71, 31))

        # validator = QtGui.QDoubleValidator()  # Create validator.
        # validator.setRange(0.05, 9999, 6)
        # self.mass_text_field.setValidator(validator)

        font2 = QFont()
        font2.setFamily(u"Bebas Neue Pro")
        font2.setPointSize(16)
        self.mass_text_field.setFont(font2)
        self.mass_text_field.setStyleSheet(u"background-color: #f1ffff;\n"
"border: 2px solid #222222;\n"
"color: black;\n"
"")
        self.mass_text_field.setAlignment(Qt.AlignCenter)
        self.mass_text_field.setClearButtonEnabled(False)
        self.mass_text_field.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.display_graph = QPushButton(self.centralwidget)
        self.display_graph.setObjectName(u"display_graph")
        self.display_graph.setGeometry(QRect(60, 690, 471, 51))
        font3 = QFont()
        font3.setFamily(u"Bebas Neue Pro SemiExp XBold")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.display_graph.setFont(font3)
        self.display_graph.setStyleSheet(u"QPushButton {\n"
"	background-color: #222222; \n"
"	color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #222222;\n"
"	color: black;\n"
"}")
        self.mass_text = QLabel(self.centralwidget)
        self.mass_text.setObjectName(u"mass_text")
        self.mass_text.setGeometry(QRect(20, 120, 241, 41))
        self.mass_text.setFont(font1)
        self.mass_text.setStyleSheet(u"color: white")
        self.m_letter = QLabel(self.centralwidget)
        self.m_letter.setObjectName(u"m_letter")
        self.m_letter.setGeometry(QRect(60, 160, 21, 41))
        font4 = QFont()
        font4.setFamily(u"Bebas Neue Pro SemiExp Book")
        font4.setPointSize(18)
        self.m_letter.setFont(font4)
        self.m_letter.setStyleSheet(u"color: white")
        self.kg_unit = QLabel(self.centralwidget)
        self.kg_unit.setObjectName(u"kg_unit")
        self.kg_unit.setGeometry(QRect(130, 210, 21, 31))
        font5 = QFont()
        font5.setFamily(u"Bebas Neue Pro SemiExp Book")
        font5.setPointSize(14)
        self.kg_unit.setFont(font5)
        self.kg_unit.setStyleSheet(u"color: white")
        self.headsurf_text_field = QLineEdit(self.centralwidget)
        self.headsurf_text_field.setObjectName(u"headsurf_text_field")
        self.headsurf_text_field.setGeometry(QRect(40, 350, 71, 31))
        self.headsurf_text_field.setFont(font2)
        self.headsurf_text_field.setStyleSheet(u"background-color: #f1ffff;\n"
"border: 2px solid #222222;\n"
"color: black;\n"
"")
        self.headsurf_text_field.setAlignment(Qt.AlignCenter)
        self.head_surface = QLabel(self.centralwidget)
        self.head_surface.setObjectName(u"head_surface")
        self.head_surface.setGeometry(QRect(20, 260, 261, 41))
        self.head_surface.setFont(font1)
        self.head_surface.setStyleSheet(u"color: white")
        self.A_letter = QLabel(self.centralwidget)
        self.A_letter.setObjectName(u"A_letter")
        self.A_letter.setGeometry(QRect(60, 300, 21, 41))
        self.A_letter.setFont(font4)
        self.A_letter.setStyleSheet(u"color: white")
        self.m2_unit = QLabel(self.centralwidget)
        self.m2_unit.setObjectName(u"m2_unit")
        self.m2_unit.setGeometry(QRect(130, 350, 41, 31))
        self.m2_unit.setFont(font5)
        self.m2_unit.setStyleSheet(u"color: white")
        self.Cd_letter = QLabel(self.centralwidget)
        self.Cd_letter.setObjectName(u"Cd_letter")
        self.Cd_letter.setGeometry(QRect(60, 440, 21, 41))
        self.Cd_letter.setFont(font4)
        self.Cd_letter.setStyleSheet(u"color: white")
        self.air_resistance_text_field = QLineEdit(self.centralwidget)
        self.air_resistance_text_field.setObjectName(u"air_resistance_text_field")
        self.air_resistance_text_field.setGeometry(QRect(40, 490, 71, 31))
        self.air_resistance_text_field.setFont(font2)
        self.air_resistance_text_field.setStyleSheet(u"background-color: #f1ffff;\n"
"border: 2px solid #222222;\n"
"color: black;\n"
"")
        self.air_resistance_text_field.setAlignment(Qt.AlignCenter)
        self.air_resistance_coef = QLabel(self.centralwidget)
        self.air_resistance_coef.setObjectName(u"air_resistance_coef")
        self.air_resistance_coef.setGeometry(QRect(20, 400, 281, 41))
        self.air_resistance_coef.setFont(font1)
        self.air_resistance_coef.setStyleSheet(u"color: white")
        self.Vi = QLabel(self.centralwidget)
        self.Vi.setObjectName(u"Vi")
        self.Vi.setGeometry(QRect(390, 160, 21, 41))
        self.Vi.setFont(font4)
        self.Vi.setStyleSheet(u"color: white")
        self.init_velocity = QLabel(self.centralwidget)
        self.init_velocity.setObjectName(u"init_velocity")
        self.init_velocity.setGeometry(QRect(350, 120, 321, 41))
        self.init_velocity.setFont(font1)
        self.init_velocity.setStyleSheet(u"color: white")
        self.init_vel_text_field = QLineEdit(self.centralwidget)
        self.init_vel_text_field.setObjectName(u"init_vel_text_field")
        self.init_vel_text_field.setGeometry(QRect(370, 210, 71, 31))
        self.init_vel_text_field.setFont(font2)
        self.init_vel_text_field.setStyleSheet(u"background-color: #f1ffff;\n"
"border: 2px solid #222222;\n"
"color: black;\n"
"")
        self.init_vel_text_field.setAlignment(Qt.AlignCenter)
        self.ms_speed_unit = QLabel(self.centralwidget)
        self.ms_speed_unit.setObjectName(u"ms_speed_unit")
        self.ms_speed_unit.setGeometry(QRect(460, 210, 41, 31))
        self.ms_speed_unit.setFont(font5)
        self.ms_speed_unit.setStyleSheet(u"color: white")
        self.alpha_symbol = QLabel(self.centralwidget)
        self.alpha_symbol.setObjectName(u"alpha_symbol")
        self.alpha_symbol.setGeometry(QRect(390, 300, 131, 41))
        self.alpha_symbol.setFont(font4)
        self.alpha_symbol.setStyleSheet(u"color: white")
        self.cannon_angle = QLabel(self.centralwidget)
        self.cannon_angle.setObjectName(u"cannon_angle")
        self.cannon_angle.setGeometry(QRect(350, 260, 321, 41))
        self.cannon_angle.setFont(font1)
        self.cannon_angle.setStyleSheet(u"color: white")
        self.degrees_text = QLabel(self.centralwidget)
        self.degrees_text.setObjectName(u"degrees_text")
        self.degrees_text.setGeometry(QRect(460, 350, 61, 31))
        self.degrees_text.setFont(font5)
        self.degrees_text.setStyleSheet(u"color: white")
        self.can_angle_text_field = QLineEdit(self.centralwidget)
        self.can_angle_text_field.setObjectName(u"can_angle_text_field")
        self.can_angle_text_field.setGeometry(QRect(370, 350, 71, 31))
        self.can_angle_text_field.setFont(font2)
        self.can_angle_text_field.setStyleSheet(u"background-color: #f1ffff;\n"
"border: 2px solid #222222;\n"
"color: black;\n"
"")
        self.can_angle_text_field.setAlignment(Qt.AlignCenter)
        self.author_name_surname = QLabel(self.centralwidget)
        self.author_name_surname.setObjectName(u"author_name_surname")
        self.author_name_surname.setGeometry(QRect(480, 818, 81, 31))
        font6 = QFont()
        font6.setFamily(u"Bebas Neue Pro Light")
        font6.setPointSize(14)
        self.author_name_surname.setFont(font6)
        self.author_name_surname.setStyleSheet(u"color: white")
        self.reset_to_default = QPushButton(self.centralwidget)
        self.reset_to_default.setObjectName(u"reset_to_default")
        self.reset_to_default.setGeometry(QRect(60, 760, 471, 51))
        self.reset_to_default.setFont(font3)
        self.reset_to_default.setStyleSheet(u"QPushButton {\n"
"	background-color: #222222; \n"
"	color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #222222;\n"
"	color: black;\n"
"}")
        self.add_analytical_solution = QLabel(self.centralwidget)
        self.add_analytical_solution.setObjectName(u"add_analytical_solution")
        self.add_analytical_solution.setGeometry(QRect(330, 535, 321, 41))
        self.add_analytical_solution.setFont(font1)
        self.add_analytical_solution.setStyleSheet(u"color: white")
        self.analyt_YES = QRadioButton(self.centralwidget)
        self.analytical_yes_no_group = QButtonGroup(MainWindow)
        self.analytical_yes_no_group.setObjectName(u"analytical_yes_no_group")
        self.analytical_yes_no_group.addButton(self.analyt_YES)
        self.analyt_YES.setObjectName(u"analyt_YES")
        self.analyt_YES.setGeometry(QRect(350, 630, 82, 31))
        font7 = QFont()
        font7.setFamily(u"Bebas Neue Pro SemiExp Book")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(50)
        self.analyt_YES.setFont(font7)
        self.analyt_YES.setStyleSheet(u"color: white")
        self.analyt_NO = QRadioButton(self.centralwidget)
        self.analytical_yes_no_group.addButton(self.analyt_NO)
        self.analyt_NO.setObjectName(u"analyt_NO")
        self.analyt_NO.setGeometry(QRect(440, 630, 82, 31))
        self.analyt_NO.setFont(font7)
        self.analyt_NO.setStyleSheet(u"color: white")

        # ----
        if default_values.analytical_solution == yes_no.YES:
            self.analyt_YES.setChecked(True)
            self.analyt_NO.setChecked(False)
        elif default_values.analytical_solution == yes_no.NO:
            self.analyt_YES.setChecked(False)
            self.analyt_NO.setChecked(True)
        # ----

        self.author_name_surname_2 = QLabel(self.centralwidget)
        self.author_name_surname_2.setObjectName(u"author_name_surname_2")
        self.author_name_surname_2.setGeometry(QRect(330, 588, 241, 31))
        self.author_name_surname_2.setFont(font6)
        self.author_name_surname_2.setStyleSheet(u"color: white")
        self.time_step_unit = QLabel(self.centralwidget)
        self.time_step_unit.setObjectName(u"time_step_unit")
        self.time_step_unit.setGeometry(QRect(460, 490, 41, 31))
        self.time_step_unit.setFont(font5)
        self.time_step_unit.setStyleSheet(u"color: white")
        self.dt = QLabel(self.centralwidget)
        self.dt.setObjectName(u"dt")
        self.dt.setGeometry(QRect(390, 440, 21, 41))
        self.dt.setFont(font4)
        self.dt.setStyleSheet(u"color: white")
        self.time_step_text_field = QLineEdit(self.centralwidget)
        self.time_step_text_field.setObjectName(u"time_step_text_field")
        self.time_step_text_field.setGeometry(QRect(370, 490, 71, 31))
        self.time_step_text_field.setFont(font2)
        self.time_step_text_field.setStyleSheet(u"background-color: #f1ffff;\n"
"border: 2px solid #222222;\n"
"color: black;\n"
"")
        self.time_step_text_field.setAlignment(Qt.AlignCenter)
        self.time_step = QLabel(self.centralwidget)
        self.time_step.setObjectName(u"time_step")
        self.time_step.setGeometry(QRect(350, 400, 321, 41))
        self.time_step.setFont(font1)
        self.time_step.setStyleSheet(u"color: white")
        self.air_resistance_YES = QRadioButton(self.centralwidget)
        self.account_for_air_resistance_2 = QButtonGroup(MainWindow)
        self.account_for_air_resistance_2.setObjectName(u"account_for_air_resistance_2")
        self.account_for_air_resistance_2.addButton(self.air_resistance_YES)
        self.air_resistance_YES.setObjectName(u"air_resistance_YES")
        self.air_resistance_YES.setGeometry(QRect(40, 630, 82, 31))
        self.air_resistance_YES.setFont(font7)
        self.air_resistance_YES.setStyleSheet(u"color: white")
        self.air_resistance_YES.setChecked(True)
        self.air_resistance_NO = QRadioButton(self.centralwidget)
        self.account_for_air_resistance_2.addButton(self.air_resistance_NO)
        self.air_resistance_NO.setObjectName(u"air_resistance_NO")
        self.air_resistance_NO.setGeometry(QRect(130, 630, 82, 31))
        self.air_resistance_NO.setFont(font7)
        self.air_resistance_NO.setStyleSheet(u"color: white")
        self.account_for_air_resistance = QLabel(self.centralwidget)
        self.account_for_air_resistance.setObjectName(u"account_for_air_resistance")
        self.account_for_air_resistance.setGeometry(QRect(20, 540, 281, 71))
        self.account_for_air_resistance.setFont(font1)
        self.account_for_air_resistance.setStyleSheet(u"color: white")

        # ----
        if default_values.account_for_air_resistance == yes_no.YES:
            self.air_resistance_YES.setChecked(True)
            self.air_resistance_NO.setChecked(False)
        elif default_values.account_for_air_resistance == yes_no.NO:
            self.air_resistance_YES.setChecked(False)
            self.air_resistance_NO.setChecked(True)
        # ----

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.mass_text_field, self.headsurf_text_field)
        QWidget.setTabOrder(self.headsurf_text_field, self.air_resistance_text_field)
        QWidget.setTabOrder(self.air_resistance_text_field, self.air_resistance_NO)
        QWidget.setTabOrder(self.air_resistance_NO, self.air_resistance_YES)
        QWidget.setTabOrder(self.air_resistance_YES, self.init_vel_text_field)
        QWidget.setTabOrder(self.init_vel_text_field, self.can_angle_text_field)
        QWidget.setTabOrder(self.can_angle_text_field, self.time_step_text_field)
        QWidget.setTabOrder(self.time_step_text_field, self.analyt_NO)
        QWidget.setTabOrder(self.analyt_NO, self.analyt_YES)
        QWidget.setTabOrder(self.analyt_YES, self.display_graph)
        QWidget.setTabOrder(self.display_graph, self.reset_to_default)

        self.retranslateUi(MainWindow)

        self.reset_to_default.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.subject_name.setText(QCoreApplication.translate("MainWindow", u"CS II PROJECT", None))
        self.project_name.setText(QCoreApplication.translate("MainWindow", u"Trajectory of a projectile", None))
        self.mass_text_field.setText(QCoreApplication.translate("MainWindow", f"{default_values.mass}", None))
        self.display_graph.setText(QCoreApplication.translate("MainWindow", u"DISPLAY GRAPH", None))
        self.mass_text.setText(QCoreApplication.translate("MainWindow", u"Mass", None))
        self.m_letter.setText(QCoreApplication.translate("MainWindow", u"m kg", None))
        self.kg_unit.setText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.headsurf_text_field.setText(QCoreApplication.translate("MainWindow", f"{default_values.head_surface}", None))
        self.head_surface.setText(QCoreApplication.translate("MainWindow", u"Head surface", None))
        self.A_letter.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.m2_unit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>m<span style=\" vertical-align:super;\">2</span></p></body></html>", None))
        self.Cd_letter.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>C<span style=\" vertical-align:sub;\">d</span></p></body></html>", None))
        self.air_resistance_text_field.setText(QCoreApplication.translate("MainWindow", f"{default_values.air_resistance_coefficient}", None))
        self.air_resistance_coef.setText(QCoreApplication.translate("MainWindow", u"Air resistance coefficient", None))
        self.Vi.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>V<span style=\" vertical-align:sub;\">i</span></p></body></html>", None))
        self.init_velocity.setText(QCoreApplication.translate("MainWindow", u"Initial velocity", None))
        self.init_vel_text_field.setText(QCoreApplication.translate("MainWindow", f"{default_values.initial_velocity}", None))
        self.ms_speed_unit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>m/s</p></body></html>", None))
        self.alpha_symbol.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u03b1</p></body></html>", None))
        self.cannon_angle.setText(QCoreApplication.translate("MainWindow", u"Cannon angle", None))
        self.degrees_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>degrees</p></body></html>", None))
        self.can_angle_text_field.setText(QCoreApplication.translate("MainWindow", f"{default_values.cannon_angle}", None))
        self.author_name_surname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">German Dagil</span></p></body></html>", None))
        self.reset_to_default.setText(QCoreApplication.translate("MainWindow", u"RESET VALUES TO DEFAULT", None))
        self.add_analytical_solution.setText(QCoreApplication.translate("MainWindow", u"Add analytical solution", None))
        self.analyt_YES.setText(QCoreApplication.translate("MainWindow", u"YES", None))
        self.analyt_NO.setText(QCoreApplication.translate("MainWindow", u"NO", None))
        self.author_name_surname_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>NOTE: Does not account for air resistance</p></body></html>", None))
        self.time_step_unit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>s</p></body></html>", None))
        self.dt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>dt</p></body></html>", None))
        self.time_step_text_field.setText(QCoreApplication.translate("MainWindow", u"0.0001", None))
        self.time_step.setText(QCoreApplication.translate("MainWindow", u"Time step", None))
        self.air_resistance_YES.setText(QCoreApplication.translate("MainWindow", u"YES", None))
        self.air_resistance_NO.setText(QCoreApplication.translate("MainWindow", u"NO", None))
        self.account_for_air_resistance.setText(QCoreApplication.translate("MainWindow", u"Account for air resistance\n"
"in numerical solution", None))
    # retranslateUi



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())