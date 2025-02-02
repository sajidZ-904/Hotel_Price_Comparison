import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BookingSpider(scrapy.Spider):
    name = "booking"
    allowed_domains = ["booking.com"]

    def __init__(self, city=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city = city or "New York"
        self.start_urls = [
            f"https://www.booking.com/searchresults.html?ss={self.city.replace(' ', '+')}"
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=5,  
                wait_until=EC.presence_of_element_located((By.XPATH, "//div[@data-testid='property-card']")),
            )

    def parse(self, response):
        hotels = response.xpath("//div[@data-testid='property-card']")
        for hotel in hotels:
            name = hotel.xpath(".//div[@data-testid='title']/text()").get(default="").strip()
            price = hotel.xpath(".//span[@data-testid='price-and-discounted-price']/text()").get()
            image_url = hotel.xpath(".//img[@data-testid='image']/@src").get()
            star_rating = hotel.xpath(".//span[@data-testid='rating-score']/text()").get()
            booking_url = hotel.xpath(".//a[@data-testid='property-card-link']/@href").get()

            if price:
                price = price.replace(",", "").replace("USD", "").strip()

            yield {
                "name": name,
                "city": self.city,
                "price": float(price) if price else 0,
                "star_rating": float(star_rating) if star_rating else 0,
                "image_url": image_url,
                "booking_url": f"https://www.booking.com{booking_url}" if booking_url else None,
                "source": "Booking",
            }
