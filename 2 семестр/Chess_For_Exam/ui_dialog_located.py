# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_located.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QPushButton, QGraphicsRectItem, QGraphicsScene)
from data import data
from logics import Game, Board

class Ui_dialog_located(object):
    def setupUi(self, ui_dialog_located):
        if not ui_dialog_located.objectName():
            ui_dialog_located.setObjectName(u"ui_dialog_located")
        ui_dialog_located.resize(455, 518)

        self.dialog_located_desk = QGraphicsView(ui_dialog_located) #доска
        self.dialog_located_desk.setObjectName(u"dialog_located_desk")
        self.dialog_located_desk.setGeometry(QRect(30, 30, 400, 400))

        self.dialog_located_confirm = QPushButton(ui_dialog_located) #кнопка сохранения в файл расположения фигур
        self.dialog_located_confirm.setObjectName(u"dialog_located_confirm")
        self.dialog_located_confirm.setGeometry(QRect(150, 450, 161, 41))
        self.dialog_located_confirm.clicked.connect(self.write_into_file)

        self.scene = QGraphicsScene()
        self.dialog_located_desk.setScene(self.scene)

        self.retranslateUi(ui_dialog_located)

        QMetaObject.connectSlotsByName(ui_dialog_located)
    # setupUi

    def retranslateUi(self, ui_dialog_located):
        ui_dialog_located.setWindowTitle(QCoreApplication.translate("ui_dialog_located", u"Dialog", None))
        self.dialog_located_confirm.setText(QCoreApplication.translate("ui_dialog_located", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0440\u0435\u0448\u0435\u043d\u0438\u044f", None))
    # retranslateUi

    def draw_board(self):
        """Отрисовка доски"""
        self.scene.clear()
        N = data["input"][0]
        existing_positions = data["coords"]

        cell_size = 400 // N - 1
        for x in range(N):
            for y in range(N):
                rect = QGraphicsRectItem(x * cell_size, y * cell_size, cell_size, cell_size)

                if (x, y) in existing_positions:
                    rect.setBrush(QColor(255, 0, 0))
                else:
                    if str(data["board"][x, y]) == "*":
                        rect.setBrush(QColor(0, 0, 255))
                    elif str(data["board"][x, y]) == "!":
                        rect.setBrush(QColor(0, 255, 0))
                    else:
                        if (x + y) % 2 == 0:
                            rect.setBrush(QColor(255, 255, 255))
                        else:
                            rect.setBrush(QColor(100, 100, 100))

                self.scene.addItem(rect)

    def write_into_file(self):
        """Обработчик при нажатии на кнопку сохранения в файл"""
        N = data["input"][0]
        L = data["input"][1]
        existing_positions = data["coords"]

        board = Board(N)
        game = Game(board, L, existing_positions)
        game.start()

        self.exit_application()

    def exit_application(self):
        QApplication.quit()


class DialogLocated(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog_located()
        self.ui.setupUi(self)
        self.ui.draw_board()
