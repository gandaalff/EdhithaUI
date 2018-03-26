import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
import numpy as np
from PyQt5.QtGui import QImage,QPixmap,QMouseEvent
from ManualUI import Ui_MainWindow
from watcher import start_observe
import _thread
import os
import matplotlib.pylab as plt
import matplotlib.widgets as widgets
from PIL import Image
import target_ui as target_ui

PATH = "."
WRITE_PATH = "."
image_list = list()
Scale = 1000

targets = 0

class manual_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.count = -1
        self.ui.next.clicked.connect(self.image_lister_next)
        self.ui.previous.clicked.connect(self.image_lister_previous)
        self.ui.crop.clicked.connect(self.getTarget)

    def getTarget(self):
        print("start cropping")
        fig = plt.figure()
        fig.canvas.set_window_title('Select crop')
        ax = fig.add_subplot(111)
        filename = image_list[self.count]
        im = Image.open(filename)
        arr = np.asarray(im)
        plt_image = plt.imshow(arr)
        rs = widgets.RectangleSelector(ax, self.onselect, drawtype='box',rectprops=dict(facecolor='red', edgecolor='black', alpha=0.5, fill=True))
        plt.show()

    def onselect(self,eclick, erelease):
        if eclick.ydata > erelease.ydata:
            eclick.ydata, erelease.ydata = erelease.ydata, eclick.ydata
        if eclick.xdata > erelease.xdata:
            eclick.xdata, erelease.xdata = erelease.xdata, eclick.xdata
        print(str(eclick.xdata) + " " + str(eclick.ydata))
        print(str(erelease.xdata) + " " + str(erelease.ydata))

        im = Image.open(image_list[self.count])
        print(im.size)

        crop_rectangle = (eclick.xdata, eclick.ydata, erelease.xdata, erelease.ydata)
        cropped_im = im.crop(crop_rectangle)

        global targets
        crop_path = WRITE_PATH + "/target"+str(targets)+".png"
        cropped_im.save(crop_path)
        print("cropped")
        targets += 1

        self.saveData(crop_path,'target'+str(targets -1))

    def saveData(self,crop_path,targetno):
        self.targetWindow = target_ui.manual_ui()
        self.targetWindow.setPath(crop_path,WRITE_PATH,targetno)
        self.targetWindow.show()


    def image_lister_previous(self):
        try:
            self.count -= 1
            self.show_image(image_list[self.count])
            print("image number : ", self.count, "name : ", image_list[self.count])
        except:
            self.count = 0
            print("end of list ", self.count)
            self.show_image(image_list[self.count])

    def image_lister_next(self):
        try:
            self.count += 1
            #print("count  ",image_list[self.count])
            print("image number : ", self.count, "name : ", image_list[self.count])
            self.show_image(image_list[self.count])
        except:
            self.count = 0
            print("end of list ", self.count)
            self.show_image(image_list[self.count])


    def show_image(self,path):
        print("showing :",path)
        pixmap = QPixmap(path)
        pixmap = pixmap.scaledToWidth(Scale)

        self.ui.p10.setPixmap(pixmap)
        self.ui.total_images.setText("Total images = "+ str(len(image_list)))
        self.ui.total_targets.setText("Targets = "+str(targets))
        self.ui.lcurrent_image_no.setText("Current image = "+str(self.count))

if __name__ == '__main__':
    _thread.start_new_thread(start_observe,(PATH,))

    files = os.listdir(PATH)

    for file in files:
        if(file.split("."))[::-1][0] == "JPG":

            image_list.append(PATH + '/' + file)

    print (image_list)

    app = QApplication(sys.argv)
    window = manual_ui()
    window.show()
    sys.exit(app.exec_())

'''
    def paste_image(self,img):
        SCALE_FACTOR = 4
        HORIZONTAL_SLICES = 4
        VERTICAL_SLICES = 3
        
        resized = cv2.resize(img, (int(img.shape[1] / SCALE_FACTOR), int(img.shape[0] / SCALE_FACTOR)), interpolation=cv2.INTER_AREA)
        img = resized.copy()
       
        stepsw = int(img.shape[1]/HORIZONTAL_SLICES)
        w = [x for x in range(0,img.shape[1]+1,stepsw)]
        
        stepsh = int(img.shape[0] / VERTICAL_SLICES)
        h = [x for x in range(0, img.shape[0]+1, stepsh)]
    
        pixmap_c = list()

        for j in range(VERTICAL_SLICES):
            s = h[j]
            e = h[j+1]
            pixmap_r = list()
            for i in range(HORIZONTAL_SLICES):
                ima = img[s:e, w[i]:w[i+1]]
                image = ima.copy()
                height, width, channel = image.shape
                bytesPerLine = 3 * width
                qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QPixmap(qImg)
                pixmap_r.append(pixmap)
            #print(len(pixmap_r))
            pixmap_c.append(pixmap_r)

        self.ui.p00.setPixmap(pixmap_c[0][0])
        self.ui.p01.setPixmap(pixmap_c[0][1])
        self.ui.p02.setPixmap(pixmap_c[0][2])
        self.ui.p03.setPixmap(pixmap_c[0][3])

        self.ui.p10.setPixmap(pixmap_c[1][0])
        self.ui.p11.setPixmap(pixmap_c[1][1])
        self.ui.p12.setPixmap(pixmap_c[1][2])
        self.ui.p13.setPixmap(pixmap_c[1][3])

        self.ui.p20.setPixmap(pixmap_c[2][0])
        self.ui.p21.setPixmap(pixmap_c[2][1])
        self.ui.p22.setPixmap(pixmap_c[2][2])
        self.ui.p23.setPixmap(pixmap_c[2][3])
'''

