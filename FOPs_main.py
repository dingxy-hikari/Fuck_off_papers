import os
import random as rd
import sys

import PyQt5.QtWidgets as Qtw
from PyQt5 import uic
from PyQt5.QtGui import QFont

M_gui = True
M_mode = '15-4'
ans_dict = {
    '15-4': {'lt': ['A', "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "D", "D", "D", "D", ], 'tm': 15},
    '10-4': {'lt': ['A', "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D", ], 'tm': 10}}


class UI(Qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.tempMgb = None
        self.font = QFont()
        self.Btn_CSM = None
        self.Lb_SHW = None
        self.Tb_SHW = None
        self.Btn_CHG = None
        self.Btn_SPW = None
        self.Btn_QT = None
        self.ui = None
        self.font.setPointSize(20)
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("FOPs_GUI.ui")
        self.Btn_SPW = self.ui.Btn_SPW
        self.Btn_CHG = self.ui.Btn_CHG
        self.Btn_CSM = self.ui.Btn_CSM
        self.Btn_QT = self.ui.Btn_QT
        self.Lb_SHW = self.ui.Lb_SHW
        self.Tb_SHW = self.ui.Tb_SHW
        self.Tb_SHW.setFont(self.font)
        self.Btn_SPW.clicked.connect(self.g_spawn)
        self.Btn_CSM.clicked.connect(self.g_temp)
        self.Btn_CHG.clicked.connect(self.g_temp)
        self.Btn_QT.clicked.connect(quit)

    def g_spawn(self):
        self.Tb_SHW.setText((ans_spawn(ans_dict[M_mode])))

    def g_temp(self):
        self.tempMgb = Qtw.QMessageBox(text='功能开发中,敬请期待! /nThis function is developing,/n please sit and relax!')
        self.tempMgb .exec()

def ans_spawn(dt):
    t_list = dt['lt'].copy()
    opt = ''
    ct = 0
    i = 0
    for i in range(dt['tm']):
        if ct == 5:
            opt += ' '
            ct = 0

        b = rd.randint(0, len(t_list) - 1)
        opt += t_list[b]
        del t_list[b]
        i += 1
        ct += 1
    return opt


if __name__ == "__main__":
    if M_gui is True:
        app = Qtw.QApplication(sys.argv)
        gui = UI()
        gui.ui.show()
        app.exec()
        a = Qtw.QTextBrowser()

    elif M_gui is False:
        while True:
            os.system('cls')
            print(ans_spawn(ans_dict[M_mode]))
            os.system('pause')

