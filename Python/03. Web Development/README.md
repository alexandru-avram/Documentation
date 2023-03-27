# Web Dev

## Web Scraping

#### [Basic Guide](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%200.%20Basic%20guide.ipynb)

    import requests
    import lxml
    import bs4

#### [Grabbing a Title](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2001.%20Grabbin%20a%20Title.ipynb)

    <head>
        <title>Title on Browser Tab</title>
    </head>
    <body>...

#### [Grabbing a Class](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2002.%20Grabbing%20a%20Class.ipynb)

* **soup.select('div')**	    All elements with the `<div>` tag
* **soup.select('#some_id')**	The HTML element containing the id attribute of some_id
* **soup.select('.notice')**	All the HTML elements with the CSS class named notice
* **soup.select('div span')**	Any elements named <span> that are within an element named `<div>`
* **soup.select('div > span')**	Any elements named <span> that are directly within an element named `<div>`, with no other element in between


#### [Grabbing an Image](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2003.%20Grabbing%20an%20Image.ipynb)

    soup.select('img')
    
#### [Multiple Pages and Items](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/03.%20Web%20Development/Web%20Scraping/Web%20Scraping%20-%2004.%20%20Multiple%20Pages%20and%20Items.ipynb)
* Understand the structure of the page
* Get name of item to grab
* Get number of pages
* Create loop to grab items

## Django

#[Django ReadMe File](https://github.com/alexandruavram-rusu/Documentation/tree/main/Python/03.%20Web%20Development/Django#readme)

