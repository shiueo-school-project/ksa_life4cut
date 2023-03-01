import string
import sys
import os
import webbrowser
from PySide6.QtCore import QTimer

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from PySide6.QtGui import QPixmap
import shutil
from modules import *
from widgets import *
from PIL import Image, ImageDraw, ImageFont
import random

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        if not os.path.isdir("./Userdata"):
            os.mkdir("Userdata")

        if not os.path.isdir("./Res"):
            os.mkdir("Res")

        if not os.path.isfile("./Userdata/null.png"):
            shutil.copyfile(load_file("images/images/null.png"), "./Userdata/null.png")

        # Timer
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(lambda: self.update())
        self.timer.start()

        self.printstr = ""

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.home_label = widgets.plainTextEdit_2
        self.label1 = widgets.label
        self.label2 = widgets.label_2
        self.label3 = widgets.label_3
        self.label4 = widgets.label_4
        self.label5 = widgets.label_5
        self.label6 = widgets.label_6
        self.label7 = widgets.label_7
        self.label8 = widgets.label_8

        self.radio8 = widgets.radioButton_8
        self.radio7 = widgets.radioButton_7
        self.radio6 = widgets.radioButton_6
        self.radio5 = widgets.radioButton_5
        self.radio4 = widgets.radioButton_4
        self.radio3 = widgets.radioButton_3
        self.radio2 = widgets.radioButton_2
        self.radio1 = widgets.radioButton_1

        self.runbtn = widgets.runButton
        self.runbtn.clicked.connect(lambda: self.runpic())

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "ksa_life4cut"
        description = "SHI3DO - ksa_life4cut"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.btn_github.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # Update Functions
    def picoperation(self, picarray):
        print(picarray)
        picf = []
        for i in range(4):
            picf.append(picarray[i])

        im1 = Image.open(f"./Userdata/{picf[0]}")
        im2 = Image.open(f"./Userdata/{picf[1]}")
        im3 = Image.open(f"./Userdata/{picf[2]}")
        im4 = Image.open(f"./Userdata/{picf[3]}")

        canvas = Image.new("RGB", (max(im1.width, im2.width, im3.width, im4.width) + 40,
                                   im1.height + im2.height + im3.height + im4.height + 600), color="#ffffff")
        canvas.paste(im1, (int(canvas.width/2 - im1.width/2), 20))
        canvas.paste(im2, (int(canvas.width/2 - im2.width/2), 40 + im1.height))
        canvas.paste(im3, (int(canvas.width/2 - im3.width/2), 60 + im1.height + im2.height))
        canvas.paste(im4, (int(canvas.width/2 - im4.width/2), 80 + im1.height + im2.height + im3.height))
        canvas.save(f"./Res/{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))}.png")

    def runpic(self):
        print(self.radio1.isChecked(), self.radio2.isChecked(), self.radio3.isChecked(), self.radio4.isChecked(),
              self.radio5.isChecked(), self.radio6.isChecked(), self.radio7.isChecked(), self.radio8.isChecked())

        photo_file_list_v2 = os.listdir("./Userdata")
        photo_file_list_v2 = [file for file in photo_file_list_v2 if
                              file.endswith(".jpg") or file.endswith(".png") and file != "null.png"]

        res_picarray = []
        try:
            if self.radio8.isChecked():
                res_picarray.append(photo_file_list_v2[0])
            if self.radio7.isChecked():
                res_picarray.append(photo_file_list_v2[1])
            if self.radio6.isChecked():
                res_picarray.append(photo_file_list_v2[2])
            if self.radio5.isChecked():
                res_picarray.append(photo_file_list_v2[3])
            if self.radio4.isChecked():
                res_picarray.append(photo_file_list_v2[4])
            if self.radio3.isChecked():
                res_picarray.append(photo_file_list_v2[5])
            if self.radio2.isChecked():
                res_picarray.append(photo_file_list_v2[6])
            if self.radio1.isChecked():
                res_picarray.append(photo_file_list_v2[7])
        except Exception as e:
            self.printstr += f"{e}\n"

        print(res_picarray)
        if not len(res_picarray) > 3:
            self.printstr += f"{res_picarray} plz pick over 4 images\n"
        else:
            self.printstr += f"{res_picarray} THX\n"
            self.picoperation(res_picarray)
            self.printstr += "sending to operator\n"

    def update(self):
        photo_file_list = os.listdir("./Userdata")
        photo_file_list = [file for file in photo_file_list if
                           file.endswith(".jpg") or file.endswith(".png") and file != "null.png"]
        self.printstr += f"{len(photo_file_list)}/8 taken \n{photo_file_list}, {len(photo_file_list)} \n\n " \
                         f"Made by shi3do(22-094)"
        self.home_label.setPlainText(self.printstr)
        self.printstr = ""
        pixarray = []
        if len(photo_file_list) < 8:
            for i in range(8 - len(photo_file_list)):
                photo_file_list.append("null.png")
        for i in range(len(photo_file_list)):
            pixarray.append(QPixmap(f"./Userdata/{photo_file_list[i]}").scaled(QSize(320, 180)))
            if i == 0:
                self.label8.setPixmap(pixarray[0])
            elif i == 1:
                self.label7.setPixmap(pixarray[1])
            elif i == 2:
                self.label6.setPixmap(pixarray[2])
            elif i == 3:
                self.label5.setPixmap(pixarray[3])
            elif i == 4:
                self.label4.setPixmap(pixarray[4])
            elif i == 5:
                self.label3.setPixmap(pixarray[5])
            elif i == 6:
                self.label2.setPixmap(pixarray[6])
            else:
                self.label1.setPixmap(pixarray[7])

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_exit":
            sys.exit(app.exec())

        if btnName == "btn_github":
            webbrowser.open("https://github.com/SHI3DO/ksa_life4cut")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: 0')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: 1')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(load_file("Icon/ksa_life4cut.ico")))
    window = MainWindow()
    sys.exit(app.exec())
