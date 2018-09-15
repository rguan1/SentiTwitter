from TwitterScrapingObj import *
from AlchemyServer import *


def main():
    singleScrapingObject = TwitterScraper()
    singleScrapingObject.parsed_json_home_timeline_scrape()
    print("TEST")
    print("TEST")
    print(is_database_empty())


if __name__ == '__main__':
    main()