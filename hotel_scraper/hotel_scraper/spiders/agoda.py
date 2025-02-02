import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AgodaSpider(scrapy.Spider):
    name = "agoda"
    allowed_domains = ["agoda.com"]

    def __init__(self, city=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city = city or "Kuala Lumpur"
        self.start_urls = [
            f"https://www.agoda.com/Search?city={self.city.replace(' ', '%20')}&checkIn=2025-02-01&rooms=1"
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, "//div[@class='DatelessPropertyCard']")),
            )

    def parse(self, response):
        hotels = response.css("//div[@class='DatelessPropertyCard']")
        for hotel in hotels:
            name = hotel.css("//div[@class='DatelessPropertyCard__ContentHeader']::text").get(default="").strip()
            price = hotel.css("div[@class='Box-sc-kv6pi1-0.gbOjPM.DatelessPropertyCard__AdditionalPriceCurrency']::text").get()
            image_url = hotel.css("//img[@class='DatelessGallery__HeroImage']::attr(src)").get()
            star_rating = hotel.css("//span[@class='star-rating.display-inline']::text").get()
            booking_url = hotel.css("//a[]::attr(href)").get()

            if price:
                price = price.replace(",", "").replace("USD", "").strip()

            yield {
                "name": name,
                "city": self.city,
                "price": float(price) if price else 0,
                "star_rating": float(star_rating) if star_rating else 0,
                "image_url": image_url,
                "booking_url": f"https://www.agoda.com{booking_url}" if booking_url else None,
                "source": "Agoda",
            }
