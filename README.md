# CS172FINALS21

## Implementation

### Part 1

We made a seedurl.txt file with the UCI website(uci.edu), which was the website we decided to crawl. In the crawler.py file we created url_visited list, which holds the visited urls and a url_queue, which hold the urls to crawl. Next, we read the seedurl from the text file(added as an input from the command line) and added it to the url_queue. For each page to crawl, we added the current url to the queue and used the requests python library to get the html. We marked the url as visited by putting in the url_visited list. We then created a folder to hold the crawled pages, and added the html from the current url to a text file.

We add all of the html from each page into a JSON format file (data.json), which is the format that elastic search requires to upload files, and is used for the index in Part 2.

 We used the Beautiful Soup library to extract all the URLS from the html files. If the URLs have not been seen before, we add then to the url_queue. After processing the URL on the queue, we remove it, and repeat the process for the remaining URLS.

The user inputs for crawler.py are the seedurl.txt file as well as the number of pages to be crawled. 


### Part 2

We build the index of our IR system by using Elasticsearch. Elasticsearch is the core component of the Elastic Stack. Elasticsearch provides search capability and offers a REST API for easy access. We first created a deployment on Elasticsearch. Then we created our index(html_index), which ignores HTML characters when searching. We bulk uploaded our data to elastic search from the data.json file we created in Part 1. We used REST API to make requests to ElasticSearch by using CURL.

### Part 3

For part 3, we decided to do a web app as our extension. We created the web app using flask. Flask is very similar to Django, it is a micro web framework in Python. Flask is very user friendly, it does not need specific libraries or tools. We created an app.py file which consisted of different routing functions. We also created two html files; one was the display of the home page with the search bar and the other page was the results page. The web app is launched by `$flask run` command, once the page is launched the user can input the term which they are looking for. Once they click the submit button they are redirected to the results page which shows the Elastic Search results, which is a ranked list in descending order of relevant documents to the query in the format of DOCID and their Scores. 


## How to Run

Install python3, BeautifulSoup, flask, lmxl using pip

To run crawler on MacOS or Linux:
In /src/ directory:
`bash indexer.sh`
This will ask you to input the number of pages to crawl. Hit enter after inputting the number of pages.

To see the website go into the src/website folder:
`cd website/`
`python3 -m flask run`
****************************************************************
To run crawler on Windows(also shown in demo video):
`python3 crawler.py seedurl.txt <numberOfPagesToCrawl>`

To see the website go into the src/website folder:
`cd website/`
`python3 -m flask run`

