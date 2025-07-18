# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from utils import resource_path

class Ui_Login_form(object):
    def setupUi(self, Login_form):
        Login_form.setObjectName("Login_form")
        Login_form.resize(520, 366)
        Login_form.setMaximumSize(QtCore.QSize(520, 366))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("img/icon.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Login_form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(parent=Login_form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 520, 366))
        self.widget.setObjectName("widget")
        self.lbl_pic = QtWidgets.QLabel(parent=self.widget)
        self.lbl_pic.setGeometry(QtCore.QRect(0, 0, 260, 366))
        self.lbl_pic.setStyleSheet("")
        self.lbl_pic.setText("")
        self.lbl_pic.setPixmap(QtGui.QPixmap(resource_path("img/login.png")))
        self.lbl_pic.setObjectName("lbl_pic")
        self.lbl_login = QtWidgets.QLabel(parent=self.widget)
        self.lbl_login.setGeometry(QtCore.QRect(260, 0, 260, 366))
        self.lbl_login.setStyleSheet("background-color:rgba(255,255,255,255);")
        self.lbl_login.setText("")
        self.lbl_login.setObjectName("lbl_login")
        self.lbl_logo = QtWidgets.QLabel(parent=self.widget)
        self.lbl_logo.setGeometry(QtCore.QRect(320, 46, 140, 38))
        self.lbl_logo.setStyleSheet("")
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.lbl_logo.setObjectName("lbl_logo")
        self.lbl_title = QtWidgets.QLabel(parent=self.widget)
        self.lbl_title.setGeometry(QtCore.QRect(343, 118, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.txt_usuario = QtWidgets.QLineEdit(parent=self.widget)
        self.txt_usuario.setGeometry(QtCore.QRect(301, 171, 178, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.txt_usuario.setStyleSheet("padding:8px;\n"
"border: 0.5px solid #C2C2C2;\n"
"\n"
"")
        self.txt_usuario.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.txt_usuario.setInputMask("")
        self.txt_usuario.setText("")
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_clave = QtWidgets.QLineEdit(parent=self.widget)
        self.txt_clave.setGeometry(QtCore.QRect(301, 213, 178, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.txt_clave.setFont(font)
        self.txt_clave.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.txt_clave.setStyleSheet("padding:8px;\n"
"border: 0.5px solid #C2C2C2;\n"
"\n"
"")
        self.txt_clave.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.txt_clave.setInputMask("")
        self.txt_clave.setText("")
        self.txt_clave.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_clave.setObjectName("txt_clave")
        self.btn_ingresar = QtWidgets.QPushButton(parent=self.widget)
        self.btn_ingresar.setGeometry(QtCore.QRect(301, 276, 178, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_ingresar.setFont(font)
        self.btn_ingresar.setStyleSheet("QPushButton#btn_ingresar {\n"
"    background-color:#000;\n"
"    color:#fff;\n"
"    border-radius:2px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btn_ingresar:hover {\n"
"    background-color:#A2BA22;\n"
"}")
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.lbl_trademark = QtWidgets.QLabel(parent=self.widget)
        self.lbl_trademark.setGeometry(QtCore.QRect(340, 340, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        self.lbl_trademark.setFont(font)
        self.lbl_trademark.setStyleSheet("color:#939393;")
        self.lbl_trademark.setObjectName("lbl_trademark")
        self.lbl_version = QtWidgets.QLabel(parent=self.widget)
        self.lbl_version.setGeometry(QtCore.QRect(490, 340, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        self.lbl_version.setFont(font)
        self.lbl_version.setObjectName("lbl_version")

        self.retranslateUi(Login_form)
        QtCore.QMetaObject.connectSlotsByName(Login_form)

    def retranslateUi(self, Login_form):
        _translate = QtCore.QCoreApplication.translate
        Login_form.setWindowTitle(_translate("Login_form", "Ingresar"))
        self.lbl_title.setText(_translate("Login_form", "INVENTARIO"))
        self.txt_usuario.setPlaceholderText(_translate("Login_form", "Usuario (\"admin\")"))
        self.txt_clave.setPlaceholderText(_translate("Login_form", "Clave (\"123\")"))
        self.btn_ingresar.setText(_translate("Login_form", "INGRESAR"))
        self.lbl_trademark.setText(_translate("Login_form", "Powered by delavware"))
        self.lbl_version.setText(_translate("Login_form", "v 1.0"))
