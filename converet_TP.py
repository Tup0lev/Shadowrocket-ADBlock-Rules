#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:34:57 2022

@author: tup0lev
"""
#把规则转变成TP-LINK 路由器适用的格式
with open("sr_direct_banad.conf", 'r', encoding='UTF-8') as file:
    while (line := file.readline()):
        if "DOMAIN-SUFFIX" in line:
            print("*" + line.replace("DOMAIN-SUFFIX,", "").replace(",Reject",""))
        if "IP-CIDR" in line:
            print(line.replace("IP-CIDR,", "").replace(",Reject",""))    

