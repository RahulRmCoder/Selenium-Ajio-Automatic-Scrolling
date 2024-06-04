from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url="https://www.ajio.com/s/footwear-4792-56591?query=%3Arelevance%3Al1l3nestedcategory%3AMen%20-%20Formal%20Shoes&curated=true&curatedid=footwear-4792-56591&gridColumns=3&segmentIds="
s=Service('C:/Users/ACER/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(url)
time.sleep(5)

height=driver.execute_script("return document.body.scrollHeight")
#print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height=driver.execute_script("return document.body.scrollHeight")
    if height== new_height:
        break
    height=new_height
    

