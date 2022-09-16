
from email.mime import image
from signal import Signals
import sys
import pandas as pd

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal
  
import datetime
import cv2
import time
import os
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from keras.models import load_model

import pandas as pd
import cv2
import numpy as np
import time
from model import model_pred
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
# class Get_Pred():
#     def __init__(self):
#         self.image_path=' '
#     def pred(self):
#         mod=load_model("classification_model_VGG16.h5")
#         test_data=pd.DataFrame([[self.image_path,'None']],columns=['path','label'])
#         Fseries = pd.Series(test_data.path, name="filepaths")
#         Lseries = pd.Series(test_data.label, name="labels")
#         data = pd.concat([Fseries,Lseries], axis=1)
#         df = pd.DataFrame(data)
#         image_gen = ImageDataGenerator(preprocessing_function= tf.keras.applications.mobilenet_v2.preprocess_input)
#         test = image_gen.flow_from_dataframe(dataframe= df,x_col="filepaths", y_col="labels",
#                                          class_mode='categorical',batch_size=6,shuffle= False)
#         mod.evaluate(test, verbose=1)
#         pred = mod.predict(test)
#         pred = np.argmax(pred, axis=1)
        
#         print('predddd',pred)
#         return str(pred[0])
# def get_text(pred_num):
#     if int(pred_num)==0:
#         return 'normal driving'
#     if int(pred_num)==1:
#         return 'texting - right'
#     if int(pred_num)==2:
#         return 'talking on the phone - right'
#     if int(pred_num)==3:
#         return 'texting - left'
#     if int(pred_num)==4:
#         return 'talking on the phone - left'
#     if int(pred_num)==5:
#         return 'operating the radio'
#     if int(pred_num)==6:
#         return 'drinking'
#     if int(pred_num)==7:
#         return 'reaching behind'
#     if int(pred_num)==8:
#         return 'hair and makeup'
#     if int(pred_num)==9:
#         return 'talking to passenger'

    
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    global img
    def run(self):
        cap = cv2.VideoCapture('C:\\Users\\omerf\\OneDrive\\Desktop\\Staj çalışmalarım\Ömer\\Driver state\\driver_test_video.mp4')#****************152******************
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # out = cv2.VideoWriter('D:\\omar\\plaka\\output.mp4', fourcc, 20.0, (2688,1520))
        # cap = cv2.VideoCapture(0)#****************152******************
        
        # cap = cv2.VideoCapture('videoplayback.mp4')
        while True:
            ret, frame = cap.read()
            if ret:
                # out.write(frame) 
                
                
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                resized = cv2.resize(frame, (640,480))
                self.img=resized
                self.changePixmap.emit(p)
                # cv2.waitKey(10)
                # cv2.waitKey(25)#for video
        #     else:
        #         break
        # out.release()
e = datetime.datetime.now()
timee=str(e.day)+'/'+ str(e.month)+'/'+ str(e.year) +'  '+str(e.hour) +':'+ str(e.minute) +':'+ str(e.second)
class App(QMainWindow):
    global save_con
    save_con=False
    def __init__(self):
        super().__init__()
        self.title = 'Koluman Plaka Tespit'
        self.text='***Demo***'
        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 200
        
        # self.setCentralWidget(self.table)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel(self)
        self.label.move(280, 120)
        self.label.resize(640, 480)
        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.start()
        # Create textbox
        # self.textbox = QLineEdit(self.text,self)
        # self.textbox.move(20, 20)
        # self.textbox.resize(280,40)
        # self.text='Koluman Plaka Tanıma Sistemi'
        self.textbox = QLineEdit(self.text,self)
        self.textbox.move(550, 600)
        self.textbox.resize(280,40)
        f = self.textbox.font()
        f.setPointSize(14) # sets the size to 27
        self.textbox.setFont(f)
        
        

       


        self.button = QPushButton('Run', self)
        self.button.move(350,600)
        f3=self.button.font()
        f3.setPointSize(14) # sets the size to 27
        self.button.setFont(f3)
        self.button.resize(175,50)
        self.button.clicked.connect(self.on_click_save)
        
        
        self.show()
        
    

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
        

    @pyqtSlot()
    def on_click_save(self):
        e = datetime.datetime.now()
        timee=str(e.day)+'+'+ str(e.month)+'+'+ str(e.year) +'  '+str(e.hour) +'+'+ str(e.minute) +'+'+ str(e.second)
        
        original_image_path=f'C:\\Users\\omerf\\OneDrive\\Desktop\\Staj çalışmalarım\\Ömer\\Driver state\\kamera_foto\\image_.png'
        self.th.changePixmap.disconnect(self.setImage)
        cv2.imwrite(original_image_path,self.th.img)
        
        
        state=model_pred()
        print(state)
        # # plate='BOF_Tesla'#AI output
        # print('saasadsasad')
        self.textbox.setText(state)
        # print('saasadsasad')
        self.th.changePixmap.connect(self.setImage)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())