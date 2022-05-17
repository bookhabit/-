from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import options
from selenium import webdriver

class stack_class :
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.insert(0,x)
    
    def top_remove(self):
        if self.empty() == True:
            pass
        else: 
            self.stack.pop(0)

    def empty(self):
        if len(self.stack) <= 0 :
            print("검색한 목록이 없습니다")
            return True

    def recent_search_show(self):  # 최근들어온 순서대로 출력
        for i in range(len(self.stack)):
            print(i+1,self.stack[i])
    
    def stack_show(self):
        print(self.stack)

    def recent_search_list(self,num): # 최근검색어 목록 번호로 가져오기
        # 인덱스와 value 한번에 가져오는 enumerate함수사용
        for index,value in enumerate(self.stack):
            # print(index,value)
            if index == num:
                return value

    def remove_recent_search(self,num):
        for index,value in enumerate(self.stack):
            # print(index,value)
            if index == num:
                self.stack.pop(index)

st = stack_class()

def search():
    baseurl = 'https://www.google.com/search?q='
    pluseurl = input('무엇을 검색할까요 : ')
    # print(pluseurl)  검색어 출력해보기
    st.push(pluseurl) # 검색목록 스택에 추가
    url = baseurl + (pluseurl)
    # st.stack_show()  스택 확인해보기
    # print(url)

    options = webdriver.ChromeOptions()  # selenium 오류해결코드
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe",options=options)
    driver.get(url)  # 구글검색창 자동입력해서 url로 가져옴

    # stop  = input("검색을 더 하실건가요? : (yes or no)")
    # if stop == "no" :
    #     print("검색을 종료합니다.")
    #     break
def recent_search(num): # 최근검색어 번호로 검색하기
    baseurl = 'https://www.google.com/search?q='
    recent_url = st.recent_search_list(num)
    url = baseurl+ recent_url
    st.push(recent_url)

    options = webdriver.ChromeOptions()  # selenium 오류해결코드
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe",options=options)
    driver.get(url)  # 구글검색창 자동입력해서 url로 가져옴

# 프로그램 시작
while True:
    print("---------------------------")
    print("1.검색기능")
    print("2.최근검색어 기능")
    print("3.종료")
    user = input("번호를 입력하시오:" )
    if user == "1" :  # 검색기능
        search()
    elif user == "2": # 최근검색어 목록
        while True:
        # 최근검색어 목록 나열하기
            print("---------------------------")
            print("최근 검색어 목록입니다.")
            st.recent_search_show()
            print("---------------------------")
            print("1.최근 검색어 목록으로 다시 검색하시겠습니까?")
            print("2.최근 검색어 목록을 지우시겠습니까?")
            print("3.최근 검색어 목록 창을 닫으시겠습니까?")
            user_search = input("번호를 입력하시오: ")
            if user_search == "1":  # 최근검색어 번호로 다시 구글검색
                print("---------------------------")
                num = int(input("검색할 최근검색어 번호를 입력하세요: "))
                if st.empty() == True:  # 최근검색어 목록이 비어있을 때 오류처리
                    print("최근검색어 목록이 없습니다")
                    break
                elif len(st.stack) < num-1 :  # 인덱스오류  최근검색어 목록 인덱스보다 높은 인덱스일경우
                    print("최근 검색어 목록에 있는 번호를 입력해주세요.") 
                    break
                recent_search(num-1) # 최근검색어 목록에서 인덱스0으로 시작하는 것 막기위해 +1 해줬으니 여기서는 -1 해주기

            elif user_search == "2": # 최근검색어 번호로 목록에서 지우기
                print("---------------------------")
                num = int(input("삭제할 최근검색어 번호를 입력하세요: "))
                if st.empty() == True:
                    print("최근 검색어 목록이 없습니다.")
                    break
                elif len(st.stack) < num-1:
                    print("최근 검색어 목록에 있는 번호를 입력해주세요: ")
                else :
                    st.remove_recent_search(num-1)
            
            elif user_search == "3":  # 최근검색어 목록 창 닫기
                break  
            else:
                print("최근 검색어 목록 번호에 있는 번호를 입력해주세요.")
    elif user == "3":
        break
    else:
        print("1,2,3번 중 번호를 입력해주세요.")


