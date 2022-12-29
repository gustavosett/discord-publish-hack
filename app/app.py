from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from app.ansi import ANSI


class Application:
    
    options: ChromeOptions
    driver: Chrome
    
    def __init__(self, discord_login):
        self.email = discord_login["email"]
        self.password = discord_login["password"]
        self.options = ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = Chrome(options=self.options)
        
    def start(self):
        try:
            print("logging into " + ANSI.color_text("34") + f"{self.email}" + ANSI.color_text("0"))
            self.log_in_discord()
            print("logging into disboard...")
            self.log_in_disboard()
            print("bumpping server...")
            bump_bool_result = self.bump_server()
            if not bump_bool_result:
                return False
            error = self.driver.find_element(By.CLASS_NAME, "notie-textbox notie-background-error notie-alert notie-container")
            if error:
                return False
            return True
        except:
            try:
                del disc_bool_result, disb_bool_result
                del bump_bool_result
            except:
                pass
            return False
    
    
    def log_in_discord(self):
        try:
            self.driver.get("https://discord.com/login")
            sleep(4)
            username_input = self.driver.find_element(By.NAME, "email")
            username_input.send_keys(self.email)
            
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(self.password)

            login_button = self.driver.find_element(By.CSS_SELECTOR, '[type=submit]')
            login_button.click()
            sleep(5)
            return True
        except:
            return False
        
    def log_in_disboard(self):
        try:
            self.driver.get("https://disboard.org/dashboard/servers")

            sleep(5)

            login_button = self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]')
            login_button.click()

            sleep(4)
            return True
        except:
            return False

    def bump_server(self):
        try:
            login_button = self.driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div/div[2]/div/a[3]')
            login_button.click()

            sleep(6)
            return True
        except:
            return False
    
    def quit(self):
        try:
            self.driver.quit()
        except:
            pass
