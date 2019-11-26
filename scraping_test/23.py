'''
create database zhaopin charset 'utf8'

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
#json = download("https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.92902817&x-zp-page-request-id=c1e3e7360fd0406cb5b9b48b202626bc-1544599047686-831208")
#data = json['data']
def get_all_jobs(json):
    job_count = len(json["data"]["results"])
    all_counts = []
    for count in range(job_count):
        workage = json["data"]["results"][count]["workingExp"]["name"]
        compy = json["data"]["results"][count]["company"]["name"]
        edu = json["data"]["results"][count]["eduLevel"]["name"]
        sala = json["data"]["results"][count]["salary"]
        job = json["data"]["results"][count]["jobName"]
        city = json["data"]["results"][count]["city"]["display"]
        print(workage, compy, edu, sala, job,city)
        counts = [job,compy, sala,workage,city, edu ]
        all_counts.append(counts)
    return all_counts

def save_job_mysql(all_contents):
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='10250125',
                               database='zhaopin',
                               charset="utf8"
                               )
        cursor = conn.cursor()
        for contents in all_contents :
            insert = "insert into zhaopin(职位,公司,工资,工龄,工作地点,学历)values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert, contents)
            conn.commit()
        cursor.close()
        conn.close()
def startup(url):
    json = download(url)
    all_contents = get_all_jobs(json)
    save_job_mysql(all_contents)
startup("https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.92902817&x-zp-page-request-id=c1e3e7360fd0406cb5b9b48b202626bc-1544599047686-831208")




