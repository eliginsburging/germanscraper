import os
import sys
from pyfiglet import Figlet
from helpers import (colors,
                     validate_line)
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from germanscraper.spiders.german_spider import GermanSpider


def getgermanwords():
    """
    validates the contents of the list of spanish words to scrape and runs the
    spider to scrape them
    """
    toscrape = True
    banner_fig = Figlet(font='banner3-D', width=120)
    warning_fig = Figlet(font='xcourb', width=120)
    print(colors.information(banner_fig.renderText('German Scraper')))
    if not os.path.exists('toscrape.txt'):
        print(colors.warning(
            warning_fig.renderText('Warning: toscrape.txt not found')))
        print(colors.warning('In order to scrape example sentences, you must '
                             'first create a file in the same directory as '
                             'getwords.py that contains a list of single '
                             'Spanish words, each on its own line.'))
        toscrape = False
    else:
        with open('toscrape.txt') as f:
            warning1 = "toscrape.txt improperly formatted"
            warning2 = ("It appears that toscrape.txt is improperly formatted."
                        " the file should contain only single Spanish words on"
                        " new lines. Exiting.")
            if f.read() == '':
                print(colors.warning(warning1 + '\n' + warning2))
                toscrape = False
            else:
                for line in f:
                    if not validate_line(line):
                        toscrape = False
                        print(colors.warning(warning1 + '\n' + warning2))
                        break
    if toscrape:
        with open('toscrape.txt') as f:
            print(colors.prompt(
                "toscrape.txt appears to be valid and contains the "
                "words listed below."))
            for l in f:
                print(
                    colors.information(
                        l.replace('\n', '')))
            print()
        proceed = input(
            colors.prompt(
                'would you like to proceed with these entries? y/n:\n'
            )
        )
        safetyvalve3 = 0
        while len(proceed) != 1 or proceed not in "yYnN":
            safetyvalve3 += 1
            if safetyvalve3 > 1000:
                raise RuntimeError(
                    "Max iterations exceeded! Exiting!"
                )
                break
            proceed = input(colors.prompt(
                'Invalid entry. Please enter y or n\n'
                ))
        if proceed in "nN":
            sys.exit(0)
        else:
            os.system('rm examples.txt >/dev/null 2>&1')
            process = CrawlerProcess(get_project_settings())
            process.crawl(GermanSpider)
            process.start()


getgermanwords()
