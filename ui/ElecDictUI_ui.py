# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ElecDictUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)
import ElecDict_rc

class Ui_ElecDictWidget(object):
    def setupUi(self, ElecDictWidget):
        if not ElecDictWidget.objectName():
            ElecDictWidget.setObjectName(u"ElecDictWidget")
        ElecDictWidget.resize(428, 751)
        self.titleWidget = QWidget(ElecDictWidget)
        self.titleWidget.setObjectName(u"titleWidget")
        self.titleWidget.setGeometry(QRect(0, 0, 428, 60))
        self.label = QLabel(self.titleWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 16, 28, 28))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(u":/main/img/logo.png"))
        self.minBtn = QPushButton(self.titleWidget)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setGeometry(QRect(335, 16, 25, 25))
        sizePolicy.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/main/img/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon)
        self.minBtn.setIconSize(QSize(20, 20))
        self.closeBtn = QPushButton(self.titleWidget)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(379, 16, 25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/main/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(20, 20))
        self.titleLabel = QLabel(self.titleWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(54, 16, 80, 27))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy1)
        self.listWidget = QListWidget(ElecDictWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(34, 171, 360, 477))
        self.searchWidget = QWidget(ElecDictWidget)
        self.searchWidget.setObjectName(u"searchWidget")
        self.searchWidget.setGeometry(QRect(34, 90, 360, 44))
        sizePolicy.setHeightForWidth(self.searchWidget.sizePolicy().hasHeightForWidth())
        self.searchWidget.setSizePolicy(sizePolicy)
        self.searchLineEdit = QLineEdit(self.searchWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(20, 7, 281, 28))
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)
        self.searchBtn = QPushButton(self.searchWidget)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setGeometry(QRect(323, 10, 25, 25))
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/main/img/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon2)
        self.searchBtn.setIconSize(QSize(25, 25))
        self.bottomWidget = QWidget(ElecDictWidget)
        self.bottomWidget.setObjectName(u"bottomWidget")
        self.bottomWidget.setGeometry(QRect(0, 687, 428, 64))
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.addBtn = QPushButton(self.bottomWidget)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setGeometry(QRect(194, 12, 40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/main/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addBtn.setIcon(icon3)
        self.addBtn.setIconSize(QSize(40, 40))

        self.retranslateUi(ElecDictWidget)

        QMetaObject.connectSlotsByName(ElecDictWidget)
    # setupUi

    def retranslateUi(self, ElecDictWidget):
        ElecDictWidget.setWindowTitle(QCoreApplication.translate("ElecDictWidget", u"Form", None))
        self.label.setText("")
        self.minBtn.setText("")
        self.closeBtn.setText("")
        self.titleLabel.setText(QCoreApplication.translate("ElecDictWidget", u"\u7535\u5b50\u8bcd\u5178", None))
        self.searchBtn.setText("")
        self.addBtn.setText("")
    # retranslateUi

