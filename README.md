# antutu-scraping

## Resume

Web Scraping using Scrapy on Antutu Benchmark site

## Requirements

- Anaconda3 (Python);
- Scrapy:

```sh
pip install scrapy
```

## How to change Anaconda Environments

```sh
# On Base
anaconda-navigator
# After creating 'int-comp' env
conda activate int-comp
# To switch back
conda activate base
```

## Scrapy commands

### Creating project

```sh
scrapy startproject antutu-scraping
```

### Generating Spider

```sh
scrapy genspider Antutu https://www.antutu.com/en/ranking/rank1.htm
```

### Executing Spider

```sh
scrapy crawl Antutu
```

### Running shell

```sh
scrapy shell https://www.antutu.com/en/ranking/rank1.htm
```

### Running and Saving to a file (.csv, .json)

```sh
scrapy crawl Antutu -o data/antutu.csv
```
