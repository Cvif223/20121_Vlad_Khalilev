# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QSizePolicy,
                               QStatusBar, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsRectItem)
from logics import Board, Game


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(725, 488)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Graphics View для отображения доски
        self.main_desk = QGraphicsView(self.centralwidget)
        self.main_desk.setObjectName(u"main_desk")
        self.main_desk.setGeometry(QRect(310, 20, 400, 400))
        self.scene = QGraphicsScene()
        self.main_desk.setScene(self.scene)

        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(80, 310, 161, 41))
        self.StartButton.clicked.connect(self.start_game)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 140, 203, 143))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Поля ввода
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 50, 258, 72))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.title_1 = QLabel(self.widget1)
        self.title_1.setObjectName(u"title_1")
        self.title_1.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.verticalLayout_2.addWidget(self.title_1)

        self.title_2 = QLabel(self.widget1)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.verticalLayout_2.addWidget(self.title_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 725, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Шахматная доска", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Старт", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Размер доски (1-20):", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Количество требуемых фигур:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Количество размещенных фигур:", None))
        self.title_1.setText(QCoreApplication.translate("MainWindow", u"Вы играете за фигуру:", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"        Альфин-Рыбка", None))

    def start_game(self):
        """Обработчик нажатия кнопки Старт"""
        try:
            # Получаем параметры из полей ввода
            N = int(self.lineEdit.text())
            L = int(self.lineEdit_2.text())
            K = int(self.lineEdit_3.text())

            if not (1 <= N <= 20):
                raise ValueError("Размер доски должен быть от 1 до 20")

            # Создаем доску и игру
            board = Board(N)
            existing_positions = []  # Здесь можно добавить начальные позиции

            # Очищаем сцену перед отрисовкой новой доски
            self.scene.clear()

            # Рассчитываем размер клетки с учетом размера доски
            cell_size = min(400 // N, 400 // N)

            # Рисуем доску
            for x in range(N):
                for y in range(N):
                    rect = QGraphicsRectItem(x * cell_size, y * cell_size, cell_size, cell_size)
                    if (x + y) % 2 == 0:
                        rect.setBrush(QColor(255, 255, 255))  # Белые клетки
                    else:
                        rect.setBrush(QColor(100, 100, 100))  # Серые клетки
                    self.scene.addItem(rect)

            # Здесь можно добавить отрисовку фигур
            # Пример отрисовки фигуры (круга) в позиции (1, 1)
            # figure = self.scene.addEllipse(1 * cell_size + 5, 1 * cell_size + 5,
            #                              cell_size - 10, cell_size - 10,
            #                              QColor(255, 0, 0))

            # Запускаем игру
            game = Game(board, L, existing_positions)
            game.start()

        except ValueError as e:
            # Выводим сообщение об ошибке
            error_label = QLabel(str(e))
            error_label.setStyleSheet("color: red;")
            self.verticalLayout.addWidget(error_label)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())