
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
 
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
 
path = "C:\\python\chromedriver.exe" #webdriver 설치 경로를 입력해주세요
driver = webdriver.Chrome(path,chrome_options=options)
driver.implicitly_wait(3) # seconds
 
naver_wfootball = "https://sports.news.naver.com/wfootball/record/index.nhn?category=ligue1&league=650&tab=player&year=2020"
driver.get(naver_wfootball)
 
page = driver.page_source
premi_team_rank_list =  BeautifulSoup(page,"html.parser")
team_rank_list = premi_team_rank_list.select('#wfootballPlayerRecordBody>table>tbody>tr')
 
for team in team_rank_list:
    num = team.select('.num > div.inner > strong')[0].text
    name = team.select('.name')[0].text    
    print(num +"위 : " + name)
