import scrapy
from ..items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'Amazon'
    page_number = 2
    start_urls = [
     'https://www.amazon.com/s?i=stripbooks&bbn=5&rh=n%3A283155%2Cn%3A5%2Cn%3A3508%2Cp_n_publication_date%3A1250226011&dc&qid=1643905060&rnid=5&ref=sr_nr_n_3'
     ]

    def parse(self, response):
      item= AmazonItem()
      product_name = response.css('.a-color-base.a-text-normal::text').extract()
      product_author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.s-link-style').css('::text').extract()
      product_price = response.css('.s-price-instructions-style .a-price-fraction , .s-price-instructions-style .a-price-whole').css('::text').extract()
      
      print(product_author)
      print(product_price)
      # Rješavanje problema s autorom
      for author in product_author: 
        if author == ', ':
          product_author.remove(author)

      for index, elem in enumerate(product_author):
        if elem == ' and ':
          new_value = product_author[index-1] + ' and '+ product_author[index+1]
          product_author[index-1] = 'to delete'
          product_author[index+1] = 'to delete'
          product_author[index] = new_value
        elif elem == ', et al.':
          new_value = product_author[index-2] + ','+ product_author[index+1] + ',et al.'
          product_author[index-2] = 'to delete'
          product_author[index-1] = 'to delete'
          product_author[index] = new_value

      author_list  = []
      for author in product_author:
        if author != 'to delete':
          author_list.append(author)

      # rješavanje problema s cijenom 

      for index, elem in enumerate(product_price):
        if elem == '.':
          new_value = product_price[index-1] + '.'+ product_price[index+1]
          product_price[index-1] = 'to delete'
          product_price[index+1] = 'to delete'
          product_price[index] = new_value

      price_list  = []
      for price in product_price:
        if price != 'to delete':
          price_list.append(price)
        

      for name, author, price in zip(product_name,author_list,price_list):
        item['product_author'] = author
        item['product_name'] = name
        item['product_price'] = price
        yield item
      
      
      next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=5&rh=n%3A283155%2Cn%3A5%2Cn%3A3508%2Cp_n_publication_date%3A1250226011&dc&page='+str(AmazonSpider.page_number)+'&qid=1643905079&rnid=5&ref=sr_pg_2'
      if AmazonSpider.page_number <= 3:
        AmazonSpider.page_number += 1
        yield response.follow(next_page, callback = self.parse)
    
