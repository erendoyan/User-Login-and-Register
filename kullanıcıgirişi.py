import sys

import time

from PyQt5 import QtWidgets

import sqlite3


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.con = sqlite3.connect("database.db")

        self.cursor = self.con.cursor()

        self.cursor.execute("Create table If not exists üyeler(kullanıcı_adı TEXT,sifre TEXT)")

        self.con.commit()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()

        self.sifre = QtWidgets.QLineEdit()

        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)

        self.yazi_alani = QtWidgets.QLabel("")

        self.giris = QtWidgets.QPushButton("Giriş")

        self.kayit_ol = QtWidgets.QPushButton("Kayıt Ol")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()

        v_box.addWidget(self.kullanici_adi)

        v_box.addWidget(self.sifre)

        v_box.addWidget(self.yazi_alani)

        v_box.addStretch()

        v_box.addWidget(self.giris)

        v_box.addWidget(self.kayit_ol)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()

        h_box.addLayout(v_box)

        h_box.addStretch()

        self.setLayout(h_box)

        self.giris.clicked.connect(self.click)

        self.kayit_ol.clicked.connect(self.click)

    def click(self):

        sender = self.sender()

        adi = self.kullanici_adi.text()

        parola = self.sifre.text()

        if sender.text() == "Kayıt Ol":

            self.cursor.execute("Insert into üyeler Values (?,?)",(adi,parola,))

            self.con.commit()

            time.sleep(2)

            self.yazi_alani.setText("Başarıyla Kayıt Olundu!\nLütfen şimdi giriş yapınız!")

            self.sifre.clear()

            self.kullanici_adi.clear()


        else:

            self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and sifre = ?",(adi,parola,))

            data = self.cursor.fetchall()

            if len(data) == 0:

                self.yazi_alani.setText("Hata!!!\nLütfen tekrar deneyiniz!!!")

            else:

                self.yazi_alani.setText("Başarıyla giriş yapıldı!!!")



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

pencere.show()

sys.exit(app.exec_())