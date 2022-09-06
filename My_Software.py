from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_SoftwarePage2 import *

import numpy as np
import cv2
import dlib
import imutils
from imutils import face_utils

class SoftwarePageWindow(QWidget,Ui_SoftwarePage):
    returnSignal = pyqtSignal()
    def __init__(self,parent=None):
        super(SoftwarePageWindow, self).__init__(parent)
        self.timer_camera = QTimer() #初始化計時器
        self.cap = cv2.VideoCapture() #初始化Webcam
        self.CAM_NUM = 0
        self.setupUi(self)
        self.initUI()
        self.slot_init()

    def initUI(self):
        self.setLayout(self.gridLayout)

    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
            #信號和槽連接
        self.LoadBtn.clicked.connect(self.openSlot)
        self.FnBtn.clicked.connect(self.Face_reading)
        self.SaveBtn.clicked.connect(self.saveSlot)  
        self.cameraButton.clicked.connect(self.slotCameraButton)

    def openSlot(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if filename == '':
            return
        self.img = cv2.imread(filename, -1)
        if self.img.size == 1:
            return
        self.showImage()
        self.SaveBtn.setEnabled(True)

    def saveSlot(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save Image', 'Image', '*.png *.jpg *.bmp')
        if filename == '':
            return
        cv2.imwrite(filename, self.img)

    def showImage(self):
        self.img = cv2.resize(self.img,(800,600))
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.cameraLabel.setPixmap(QPixmap.fromImage(self.qImg))


    def Face_reading(self):  #臉部偵測
        gray = cv2.cvtColor(self.img , cv2.COLOR_BGR2GRAY)
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks_GTX.dat')
        
        # 偵測人臉
        face_rects = detector(self.img, 0)

        #以紅點標示人的五官
        for rect in face_rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            (x, y, w, h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            for (s0, s1) in shape:
                cv2.circle(self.img, (s0, s1), 1, (0, 0, 255), 2)

        # 取出所有偵測的結果
        for i, d in enumerate(face_rects):
            x1 = d.left()
            y1 = d.top()
            x2 = d.right()
            y2 = d.bottom()

        # 以方框標示偵測的人臉
            cv2.rectangle(self.img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)
        self.showImage()


    def show_camera(self):
        flag,img = self.cap.read()
        img = cv2.resize(img,(800,600))
        #face_reading
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks_GTX.dat')
        
        # 偵測人臉
        face_rects = detector(img, 0)

        #以紅點標示人的五官
        for rect in face_rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            (x, y, w, h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            for (s0, s1) in shape:
                cv2.circle(img, (s0, s1), 1, (0, 0, 255), 2)

        # 取出所有人臉偵測的結果
        for i, d in enumerate(face_rects):
            x1 = d.left()
            y1 = d.top()
            x2 = d.right()
            y2 = d.bottom()

        # 以方框標示偵測的人臉
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)

        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        showImage = QImage(self.img.data, self.img.shape[1],self.img.shape[0],QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))

    #打開關閉Webcam控制
    def slotCameraButton(self):
        if self.timer_camera.isActive() == False:
            #打開Webcam並顯示圖像資訊
           self.openCamera()
        else:
        #關閉Webcam並清空顯示資訊
            self.closeCamera()

    #打開Webcam
    def openCamera(self):
        flag = self.cap.open(self.CAM_NUM)
        if flag == False:
            msg = QMessageBox.Warning(self, u'Warning', u'請檢測Webcom與電腦是否連接正確',
            buttons=QMessageBox.Ok,
            defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30)
            self.cameraButton.setText('Close WebCam')

    #關閉Webcam
    def closeCamera(self):
        self.timer_camera.stop()
        self.cap.release()
        self.cameraLabel.clear()
        self.cameraButton.setText('WebCam')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SoftwarePageWindow()
    MainWindow.show()
    sys.exit(app.exec_())

