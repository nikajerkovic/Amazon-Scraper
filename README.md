# Amazon Scraper

[Scrapy](https://docs.scrapy.org/en/latest/) is a Python framework for large scale web scraping. It gives you all the tools you need to efficiently extract data from websites, process them as you want, and store them in your preferred structure and format.





Amazon Scraper is a project made as a college assignment.

[Category](https://www.amazon.com/s?i=stripbooks&bbn=5&rh=n%3A283155%2Cn%3A5%2Cn%3A3508%2Cp_n_publication_date%3A1250226011&dc&qid=1643905060&rnid=5&ref=sr_nr_n_3): Books -> Computers & Technology -> Computer Science


## Installation

Use the package manager pip to install scrapy and make a new scrapy project.

```bash
  pip install scrapy
  !scrapy startproject amazon
```
Since the spider named amazon already exists, you just have to start the spider and you could choose to save data.

```bash
  !scrapy crawl Amazon -o data.csv
```
    
You can display data using Pandas with commands shown below:

```bash
  import pandas as pd
  data = pd.read_csv('data.csv')
  data.head()
```
## License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
