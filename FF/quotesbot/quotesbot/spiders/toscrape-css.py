# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    usuario = "davidkaufer"# Thalita

    start_urls = [
        'https://pt.foursquare.com/%s' % usuario
    ]

    def parse(self, response):
        for quotee in response.css("div.userCitiesContainer"):
            for quote in quotee.css("div.cityCard"):
                yield {
                    'cidades': quote.css("div.cityName::text").extract_first()

                }

