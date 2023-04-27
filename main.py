#!/usr/bin/env python

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pykeyboard

font = QFont("Helvetica",32)
wordlist = open("/Users/ozan/Documents/PycharmProjects/NewProject/Wordle/besli.txt","r",encoding= "utf-8")
fullkelimeler = wordlist.readlines()
kelimeler = []
kelimeson = kelimeler
for p in fullkelimeler:
    kelime = p[0:5]
    kelimeler.append(kelime)

#key = pykeyboard.InlineKeyboard

class Pencere(QWidget):
    def __init__(self):
        global kelimeson
        super().__init__()
        self.setGeometry(300,250,700,400)

        self.ilkharf = harf_kutusu()
        self.ilktus = renktusu()
        self.ilktus.clicked.connect(self.ilkharf.renkdegis)
        self.ikinciharf = harf_kutusu()
        self.ikincitus = renktusu()
        self.ikincitus.clicked.connect(self.ikinciharf.renkdegis)
        self.ucuncuharf = harf_kutusu()
        self.ucuncutus = renktusu()
        self.ucuncutus.clicked.connect(self.ucuncuharf.renkdegis)
        self.dorduncuharf = harf_kutusu()
        self.dorduncutus = renktusu()
        self.dorduncutus.clicked.connect(self.dorduncuharf.renkdegis)
        self.besinciharf = harf_kutusu()
        self.besincitus = renktusu()
        self.besincitus.clicked.connect(self.besinciharf.renkdegis)

        self.sonuclar = QLabel("Sonuçlar burada görünür: ")
        self.sonuclar.setAlignment(Qt.AlignCenter)
        self.sonuckutusu = QTextEdit()
        self.tamamtusu = QPushButton("Onayla...")
        self.tamamtusu.clicked.connect(self.kelimeleri_tara)
        self.yeniletusu = QPushButton("Kelimeleri sıfırla")
        self.yeniletusu.clicked.connect(self.kelime_sifirla)

        dikey = QVBoxLayout()
        yatayharfler = QHBoxLayout()
        yataybuton = QHBoxLayout()

        yatayharfler.addStretch()
        yatayharfler.addWidget(self.ilkharf)
        yatayharfler.addWidget(self.ikinciharf)
        yatayharfler.addWidget(self.ucuncuharf)
        yatayharfler.addWidget(self.dorduncuharf)
        yatayharfler.addWidget(self.besinciharf)
        yatayharfler.addStretch()

        yataybuton.addStretch()
        yataybuton.addWidget(self.ilktus)
        yataybuton.addWidget(self.ikincitus)
        yataybuton.addWidget(self.ucuncutus)
        yataybuton.addWidget(self.dorduncutus)
        yataybuton.addWidget(self.besincitus)
        yataybuton.addStretch()

        dikey.addStretch()
        dikey.addLayout(yatayharfler)
        dikey.addLayout(yataybuton)
        dikey.addStretch()
        dikey.addWidget(self.sonuclar)
        dikey.addWidget(self.sonuckutusu)
        dikey.addWidget(self.tamamtusu)
        dikey.addWidget(self.yeniletusu)
        self.setLayout(dikey)

        self.show()
    def kelimeleri_tara(self):
        harf1 = self.ilkharf.text().lower()
        renk1 = self.ilkharf.renk
        harf2 = self.ikinciharf.text().lower()
        renk2 = self.ikinciharf.renk
        harf3 = self.ucuncuharf.text().lower()
        renk3 = self.ucuncuharf.renk
        harf4 = self.dorduncuharf.text().lower()
        renk4 = self.dorduncuharf.renk
        harf5 = self.besinciharf.text().lower()
        renk5 = self.besinciharf.renk

        self.ilk_harf(harf1,renk1)
        self.ikinci_harf(harf2,renk2)
        self.ucuncu_harf(harf3,renk3)
        self.dorduncu_harf(harf4,renk4)
        self.besinci_harf(harf5,renk5)
        text = ""
        for i in kelimeson:
            text = text + i +", "
        self.sonuckutusu.setText(text)


    def ilk_harf(self,harf,renk):
        harfal = str(harf)
        t = 0
        if renk == "Gray":
            while t < 20:
                for i in kelimeler:
                    veri = str(i)
                    if harfal in veri:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "Yellow":
            while t < 20:
                for q in kelimeler:
                    veri = str(q)
                    if harfal not in veri:
                        kelimeson.remove(veri)
                t+=1
        elif renk == "Green":
            while t < 20:
                for l in kelimeler:
                    veri = str(l)
                    if not harfal == veri[0]:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "White":
            pass
    def ikinci_harf(self,harf,renk):
        harfal = str(harf)
        t = 0
        if renk == "Gray":
            while t < 20:
                for i in kelimeler:
                    veri = str(i)
                    if harfal in veri:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "Yellow":
            while t < 20:
                for q in kelimeler:
                    veri = str(q)
                    if harfal not in veri:
                        kelimeson.remove(veri)
                t+=1
        elif renk == "Green":
            while t < 20:
                for l in kelimeler:
                    veri = str(l)
                    if not harfal == veri[1]:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "White":
            pass
    def ucuncu_harf(self,harf,renk):
        harfal = str(harf)
        t = 0
        if renk == "Gray":
            while t < 20:
                for i in kelimeler:
                    veri = str(i)
                    if harfal in veri:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "Yellow":
            while t < 20:
                for q in kelimeler:
                    veri = str(q)
                    if harfal not in veri:
                        kelimeson.remove(veri)
                t+=1
        elif renk == "Green":
            while t < 20:
                for l in kelimeler:
                    veri = str(l)
                    if not harfal == veri[2]:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "White":
            pass
    def dorduncu_harf(self,harf,renk):
        harfal = str(harf)
        t = 0
        if renk == "Gray":
            while t < 20:
                for i in kelimeler:
                    veri = str(i)
                    if harfal in veri:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "Yellow":
            while t < 20:
                for q in kelimeler:
                    veri = str(q)
                    if harfal not in veri:
                        kelimeson.remove(veri)
                t+=1
        elif renk == "Green":
            while t < 20:
                for l in kelimeler:
                    veri = str(l)
                    if not harfal == veri[3]:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "White":
            pass
    def besinci_harf(self,harf,renk):
        harfal = str(harf)
        t = 0
        if renk == "Gray":
            while t < 20:
                for i in kelimeler:
                    veri = str(i)
                    if harfal in veri:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "Yellow":
            while t < 20:
                for q in kelimeler:
                    veri = str(q)
                    if harfal not in veri:
                        kelimeson.remove(veri)
                t+=1
        elif renk == "Green":
            while t < 20:
                for l in kelimeler:
                    veri = str(l)
                    if not harfal == veri[4]:
                        kelimeson.remove(veri)
                t += 1
        elif renk == "White":
            pass
    def kelime_sifirla(self):
        for p in fullkelimeler:
            kelime = p[0:5]
            kelimeler.append(kelime)
        kelimeson = kelimeler

class harf_kutusu(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFont(font)
        self.setFixedSize(50, 50)
        self.setMaxLength(1)
        self.setAlignment(Qt.AlignCenter)
        self.renk = "White"
        self.yazi = self.text()
        self.textChanged.connect(self.sonrakine_git)
    def renkdegis(self):
        if self.renk == "Green":
            self.renk = "Yellow"
            self.setStyleSheet("QLineEdit {background : Yellow ;}")
        elif self.renk == "Yellow":
            self.renk = "Gray"
            self.setStyleSheet("QLineEdit {background : Gray ;}")
        elif self.renk == "Gray":
            self.renk = "Green"
            self.setStyleSheet("QLineEdit {background : Green ;}")
        elif self.renk == "White":
            self.renk = "Green"
            self.setStyleSheet("QLineEdit {background : Green ;}")

    def sonrakine_git(self):
        pass


class renktusu(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(60,30)


uygulama=QApplication(sys.argv)
pencere=Pencere()
sys.exit(uygulama.exec_())
