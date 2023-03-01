from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import csv

url = "https://markets.hankyung.com/indices/kospi200"

# 브라우저를 실행하고 웹사이트 접속하기
driver = webdriver.Chrome("C:/Users/user/PycharmProjects/DaishinAPI/chromedriver_win32/chromedriver")
driver.get(url)

# 웹사이트에서 HTML 코드 가져오기
html = driver.page_source

# BeautifulSoup을 사용해 HTML 코드 파싱하기
soup = BeautifulSoup(html, "html.parser")

# 원하는 태그를 찾아서 데이터 추출하기
data_list = []

# 1페이지
for tag in soup.find_all("p", class_="code txt-num ellip"):
    data_list.append(tag.text)

print(data_list)

# CSV 파일로 저장할 파일명 지정
filename = "Creon-Datareader-master/db/code_list_kospi200.csv"

# data_list를 CSV 파일로 저장하기
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    for data in data_list:
        writer.writerow([data])

# 브라우저 종료하기
driver.quit()

