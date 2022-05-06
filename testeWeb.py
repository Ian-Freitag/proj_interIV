from selenium import webdriver

website = 'https://www.webmotors.com.br/carros-usados/estoque?lkid=1000'
path = 'C:/Users/IAN.FREITAG/Documents/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

#botaoCarros = driver.find_elements_by_xpath('//div[@class="sc-gqPbQI ldOiUz"]')
#botaoCarros.click()

matches = driver.find_elements_by_tag_name('h2')

for match in matches:
    print(match.text)