from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

fire = webdriver.Firefox()
fire.get("https://www.jingdong.com")
time.sleep(4)

my_jd = fire.find_element_by_xpath('//ul[@class="fr"]/li[@id="ttbar-myjd"]')
ActionChains(fire).move_to_element(my_jd).perform()
time.sleep(2)
# 定位订单处理
fire.find_element_by_link_text('待处理订单').click()
