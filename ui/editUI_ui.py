# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import ElecDict_rc

class Ui_EditWidget(object):
    def setupUi(self, EditWidget):
        if not EditWidget.objectName():
            EditWidget.setObjectName(u"EditWidget")
        EditWidget.resize(370, 260)
        EditWidget.setStyleSheet(u"")
        self.okBtn = QPushButton(EditWidget)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setGeometry(QRect(48, 195, 104, 39))
        self.cancelBtn = QPushButton(EditWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(222, 195, 104, 39))
        self.editLabel = QLabel(EditWidget)
        self.editLabel.setObjectName(u"editLabel")
        self.editLabel.setGeometry(QRect(49, 20, 96, 32))
        self.cnEditLine = QLineEdit(EditWidget)
        self.cnEditLine.setObjectName(u"cnEditLine")
        self.cnEditLine.setGeometry(QRect(22, 131, 327, 44))
        self.label_3 = QLabel(EditWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 20, 28, 28))
        self.label_3.setPixmap(QPixmap(u":/main/img/edit.png"))
        self.widget = QWidget(EditWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 76, 370, 37))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.enEditLine = QLineEdit(self.widget)
        self.enEditLine.setObjectName(u"enEditLine")
        self.enEditLine.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.enEditLine)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(EditWidget)

        QMetaObject.connectSlotsByName(EditWidget)
    # setupUi

    def retranslateUi(self, EditWidget):
        EditWidget.setWindowTitle(QCoreApplication.translate("EditWidget", u"Dialog", None))
        self.okBtn.setText(QCoreApplication.translate("EditWidget", u"\u786e\u8ba4", None))
        self.cancelBtn.setText(QCoreApplication.translate("EditWidget", u"\u53d6\u6d88", None))
        self.editLabel.setText(QCoreApplication.translate("EditWidget", u"\u4fee\u6539/\u589e\u52a0", None))
        self.label_3.setText("")
        self.enEditLine.setText(QCoreApplication.translate("EditWidget", u"Apple", None))
    # retranslateUi

