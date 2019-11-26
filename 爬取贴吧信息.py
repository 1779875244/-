# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


# 抓取网页的通用框架,获取页面的内容
def downloadcode(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 获取正确的编码格式
        r.encoding = "utf-8"
        # 打印内容
        return r.text


    except:
        return "wrong!"


# 分析网页的html文件，整理信息，保存问列表文件中
def get_content(url):
    # 初始化一个列表来保存所有的帖子信息
    contents = []
    # 获取网页的内容
    html = downloadcode(url)
    soup = BeautifulSoup(html, 'lxml')
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
    print(len(liTags))

    # 循环这个内容li集合
    for li in liTags:
        # 将爬取到了每一条信息。保存到字典里
        content = {}
        try:
            # 开始筛选信息
            content['title'] = li.find('a', attrs={"class": "j_th_tit"}).text.strip()  # .strip()  翻译为中文
            print(li.find('a', attrs={"class": "j_th_tit"}).text.strip())

            # 获取a标签的内部属性
            content['link'] = "http://tieba.baidu.com/" + li.find('a', attrs={"class": "j_th_tit"})["href"]
            print("http://tieba.baidu.com/" + li.find('a', attrs={"class": "j_th_tit"})["href"])

            content['author'] = li.find('span', attrs={"class": 'tb_icon_author '}).text.strip()
            print(li.find('span', attrs={"class": 'tb_icon_author '}).text.strip())

            content['responseNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            print(li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip())
            content['creatTime'] = li.find('span', attrs={"class": 'pull-right is_show_create_time'}).text.strip()
            print(li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip())
            # 将字典加入到列表中
            contents.append(content)


        except:
            print('出问题')
        # 返回数据
    return contents


def writeTxt(content):
    f = open("tieba.txt", 'a+', encoding='utf-8')

    for c in content:
        f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
            c['title'], c['link'], c['author'], c['creatTime'], c['responseNum']))


url = "https://tieba.baidu.com/f?kw=%E6%9F%90%E7%A7%91%E5%AD%A6%E7%9A%84%E8%B6%85%E7%94%B5%E7%A3%81%E7%82%AE&ie=utf-8&pn=50"
page = 2


def all_url(url, page):
    url_list = []
    # 将所需要爬去的url放到列表中
    for i in range(0, page):
        url_list.append(url + '&pn=' + str(i * 50))

    for u in url_list:
        content = get_content(u)
        writeTxt(content)


if __name__ == "__main__":
    all_url(url, page)
    # get_content("http://tieba.baidu.com/f?ie=utf-8&kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&red_tag=z0177533255")
    get_content('https://tieba.baidu.com/f?kw=%E6%9F%90%E7%A7%91%E5%AD%A6%E7%9A%84%E8%B6%85%E7%94%B5%E7%A3%81%E7%82%AE&ie=utf-8&pn=50')