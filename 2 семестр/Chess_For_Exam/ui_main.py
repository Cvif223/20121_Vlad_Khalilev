# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from logics import Board, Game
from ui_dialog_located import DialogLocated
from ui_dialog_place import PlaceFigureDialog
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton,
    QStatusBar, QVBoxLayout, QWidget)
from data import data
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.first_run: bool = True
        self._N: int
        self._L: int

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(315, 518)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.start_button = QPushButton(self.centralwidget) #кнопка отрисовки окна с размещёнными фигурами
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(80, 320, 161, 41))
        self.start_button.clicked.connect(self.start)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 140, 203, 101))

        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.verticalLayout.addWidget(self.label)

        self.user_desk_size_input = QLineEdit(self.layoutWidget) #окно пользовательского ввода размера доски
        self.user_desk_size_input.setObjectName(u"user_desk_size_input")
        self.verticalLayout.addWidget(self.user_desk_size_input)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.user_required_figures_input = QLineEdit(self.layoutWidget) #окно пользовательского ввода требуемых к расстановке фигур
        self.user_required_figures_input.setObjectName(u"user_required_figures_input")
        self.verticalLayout.addWidget(self.user_required_figures_input)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 50, 258, 72))

        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.title_1 = QLabel(self.layoutWidget1)
        self.title_1.setObjectName(u"title_1")
        self.title_1.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.verticalLayout_2.addWidget(self.title_1)

        self.title_2 = QLabel(self.layoutWidget1)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.verticalLayout_2.addWidget(self.title_2)

        self.exit_button = QPushButton(self.centralwidget) #кнопка выхода
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(80, 360, 161, 41))
        self.exit_button.clicked.connect(self.exit_application)

        self.place_user_figures_button = QPushButton(self.centralwidget) #кнопка отрисовки окна для размещения фигур
        self.place_user_figures_button.setObjectName(u"place_user_figures_button")
        self.place_user_figures_button.setGeometry(QRect(80, 280, 161, 41))
        self.place_user_figures_button.clicked.connect(self.place_user_figures)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 315, 33))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0434\u043e\u0441\u043a\u0438 N:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0440\u0435\u0431\u0443\u0435\u043c\u044b\u0445 \u0444\u0438\u0433\u0443\u0440 L:", None))
        self.title_1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b \u0438\u0433\u0440\u0430\u0442\u0435\u0442\u0435 \u0437\u0430 \u0444\u0438\u0433\u0443\u0440\u0443:", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow",u"        \u0410\u043b\u0444\u0438\u043d-\u0420\u044b\u0431\u043a\u0430", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.place_user_figures_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u043e\u043f. \u0444\u0438\u0433\u0443\u0440\u044b", None))
    # retranslateUi


    def place_user_figures(self):
        """Обработчик нажатия кнопки пользовательского ввода фигур"""
        if self.user_desk_size_input.text() == "" or self.user_required_figures_input.text() == "": #проверка пользовательского ввода
            pass
        else:
            self._N = int(self.user_desk_size_input.text())
            self._L = int(self.user_required_figures_input.text())
            data["input"] = (self._N, self._L)
            dialog = PlaceFigureDialog()

            if dialog.exec() == QDialog.DialogCode.Accepted:
                dialog.get_selected_positions()

    def start(self):
        """обработчик нажатия кнопки старт"""
        if self.user_desk_size_input.text() == "" or self.user_required_figures_input.text() == "" or self.first_run == False:
            pass
        else:
            board = Board(self._N)
            existing_positions = data["coords"]

            game = Game(board, self._L, existing_positions)
            game.start(ui_solution=True)

            dialog = DialogLocated()
            dialog.exec()

    def exit_application(self):
        """Выход"""
        QApplication.quit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())