import time
import json
import undetected_chromedriver as uc
from rich import print
from selenium.webdriver.common.by import By


def scrape_starter():
    print("Start ucdriver")
    link = "https://www.studocu.com/en-us/document/orta-dogu-teknik-universitesi/general-physics/phys-105-past-exam-questions/22674597?origin=search-results"

    # setting profile
    driver = uc.Chrome(
        user_data_dir="user-data-dir=/Users/dmini/Library/Application Support/Google/Chrome/Profile 1",
        use_subprocess=True,
        version_main=137,
    )
    print("activated driver")
    driver.get(link)
    table = driver.find_element(by=By.XPATH, value='//*[@id="page-container"]')
    div_list = table.find_elements(By.XPATH, "./div")
    download_list = []
    for div in div_list:
        time.sleep(3)
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

    driver.quit()
    print("driver closed")


def main():
    scrape_starter()


if __name__ == "__main__":
    main()
