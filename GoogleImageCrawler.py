import os
import downloader
import readClassName
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def scroll(driver):
    for i in range(0, 5):
        jsCode = 'window.scrollTo(0, document.body.scrollHeight)'
        driver.execute_script(jsCode)
        sleep(1)


def isElementExist(driver):
    try:
        driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
        # driver.find_element(By.CLASS_NAME, 'mye4qd')
        scroll(driver)
        sleep(2)
        return True

    except:
        return False


class GoogleImageCrawler:
    url = 'https://www.google.com/imghp'

    # manually enter keywords
    # keywords = input('Enter your keyword: ')

    # read the keywords from file
    path = "targetList.txt"
    keywords = readClassName.classNameReader(path)

    errorList = []

    for i in range(0, len(keywords)):
        img_file_path = 'images/' + keywords[i]
        if not os.path.exists(img_file_path):
            driver = webdriver.Safari()
            # driver.set_window_size(1280, 720)
            driver.maximize_window()
            try:
                # connecting google image search
                driver.get(url)
                inputElement = driver.find_element("name", "q")
                inputElement.send_keys(keywords[i])
                inputElement.submit()
                sleep(2)

                scroll(driver)

                for j in range(1, 10):
                    ans = isElementExist(driver)
                    print(str(j) + "-" + str(ans))

                # if ans:
                    # driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
                    # scroll(driver)
                    # sleep(2)

                # starting downloading
                imageElements = driver.find_elements(By.TAG_NAME, 'img')
                imageURLs = downloader.collect_img(imageElements)
                print('===============================================')
                print('Total Image on this page: ' + str(len(imageURLs)))
                print('===============================================')
                print('Starting download...')
                downloader.downloader(img_file_path, imageURLs, keywords[i])
                print('Done')
                driver.quit()

            except Exception as e:
                errorList.append(keywords[i])
                print(e)
                driver.quit()

    print(errorList)
