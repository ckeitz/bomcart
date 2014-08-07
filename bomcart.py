import selenium
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys

import numpy
from numpy import genfromtxt

BoM = genfromtxt()

browser = web.Firefox()
browser.get('http://www.mouser.com/Cart/Cart.aspx')

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

# Define the CSS selectors for the input boxes (could change in time)
MPN_BOX_CSS		 	= "input[name$='Main$txt1']"		# Manufacturer P/N
NPN_BOX_CSS			= "input[name$='Main$txt2']"		# Internal P/N
QTY_BOX_CSS			= "input[name$='Main$txt3']"		# Quantity
ADD_BTN_CSS			= "input[name$='Main$btn1']"		# Add button

# Allow up to 10 seconds to find an element on the page before timing out
browser.implicitly_wait(10)

EnterMPN('71-CRCW1206-0-E3')
EnterNPN('Resistor 0603')
EnterQTY('50')
AddToCart()