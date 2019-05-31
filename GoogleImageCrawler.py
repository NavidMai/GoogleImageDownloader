from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Scroll import ScrollPage
from Downloader import ImageDownloader


class GoogleImageCrawler():
    url = 'https://www.google.no/imghp'
    keyword = input('Enter your keyword: ')
    img_file_path = 'Image'
    driver = webdriver.Safari()
    driver.maximize_window()

    try:
        # connecting google image search
        driver.get(url)
        inputElement = driver.find_element_by_name('q')
        inputElement.send_keys(keyword)
        inputElement.submit()
        sleep(2)

        # find button of 'more result'
        element_id = 'smb'
        element = driver.find_element_by_id(element_id)
        ScrollPage.scroll(driver)
        ans = ScrollPage.isElementExist(element)

        if ans:
            ActionChains(driver).click(element).perform()
            ScrollPage.scroll(driver)

        else:
            sleep(2)
            driver.quit()

        # starting downloading
        imageElements = driver.find_elements_by_tag_name("img")
        imageURLs = ImageDownloader.collect_img(imageElements)
        print('===============================================')
        print('Total Image on this page: ' + str(len(imageURLs)))
        print('===============================================')
        print('Starting download...')
        ImageDownloader.downloader(img_file_path, imageURLs, keyword)
        print('Done')
        driver.quit()

    except Exception as e:
        print(e)
        driver.quit()
