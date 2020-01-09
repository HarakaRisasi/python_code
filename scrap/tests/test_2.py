# Scraping Dynamic Web Pages with Python and Selenium
# Начало работы с Selenium
#
# Selenium WebDriver – это программная библиотека для управления браузерами. 
# WebDriver представляет собой драйверы для различных браузеров 
# и клиентские библиотеки на разных языках программирования, предназначенные для управления этими драйверами.
# По сути своей использование такого веб-драйвера сводится к созданию бота, 
# выполняющего всю ручную работу с браузером автоматизированно.
###############################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

###############################################################################

# Схема навигации в Selenium:
# - Определите элемент, с которым вы хотите взаимодействовать.
# - Взаимодействуйте по мере необходимости 
#   (установите некоторый текст, извлеките значение, отправьте нажатие клавиши и т. Д.).
# Элементы могут быть найдены с использованием xPath
#   «driver.find_element_by_xpath» или более высокоуровневых методов, таких как «find_element_by_id».