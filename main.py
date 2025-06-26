import time
import undetected_chromedriver as uc
from rich import print
from rich import print as rprint
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scrape_starter():
    print("Start ucdriver")
    link = "https://www.studocu.com/row/document/orta-dogu-teknik-universitesi/physics/phys-106-past-fin-phys-106-past-final-includes-until-2016/63131921?origin=organic-success-document-viewer-cta"

    # setting profile
    # options.add_experimental_option("detach", "true")
    driver = uc.Chrome(
        user_data_dir="user-data-dir=/Users/deniz/Library/Application Support/Google/Chrome/Profile 1",
        use_subprocess=True,
        version_main=137,
    )
    print("activated driver")
    driver.get(link)
    time.sleep(0.5)
    table = driver.find_element(by=By.XPATH, value='//*[@id="page-container"]')
    div_list = table.find_elements(By.XPATH, "./div")
    i = 0
    for div in div_list[1:4]:
        i = i + 1
        # div.find_element(By.XPATH,'//*[@id="pf1"]/div/div[1]')
        element = div.find_element(By.XPATH, '//*[starts-with(@id, "pf")]/div/div[1]')
        print(element)

        # print(div.get_attribute("data-page-index"))
        # img = div.find_element(By.XPATH, "//*[@id="pf4"]/div/div[1]/img")
        # element = div.find_element(By.XPATH, '//*[starts-with(@id, "pf")]/div')
        # print(element.get_attribute("data-test-selector"))
        # img = element.find_element(
        #     By.XPATH, './/div[contains(@id, "pf")]/div/div[1]/img'
        # )
        # # src = img.get_attribute("src")
        # print(img)

    driver.quit()
    print(i)
    print("driver closed")
    return


def main():
    scrape_starter()


if __name__ == "__main__":
    main()
