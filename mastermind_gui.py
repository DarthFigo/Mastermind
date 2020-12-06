from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from random import randint
from os import execv


class Mastermind(QtCore.QThread):
    def __init__(self):
        super().__init__()
        self.colours = ["cyan", "orange", "purple", "red", "blue", "green"]
        self.code = []
        self.game_started = False

        self.turn = 0
        self.guess0 = ""
        self.guess1 = ""
        self.guess2 = ""
        self.guess3 = ""

    def create_code(self):
        for i in range(4):
            self.code.append(self.colours[int(randint(0, 5))])

    def start_game(self):
        self.game_started = True
        self.create_code()

    def evaluate(self):
        self.turn += 1

        guesses = [self.guess0, self.guess1, self.guess2, self.guess3]
        peg_counter = []

        for i in range(4):
            if guesses[i] == self.code[i]:
                peg_counter.append("black")
            elif guesses[i] in self.code:
                peg_counter.append("white")
            else:
                peg_counter.append("empty")

        return peg_counter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, counter):
        self.counter = counter

        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle("Message")
        self.msgBox.setStandardButtons(QMessageBox.Ok)

        MainWindow.resize(744, 1346)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.labelBoard = QtWidgets.QLabel(self.centralwidget)
        self.labelBoard.setGeometry(QtCore.QRect(10, -50, 501, 1381))
        self.labelBoard.setText("")
        self.labelBoard.setPixmap(QtGui.QPixmap("pictures/board.png"))
        self.labelBoard.setObjectName("labelBoard")

        self.buttonBall01 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall01.setGeometry(QtCore.QRect(250, 1030, 50, 70))
        self.buttonBall01.setStyleSheet("background: Transparent;")
        self.buttonBall01.setText("")
        self.buttonBall01.setObjectName("buttonBall01")
        self.buttonBall01.clicked.connect(lambda: self.ball_button_pressed("01"))
        self.buttonBall02 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall02.setGeometry(QtCore.QRect(310, 1030, 51, 70))
        self.buttonBall02.setStyleSheet("background: Transparent;")
        self.buttonBall02.setText("")
        self.buttonBall02.setObjectName("buttonBall02")
        self.buttonBall02.clicked.connect(lambda: self.ball_button_pressed("02"))
        self.buttonBall00 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall00.setGeometry(QtCore.QRect(190, 1030, 51, 70))
        self.buttonBall00.setStyleSheet("background: Transparent;")
        self.buttonBall00.setText("")
        self.buttonBall00.setObjectName("buttonBall00")
        self.buttonBall00.clicked.connect(lambda: self.ball_button_pressed("00"))
        self.buttonBall03 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall03.setGeometry(QtCore.QRect(380, 1030, 51, 70))
        self.buttonBall03.setStyleSheet("background: Transparent;")
        self.buttonBall03.setText("")
        self.buttonBall03.setObjectName("buttonBall03")
        self.buttonBall03.clicked.connect(lambda: self.ball_button_pressed("03"))
        self.buttonBall13 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall13.setGeometry(QtCore.QRect(380, 940, 51, 61))
        self.buttonBall13.setStyleSheet("background: Transparent;")
        self.buttonBall13.setText("")
        self.buttonBall13.setObjectName("buttonBall13")
        self.buttonBall13.clicked.connect(lambda: self.ball_button_pressed("13"))
        self.buttonBall23 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall23.setGeometry(QtCore.QRect(380, 840, 51, 70))
        self.buttonBall23.setStyleSheet("background: Transparent;")
        self.buttonBall23.setText("")
        self.buttonBall23.setObjectName("buttonBall23")
        self.buttonBall23.clicked.connect(lambda: self.ball_button_pressed("23"))
        self.buttonBall33 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall33.setGeometry(QtCore.QRect(380, 750, 51, 70))
        self.buttonBall33.setStyleSheet("background: Transparent;")
        self.buttonBall33.setText("")
        self.buttonBall33.setObjectName("buttonBall33")
        self.buttonBall33.clicked.connect(lambda: self.ball_button_pressed("33"))
        self.buttonBall43 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall43.setGeometry(QtCore.QRect(380, 650, 51, 70))
        self.buttonBall43.setStyleSheet("background: Transparent;")
        self.buttonBall43.setText("")
        self.buttonBall43.setObjectName("buttonBall43")
        self.buttonBall43.clicked.connect(lambda: self.ball_button_pressed("43"))
        self.buttonBall53 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall53.setGeometry(QtCore.QRect(380, 560, 51, 70))
        self.buttonBall53.setStyleSheet("background: Transparent;")
        self.buttonBall53.setText("")
        self.buttonBall53.setObjectName("buttonBall53")
        self.buttonBall53.clicked.connect(lambda: self.ball_button_pressed("53"))
        self.buttonBall63 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall63.setGeometry(QtCore.QRect(380, 460, 51, 70))
        self.buttonBall63.setStyleSheet("background: Transparent;")
        self.buttonBall63.setText("")
        self.buttonBall63.setObjectName("buttonBall63")
        self.buttonBall63.clicked.connect(lambda: self.ball_button_pressed("63"))
        self.buttonBall73 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall73.setGeometry(QtCore.QRect(380, 370, 51, 70))
        self.buttonBall73.setStyleSheet("background: Transparent;")
        self.buttonBall73.setText("")
        self.buttonBall73.setObjectName("buttonBall73")
        self.buttonBall73.clicked.connect(lambda: self.ball_button_pressed("73"))
        self.buttonBall83 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall83.setGeometry(QtCore.QRect(380, 280, 51, 70))
        self.buttonBall83.setStyleSheet("background: Transparent;")
        self.buttonBall83.setText("")
        self.buttonBall83.setObjectName("buttonBall83")
        self.buttonBall83.clicked.connect(lambda: self.ball_button_pressed("83"))
        self.buttonBall93 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall93.setGeometry(QtCore.QRect(380, 180, 51, 70))
        self.buttonBall93.setStyleSheet("background: Transparent;")
        self.buttonBall93.setText("")
        self.buttonBall93.setObjectName("buttonBall93")
        self.buttonBall93.clicked.connect(lambda: self.ball_button_pressed("93"))
        self.buttonBall10 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall10.setGeometry(QtCore.QRect(190, 930, 51, 70))
        self.buttonBall10.setStyleSheet("background: Transparent;")
        self.buttonBall10.setText("")
        self.buttonBall10.setObjectName("buttonBall10")
        self.buttonBall10.clicked.connect(lambda: self.ball_button_pressed("10"))
        self.buttonBall11 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall11.setGeometry(QtCore.QRect(250, 940, 51, 70))
        self.buttonBall11.setStyleSheet("background: Transparent;")
        self.buttonBall11.setText("")
        self.buttonBall11.setObjectName("buttonBall11")
        self.buttonBall11.clicked.connect(lambda: self.ball_button_pressed("11"))
        self.buttonBall12 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall12.setGeometry(QtCore.QRect(310, 940, 51, 70))
        self.buttonBall12.setStyleSheet("background: Transparent;")
        self.buttonBall12.setText("")
        self.buttonBall12.setObjectName("buttonBall12")
        self.buttonBall12.clicked.connect(lambda: self.ball_button_pressed("12"))
        self.buttonBall20 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall20.setGeometry(QtCore.QRect(190, 840, 51, 70))
        self.buttonBall20.setStyleSheet("background: Transparent;")
        self.buttonBall20.setText("")
        self.buttonBall20.setObjectName("buttonBall20")
        self.buttonBall20.clicked.connect(lambda: self.ball_button_pressed("20"))
        self.buttonBall21 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall21.setGeometry(QtCore.QRect(250, 840, 51, 70))
        self.buttonBall21.setStyleSheet("background: Transparent;")
        self.buttonBall21.setText("")
        self.buttonBall21.setObjectName("buttonBall21")
        self.buttonBall21.clicked.connect(lambda: self.ball_button_pressed("21"))
        self.buttonBall22 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall22.setGeometry(QtCore.QRect(310, 840, 61, 70))
        self.buttonBall22.setStyleSheet("background: Transparent;")
        self.buttonBall22.setText("")
        self.buttonBall22.setObjectName("buttonBall22")
        self.buttonBall22.clicked.connect(lambda: self.ball_button_pressed("22"))
        self.buttonBall30 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall30.setGeometry(QtCore.QRect(190, 750, 51, 70))
        self.buttonBall30.setStyleSheet("background: Transparent;")
        self.buttonBall30.setText("")
        self.buttonBall30.setObjectName("buttonBall30")
        self.buttonBall30.clicked.connect(lambda: self.ball_button_pressed("30"))
        self.buttonBall31 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall31.setGeometry(QtCore.QRect(250, 750, 51, 70))
        self.buttonBall31.setStyleSheet("background: Transparent;")
        self.buttonBall31.setText("")
        self.buttonBall31.setObjectName("buttonBall31")
        self.buttonBall31.clicked.connect(lambda: self.ball_button_pressed("31"))
        self.buttonBall32 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall32.setGeometry(QtCore.QRect(310, 750, 61, 70))
        self.buttonBall32.setStyleSheet("background: Transparent;")
        self.buttonBall32.setText("")
        self.buttonBall32.setObjectName("buttonBall32")
        self.buttonBall32.clicked.connect(lambda: self.ball_button_pressed("32"))
        self.buttonBall40 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall40.setGeometry(QtCore.QRect(190, 650, 51, 70))
        self.buttonBall40.setStyleSheet("background: Transparent;")
        self.buttonBall40.setText("")
        self.buttonBall40.setObjectName("buttonBall40")
        self.buttonBall40.clicked.connect(lambda: self.ball_button_pressed("40"))
        self.buttonBall41 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall41.setGeometry(QtCore.QRect(250, 650, 51, 70))
        self.buttonBall41.setStyleSheet("background: Transparent;")
        self.buttonBall41.setText("")
        self.buttonBall41.setObjectName("buttonBall41")
        self.buttonBall41.clicked.connect(lambda: self.ball_button_pressed("41"))
        self.buttonBall42 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall42.setGeometry(QtCore.QRect(310, 650, 61, 70))
        self.buttonBall42.setStyleSheet("background: Transparent;")
        self.buttonBall42.setText("")
        self.buttonBall42.setObjectName("buttonBall42")
        self.buttonBall42.clicked.connect(lambda: self.ball_button_pressed("42"))
        self.buttonBall50 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall50.setGeometry(QtCore.QRect(190, 560, 51, 70))
        self.buttonBall50.setStyleSheet("background: Transparent;")
        self.buttonBall50.setText("")
        self.buttonBall50.setObjectName("buttonBall50")
        self.buttonBall50.clicked.connect(lambda: self.ball_button_pressed("50"))
        self.buttonBall51 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall51.setGeometry(QtCore.QRect(250, 560, 51, 70))
        self.buttonBall51.setStyleSheet("background: Transparent;")
        self.buttonBall51.setText("")
        self.buttonBall51.setObjectName("buttonBall51")
        self.buttonBall51.clicked.connect(lambda: self.ball_button_pressed("51"))
        self.buttonBall52 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall52.setGeometry(QtCore.QRect(310, 560, 61, 70))
        self.buttonBall52.setStyleSheet("background: Transparent;")
        self.buttonBall52.setText("")
        self.buttonBall52.setObjectName("buttonBall52")
        self.buttonBall52.clicked.connect(lambda: self.ball_button_pressed("52"))
        self.buttonBall60 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall60.setGeometry(QtCore.QRect(190, 460, 51, 70))
        self.buttonBall60.setStyleSheet("background: Transparent;")
        self.buttonBall60.setText("")
        self.buttonBall60.setObjectName("buttonBall60")
        self.buttonBall60.clicked.connect(lambda: self.ball_button_pressed("60"))
        self.buttonBall61 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall61.setGeometry(QtCore.QRect(250, 460, 51, 70))
        self.buttonBall61.setStyleSheet("background: Transparent;")
        self.buttonBall61.setText("")
        self.buttonBall61.setObjectName("buttonBall61")
        self.buttonBall61.clicked.connect(lambda: self.ball_button_pressed("61"))
        self.buttonBall62 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall62.setGeometry(QtCore.QRect(310, 460, 61, 70))
        self.buttonBall62.setStyleSheet("background: Transparent;")
        self.buttonBall62.setText("")
        self.buttonBall62.setObjectName("buttonBall62")
        self.buttonBall62.clicked.connect(lambda: self.ball_button_pressed("62"))
        self.buttonBall70 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall70.setGeometry(QtCore.QRect(190, 370, 51, 70))
        self.buttonBall70.setStyleSheet("background: Transparent;")
        self.buttonBall70.setText("")
        self.buttonBall70.setObjectName("buttonBall70")
        self.buttonBall70.clicked.connect(lambda: self.ball_button_pressed("70"))
        self.buttonBall71 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall71.setGeometry(QtCore.QRect(250, 370, 51, 70))
        self.buttonBall71.setStyleSheet("background: Transparent;")
        self.buttonBall71.setText("")
        self.buttonBall71.setObjectName("buttonBall71")
        self.buttonBall71.clicked.connect(lambda: self.ball_button_pressed("71"))
        self.buttonBall72 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall72.setGeometry(QtCore.QRect(310, 370, 61, 70))
        self.buttonBall72.setStyleSheet("background: Transparent;")
        self.buttonBall72.setText("")
        self.buttonBall72.setObjectName("buttonBall72")
        self.buttonBall72.clicked.connect(lambda: self.ball_button_pressed("72"))
        self.buttonBall80 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall80.setGeometry(QtCore.QRect(190, 270, 51, 70))
        self.buttonBall80.setStyleSheet("background: Transparent;")
        self.buttonBall80.setText("")
        self.buttonBall80.setObjectName("buttonBall80")
        self.buttonBall80.clicked.connect(lambda: self.ball_button_pressed("80"))
        self.buttonBall81 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall81.setGeometry(QtCore.QRect(250, 270, 51, 70))
        self.buttonBall81.setStyleSheet("background: Transparent;")
        self.buttonBall81.setText("")
        self.buttonBall81.setObjectName("buttonBall81")
        self.buttonBall81.clicked.connect(lambda: self.ball_button_pressed("81"))
        self.buttonBall82 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall82.setGeometry(QtCore.QRect(310, 270, 61, 70))
        self.buttonBall82.setStyleSheet("background: Transparent;")
        self.buttonBall82.setText("")
        self.buttonBall82.setObjectName("buttonBall82")
        self.buttonBall82.clicked.connect(lambda: self.ball_button_pressed("82"))
        self.buttonBall90 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall90.setGeometry(QtCore.QRect(190, 180, 51, 70))
        self.buttonBall90.setStyleSheet("background: Transparent;")
        self.buttonBall90.setText("")
        self.buttonBall90.setObjectName("buttonBall90")
        self.buttonBall90.clicked.connect(lambda: self.ball_button_pressed("90"))
        self.buttonBall91 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall91.setGeometry(QtCore.QRect(250, 180, 51, 70))
        self.buttonBall91.setStyleSheet("background: Transparent;")
        self.buttonBall91.setText("")
        self.buttonBall91.setObjectName("buttonBall91")
        self.buttonBall91.clicked.connect(lambda: self.ball_button_pressed("91"))
        self.buttonBall92 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBall92.setGeometry(QtCore.QRect(310, 180, 61, 70))
        self.buttonBall92.setStyleSheet("background: Transparent;")
        self.buttonBall92.setText("")
        self.buttonBall92.setObjectName("buttonBall92")
        self.buttonBall92.clicked.connect(lambda: self.ball_button_pressed("92"))

        self.buttonEvaluate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEvaluate.setGeometry(QtCore.QRect(520, 600, 181, 121))
        self.buttonEvaluate.setText("Start Game")
        self.buttonEvaluate.clicked.connect(lambda: self.evaluate())

        self.labelPeg00 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg00.setGeometry(QtCore.QRect(130, 1060, 30, 30))
        self.labelPeg00.setText("")
        self.labelPeg00.setScaledContents(True)
        self.labelPeg00.setObjectName("labelPeg00")
        self.labelPeg01 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg01.setGeometry(QtCore.QRect(130, 1030, 30, 30))
        self.labelPeg01.setText("")
        self.labelPeg01.setScaledContents(True)
        self.labelPeg01.setObjectName("labelPeg01")
        self.labelPeg02 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg02.setGeometry(QtCore.QRect(100, 1060, 30, 30))
        self.labelPeg02.setText("")
        self.labelPeg02.setScaledContents(True)
        self.labelPeg02.setObjectName("labelPeg02")
        self.labelPeg03 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg03.setGeometry(QtCore.QRect(100, 1030, 30, 30))
        self.labelPeg03.setText("")
        self.labelPeg03.setScaledContents(True)
        self.labelPeg03.setObjectName("labelPeg03")
        self.labelPeg10 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg10.setGeometry(QtCore.QRect(130, 970, 30, 30))
        self.labelPeg10.setText("")
        self.labelPeg10.setScaledContents(True)
        self.labelPeg10.setObjectName("labelPeg10")
        self.labelPeg11 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg11.setGeometry(QtCore.QRect(130, 940, 30, 30))
        self.labelPeg11.setText("")
        self.labelPeg11.setScaledContents(True)
        self.labelPeg11.setObjectName("labelPeg11")
        self.labelPeg13 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg13.setGeometry(QtCore.QRect(100, 940, 30, 30))
        self.labelPeg13.setText("")
        self.labelPeg13.setScaledContents(True)
        self.labelPeg13.setObjectName("labelPeg13")
        self.labelPeg12 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg12.setGeometry(QtCore.QRect(100, 970, 30, 30))
        self.labelPeg12.setText("")
        self.labelPeg12.setScaledContents(True)
        self.labelPeg12.setObjectName("labelPeg12")
        self.labelPeg21 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg21.setGeometry(QtCore.QRect(130, 850, 30, 30))
        self.labelPeg21.setText("")
        self.labelPeg21.setScaledContents(True)
        self.labelPeg21.setObjectName("labelPeg21")
        self.labelPeg23 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg23.setGeometry(QtCore.QRect(100, 850, 30, 30))
        self.labelPeg23.setText("")
        self.labelPeg23.setScaledContents(True)
        self.labelPeg23.setObjectName("labelPeg23")
        self.labelPeg20 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg20.setGeometry(QtCore.QRect(130, 880, 30, 30))
        self.labelPeg20.setText("")
        self.labelPeg20.setScaledContents(True)
        self.labelPeg20.setObjectName("labelPeg20")
        self.labelPeg22 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg22.setGeometry(QtCore.QRect(100, 880, 30, 30))
        self.labelPeg22.setText("")
        self.labelPeg22.setScaledContents(True)
        self.labelPeg22.setObjectName("labelPeg22")
        self.labelPeg31 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg31.setGeometry(QtCore.QRect(130, 750, 30, 30))
        self.labelPeg31.setText("")
        self.labelPeg31.setScaledContents(True)
        self.labelPeg31.setObjectName("labelPeg31")
        self.labelPeg33 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg33.setGeometry(QtCore.QRect(100, 750, 30, 30))
        self.labelPeg33.setText("")
        self.labelPeg33.setScaledContents(True)
        self.labelPeg33.setObjectName("labelPeg33")
        self.labelPeg30 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg30.setGeometry(QtCore.QRect(130, 780, 30, 30))
        self.labelPeg30.setText("")
        self.labelPeg30.setScaledContents(True)
        self.labelPeg30.setObjectName("labelPeg30")
        self.labelPeg32 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg32.setGeometry(QtCore.QRect(100, 780, 30, 30))
        self.labelPeg32.setText("")
        self.labelPeg32.setScaledContents(True)
        self.labelPeg32.setObjectName("labelPeg32")
        self.labelPeg41 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg41.setGeometry(QtCore.QRect(130, 650, 30, 30))
        self.labelPeg41.setText("")
        self.labelPeg41.setScaledContents(True)
        self.labelPeg41.setObjectName("labelPeg41")
        self.labelPeg43 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg43.setGeometry(QtCore.QRect(100, 650, 30, 30))
        self.labelPeg43.setText("")
        self.labelPeg43.setScaledContents(True)
        self.labelPeg43.setObjectName("labelPeg43")
        self.labelPeg40 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg40.setGeometry(QtCore.QRect(130, 680, 30, 30))
        self.labelPeg40.setText("")
        self.labelPeg40.setScaledContents(True)
        self.labelPeg40.setObjectName("labelPeg40")
        self.labelPeg42 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg42.setGeometry(QtCore.QRect(100, 680, 30, 30))
        self.labelPeg42.setText("")
        self.labelPeg42.setScaledContents(True)
        self.labelPeg42.setObjectName("labelPeg42")
        self.labelPeg51 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg51.setGeometry(QtCore.QRect(130, 560, 30, 30))
        self.labelPeg51.setText("")
        self.labelPeg51.setScaledContents(True)
        self.labelPeg51.setObjectName("labelPeg51")
        self.labelPeg53 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg53.setGeometry(QtCore.QRect(100, 560, 30, 30))
        self.labelPeg53.setText("")
        self.labelPeg53.setScaledContents(True)
        self.labelPeg53.setObjectName("labelPeg53")
        self.labelPeg50 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg50.setGeometry(QtCore.QRect(130, 590, 30, 30))
        self.labelPeg50.setText("")
        self.labelPeg50.setScaledContents(True)
        self.labelPeg50.setObjectName("labelPeg50")
        self.labelPeg52 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg52.setGeometry(QtCore.QRect(100, 590, 30, 30))
        self.labelPeg52.setText("")
        self.labelPeg52.setScaledContents(True)
        self.labelPeg52.setObjectName("labelPeg52")
        self.labelPeg61 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg61.setGeometry(QtCore.QRect(130, 460, 30, 30))
        self.labelPeg61.setText("")
        self.labelPeg61.setScaledContents(True)
        self.labelPeg61.setObjectName("labelPeg61")
        self.labelPeg63 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg63.setGeometry(QtCore.QRect(100, 460, 30, 30))
        self.labelPeg63.setText("")
        self.labelPeg63.setScaledContents(True)
        self.labelPeg63.setObjectName("labelPeg63")
        self.labelPeg60 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg60.setGeometry(QtCore.QRect(130, 490, 30, 30))
        self.labelPeg60.setText("")
        self.labelPeg60.setScaledContents(True)
        self.labelPeg60.setObjectName("labelPeg60")
        self.labelPeg62 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg62.setGeometry(QtCore.QRect(100, 490, 30, 30))
        self.labelPeg62.setText("")
        self.labelPeg62.setScaledContents(True)
        self.labelPeg62.setObjectName("labelPeg62")
        self.labelPeg71 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg71.setGeometry(QtCore.QRect(130, 370, 30, 30))
        self.labelPeg71.setText("")
        self.labelPeg71.setScaledContents(True)
        self.labelPeg71.setObjectName("labelPeg71")
        self.labelPeg73 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg73.setGeometry(QtCore.QRect(100, 370, 30, 30))
        self.labelPeg73.setText("")
        self.labelPeg73.setScaledContents(True)
        self.labelPeg73.setObjectName("labelPeg73")
        self.labelPeg70 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg70.setGeometry(QtCore.QRect(130, 400, 30, 30))
        self.labelPeg70.setText("")
        self.labelPeg70.setScaledContents(True)
        self.labelPeg70.setObjectName("labelPeg70")
        self.labelPeg72 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg72.setGeometry(QtCore.QRect(100, 400, 30, 30))
        self.labelPeg72.setText("")
        self.labelPeg72.setScaledContents(True)
        self.labelPeg72.setObjectName("labelPeg72")
        self.labelPeg81 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg81.setGeometry(QtCore.QRect(130, 270, 30, 30))
        self.labelPeg81.setText("")
        self.labelPeg81.setScaledContents(True)
        self.labelPeg81.setObjectName("labelPeg81")
        self.labelPeg83 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg83.setGeometry(QtCore.QRect(100, 270, 30, 30))
        self.labelPeg83.setText("")
        self.labelPeg83.setScaledContents(True)
        self.labelPeg83.setObjectName("labelPeg83")
        self.labelPeg80 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg80.setGeometry(QtCore.QRect(130, 300, 30, 30))
        self.labelPeg80.setText("")
        self.labelPeg80.setScaledContents(True)
        self.labelPeg80.setObjectName("labelPeg80")
        self.labelPeg82 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg82.setGeometry(QtCore.QRect(100, 300, 30, 30))
        self.labelPeg82.setText("")
        self.labelPeg82.setScaledContents(True)
        self.labelPeg82.setObjectName("labelPeg82")
        self.labelPeg91 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg91.setGeometry(QtCore.QRect(130, 180, 30, 30))
        self.labelPeg91.setText("")
        self.labelPeg91.setScaledContents(True)
        self.labelPeg91.setObjectName("labelPeg91")
        self.labelPeg93 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg93.setGeometry(QtCore.QRect(100, 180, 30, 30))
        self.labelPeg93.setText("")
        self.labelPeg93.setScaledContents(True)
        self.labelPeg93.setObjectName("labelPeg93")
        self.labelPeg90 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg90.setGeometry(QtCore.QRect(130, 210, 30, 30))
        self.labelPeg90.setText("")
        self.labelPeg90.setScaledContents(True)
        self.labelPeg90.setObjectName("labelPeg90")
        self.labelPeg92 = QtWidgets.QLabel(self.centralwidget)
        self.labelPeg92.setGeometry(QtCore.QRect(100, 210, 30, 30))
        self.labelPeg92.setText("")
        self.labelPeg92.setScaledContents(True)
        self.labelPeg92.setObjectName("labelPeg92")

        self.label0x = QtWidgets.QLabel(self.centralwidget)
        self.label0x.setGeometry(QtCore.QRect(90, 1030, 80, 81))
        self.label0x.setText("")
        self.label0x.setScaledContents(True)
        self.label0x.setObjectName("label0x")
        self.label1x = QtWidgets.QLabel(self.centralwidget)
        self.label1x.setGeometry(QtCore.QRect(90, 930, 80, 81))
        self.label1x.setText("")
        self.label1x.setScaledContents(True)
        self.label1x.setObjectName("label1x")
        self.label2x = QtWidgets.QLabel(self.centralwidget)
        self.label2x.setGeometry(QtCore.QRect(90, 840, 80, 81))
        self.label2x.setText("")
        self.label2x.setScaledContents(True)
        self.label2x.setObjectName("label2x")
        self.label3x = QtWidgets.QLabel(self.centralwidget)
        self.label3x.setGeometry(QtCore.QRect(90, 740, 80, 81))
        self.label3x.setText("")
        self.label3x.setScaledContents(True)
        self.label3x.setObjectName("label3x")
        self.label4x = QtWidgets.QLabel(self.centralwidget)
        self.label4x.setGeometry(QtCore.QRect(90, 650, 80, 81))
        self.label4x.setText("")
        self.label4x.setScaledContents(True)
        self.label4x.setObjectName("label4x")
        self.label5x = QtWidgets.QLabel(self.centralwidget)
        self.label5x.setGeometry(QtCore.QRect(90, 550, 80, 81))
        self.label5x.setText("")
        self.label5x.setScaledContents(True)
        self.label5x.setObjectName("label5x")
        self.label6x = QtWidgets.QLabel(self.centralwidget)
        self.label6x.setGeometry(QtCore.QRect(90, 460, 80, 81))
        self.label6x.setText("")
        self.label6x.setScaledContents(True)
        self.label6x.setObjectName("label6x")
        self.label7x = QtWidgets.QLabel(self.centralwidget)
        self.label7x.setGeometry(QtCore.QRect(90, 360, 80, 81))
        self.label7x.setText("")
        self.label7x.setScaledContents(True)
        self.label7x.setObjectName("label7x")
        self.label8x = QtWidgets.QLabel(self.centralwidget)
        self.label8x.setGeometry(QtCore.QRect(90, 270, 80, 81))
        self.label8x.setText("")
        self.label8x.setScaledContents(True)
        self.label8x.setObjectName("label8x")
        self.label9x = QtWidgets.QLabel(self.centralwidget)
        self.label9x.setGeometry(QtCore.QRect(90, 180, 80, 81))
        self.label9x.setText("")
        self.label9x.setScaledContents(True)
        self.label9x.setObjectName("label9x")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 36))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_game = QtWidgets.QAction(MainWindow)
        self.actionNew_game.setObjectName("actionNew_game")
        self.menuFile.addAction(self.actionNew_game)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionNew_game.triggered.connect(lambda: execv(sys.executable, ['python'] + sys.argv))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Mastermind", "Mastermind"))
        self.buttonEvaluate.setText(_translate("MainWindow", "Start Game"))
        self.menuFile.setTitle(_translate("MainWindow", "Game"))
        self.actionNew_game.setText(_translate("MainWindow", "New game"))

    def reset_vars(self):
        self.counter = 0
        mastermind.guess0 = ""
        mastermind.guess1 = ""
        mastermind.guess2 = ""
        mastermind.guess3 = ""

    def ball_button_pressed(self, code):
        if mastermind.game_started:
            if str(mastermind.turn) == code[0]:
                colour = ""
                if self.counter == 0:
                    colour = "cyan"
                    self.counter += 1

                elif self.counter == 1:
                    colour = "orange"
                    self.counter += 1

                elif self.counter == 2:
                    colour = "purple"
                    self.counter += 1

                elif self.counter == 3:
                    colour = "red"
                    self.counter += 1

                elif self.counter == 4:
                    colour = "blue"
                    self.counter += 1

                elif self.counter == 5:
                    colour = "green"
                    self.counter = 0

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("pictures/" + colour + "_ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                # if there is a better way to do this please tell me
                if code == "00":
                    self.buttonBall00.setIcon(icon)
                    self.buttonBall00.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "01":
                    self.buttonBall01.setIcon(icon)
                    self.buttonBall01.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "02":
                    self.buttonBall02.setIcon(icon)
                    self.buttonBall02.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "03":
                    self.buttonBall03.setIcon(icon)
                    self.buttonBall03.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "10":
                    self.buttonBall10.setIcon(icon)
                    self.buttonBall10.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "11":
                    self.buttonBall11.setIcon(icon)
                    self.buttonBall11.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "12":
                    self.buttonBall12.setIcon(icon)
                    self.buttonBall12.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "13":
                    self.buttonBall13.setIcon(icon)
                    self.buttonBall13.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "20":
                    self.buttonBall20.setIcon(icon)
                    self.buttonBall20.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "21":
                    self.buttonBall21.setIcon(icon)
                    self.buttonBall21.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "22":
                    self.buttonBall22.setIcon(icon)
                    self.buttonBall22.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "23":
                    self.buttonBall23.setIcon(icon)
                    self.buttonBall23.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "30":
                    self.buttonBall30.setIcon(icon)
                    self.buttonBall30.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "31":
                    self.buttonBall31.setIcon(icon)
                    self.buttonBall31.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "32":
                    self.buttonBall32.setIcon(icon)
                    self.buttonBall32.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "33":
                    self.buttonBall33.setIcon(icon)
                    self.buttonBall33.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "40":
                    self.buttonBall40.setIcon(icon)
                    self.buttonBall40.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "41":
                    self.buttonBall41.setIcon(icon)
                    self.buttonBall41.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "42":
                    self.buttonBall42.setIcon(icon)
                    self.buttonBall42.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "43":
                    self.buttonBall43.setIcon(icon)
                    self.buttonBall43.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "50":
                    self.buttonBall50.setIcon(icon)
                    self.buttonBall50.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "51":
                    self.buttonBall51.setIcon(icon)
                    self.buttonBall51.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "52":
                    self.buttonBall52.setIcon(icon)
                    self.buttonBall52.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "53":
                    self.buttonBall53.setIcon(icon)
                    self.buttonBall53.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "60":
                    self.buttonBall60.setIcon(icon)
                    self.buttonBall60.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "61":
                    self.buttonBall61.setIcon(icon)
                    self.buttonBall61.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "62":
                    self.buttonBall62.setIcon(icon)
                    self.buttonBall62.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "63":
                    self.buttonBall63.setIcon(icon)
                    self.buttonBall63.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "70":
                    self.buttonBall70.setIcon(icon)
                    self.buttonBall70.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "71":
                    self.buttonBall71.setIcon(icon)
                    self.buttonBall71.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "72":
                    self.buttonBall72.setIcon(icon)
                    self.buttonBall72.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "73":
                    self.buttonBall73.setIcon(icon)
                    self.buttonBall73.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "80":
                    self.buttonBall80.setIcon(icon)
                    self.buttonBall80.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "81":
                    self.buttonBall81.setIcon(icon)
                    self.buttonBall81.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "82":
                    self.buttonBall82.setIcon(icon)
                    self.buttonBall82.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "83":
                    self.buttonBall83.setIcon(icon)
                    self.buttonBall83.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                elif code == "90":
                    self.buttonBall90.setIcon(icon)
                    self.buttonBall90.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess0 = colour

                elif code == "91":
                    self.buttonBall91.setIcon(icon)
                    self.buttonBall91.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess1 = colour

                elif code == "92":
                    self.buttonBall92.setIcon(icon)
                    self.buttonBall92.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess2 = colour

                elif code == "93":
                    self.buttonBall93.setIcon(icon)
                    self.buttonBall93.setIconSize(QtCore.QSize(60, 60))
                    mastermind.guess3 = colour

                else:
                    raise Exception("Something went wrong")

                # print(colour, mastermind.turn, mastermind.guess0, mastermind.guess1, mastermind.guess2, mastermind.guess3, mastermind.code)

            else:
                self.msgBox.setText("You cant change that ball, its not the correct turn")
                self.msgBox.exec()
        else:
            self.msgBox.setText("The game has not started yet")
            self.msgBox.exec()

    def evaluate(self):
        if not mastermind.game_started:
            mastermind.game_started = True
            self.buttonEvaluate.setText("Evaluate")
            return ""

        elif mastermind.turn == 10: self.buttonEvaluate.setText("End Game")

        peg_list = mastermind.evaluate()
        black_peg = 0
        empty = 0
        skip = False

        for i in range(4):
            if peg_list[i] == "black": black_peg += 1
            elif peg_list[i] == "empty": empty += 1

        if empty == 4:
            if mastermind.turn == 1: self.label0x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 2: self.label1x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 3: self.label2x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 4: self.label3x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 5: self.label4x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 6: self.label5x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 7: self.label6x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 8: self.label7x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 9: self.label8x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            elif mastermind.turn == 10: self.label9x.setPixmap(QtGui.QPixmap("pictures/x.png"))
            skip = True

        for i in range(4):
            if skip: break

            elif mastermind.turn == 1:
                if i == 0:
                    self.labelPeg00.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg01.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg02.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg03.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 2:
                if i == 0:
                    self.labelPeg10.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg11.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg12.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg13.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 3:
                if i == 0:
                    self.labelPeg20.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg21.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg22.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg23.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 4:
                if i == 0:
                    self.labelPeg30.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg31.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg32.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg33.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 5:
                if i == 0:
                    self.labelPeg40.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg41.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg42.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg43.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 6:
                if i == 0:
                    self.labelPeg50.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg51.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg52.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg53.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 7:
                if i == 0:
                    self.labelPeg60.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg61.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg62.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg63.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 8:
                if i == 0:
                    self.labelPeg70.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg71.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg72.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg73.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 9:
                if i == 0:
                    self.labelPeg80.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg81.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg82.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg83.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

            elif mastermind.turn == 10:
                if i == 0:
                    self.labelPeg90.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 1:
                    self.labelPeg91.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 2:
                    self.labelPeg92.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))
                elif i == 3:
                    self.labelPeg93.setPixmap(QtGui.QPixmap("pictures/" + peg_list[i] + "_peg.png"))

        if black_peg == 4:
            self.msgBox.setText("You win!")
            self.msgBox.exec()
            execv(sys.executable, ['python'] + sys.argv)

        elif mastermind.turn >= 10:
            self.msgBox.setText("You lose, the code was " + str(mastermind.code))
            self.msgBox.exec()
            execv(sys.executable, ['python'] + sys.argv)

        self.reset_vars()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    mastermind = Mastermind()
    mastermind.finished.connect(app.exit)
    mastermind.create_code()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, 0)
    MainWindow.show()
    sys.exit(app.exec_())