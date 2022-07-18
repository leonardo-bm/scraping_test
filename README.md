# Scraping Test

This program will extract information from a few different blogs and websites, as quickly as possible.

- https://www.theverge.com/
- https://www.phoronix.com/
- https://es.gizmodo.com/
- https://www.engadget.com/

## For each one of the websites above, the program should:

- Fetch its HTML
- Extract the RSS or Atom feed URL from the HTML
- Fetch the feed contents
- Extract the <title>, <pubDate> / <published> and <link> from the first 10 feed entries.
- Save a JSON file containing the extracted information.
- Able to run using Docker.

# Usage

The main.py file will execute all the crawlers at the same time and extract the data requested in JSON format.

## To run the program using Docker, follow the steps below.

### Build docker image
```
sudo docker build -t scraping_test .
```

### Run docker image
```
sudo docker run --rm -v $PWD:/opt/ --name scraping_container scraping_test
```

This will return a file called "main_result.json"