# -*- coding: utf-8 -*-
import base64, os, requests, re, selenium, sys, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

user = "" #user email
password = "" #user password

login_url = str("https://plataforma.bvirtual.com.br/Account/Login")
home = "https://plataforma.bvirtual.com.br/"
url = str(input("Enter the ebook url: ")) #Example: https://plataforma.bvirtual.com.br/Acervo/Publicacao/187110

caps = DesiredCapabilities().FIREFOX
caps['pageLoadStrategy'] = 'eager'
options = Options()
options.set_preference("browser.link.open_newwindow.restriction", 0)
options.set_preference("browser.link.open_newwindow", 1)
#options.add_argument('-headless') #This is for a silent download
#binary = FirefoxBinary(r'/usr/bin/firefox') #Linux
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe') #Windows
profile = selenium.webdriver.FirefoxProfile()
profile.set_preference('javascript.enabled',True)
profile.set_preference('browser.helperApps.alwaysAsk.force',False)
profile.set_preference('security.dialog_enable_delay',0)
profile.set_preference('pref.downloads.disable_button.edit_actions',True)
browser = selenium.webdriver.Firefox(firefox_binary=binary,options=options,capabilities=caps,firefox_profile=profile)
browser.implicitly_wait(15)
browser.maximize_window()
browser.get(login_url)
username = browser.find_element_by_name("UserName")
password = browser.find_element_by_name("Password")
username.send_keys(user)
password.send_keys(password)
browser.find_element_by_css_selector('.button').click()
browser.get(url)
book_title = browser.find_element_by_class_name("book__title").text
page_total = browser.find_element_by_css_selector(".book__infos > p:nth-child(1)").get_attribute("innerHTML")
page_total = int(re.search(r'\d+', page_total).group(0))
try:
	book_title = book_title.replace(':',' -')
except ValueError:
	pass
try:
	os.mkdir(book_title)
except:
	pass
browser.find_element_by_link_text("Ler agora").click()
WebDriverWait(browser,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#page")))
page_number = 1
while page_number <= page_total:
	WebDriverWait(browser,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#page-canvas")))
	time.sleep(1)
	sys.stdout.write('Downloading {} - {}\r'.format(page_number,page_total))
	sys.stdout.flush()
	link = ''
	link = browser.find_element_by_css_selector("#page-canvas")
	link = browser.execute_script("return arguments[0].toDataURL('image/png');",link)
	link = link.split(',')[-1]
	link = link.encode('utf-8')
	browser.find_element_by_id('right-control').click()
	if page_number < 10:
		with open(os.path.join(book_title,'000{}.png'.format(page_number)),'wb') as img:
			img.write(base64.decodebytes(link))
	elif page_number < 100:
		with open(os.path.join(book_title,'00{}.png'.format(page_number)),'wb') as img:
			img.write(base64.decodebytes(link))
	elif page_number < 1000:
		with open(os.path.join(book_title,'0{}.png'.format(page_number)),'wb') as img:
			img.write(base64.decodebytes(link))
	else:
		with open(os.path.join(book_title,'{}.png'.format(page_number)),'wb') as img:
			img.write(base64.decodebytes(link))
	page_number += 1
print("Download finished!")
browser.get(home)
browser.execute_script("document.getElementById('user-info-menu').style.display='block';")
browser.find_element_by_link_text("Sair").click()
browser.find_element_by_css_selector('a.icon-card:nth-child(2)').click()
WebDriverWait(browser,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR,".login__form-title")))
browser.close()
time.sleep(1)
os.remove("geckodriver.log") #Comment this if you want to keep the geckodriver.log
