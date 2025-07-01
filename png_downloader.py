import requests
import json
import time


def downloader():
    with open(
        "/Users/dmini/iCloud/Research/Data_Science/Projects/phys_links/download_list_phys106_pastexam.json",
        "r",
    ) as f:
        json_data = json.loads(f.read())

    for i, url in enumerate(json_data):
        response = requests.get(url)

        with open(f"data/page_{i}.png", "wb") as f:
            f.write(response.content)

        time.sleep(2)


if __name__ == "__main__":
    downloader()
