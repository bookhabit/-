from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import options
from selenium import webdriver

class stack_class :
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.insert(0,x)
    
    def pop(self):
        if self.empty() == True:
            pass
        else: 
            self.stack.pop(0)

    def empty(self):
        if len(self.stack) <= 0 :
            print("검색한 목록이 없습니다")
            return True
        print(len(self.stack),"개를 검색했습니다.")  
        return False

    def show(self):  # 뒤에서부터 출력해줘야함
        for i in self.stack:
            print(i)
    
    def stack_show(self):
        print(self.stack)

st = stack_class()
while True:
    baseurl = 'https://www.google.com/search?q='
    pluseurl = input('무엇을 검색할까요 : ')
    print(pluseurl)
    st.push(pluseurl) # 검색목록 스택에 추가
    url = baseurl + (pluseurl)
    st.stack_show()
    # print(url)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe",options=options)
    driver.get(url)

    stop  = input("검색을 더 하실건가요? : (yes or no)")
    if stop == "no" :
        print("검색을 종료합니다.")
        # 최근검색어 목록 나열하기
        print("최근 검색어 목록입니다.")
        st.show()
        break

