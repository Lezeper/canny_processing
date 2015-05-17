# coding=utf8
 
import cv
import sys

from PyQt4 import QtGui
from PyQt4.QtCore import QObject, SIGNAL, QTimer
from test import Ui_imageGUI
import cv2


class Image(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_imageGUI()
        self.ui.setupUi(self)
        self.scene = QtGui.QGraphicsScene()
        self.ui.threadSlider.setValue(40)
        self.ui.weightSrc.setValue(100)

        QObject.connect(self.ui.openImageButton, SIGNAL("clicked()"), self.open_image_file)
        QObject.connect(self.ui.openVideoButton, SIGNAL("clicked()"), self.open_video_file)
        QObject.connect(self.ui.extractButton1, SIGNAL("clicked()"), self.exe_canny)
        QObject.connect(self.ui.saveAsImageButton, SIGNAL("clicked()"), self.saveAsFile)

        self.ui.threadSlider.valueChanged.connect(self.exe_canny)
        self.ui.weightSrc.valueChanged.connect(self.exe_canny)

        self.cap = cv2.VideoCapture()

    def open_video_file(self):
        self.filePath = QtGui.QFileDialog.getOpenFileName(self, self.tr("Open Image"), '',
                                               self.tr("Video Files (*.avi *.mp4 *.mpeg *.rmvb *.mpg *.flv)"))

        # if user didn't press the 'cancel' button, then do nothing
        if self.filePath:
            try:
                print self.filePath
            except Exception:
                QtGui.QMessageBox.warning(self, "warning!", "The Path can only contain English letters!")
                self.open_video_file()

            self._timer = QTimer(self)
            self._timer.timeout.connect(self.exe_canny)
            # Paint every 40 ms
            self._timer.start(40)

            self.ui.filePath.setText(self.filePath)
            self.cap = cv2.VideoCapture(str(self.filePath))

    def open_image_file(self):

        self.filePath = QtGui.QFileDialog.getOpenFileName(self, self.tr("Open Image"), '',
                                               self.tr("Image Files(*.png *.jpg *.bmp)"))

        # if user didn't press the 'cancel' button, then do nothing
        if self.filePath:

            if self.cap.isOpened():
                self._timer.stop()
                self.cap.release()

            try:
                    print self.filePath
            except Exception:
                QtGui.QMessageBox.warning(self, "warning!", "The Path can only contain English letters!")
                self.open_image_file()

            self.ui.filePath.setText(self.filePath)
            self.exe_canny()

    def saveAsFile(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save Image"), '',
                                                self.tr("Image Files(*.png *.jpg *.bmp)"))
        cv2.cvtColor(self.add, cv.CV_BGR2RGB, self.add)
        cv2.imwrite(str(fileName), self.add)

    def canny(self, img):
        canny = cv2.Canny(img, self.ui.threadSlider.value(), self.ui.threadSlider.value() * 0.4)
        return cv2.bitwise_not(canny)

    def exe_canny(self):

        if self.cap.isOpened():
            ret, img = self.cap.read()
        else:
            picPath = str(self.filePath)
            img = cv2.imread(picPath)

        img2 = img.copy()

        canny = self.canny(cv2.GaussianBlur(img2, (3, 3), 0))

        edges2 = img.copy()
        for i in (0, 1, 2):
            edges2[:, :, i] = canny
        # the weight of src and edge pic
        self.add = cv2.addWeighted(img, self.ui.weightSrc.value()/100.0, edges2,
                                   (100 - self.ui.weightSrc.value())/100.0, 0)

        cv2.imshow('frame', self.add)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Image()

    myapp.show()
    sys.exit(app.exec_())