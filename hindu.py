import scrapy
import requests
import MySQLdb

class MySpider(scrapy.Spider):
    name = 'hindu'
    start_urls = [
        'http://www.thehindu.com/entertainment/movies/'
    ]

    def parse(self, response):
	print response.url
	links = response.xpath('//p[@class="story-card-33-heading"]/a/@href').extract()
        for link in links :
	    yield scrapy.Request(link,callback=self.parse_url)

    def parse_url(self, response):
            
	    title= response.xpath('//h1[@class="title"]/text()').extract()
	    link= response.xpath('//a[@class="auth-nm lnk"]/@href').extract()
	    year=response.xpath('//span[@class="blue-color ksl-time-stamp"]/none/text()').extract()
	    image=response.xpath('//img[@class="media-object adaptive placeholder lead-img"]/@src').extract()
	    print title
	    print link
	    print year
	    print image
	    db= MySQLdb.connect(host="localhost",user="root",passwd="root",db="hindudb")
	    cursor=db.cursor()
	    sql="""insert into h(title,link,year,image) values(title,link,year,image);"""
	    import pdb;pdb.set_trace()
	    try:
		   cursor.execute(sql)
		   db.commit()
	    except:
		   db.rollback()
		   db.close()
   
