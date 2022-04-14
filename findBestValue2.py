# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:09:05 2022

@author: Austin
"""
# define valiables

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

#generate values for domestic trip
price_domestic_list = [van_tor_price, van_ott_price, van_mon_price
                       , van_edm_price,van_cal_price]
time_domestic_list = [van_tor_travel_time, van_ott_travel_time
                      , van_mon_travel_time, van_edm_travel_time
                      , van_cal_travel_time]
value_list = [0 for i in range(len(price_domestic_list))]
for i in range(0,len(price_domestic_list)):
    value_list[i] = int(price_domestic_list[i]) / int(time_domestic_list[i])
print(value_list)

#find max value of domestic
best_dom = min(value_list)

#find best value going to London
price_inter=[mon_lon_price
             ,edm_lon_price
             ,cal_lon_price]
time_inter=[mon_lon_travel_time + mon_layover
            ,edm_lon_travel_time + edm_layover
            ,cal_lon_travel_time + cal_layover
            ]
value_inter = [0 for i in range(len(price_inter))]
for i in range(0,len(price_inter)):
    value_inter[i] = int(price_inter[i]) / int(time_inter[i])
best_inter=min(value_inter)

#find international airport
if best_dom == 0:
    print("Go to Munich via Toronto")
elif best_dom == 1:
    print("Go to Berlin via Ottawa")
else:
    if best_inter == 0:
        print("Go to London via Montreal")
    elif best_inter == 1:
        print("Go to London via Edmonton")
    else:
        print ("Go to Lodon via Calgary")
