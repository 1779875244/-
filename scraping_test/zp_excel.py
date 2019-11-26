import  requests
import xlwt

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
#保存到Excel
def save_job_excel(all_contents):
    # 准备excel文件 字符集为utf-8
    book = xlwt.Workbook(encoding='utf-8')
    # 准备sheet文件
    sheet = book.add_sheet('招聘信息')
    #字样准备 字体 行高 列宽 颜色
    style = xlwt.easyxf('font:name 楷体,'
                        'bold on,'
                        'color blue'
                        )
    headers = ['职位：','公司：','工资：','工龄:','工作地点','学历:']
    for col_index, col_value in enumerate(headers):
        # 设置单元格宽度
        sheet.col(col_index).width = 7000
        sheet.write(0, col_index, col_value)
    #  行 all_contents 的索引
    for row_index,contents in enumerate(all_contents):
        # 获取每一行的每一列内容和索引
        for col_index , content in enumerate(contents):
                sheet.write(row_index+1,col_index,content)
    #  保存
    book.save("D:\\node\\招聘信息.xls")
    pass

def startup(url):
    #通过json获取源码
    json = download(url)
    #获取json所有招聘信息
    all_contens = get_all_jobs(json)
    #存储信息到Excel
    save_job_excel(all_contens)

startup("https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.92902817&x-zp-page-request-id=c1e3e7360fd0406cb5b9b48b202626bc-1544599047686-831208")




