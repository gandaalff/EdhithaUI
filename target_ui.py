
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
from PyQt5.QtGui import QImage,QPixmap,QMouseEvent
import target as targetUI
import json

class manual_ui(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = targetUI.Ui_Target()
        self.ui.setupUi(self)

        self.ui.save.clicked.connect(self.getSaveData)

    def setPath(self,crop_path,WritePath,targetno):
        self.filename = targetno
        self.WRITEPATH = WritePath
        pixmap = QPixmap(crop_path)
        pixmap = pixmap.scaledToWidth(200)
        self.ui.label.setPixmap(pixmap)


    def getSaveData(self):
        prop = dict()
        prop["shape"] = self.ui.t1.text()
        prop["shapeColor"] = self.ui.t2.text()
        prop["character"] = self.ui.t3.text()
        prop["characterColor"] = self.ui.t4.text()
        prop["orientaion"] = self.ui.t5.text()
        prop["comment"] = self.ui.t6.text()

        with open(self.WRITEPATH+'/'+self.filename+'.txt','w') as f:
            json.dump(prop,f,ensure_ascii=False)


