from selenium import webdriver
from time import sleep
import urllib.request
from datetime import datetime
import random
USERNAME = "nicolbolasjoder@gmail.com"
PASSWORD = "06091996Eduard"

#Remember to check the chrome version for the webdriver!!!

class Tinderbot():
    def __init__(self):
      
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--lang=en')
        self.driver = webdriver.Chrome(chrome_options=self.options)
    def login(self):
        self.driver.get('https://tinder.com')

        
        sleep(2)
        fb_btn1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')

  
        m = fb_btn1.get_attribute('aria-label')
        print(m)
        if m == "Log in with Facebook":
            fb_btn1.click()

        elif m =="Log in with phone number":
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            fb_btn_description = fb_btn.get_attribute('aria-label')
            n= fb_btn.get_property('outerText')
            print(n)
            fb_btn.click()
            fb_btn2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
            fb_btn2.click()
 

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(USERNAME)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(PASSWORD)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)
        sleep(6)
        allow_ubi = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_ubi.click()
        sleep(2)
        decline_not = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        decline_not.click()

        decline_cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/div/button')
    
        decline_cookies.click()

        sleep(3)
        #Add try and catch, once quarantine is over this wont appear.
        no_passport = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        no_passport.click()


    def get_images(self):
        Swiper = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]')
        num_images = Swiper.get_property('childNodes')
        #num_images = Swiper.get_property('childElementCount')
        print(num_images)
        i=1
        
        for image in num_images:
            image.click()
            sleep(1)
            image_path = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[{}]/div/div'.format(i)
            print(image_path)
            img = self.driver.find_element_by_xpath(image_path)
            print(img)
            print(i)
            image_attributes = img.get_attribute('style') 
            image_attributes.find('"')
            link_img = image_attributes[image_attributes.find('"')+1:image_attributes.find('"',25)]
            print(link_img)
            urllib.request.urlretrieve(link_img, "{}.jpg".format(datetime.now().strftime("%Y%H%M%S%f")))
            
            i+=1


        choice = random.random()    
        
        
        like ='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
               
        dislike ='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'
        print(choice)          
        if choice >= 0.5:
            next_btn = self.driver.find_element_by_xpath(like)
            next_btn.click()
        else:
            next_btn = self.driver.find_element_by_xpath(dislike)
            next_btn.click()
        sleep(1+choice*2)
           





if __name__ == "__main__":
    bot = Tinderbot()
    bot.login()    
    for i in range(10):
        bot.get_images()
        sleep(0.2)
