from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chrome_debugmode import run_chrome_debug
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.action_chains import ActionChains
import time

#url = 'https://naver.com'
url = 'http://vlm.lge.com/issue/plugins/servlet/group-config/REAVN/groupsUser?groupName=REAVN_aivi2-developers_xlm'



def set_new_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r"user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data\Default")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    #driver.get(url)
    return driver

def set_debug_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


#./run_chrome_debug()

driver2 = set_debug_chrome_driver()
driver2.get(url)
driver2.maximize_window()
driver2.find_element(By.NAME, "multiuserImage").click()

parent_window = driver2.current_window_handle
all_windows = driver2.window_handles

child_window = [window for window in all_windows if window != parent_window][0]
driver2.switch_to.window(child_window)

driver2.find_element(By.ID, "nameFilter").send_keys("youngsoo.cho")
driver2.find_element(By.ID, "filterName").click()
print(driver2.window_handles)