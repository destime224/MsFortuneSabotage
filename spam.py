import data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class MsFortune:
	
	def __init__(self,login,password):
		self.__login = login
		self.__password = password
		self.__driver = None
		
	def does_element_exist(self,by,element):
		try:
			self.__driver.find_element(by,element)
			exist = True
		except NoSuchElementException:
			exist = False
		return exist
	
	def open_site(self,url='https://discord.com/login', driver=data.DRIVER):
		try:
			self.__driver = getattr(webdriver, driver)()
			driver = self.__driver
			driver.get(url)
			driver.implicitly_wait(5)
			
			loginBox = driver.find_element(By.NAME, 'email')
			loginBox.clear()
			loginBox.send_keys(self.__login)
			
			passBox = driver.find_element(By.NAME, 'password')
			passBox.clear()
			passBox.send_keys(self.__password)
			
			enterButton = driver.find_element(By.CSS_SELECTOR,'button[type=submit]')
			enterButton.click()
			
			sleep(1)
			if self.does_element_exist(By.XPATH, '//label[@id="uid_11"]'):
				raise ValueError("The username or password is incorrect")
			
			msg = input("Choose a channel and print the message: ")
			if msg != "":
				try:
					while True:
						textbox = driver.find_element(By.XPATH,'//div[@role="textbox"]')
						textbox.send_keys(msg)
						textbox.send_keys(Keys.ENTER)
						sleep(data.DELAY)
				except NoSuchElementException:
					raise NoSuchElementException("There's no textbox to print the message")
				finally:
					driver.quit()
			else:
				driver.quit()
			
		except AttributeError:
			raise ValueError(f"The driver {driver} does not exist")
			
if __name__ == "__main__":
	bot = MsFortune(data.USERNAME, data.PASSWORD)
	bot.open_site()
	

