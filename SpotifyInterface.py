import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from SpotifyViewer import SpotifyViewer
import threading
from datetime import datetime
import traceback, sys


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()


class Ui_SpotifyStreamer(object):
    def setupUi(self, SpotifyStreamer):
        self.running = False
        self.chrome = True
        self.firefox = False
        self.threadpool = QThreadPool()
        SpotifyStreamer.setObjectName("SpotifyStreamer")
        SpotifyStreamer.resize(600, 420)
        SpotifyStreamer.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(SpotifyStreamer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 80, 40)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setObjectName("username")
        

        self.horizontalLayout_2.addWidget(self.username)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)

        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QLineEdit.Password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.song_link = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.song_link.sizePolicy().hasHeightForWidth())
        self.song_link.setSizePolicy(sizePolicy)
        self.song_link.setObjectName("song_link")
        self.horizontalLayout_4.addWidget(self.song_link)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, 80, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout.addWidget(self.timeEdit)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.hoursToPlayForEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hoursToPlayForEdit.sizePolicy().hasHeightForWidth())
        self.hoursToPlayForEdit.setSizePolicy(sizePolicy)
        self.hoursToPlayForEdit.setObjectName("hours")
        self.hoursToPlayForEdit.setText("1")
        self.horizontalLayout_9.addWidget(self.hoursToPlayForEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        #region browser check boxes
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(250, 0, 0, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.chrome_RdBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.chrome_RdBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chrome_RdBtn.setObjectName("chrome_RdBtn")
        self.chrome_RdBtn.setChecked(True)
        self.chrome_RdBtn.clicked.connect(self.browser_selection)
        self.horizontalLayout_10.addWidget(self.chrome_RdBtn)

        self.firefox_RdBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.firefox_RdBtn.setSizePolicy(sizePolicy)

        self.firefox_RdBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.firefox_RdBtn.clicked.connect(self.browser_selection)
        self.horizontalLayout_10.addWidget(self.firefox_RdBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        #endregion browser check boxes

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(200, 80, 100, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start_stream)
        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.stop_stream)
        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        SpotifyStreamer.setCentralWidget(self.centralwidget)
        self.actionClose = QtWidgets.QAction(SpotifyStreamer)
        self.actionClose.setObjectName("actionClose")

        self.timeCheck = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeCheck.sizePolicy().hasHeightForWidth())
        self.timeCheck.setSizePolicy(sizePolicy)
        self.timeCheck.setObjectName("timeCheck")
        self.verticalLayout_2.addWidget(self.timeCheck)

        self.retranslateUi(SpotifyStreamer)
        QtCore.QMetaObject.connectSlotsByName(SpotifyStreamer)
        self.pushButton_2.setDisabled(True)
        self.pushButton.setDisabled(False)
        self.timeCheck.setChecked(True)

    def browser_selection(self):
        if self.chrome_RdBtn.isChecked():
            self.chrome = True
        else:
            self.chrome = False

        if self.firefox_RdBtn.isChecked():
            self.firefox = True
        else:
            self.firefox = False
    def start_stream(self):
        if not self.running:
            self.running = True
            self.pushButton_2.setDisabled(False)
            self.pushButton.setDisabled(True)
            worker = Worker(self.run_viewer)  # Any other args, kwargs are passed to the run function
            self.threadpool.start(worker)

    def get_seconds_to_wait_for(self):
        date = datetime.strptime(self.timeEdit.text(), "%I:%M %p")
        start_time = date.time().strftime('%H:%M:%S')
        end_time = datetime.now().time().strftime('%H:%M:%S')
        total_time = (datetime.strptime(end_time, '%H:%M:%S') - datetime.strptime(start_time, '%H:%M:%S'))
        total_time_in_sec = str(total_time).split(":")
        total_time_in_sec = int(total_time_in_sec[0])*60*60 + int(total_time_in_sec[1])*60 + int(total_time_in_sec[2])
        print("Wait in Hours: {0}".format(str(int(total_time_in_sec)/(60*60))))
        return total_time_in_sec

    def run_viewer(self, progress_callback):
        import time
        if not self.timeCheck.isChecked():
            time.sleep(self.get_seconds_to_wait_for())
        self.streamer = SpotifyViewer(self.username.text(), self.password.text(),
                                      self.song_link.text(), float(self.hoursToPlayForEdit.text()), self.chrome, self.firefox)
        self.streamer.run_viewer()
        return True

    def stop_stream(self):
        if self.running:
            self.running = False
            self.streamer.stop_stream()
            self.pushButton.setDisabled(False)
            self.pushButton_2.setDisabled(True)

    def retranslateUi(self, SpotifyStreamer):
        _translate = QtCore.QCoreApplication.translate
        SpotifyStreamer.setWindowTitle(_translate("SpotifyStreamer", "MainWindow"))
        self.label_2.setText(_translate("SpotifyStreamer", "Spotify Email/Username:"))
        self.label_3.setText(_translate("SpotifyStreamer", "Password:"))
        self.label_4.setText(_translate("SpotifyStreamer", "Song/Artist/Playlist Link:"))
        self.label.setText(_translate("SpotifyStreamer", "Time at which song is played"))
        self.label_5.setText(_translate("SpotifyStreamer", "For how long (hours):"))
        self.pushButton.setText(_translate("SpotifyStreamer", "Start "))
        self.pushButton_2.setText(_translate("SpotifyStreamer", "Stop "))
        self.timeCheck.setText(_translate("SpotifyStreamer", "Play Immediately! "))
        self.actionClose.setText(_translate("SpotifyStreamer", "Close"))
        self.chrome_RdBtn.setText(_translate("SpotifyStreamer", "Chrome"))
        self.firefox_RdBtn.setText(_translate("SpotifyStreamer", "Firefox"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_SpotifyStreamer()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

"""
secan.akbulut@gmail.com
Hasosecan123
"""