from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url="https://moibit.io"

firefox_option=Options()   
firefox_option.add_argument('--headless')

def test_moibit():
    driver=webdriver.Firefox(options=firefox_option)
    wait=WebDriverWait(driver,10)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    h1TitleDataCheck1=driver.find_element(By.XPATH, '//div[@class="container grid md:gap-48 gap-32"]/h1')
    assert h1TitleDataCheck1.text=='Your data, managed your way'

    #header
    driver.find_element(By.LINK_TEXT, 'Pricing').click()
    h1TitleDataCheck2=driver.find_element(By.TAG_NAME, 'h1')
    assert h1TitleDataCheck2.text=="Personalised web3 storage that scales with your needs"
    driver.back()
    parent=driver.current_window_handle
    app=driver.find_element(By.LINK_TEXT, 'Go to app')
    driver.execute_script('arguments[0].click()',app)
    driver.switch_to.window(driver.window_handles[1])   
    # p1TitleDataCheck1=driver.find_element(By.XPATH, '//div[@style="color: rgb(255, 255, 255); margin-top: 30px;"]/p[1]')
    # assert p1TitleDataCheck1.text=='A FILE IN MOIBIT IS'
    # driver.switch_to.window(parent) 
    # driver.find_element(By.XPATH, '//button[@class="btn btn_primary px-8 py-2"]').click()
    # driver.switch_to.window(driver.window_handles[1])
    # p1TitleDataCheck2=driver.find_element(By.XPATH, '//div[@style="color: rgb(255, 255, 255); margin-top: 30px;"]/p[1]')
    # assert p1TitleDataCheck2.text=='A FILE IN MOIBIT IS'
    # driver.switch_to.window(parent)
    # driver.find_element(By.XPATH, '//button[@class="btn btn_secondary"]').click()
    # h1TitleDataCheck3=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck3.text=='Introduction'
    # driver.back()
    # driver.find_element(By.XPATH, '//div[@class="moi-contribute-card card h-full"][1]').click()
    # driver.switch_to.window(driver.window_handles[1])
    # id=driver.find_element(By.ID, '330d')
    # assert id.text=='The Decentralization Dance.'
    # driver.switch_to.window(parent)
    # driver.find_element(By.XPATH, '//div[@class="moi-contribute-card card h-full"][2]').click()
    # driver.switch_to.window(driver.window_handles[1])
    # check1=driver.find_element(By.XPATH, '//strong[1]')
    # assert check1.text=='About Aicumen Technologies:'
    # driver.switch_to.window(parent)
    # driver.find_element(By.XPATH, '//div[@class="moi-contribute-card card h-full"][3]').click()
    # driver.switch_to.window(driver.window_handles[1])
    # h1TitleDataCheck4=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck4.text=='MoiBit — The practical Decentralized Cloud Storage Network'
    # driver.switch_to.window(parent)
    # driver.find_element(By.XPATH, '//*[@id="blogs"]/div/a/button').click()
    # driver.switch_to.window(driver.window_handles[1])
    # h1TitleDataCheck5=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck5.text=='MOI Technology'
    # driver.switch_to.window(parent)

    # driver.find_element(By.LINK_TEXT, 'Documentation').click()
    # driver.switch_to.window(driver.window_handles[1])
    # h1TitleDataCheck6=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck6.text=='Introduction'
    # driver.switch_to.window(parent)
    # driver.find_element(By.LINK_TEXT, 'Pricing').click()
    # h1TitleDataCheck7=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck7.text=='Personalised web3 storage that scales with your needs'
    # driver.back()
    # driver.find_element(By.LINK_TEXT, 'Privacy Policy').click()
    # driver.switch_to.window(driver.window_handles[1])
    # h1TitleDataCheck8=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck8.text=='PRIVACY NOTICE'
    # driver.switch_to.window(parent)
    # driver.find_element(By.LINK_TEXT, 'Cookie Policy').click()
    # driver.switch_to.window(driver.window_handles[1])
    # h1TitleDataCheck9=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck9.text=='COOKIE POLICY'
    # driver.switch_to.window(parent)
    # driver.find_element(By.LINK_TEXT, 'Terms & Condition').click()
    # driver.switch_to.window(driver.window_handles[1])
    # h1TitleDataCheck10=driver.find_element(By.TAG_NAME, 'h1')
    # assert h1TitleDataCheck10.text=='TERMS OF SERVICE'
    # driver.switch_to.window(parent)
    # driver.find_element(By.LINK_TEXT, 'MOI Nation').click()
    # driver.switch_to.window(driver.window_handles[1])
    # tag=driver.find_element(By.TAG_NAME, 'button')
    # assert tag.text=='login'
    # driver.switch_to.window(parent)
    # driver.find_element(By.LINK_TEXT, 'IOME').click()
    # driver.switch_to.window(driver.window_handles[1])
    # span=driver.find_element(By.TAG_NAME, 'span')
    # assert span.text=='Go to app'
    # driver.switch_to.window(parent)
    # driver.find_element(By.LINK_TEXT, 'Mint Valley').click()
    # driver.switch_to.window(driver.window_handles[1])
    # h1TitleDataCheck11=driver.find_element(By.LINK_TEXT, 'Create')
    # assert h1TitleDataCheck11.text=='Create'
