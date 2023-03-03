from bs4 import BeautifulSoup
import requests
import os

class ImageScraper:
    GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

    def __init__(self):
        self.data = ''
        self.n_images = 0
        
    def input_data(self, data, n_images):
        self.data = data
        self.n_images = n_images
    
    def search_images(self):
        url = self.GOOGLE_IMAGE + 'q=' + self.data
        print('Start searching...')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img', limit=self.n_images)
        
        if not os.path.exists('images'):
            os.makedirs('images')

        for i, image in enumerate(images):
            try:
                image_url = image['src']
                response = requests.get(image_url)
                filename = 'images/image{}.jpg'.format(i)
                with open(filename, 'wb') as f:
                    f.write(response.content)
            except:
                pass
                print('Done')