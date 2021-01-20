# !/urs/bin/python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

import os
import sys


class App(QWidget):
	def __init__(self):
		self.start()

	def start(self):
		self.ui = uic.loadUi('untitled.ui')
		self.ui.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	app.exec_()