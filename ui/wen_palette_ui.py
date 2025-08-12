# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wen_palette.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_WENPalette(object):
    def setupUi(self, WENPalette):
        if not WENPalette.objectName():
            WENPalette.setObjectName(u"WENPalette")
        WENPalette.resize(300, 500)
        self.verticalLayout = QVBoxLayout(WENPalette)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chromeButton = QPushButton(WENPalette)
        self.chromeButton.setObjectName(u"chromeButton")

        self.verticalLayout.addWidget(self.chromeButton)

        self.cwtButton = QPushButton(WENPalette)
        self.cwtButton.setObjectName(u"cwtButton")

        self.verticalLayout.addWidget(self.cwtButton)


        self.retranslateUi(WENPalette)

        QMetaObject.connectSlotsByName(WENPalette)
    # setupUi

    def retranslateUi(self, WENPalette):
        WENPalette.setWindowTitle(QCoreApplication.translate("WENPalette", u"WEN Palette", None))
        self.chromeButton.setText(QCoreApplication.translate("WENPalette", u"Chrome", None))
        self.cwtButton.setText(QCoreApplication.translate("WENPalette", u"Launch CWT", None))
    # retranslateUi

