import os
import urllib
import urllib.request


class ImageDownloader():
    def collect_img(imageElements):
        imageURLs = []
        for imageElement in imageElements:
            imageURL = imageElement.get_attribute('src')
            if imageURL != None and (imageURL not in imageURLs):
                imageURLs.append(imageURL)
        del imageURLs[0]
        return imageURLs

    def downloader(img_file_path, imageURLs, keyword):
        i = 0
        for imageURL in imageURLs:
            i = i + 1
            try:
                if not os.path.exists(img_file_path):
                    print(img_file_path + ' does not exist.')
                    print('Creating file....')
                    os.makedirs(img_file_path)

                # downloading image from google image
                img_filename = img_file_path + '/' + keyword + str(i) + '.jpg'
                print('Downloading ' + img_filename)
                urllib.request.urlretrieve(imageURL, img_filename)

            except IOError as e:
                print(e)
            except Exception as e:
                print(e)