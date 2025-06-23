import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication,QMessageBox, QMainWindow  # Importa QMainWindow correctamente
from PyQt6.QtGui import QBrush, QColor, QIcon
from login_ui import Ui_Login_form
from menu_ui import Ui_Main_window

class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi('menu.ui', self)
        self.ui = Ui_Main_window()
        self.ui.setupUi(self)

class LoginApp(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login_form()
        self.ui.setupUi(self)
        self.ui.btn_ingresar.clicked.connect(self.verificar)

    def verificar(self):
        usuario = self.ui.txt_usuario.text()
        clave = self.ui.txt_clave.text()

        if usuario == "admin" and clave == "123":
            self.menu_window = MenuApp()
            self.menu_window.show()
            self.close()
        else:
            self.ui.txt_usuario.setText("")
            self.ui.txt_clave.setText("")
            self.ui.txt_usuario.setFocus()
            self.mostrar_error()
        
    def mostrar_error(self):
        QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginApp()
    login.show()
    sys.exit(app.exec())
