# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_error.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_error_dialog(object):
    def setupUi(self, error_dialog):
        if not error_dialog.objectName():
            error_dialog.setObjectName(u"error_dialog")
        error_dialog.resize(189, 115)
        self.error_label = QLabel(error_dialog)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(70, 30, 51, 20))
        self.confirm_error_dialog = QPushButton(error_dialog)
        self.confirm_error_dialog.setObjectName(u"confirm_error_dialog")
        self.confirm_error_dialog.setGeometry(QRect(40, 70, 111, 41))

        self.retranslateUi(error_dialog)

        QMetaObject.connectSlotsByName(error_dialog)
    # setupUi

    def retranslateUi(self, error_dialog):
        error_dialog.setWindowTitle(QCoreApplication.translate("error_dialog", u"Dialog", None))
        self.error_label.setText(QCoreApplication.translate("error_dialog", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.confirm_error_dialog.setText(QCoreApplication.translate("error_dialog", u"\u041e\u041a", None))
    # retranslateUi

