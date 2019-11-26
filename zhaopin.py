# 检索智联招聘指定职位
url = 'https://www.zhaopin.com/'
# 1-导入模块
from time import sleep
from selenium import webdriver
# 2-启动浏览器
fire = webdriver.Firefox()
# 3-打开指定网站
fire.get(url)
sleep(1)
# 4-定位职位搜索框并键入指定职位
fire.find_element_by_class_name('zp-search__input').send_keys('爬虫工程师')
# 5-定位搜索按钮并响应 zp-search__btn zp-search__btn--blue
fire.find_element_by_class_name('zp-search__btn').click()
sleep(2)
# 切换窗口-switch--唯一标识：句柄-handle
# 6-查看网页窗口的个数
handles = fire.window_handles
handle = fire.current_window_handle
print(handles,handle)
# 7-切换网页窗口
for h in handles:
    if h != handle:
        fire.switch_to_window(h)
print(fire.title)
sleep(3)
# 8-当前网页的职位名--列表：60
jobname_list = fire.find_elements_by_class_name('contentpile__content__wrapper__item__info__box__jobname__title')
print(len(jobname_list))
# for jobname in jobname_list:
#     print(jobname.text)
#for index,job_element in enumerate(jobname_list):
#    print(index+1,'--->',job_element.text)
# 9-职位，公司，薪资，地点，工龄，学历
# 9-1 先确定网页的职位信息的整个区域
listContent = fire.find_element_by_id('listContent')
# 9-2确定整个区域的子元素块<div>--60
list_contents = listContent.find_elements_by_css_selector('.contentpile__content__wrapper.clearfix')
print(len(list_contents))
# 9-3访问每一个子元素块的具体内容
for content in list_contents:
    #print(content.text)
    jobname = content.find_element_by_class_name('jobName').text
    commpanyName = content.find_element_by_class_name('commpanyName').text
    # 薪资:%s，地点:%s，工龄%s，学历:%s
    print("职位:%s，公司:%s，"%(jobname,commpanyName))





















