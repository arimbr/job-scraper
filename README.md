job-scraper
===========

Scraping jobs data from Stack Overflow Careers

Requried packages:
```
sudo apt-get install python-dev libxml2-dev libxslt-dev libffi-dev
```
Set up:
```
virtualenv env

source env/bin/activate

pip install -r requirements.txt
```
Run:
```
scrapy crawl jobs
```
