# germanscraper
Automated pipeline for scraping German flashcards for Anki

## DISCLAIMER: This repository is meant to serve merely as an example of how one might use Scrapy to automate the generation of Anki flashcards.
By uploading this project, I do not intend to advocate or encourage the scraping any website. Before scraping any website, you should review that website's terms of service to make sure you do not violate them. 

1. Install requirements.txt in a virtual environment
2. Put a list of single German words on newlines in a file called "toscrape.txt" in the same directory as getwords.py
3. run getwords.py in a terminal
4. follow prompts to select desired examples from Langenscheidt dictionary
5. the output file (examples.txt) can be uploaded into Anki to create two-field flashcards (use the import feature with | as the separator)
