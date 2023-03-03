import images as ig
data = input('What are you looking for? ')
n_images = int(input('How many images do you want? '))
scraper = ig.ImageScraper()
scraper.input_data(data, n_images)
scraper.search_images()