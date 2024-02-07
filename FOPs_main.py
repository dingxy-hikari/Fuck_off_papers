import os
import random as rd
import sys

import PyQt5.QtWidgets as Qtw
from PyQt5 import uic

M_GUI = False
ans_list = ['A', "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "D", "D", "D", "D", ]


class UI(Qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.load("FOPs_GUI.ui")


def ans_spawn(lt, tm):
    t_list = lt.copy()
    outputting = ''
    ct = 0
    i = 0
    for i in range(tm):
        if ct == 5:
            outputting += ' '
            ct = 0

        b = rd.randint(0, len(t_list)-1)
        outputting += t_list[b]
        del t_list[b]
        i += 1
        ct += 1
    return outputting


if __name__ == "__main__":
    print(sys.argv)
    if M_GUI is True:
        pass
    elif M_GUI is False:
        while True:
            os.system('cls')
            print(ans_spawn(ans_list, 15))
            os.system('pause')
