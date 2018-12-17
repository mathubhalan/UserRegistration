# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:34:48 2018

@author: Mathu_Gopalan
"""

import pandas as pd
import time
from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select

df = pd.read_csv("./user_f.csv")

driver = wd.Chrome()
driver.get("https://gskstaging9:Respect18@gskhealthpartner-com-preprod-cf5.gdsgsk.com/en-gb/registration/")
driver.maximize_window()

for i in range(df.shape[0]):
    driver.implicitly_wait(4000)
    #email id
    driver.find_element_by_xpath("//*[@id='gigya-textbox-123604655191569820']").send_keys(df.email[i])
    
    #password
    driver.find_element_by_xpath("//*[@id='gigya-password-100441485882955890']").send_keys("Gsk@12345")
    
    #re-password
    driver.find_element_by_xpath("//*[@id='gigya-password-148332260324895170']").send_keys("Gsk@12345")
    
    #title
    select = Select(driver.find_element_by_xpath("//*[@id='gigya-dropdown-19384613975084292']"))
    select.select_by_value("Mr")
    #select.select_by_visible_text("Mr")
    
    #fname
    driver.find_element_by_xpath("//*[@id='gigya-textbox-120033521847592300']").send_keys(df.fname[i])
    
    #familyname
    driver.find_element_by_xpath("//*[@id='gigya-textbox-80919111488792770']").send_keys(df.sname[i])
    
    #profession
    select = Select(driver.find_element_by_xpath("//*[@id='gigya-dropdown-65749208947691660']"))
    select.select_by_value("Dental Professional")
    
    #specialty
    select = Select(driver.find_element_by_xpath("//*[@id='gigya-dropdown-57197776902830760']"))
    select.select_by_value("003")
    
    #Graduation year
    select = Select(driver.find_element_by_xpath("//*[@id='gigya-dropdown-93244470116644780']"))
    select.select_by_value("2006")
    
    #HCP ID
    driver.find_element_by_xpath("//*[@id='gigya-textbox-98546222849492380']").send_keys("123456")
    
    #Practise Name
    driver.find_element_by_xpath("//*[@id='gigya-textbox-7445288553003840']").send_keys(df.prac_name[i])
    
    #Practise Addr1
    driver.find_element_by_xpath("//*[@id='gigya-textbox-13206145755180180']").send_keys(df.prac_addr[i])
    
    #city
    driver.find_element_by_xpath("//*[@id='gigya-textbox-4301621522214302']").send_keys(df.city[i])
    
    #post code
    driver.find_element_by_xpath("//*[@id='gigya-textbox-1203601945225582']").send_keys(df.code[i])
    
    #phone num
    driver.find_element_by_xpath("//*[@id='gigya-textbox-8333917409131546']").send_keys("446565652210")
    
    #submit
    driver.find_element_by_xpath("//*[@id='register-social-login']/div[1]/div[43]/input").click()
    
    print("{} User Created for Email ID {}".format(i,df.email[i]))
    time.sleep(3)
    driver.get("https://gskstaging9:Respect18@gskhealthpartner-com-preprod-cf5.gdsgsk.com/en-gb/registration/")
    time.sleep(3)

    








