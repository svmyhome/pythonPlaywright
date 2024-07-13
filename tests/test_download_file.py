import os

from playwright.sync_api import Page


def test_download_1(page: Page):
    page.goto('https://demoqa.com/upload-download', timeout=60000)
    with page.expect_download() as download_info:
        page.locator('#downloadButton').click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder = './'
    download.save_as(os.path.join(destination_folder, file_name))
    print(download_info.value)
    print(download.suggested_filename)
    print(download.url)


def test_download_2(page):

    page.goto("https://demoqa.com/upload-download", timeout=60000)

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))
