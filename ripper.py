from selenium import webdriver
from time import sleep
import os
import sys

options = webdriver.ChromeOptions()
options.add_argument('headless')

driverOne = webdriver.Chrome(chrome_options=options)

source = sys.argv[1]
destination = sys.argv[2]

driverOne.get(source)
preview_button = driverOne.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[1]/div/a')[0].get_attribute('href')
print(preview_button)
driverOne.close()

driverTwo = webdriver.Chrome(chrome_options=options)
driverTwo.get(preview_button)

full_frame_button = driverTwo.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/a')[0].get_attribute('href')
print(full_frame_button)
driverTwo.close()

command = "wget -e robots=off -P "+destination+" -m " + full_frame_button

os.system(command)
