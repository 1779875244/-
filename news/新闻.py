from selenium import webdriver
import time
fire=webdriver.Firefox()

url='http://www.baidu.com'
fire.get(url)
time.sleep(3)
fire.find_element_by_partial_link_text('新闻').click()


time.sleep(3)
listContent = fire.find_element_by_xpath('//div[@class="mod-tab-content"]')
list_contents=listContent.find_elements_by_xpath('//div[@class="mod-tab-pane active"]')

for content in list_contents:
    yaodian = content.find_element_by_xpath('//div[@class="hotnews"]').text
    huati1 = content.find_element_by_xpath('//ul[1][@class="ulist focuslistnews"]').text
    huati2 = content.find_element_by_xpath('//ul[2][@class="ulist focuslistnews"]').text
    huati3 = content.find_element_by_xpath('//ul[3][@class="ulist focuslistnews"]').text
    huati4 = content.find_element_by_xpath('//ul[4][@class="ulist focuslistnews"]').text
    huati5 = content.find_element_by_xpath('//ul[5][@class="ulist focuslistnews"]').text
    print("要点:%s" % (yaodian))
    print("新闻:%s" % (huati1))
    print("新闻:%s" % (huati2))
    print("新闻:%s" % (huati3))
    print("新闻:%s" % (huati4))
    print("新闻:%s" % (huati5))
