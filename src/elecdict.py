import difflib
import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QMainWindow, QWidget
from ui.editUI import Ui_EditWidget
from ui.ElecDictUI import Ui_ElecDictWidget


def loadQss(widget, qsspath):
    with open(qsspath, 'r') as f:
        widget.setStyleSheet(f.read())

class ElecDict(QWidget, Ui_ElecDictWidget,Ui_EditWidget):
    ITEMS = {}

    def __init__(self):
        super(ElecDict, self).__init__()
        self.setupUi(self)

        self.editWidget = QDialog()
        self.editWidget.setWindowFlags(Qt.FramelessWindowHint)
        self.editUi = Ui_EditWidget()
        self.editUi.setupUi(self.editWidget)
        
        
        loadQss(self,'resource/qss/ElecDict.qss')
        loadQss(self.editWidget,'resource/qss/edit.qss')
        self.initUI()
        

    def initUI(self):
        # 设置无边框窗口
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 绑定最小化按钮事件
        self.minBtn.clicked.connect(self.showMinimized)
        # 绑定关闭按钮事件
        self.closeBtn.clicked.connect(self.close)
        # 载入字典
        self.loadDict('resource/dict/dict001.json')
        # 绑定搜索框事件
        self.searchLineEdit.textChanged.connect(self.updateListWidget)
        # 绑定编辑按钮事件
        self.addBtn.clicked.connect(self.popupEditWidget)
        # 绑定词条编辑事件、
        self.listWidget.itemDoubleClicked.connect(self.itemEdit)
        # 绑定编辑窗口确认按钮事件
        self.editUi.okBtn.clicked.connect(lambda: self.modifyDict(self.editUi.enEditLine.text(), self.editUi.cnEditLine.text()))
        # 绑定编辑窗口取消按钮事件
        self.editUi.cancelBtn.clicked.connect(self.popupEditWidget)

    '''Logic Func below'''

    

    def loadDict(self, dictPath):
        '''载入字典'''
        with open(dictPath, 'r', encoding="utf-8") as f:
            d = json.load(f)

        for key in d:
            self.ITEMS[key] = d[key]

        # 将字典中的单词添加到listWidget中
        for key,value in self.ITEMS.items():
            item = QListWidgetItem()
            item.setText("{0:<15}{1}".format(key, value))
            # item.setToolTip(i[1])
            self.listWidget.addItem(item)


    def updateListWidget(self, kw):
        '''更新listWidget'''
        self.listWidget.clear()

        if kw == '':
            for key, value in self.ITEMS.items():
                item = QListWidgetItem()
                item.setText("{0:<15}{1}".format(key, value))
                self.listWidget.addItem(item)
            return
        else:
            kw = kw.lower()
            sorted_items = sorted(self.ITEMS.items(), key=lambda item: max(
                difflib.SequenceMatcher(None, kw, item[0].lower()).quick_ratio(),
                difflib.SequenceMatcher(None, kw, item[1].lower()).quick_ratio()
            ), reverse=True)

            for key, value in sorted_items:
                ratio_1 = difflib.SequenceMatcher(None, kw, key.lower()).quick_ratio()
                ratio_2 = difflib.SequenceMatcher(None, kw, value.lower()).quick_ratio()
                if ratio_1 > 0.3 or ratio_2 > 0.3:
                    item = QListWidgetItem()
                    item.setText("{0:<15}{1}".format(key, value))
                    self.listWidget.addItem(item)


    def popupEditWidget(self):
        '''弹出编辑窗口'''
        self.editUi.enEditLine.setText('')
        self.editUi.cnEditLine.setText('')
        if self.editWidget.isHidden():
            self.editWidget.show()
        else:
            self.editWidget.hide()
            self.editUi.enEditLine.setText('')
            self.editUi.cnEditLine.setText('')

    def itemEdit(self):
        '''编辑词条'''
        if self.editWidget.isHidden():
            self.editUi.enEditLine.setText(self.listWidget.currentItem().text().split()[0])
            self.editUi.cnEditLine.setText(self.listWidget.currentItem().text().split()[1])
            self.editWidget.show()
        else:
            self.editWidget.hide()
            self.editUi.enEditLine.setText('')
            self.editUi.cnEditLine.setText('')

    def modifyDict(self, en, cn):
        '''修改字典'''
        if en == '' or cn == '':
            self.popupEditWidget()
            return
        else:
            self.ITEMS[en] = cn
            self.updateListWidget('')
            self.popupEditWidget()
