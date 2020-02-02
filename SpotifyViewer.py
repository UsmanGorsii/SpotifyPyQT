import sys
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions


class SpotifyViewer:
    def __init__(self, username, password, song_link, time_to_play, chrome=False, firefox=False):
        self.username = username
        self.chrome = chrome
        self.firefox = firefox
        self.password = password
        self.song_link = song_link
        self.base_url = "https://www.spotify.com/"
        self.site_re_captcha_token = "6Lfdz4QUAAAAABK1wbAdKww1AEvuJuCTVHoWvX8S"
        self.anti_re_captcha_key = "64d5877a4330ce8101f78fa2f2f6a5f6"
        self.driver = None
        self.time_to_play = time_to_play
        self.notified = False
        self.repeat_dict = {"Enable repeat": "Disable repeat",
                            "Enable repeat one": "Enable repeat",
                            "Disable repeat": "Enable repeat one"}

    @staticmethod
    def write_to_console(text):
        sys.stdout.write("\r" + text)
        sys.stdout.flush()

    def wait_till_elements(self, xpath):
        while True:
            try:
                elements = self.driver.find_elements_by_xpath(xpath)
                return elements
            except:
                None

    def wait_till_element(self, xpath, text=False, index=0, retries=10):
        while True:
            retries -= 1

            try:
                elements = self.wait_till_elements(xpath)
                elements[0]
                break
            except:

                if retries <= 0:
                    return 'NA'
                sleep(0.5)

        if text:
            return elements[index].text
        else:
            return elements[index]

    def send_keys(self, xpath, keys, sleeptime=0.5, clear=True):
        while True:
            try:
                element = self.wait_till_element(xpath)
                self.driver.execute_script("arguments[0].click();", element)
                sleep(0.5)

                if clear:
                    element.clear()

                element.send_keys(keys)
                sleep(sleeptime)
                break
            except:
                None

    def button_click(self, xpath, sleep_time=3):
        sleep(1)
        element = self.wait_till_element(xpath)
        sleep(0.5)
        # try:
        element.click()
        # except:
        #     pass
        # driver_arg.execute_script("arguments[0].click();", element)
        sleep(sleep_time)

    @staticmethod
    def get_chrome():
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        driver_fun = webdriver.Chrome(options=chrome_options)
        return driver_fun

    @staticmethod
    def get_firefox():
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver_fun = webdriver.Firefox(firefox_profile=profile)
        driver_fun.maximize_window()
        return driver_fun

    def get_driver(self):
        if self.firefox:
            driver_fun = self.get_firefox()
        else:
            driver_fun = self.get_chrome()

        login_url = self.base_url + "en/login"
        driver_fun.get(login_url)
        return driver_fun

    def is_visible(self, xpath, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False

    def verify_google_re_captcha(self):
        re_captcha_div_xpath = './/div[@id="captcha-div"]'
        sleep(0.1)
        while True:
            try:
                self.driver.find_element_by_xpath(re_captcha_div_xpath)
                self.write_to_console('Waiting for Captcha bypass...')
            except:
                self.write_to_console('Started... ')
                break

    def redirect_to_song(self):
        self.driver.get(self.song_link)
        return True

    def check_song_time(self):
        play_button_xpath = '//button[contains(@class, "btn-green")]'
        sleep(5)
        self.button_click(play_button_xpath)
        minutes_wait = self.time_to_play * 60
        print(self.username+ " is waiting for - > " + str(self.time_to_play) + " hours")
        time_to_wait = minutes_wait * 60
        start_time = time.time()
        button_delay = time.time()
        hits = 0
        while (time.time() - start_time) < time_to_wait:
            self.write_to_console(str("Time spent: " + str(time.time() - start_time) + " sec" ))
            sleep(1)
            if time.time() - button_delay >= 10:
                button_delay = time.time()
                if hits >= 3:
                    return False
                hits = 0
            try:
                if self.wait_till_element(play_button_xpath, text=True) == "PLAY":
                    self.button_click(play_button_xpath)
                    hits += 1
            except:
                hits += 1
                pass
            if time_to_wait - (time.time() - start_time) <= 5*60 and not self.notified:
                self.notified = True
                self.notify_user()
        self.notified = False
        return True

    @staticmethod
    def notify_user():
        print("Bot will stop in less than 5 minutes!")

    def login(self, username_arg, password_arg):
        password_ib_xpath = '//*/input[@id="login-password"]'
        submit_btn_xpath = '//*/button[@id="login-button"]'
        username_ib_xpath = '//*/input[@id="login-username"]'
        self.send_keys(username_ib_xpath, username_arg)
        self.send_keys(password_ib_xpath, password_arg)
        self.verify_google_re_captcha()
        self.button_click(submit_btn_xpath)

    def repeat_fun(self, change_to_arg):
        while True:
            sleep(5)
            element = self.wait_till_element('//button[contains(@class, "spoticon-repeat")]')
            print(element.get_attribute('title'))
            current_title = element.get_attribute('title')
            if change_to_arg == self.repeat_dict[current_title]:
                break
            else:
                self.button_click('//button[contains(@class, "spoticon-repeat")]')

    def run_viewer(self):
        # try:
        while True:
            self.driver = self.get_driver()
            self.login(self.username, self.password)
            if self.is_visible('//span[@ng-if="response.error"]', timeout=8):
                print("Login Failed: ", self.username)
                self.driver.close()
                return
            self.redirect_to_song()
            if self.song_link.__contains__("track"):
                self.repeat_fun('Enable repeat one')
            else:
                self.repeat_fun('Enable repeat')

            start_again = self.check_song_time()
            self.driver.close()
            if start_again:
                break

        # except:
        #     pass

    def stop_stream(self):
        try:
            self.driver.close()
        except:
            pass