#네이버에 로그인하기 


from selenium import webdriver

# 드라이버 경로 유의!!!!!!
driver = webdriver.Chrome('/home/ubuntu/Desktop/data_handling_basic/web_crawling_basic/chromedriver')

#암묵적으로 웹 자원 로드를 위해 n초까지 기다려 준다.
driver.implicitly_wait(3)

#내가 특정한 url 에 접근한다

driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('ssh_1678')
driver.find_element_by_name('pw').send_keys('ejsvk119')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
