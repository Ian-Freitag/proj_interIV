from selenium import webdriver

website = 'https://www.kavak.com/br/carros-usados'
path = 'C:/Users/IAN.FREITAG/Documents/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

#driver.find_element_by_xpath('//div[@class="sc-gqPbQI ldOiUz"]')
#botao = driver.find_element_by_xpath(div="col-sm-6 col-car col-lg-4 col-xl-3 ng-star-inserted")
#botao.click()

matches = driver.find_elements_by_tag_name('h2')

for match in matches:
    print(match.text)