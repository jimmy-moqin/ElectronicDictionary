# import os

# uipath = os.path.dirname(os.path.abspath(__file__)) + '/ui/'
# os.system("pyuic5 \"" + uipath + "ElecDictUI.ui\" --import-from=resource.qrc -o \""+ uipath +"ElecDictUI.py\"")
# os.system("pyuic5 \"" + uipath + "editUI.ui\" --import-from=resource.qrc -o \""+ uipath +"editUI.py\"")
# resousepath = os.path.dirname(os.path.abspath(__file__)) + '/resource/qrc/'
# os.system("pyrcc5 \"" + resousepath + "ElecDict.qrc\" -o \""+ resousepath +"ElecDict_rc.py\"")
from PyQt5.QtWidgets import QApplication

from src.elecdict import ElecDict

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Ui_ElecDict=ElecDict()
    Ui_ElecDict.show()
    sys.exit(app.exec_())
