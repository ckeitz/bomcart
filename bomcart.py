import selenium
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys

import numpy
from numpy import genfromtxt

import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

# Define the CSS selectors for the input boxes (could change in time)
MPN_BOX_CSS		 	= "input[name$='Main$txt1']"		# Manufacturer P/N
NPN_BOX_CSS			= "input[name$='Main$txt2']"		# Internal P/N
QTY_BOX_CSS			= "input[name$='Main$txt3']"		# Quantity
ADD_BTN_CSS			= "input[name$='Main$btn1']"		# Add button

# Get BoM file and QTY of boards to order
root_window = tk.Tk()
root_window.withdraw()
bomfile = askopenfilename(title="Choose a Bill of Materials File")
with open(bomfile) as bom:
	data = [line.split('\t') for line in bom]
board_qty = int(input("How many boards are we ordering? "))

# Open a Firefox instance and direct to Mouser
browser = web.Firefox()
browser.get('http://www.mouser.com/Cart/Cart.aspx')

# Form interactions
def EnterMPN(mpn_string):
	elem = browser.find_element_by_css_selector(MPN_BOX_CSS)
	elem.send_keys(mpn_string)

def EnterNPN(npn_string):
	elem = browser.find_element_by_css_selector(NPN_BOX_CSS)
	elem.send_keys(npn_string)

def EnterQTY(qty_string):
	elem = browser.find_element_by_css_selector(QTY_BOX_CSS)
	elem.clear()
	elem.send_keys(qty_string)

def AddToCart():
	elem = browser.find_element_by_css_selector(ADD_BTN_CSS)
	elem.send_keys(Keys.RETURN)

# Allow up to 10 seconds to find an element on the page before timing out
browser.implicitly_wait(10)

header = data[0]
mpn_index = header.index('Mouser')
qty_index = header.index('QTY\n')

for part in data:
	if(part[mpn_index] and part[mpn_index] != 'Mouser'):
		EnterMPN(part[mpn_index])
		EnterNPN('')
		qty = int(part[qty_index])
		qty *= board_qty
		EnterQTY(str(qty))
		AddToCart()