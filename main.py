import time
import json
import undetected_chromedriver as uc
from rich import print
from rich import print as rprint
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def scrape_starter():
    print("Start ucdriver")
    link = "https://www.studocu.com/en-us/document/orta-dogu-teknik-universitesi/general-physics/phys-105-past-exam-questions/22674597?origin=search-results"

    # setting profile
    # options.add_experimental_option("detach", "true")
    driver = uc.Chrome(
        user_data_dir="user-data-dir=/Users/dmini/Library/Application Support/Google/Chrome/Profile 1",
        use_subprocess=True,
        version_main=137,
    )
    print("activated driver")
    driver.get(link)
    # time.sleep(1000_000)
    table = driver.find_element(by=By.XPATH, value='//*[@id="page-container"]')
    div_list = table.find_elements(By.XPATH, "./div")
    download_list = []
    for div in div_list:
        time.sleep(3)
        # div.find_element(By.XPATH,'//*[@id="pf1"]/div/div[1]')
        driver.execute_script("window.scrollBy(0, 2000);")  # scroll down 500px
        elmt = div.find_elements(By.XPATH, '//*[starts-with(@id, "pf")]/div/div[1]')
        for el in elmt:
            img_el = el.find_element(By.TAG_NAME, "img")
            download_list.append(img_el.get_attribute("src"))

        download_list = list(set(download_list))

    json_data = json.dumps(download_list)
    with open(
        "download_list.json",
        "w",
    ) as f:
        f.write(json_data)

        # img = div.find_element(By.XPATH, "//*[@id="pf4"]/div/div[1]/img")
        # element = div.find_element(By.XPATH, '//*[starts-with(@id, "pf")]/div')
        # print(element.get_attribute("data-test-selector"))
        # img = element.find_element(
        #     By.XPATH, './/div[contains(@id, "pf")]/div/div[1]/img'
        # )
        # # src = img.get_attribute("src")
        # print(img)

    driver.quit()
    print("driver closed")


def main():
    scrape_starter()


if __name__ == "__main__":
    main()
