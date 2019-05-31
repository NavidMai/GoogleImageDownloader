from time import sleep


class ScrollPage():
    def scroll(driver):
        for i in range(0, 5):
            jsCode = 'window.scrollTo(0, document.body.scrollHeight)'
            driver.execute_script(jsCode)
            sleep(1)

    def isElementExist(element):
        try:
            element;
            return True

        except:
            return False
