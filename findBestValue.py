# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:09:08 2022

@author: Austin
"""

van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 150
van_cal_price = 180

van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

ott_ber_price = 1350
mon_lon_price = 1300
edm_lon_price = 1290
cal_lon_price = 1400
tor_mun_price = 990

ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

ott_ber_travel_time = 9
mon_lon_travel_time = 8
edm_lon_travel_time = 10
cal_lon_travel_time = 10
tor_mun_travel_time = 9.5

#generate values
price_domestic_list = [van_tor_price
                       , van_ott_price
                       , van_mon_price
                       , van_edm_price
                       ,van_cal_price]
time_domestic_list = [van_tor_travel_time
                      , van_ott_travel_time
                      , van_mon_travel_time
                      , van_edm_travel_time
                      , van_cal_travel_time]
value_list = [0 for i in range(len(price_domestic_list))]
for i in range(0,len(price_domestic_list)):
    value_list[i] = int(price_domestic_list[i]) / int(time_domestic_list[i])
print(value_list)
price_inter=[ott_ber_price
             ,mon_lon_price
             ,edm_lon_price
             ,cal_lon_price
             ,tor_mun_price]
time_inter=[ott_ber_travel_time + ott_layover
            ,mon_lon_travel_time + mon_layover
            ,edm_lon_travel_time + edm_layover
            ,cal_lon_travel_time + cal_layover
            ,tor_mun_travel_time + tor_layover]
value_inter = [0 for i in range(len(price_inter))]
for i in range(0,len(price_inter)):
    value_inter[i] = int(price_inter[i]) / int(time_inter[i])
print(value_inter)
#find the best path
k=0
calc_value = [0 for i in range(len(value_list)*len(value_inter))]
for i in range(len(value_list)):
    for j in range(len(value_inter)):
        calc_value[i+j+k]=[int(value_list[i])+int(value_inter[j])]
    k +=4
print(len(calc_value))
print(calc_value)
#retrieve Max value and posion
max_value=min(calc_value)
max_index=calc_value.index(max_value)
print(max_index)
domes=""
inter=""
if max_index // 5 == 0:
    domes="Toronto"
elif max_index // 5 == 1:
    domes="Ottawa"
elif max_index // 5 == 2:
    domes="Montreal"
elif max_index // 5 == 3:
    domes="Edmonton"
elif max_index // 5 == 4:
    domes="Calgary"
else:
    print("error")
if max_index % 5 == 0:
    inter="Ottawa to Berlin"
elif max_index % 5 == 1:
    inter="Montreal to London"
elif max_index % 5 == 2:
    inter="Edmonton to London"
elif max_index % 5 == 3:
    inter="Calgary to London"
elif max_index % 5 == 4:
    inter="Toronto to Munich"
else:
    print("error")
print(domes + " "+ inter)
        
        

