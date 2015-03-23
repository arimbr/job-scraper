job-scraper
===========

Scraping jobs data from Stack Overflow Careers

Requried packages:
```
sudo apt-get install python-dev libxml2-dev libxslt-dev libffi-dev build-essential libssl-dev libffi-dev
```
Set up:
```
virtualenv env

source env/bin/activate

pip install -r requirements.txt

cd stackoverflow/stackoverflow

touch items.json
```
Run:
```
scrapy crawl jobs
```
