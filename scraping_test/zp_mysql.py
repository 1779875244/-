'''
创建数据库
create database zhaopin charset 'utf8'
创建数据表
create table zhaopin(
cunm int(4) primary key auto_increment,
职位 varchar(50),
公司 varchar(50),
工资 varchar(15),
工龄 varchar(15),
工作地点 varchar(50),
学历 varchar(15)
)engine='InnoDB'  charset='utf8'
'''
import  requests
import pymysql
#查看下载网页源码
def download(url):
    response = requests.get(url)
    return response.json()
#获取所有信息
def get_all_jobs(json):
    job_count = len(json["data"]["results"])
    all_counts = []
    for count in range(job_count):
        jobname = json["data"]["results"][count]["jobName"] #职位
        company = json["data"]["results"][count]["company"]["name"] #公司
        salary = json["data"]["results"][count]["salary"] #工资
        workage = json["data"]["results"][count]["workingExp"]["name"] #工龄
        city = json["data"]["results"][count]["city"]["display"] #工作地点
        edulevel = json["data"]["results"][count]["eduLevel"]["name"] #学历
        print(jobname,company, salary,workage,city, edulevel)
        counts = [jobname,company, salary,workage,city, edulevel ]
        all_counts.append(counts)
    return all_counts
#存储到数据库
def save_job_mysql(all_contents):
        #建立python与mysql的联系
        conn = pymysql.connect(host='localhost', #ip
                               port=3306, #端口号
                               user='root', #用户名
                               password='10250125', #密码
                               database='zhaopin', #数据库名
                               charset="utf8" #字符集
                               )
        #操作对象
        cursor = conn.cursor()
        #执行语句
        for contents in all_contents :
            insert = "insert into zhaopin(职位,公司,工资,工龄,工作地点,学历)values(%s,%s,%s,%s,%s,%s)" #sql插入语句
            cursor.execute(insert, contents)
        #反馈执行结果
            conn.commit()
        #关闭资源
        cursor.close()
        conn.close()


def startup(url):
    #通过json获取源码
    json = download(url)
    #获取json所有招聘信息
    all_contents = get_all_jobs(json)
    #存储信息到数据库
    save_job_mysql(all_contents)

startup("https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.92902817&x-zp-page-request-id=c1e3e7360fd0406cb5b9b48b202626bc-1544599047686-831208")







