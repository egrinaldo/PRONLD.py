from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

chromedrive_path = 'C:\Users\egrin\Downloads\Compressed\chromedriver_win32_2\chromedriver.exe'
webdriver = webdriver.Chrome(executable_path = chromedrive_path)
sleep(2)
webdriver.get('https://www.instagram.com/')
sleep(2)

usuario = webdriver.find_element_by_name('username')
usuario.send_keys('junior_sarmento')
senha = webdriver.find_element_by_name('password')
senha.send_keys('Suopes30')

button_login = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
button_login.click()
sleep(2)

hashtag_list = ['vidasaudavel','treino','musculacao','suplementacao','paulomuzy','saudavel']

novos_users_seguidos = []

tag = 0
seguindo = 0
likes = 0
comemtarios = 0

for hashtag in hashtag_list:
    tag = tag + 1
    webdriver.get('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div._0aCwM > input' + hashtag_list[tag] + '/')
    sleep(2)
    primeria_thumb = webdriver.find_element_by_xpath('/html/body/div[2]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[2]')
    sleep(randint(2,3))
    
    try:
        for _ in range (1,10000000):
            usuario = webdriver.find_element_by_xpath('/html/body/div[7]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a')
            
            if usuario not in novos_users_seguidos:
                if webdriver.find_element_by_xpath('/html/body/div[7]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').text == 'seguir':
                    ifwebdriver.find_element_by_xpath('/html/body/div[7]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()
                    novos_users_seguidos.append(usuario)
                    seguindo = seguindo + 1 
                    
                    button_like = webdriver.find_element_by_xpath('/html/body/div[7]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
                    button_like.click()
                    likes = likes + 1
                    sleep(randint(2,3))
                    
                    webdriver.find_element_by_xpath('/html/body/div[7]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button').click()
                    comment_box = webdriver.find_element_by_xpath('/html/body/div[7]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
                    
                    com = randint(1,10)
                    if com < 6:
                        comment_box.send_keys('Top')
                        sleep(2)
                    elif com > 5 and com < 9:
                        comment_box.send_keys('Excellent')
                        sleep(2)
                    elif com == 9:
                        comment_box.send_keys('LoL!')
                        sleep(2)
                    elif com == 10:
                        comment_box.send_keys('Maneiro!')
                        sleep(2)
                    comment_box.send_keys(Keys.ENTER)    
                    comentarios = comemtarios + 1
                    sleep(randint(1,3))
                
                webdriver.find_elements_by_link_text('Avançar').click()
                sleep(randint(1,2))
            else:
                webdriver.find_elements_by_link_text('Avançar').click()
                sleep(randint(1,2))
    except:
        continue
    
