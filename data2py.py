#!/usr/bin/python3
#-*-coding:utf-8-*-

data_file_name = '1_Poisy-ParcDesGlaisins.txt'
data_file_name1 = '2_Piscine-Patinoire_Campus.txt'


try:
    with open(data_file_name, 'r') as f:
        content1 = f.read()
    with open(data_file_name1, 'r') as g:
        content2 = g.read()

except OSError:
    # 'File not found' error message.
    print("File not found")
    


def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    #print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic



  
slited_content = content1.split("\n\n")
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])



  
slited_content = content2.split("\n\n")
regular_path2 = slited_content[0]
regular_date_go2 = dates2dic(slited_content[1])
regular_date_back2 = dates2dic(slited_content[2])
we_holidays_path2 = slited_content[3]
we_holidays_date_go2 = dates2dic(slited_content[4])
we_holidays_date_back2 = dates2dic(slited_content[5])

regular_date_go0 = [regular_date_go , regular_date_go2]
regular_date_back0 = [regular_date_back , regular_date_back2]
we_holidays_date_go0 = [we_holidays_date_go, we_holidays_date_go2]
we_holidays_date_back0 = [we_holidays_date_back, we_holidays_date_back2]