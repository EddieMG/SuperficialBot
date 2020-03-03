from selenium import webdriver
from time import sleep

NUMBER = "6"

class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self,number):
        self.driver.get('https://tinder.com')
        
        sleep(3)

        #login_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/button')
        #login_btn.click()
        #sleep(2)
        #number_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        #number_in.send_keys(number)
        #continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
    



if __name__ == "__main__":
    bot = Tinderbot()
    bot.login(NUMBER)    