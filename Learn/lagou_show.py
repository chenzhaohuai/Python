#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-12 18:12
# @Author  : Anthony
# @Email   : ianghont7@163.com
# @File    : 2 lagou_job_read_txt.py


import csv

with open('./job_lagou.txt','r',encoding="utf-8") as files:
    for file in files:
        for line in eval(file):
            job_name = line['职位名']
            job_money = line['薪资范围'].split('-')[1].split('k')[0]
            company_name = line['公司名']
            company_detail = line['公司描述']
            # 公司人数
            company_people_num = company_detail.split('/')[-1].split('人')[0]
            if '-' in company_people_num:
                company_people_num = company_people_num.split('-')[1]
                company_people_num = company_people_num.strip()
            else:
                company_people_num = company_people_num.strip()
            job_time = line['工作经验'].split('/')[-1].strip()


            fieldnames = ["职位名称","薪资范围","公司名称","公司人数","工作经验"]
            with open('./lagou_job.csv',"a+") as writer_csvfile:
                writer = csv.DictWriter(writer_csvfile,fieldnames=fieldnames)
                with open('./lagou_job.csv',"r") as read_csvfile:
                    reader = csv.reader(read_csvfile)
                    if not [row for row in reader]:
                        writer.writeheader()
                        writer.writerow({"职位名称":job_name,"薪资范围":job_money,"公司名称":company_name,"公司人数":company_people_num,"工作经验":job_time})
                    else:
                        writer.writerow({"职位名称":job_name,"薪资范围":job_money,"公司名称":company_name,"公司人数":company_people_num,"工作经验":job_time})
