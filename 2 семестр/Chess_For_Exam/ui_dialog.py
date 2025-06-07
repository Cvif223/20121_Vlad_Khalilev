# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView,QGraphicsScene, QGraphicsRectItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_place_user_figure_dialog(object):
    def setupUi(self, place_user_figure_dialog):
        if not place_user_figure_dialog.objectName():
            place_user_figure_dialog.setObjectName(u"place_user_figure_dialog")
        place_user_figure_dialog.resize(422, 491)
        self.dialog_desk = QGraphicsView(place_user_figure_dialog)
        self.dialog_desk.setObjectName(u"dialog_desk")
        self.dialog_desk.setGeometry(QRect(10, 10, 400, 400))
        self.dialog_confirm = QPushButton(place_user_figure_dialog)
        self.dialog_confirm.setObjectName(u"dialog_confirm")
        self.dialog_confirm.setGeometry(QRect(30, 430, 161, 41))
        self.dialog_cancel = QPushButton(place_user_figure_dialog)
        self.dialog_cancel.setObjectName(u"dialog_cancel")
        self.dialog_cancel.setGeometry(QRect(230, 430, 161, 41))

        self.retranslateUi(place_user_figure_dialog)

        QMetaObject.connectSlotsByName(place_user_figure_dialog)
        self.scene = QGraphicsScene()
        self.dialog_desk.setScene(self.scene)
        self.selected_positions = []
        self.init_board()
    # setupUi

    def retranslateUi(self, place_user_figure_dialog):
        place_user_figure_dialog.setWindowTitle(QCoreApplication.translate("place_user_figure_dialog", u"Dialog", None))
        self.dialog_confirm.setText(QCoreApplication.translate("place_user_figure_dialog", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.dialog_cancel.setText(QCoreApplication.translate("place_user_figure_dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))

    def init_board(self):
        self.scene.clear()
        print(open("input.txt", "r").readlines())
        print(open("input.txt", "r").readlines()[0].split(" ")[0])
        self.board_size = int(open("input.txt", "r").readlines()[0].split(" ")[0])
        self.cell_size = 399 // self.board_size
        print(self.cell_size)

        # Создаем кнопки-клетки
        for x in range(self.board_size):
            for y in range(self.board_size):
                rect = QGraphicsRectItem(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)

                if (x + y) % 2 == 0:
                    rect.setBrush(QColor(255, 255, 255))  # Белые клетки
                else:
                    rect.setBrush(QColor(100, 100, 100))  # Серые клетки
                    # Сохраняем координаты и исходный цвет
                rect.setData(0, (x, y))
                rect.setData(1, rect.brush().color())  # Сохраняем исходный цвет

                self.scene.addItem(rect)

                # Подключаем обработчик событий мыши
            self.dialog_desk.setMouseTracking(True)
            self.scene.mousePressEvent = self.handle_mouse_click

    def handle_mouse_click(self, event):
        """Обработка кликов мыши"""
        item = self.scene.itemAt(event.scenePos(), self.dialog_desk.transform())
        if isinstance(item, QGraphicsRectItem):
            x, y = item.data(0)

            # Левый клик - установка красного цвета
            if event.button() == Qt.LeftButton:
                item.setBrush(QColor(255, 0, 0))  # Красный
                if (x, y) not in self.selected_positions:
                    self.selected_positions.append((x, y))

            # Правый клик - возврат исходного цвета
            elif event.button() == Qt.RightButton:
                original_color = item.data(1)
                item.setBrush(original_color)
                if (x, y) in self.selected_positions:
                    self.selected_positions.remove((x, y))

    def save_to_file(self):
        """Сохранение координат в файл"""
        try:
            with open('coords.txt', 'w') as f:
                for pos in self.selected_positions:
                    f.write(f"{pos[0]} {pos[1]}\n")
        except IOError as e:
            print(f"Ошибка сохранения: {e}")
    def on_cell_selected(self):
        """Обработчик выбора клетки"""
        selected_items = self.scene.selectedItems()
        if selected_items:
            item = selected_items[0]
            x, y = item.data(0)  # Получаем координаты

            # Добавляем или удаляем позицию
            if (x, y) in self.selected_positions:
                self.selected_positions.remove((x, y))
                color = QColor(100, 100, 100) if (x + y) % 2 else QColor(255, 255, 255)
                item.setBrush(color)
            else:
                self.selected_positions.append((x, y))
                item.setBrush(QColor(255, 0, 0))  # Красный для выбранной клетки

                # Снимаем выделение
                item.setSelected(False)


class PlaceFigureDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_place_user_figure_dialog()
        self.ui.setupUi(self)

        # Подключаем кнопки
        self.ui.dialog_confirm.clicked.connect(self.on_confirm)
        self.ui.dialog_cancel.clicked.connect(self.reject)

    def on_confirm(self):
        """Обработчик кнопки Готово"""
        self.ui.save_to_file()
        self.accept()

    def get_selected_positions(self):
        """Возвращает выбранные позиции"""
        return self.ui.selected_positions

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = PlaceFigureDialog()
    if dialog.exec() == QDialog.Accepted:
        print("Выбранные позиции:", dialog.get_selected_positions())
    sys.exit(app.exec())
