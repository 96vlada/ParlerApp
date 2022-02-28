import time
import xlsxwriter

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import random

import threading
import os, sys

from datetime import datetime, timedelta
import openpyxl

class ListOfFollowers:

	def createExcelWithListOfFollowers(self):

		ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
		CONFIG_PATH = os.path.join(ROOT_DIR, 'chromedriver.exe')
		service = Service(CONFIG_PATH)
		# service = Service('C:/Users/chromedriver.exe')
		driver = webdriver.Chrome(service=service)
		driver.set_window_size(1980, 1020)
		driver.get("https://parler.com/login.php")

		# options = Options()
		# options.add_argument('--headless')
		# options.add_argument('--disable-gpu')

		# chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")

		# driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
		# driver.set_window_size(1980, 1020)
		# driver.get("https://parler.com/login.php")
		driver.implicitly_wait(356)


		def send_keys_delay(controller,keys,min_delay=0.05,max_delay=0.05):
			for key in keys:
				controller.send_keys(key)
				time.sleep(random.uniform(min_delay,max_delay))

		send_keys_delay(driver.find_element(By.XPATH, '//input[@type="text"]'), self.parlerUsername)
		send_keys_delay(driver.find_element(By.XPATH, '//input[@type="password"]'), self.parlerPassword)
		driver.find_element(By.XPATH, '//button[@class="button"]').click()
		time.sleep(4)

		driver.find_elements_by_xpath('//ul[@class="sidebar__menu"]/li/a')[1].click()

		time.sleep(4)

		driver.find_elements_by_xpath('//p[@class="user-card__follow"]/a')[0].click()
		time.sleep(2)


		
		for x in range(90):
			time.sleep(4)
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

			# if(x == 89):
			# 	for x1 in driver.find_elements_by_xpath('//ul[@class="basic-list"]/li/div/a[2]/h3'):
			# 		self.listOfFollowers.append(x1.text);

		time.sleep(356)
		for x1 in driver.find_elements_by_xpath('//ul[@class="basic-list"]/li/div/a[2]/h3'):
			self.listOfFollowers.append(x1.text);

		
		# time.sleep(356)
		# print("############################################################")
		# print("Last in the list")
		# print("############################################################")
		# testinc = 0;
		# for x in driver.find_elements_by_xpath('//ul[@class="basic-list"]/li/div/a[2]/h3'):
		# 	testinc = testinc + 1
		# 	testinc2 = "-" + str(testinc)
		# 	testinc2 = int(testinc2)
		# 	print(driver.find_elements_by_xpath('//ul[@class="basic-list"]/li/div[2]')[testinc2].text)










			# print(driver.find_elements_by_xpath('//ul[@class="basic-list"]/li/div/a[2]/h3')[testinc2].text)




		# time.sleep(50)
		# for x1 in driver.find_elements_by_xpath('//ul[@class="basic-list"]/li/div/a[2]/h3'):
		# 	self.listOfFollowers.append(x1.text); 


		
		if(os.path.exists(os.path.abspath("") + "\\" + "listOfFollowers.xlsx")):
			if (os.access(os.path.abspath("") + "\\" + "listOfFollowers.xlsx",os.R_OK)):

				book = openpyxl.load_workbook(filename=os.path.abspath("") + "\\" + "listOfFollowers.xlsx")
				sheet = book.active
				incForFollowersInc = 0
				for item in self.listOfFollowers:
					incForFollowersInc = incForFollowersInc + 1;
					sheet.cell(row=incForFollowersInc, column=1).value = item
				book.save(os.path.abspath("") + "\\" + "listOfFollowers.xlsx")
				book.close()

		


		# time.sleep(4)




	def __init__(self, parlerUsername, parlerPassowrd, unfollowException, unfollowLimit):
		self.parlerUsername = parlerUsername
		self.parlerPassword = parlerPassowrd
		self.listOfFollowers = []

		t21 = threading.Thread(target=self.createExcelWithListOfFollowers);
		t21.start()

		t21.join()
		print("Followers list module")