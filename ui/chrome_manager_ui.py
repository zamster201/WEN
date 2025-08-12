# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chrome_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ChromeManager(object):
    def setupUi(self, ChromeManager):
        if not ChromeManager.objectName():
            ChromeManager.setObjectName(u"ChromeManager")
        ChromeManager.resize(600, 400)
        self.mainLayout = QVBoxLayout(ChromeManager)
        self.mainLayout.setObjectName(u"mainLayout")
        self.chromeWindowList = QListWidget(ChromeManager)
        self.chromeWindowList.setObjectName(u"chromeWindowList")

        self.mainLayout.addWidget(self.chromeWindowList)


        self.retranslateUi(ChromeManager)

        QMetaObject.connectSlotsByName(ChromeManager)
    # setupUi

    def retranslateUi(self, ChromeManager):
        ChromeManager.setWindowTitle(QCoreApplication.translate("ChromeManager", u"Chrome Manager", None))
    # retranslateUi

