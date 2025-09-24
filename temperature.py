from selectorlib import Extractor
import requests

class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage.
    """
    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Builds the url string adding country and city"""
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """Extracts a value as instructed by the yml file and returns a dictionary"""
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """Cleans the output of _scrape"""
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°F", "").strip())

if __name__ == "__main__":
    temperature = Temperature(country='usa', city='san francisco')
    print(temperature.get())


