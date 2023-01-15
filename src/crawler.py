from bs4 import BeautifulSoup
import requests
import sys
import os
import os.path 
import time
import json

url_queue = []
url_visited = []
randFileId = 123 
html_dict = {}
index_dict = {}
i=0


f = open( sys.argv[1] , "r")
if f.mode == "r":
    url = f.read()
    url_queue.append(url)

num_pages = int(sys.argv[2])

open("data.json", "w").close()

for x in range(num_pages):  # user input will be the range( number of pages to crawl)
 
    curr_url = url_queue[0]

    get_html = requests.get(curr_url)
    html = get_html.text

    url_visited.append(curr_url)
    
    currDir = os.getcwd() #get current working directory
    
    #create folder called crawled pages
    folderDir = os.path.join(currDir,r'crawledPages')
    if not os.path.exists(folderDir):  #check if there is a folder with the same name
        os.makedirs(folderDir)

    #code to output crawled pages (html files) in a folder.
      #part of file name
    with open(os.path.join(folderDir, str(randFileId)+".txt")  , 'w+',encoding='utf-8') as file:  #open file to write to it
        file.write(html)    #write information to file
        randFileId += 100 #add 100 to file name so it outputs to a new file at next iteratio 

    index_dict = {"index": {}}
    html_dict = {"html": html }
    out_file = open("data.json", "a+")
    json.dump(index_dict,out_file)
    out_file.write("\n")
    json.dump(html_dict,out_file)
    out_file.write("\n")
    out_file.close()
    
    

    soup = BeautifulSoup(html, 'lxml')
    tags = soup.find_all('a')

    for tag in tags:
        extracted_url = tag.get('href')
        if extracted_url is not None:
            if extracted_url.startswith('http'):
                if (extracted_url not in url_visited):
                    url_queue.append(extracted_url)
    
    url_queue.remove(curr_url)
    time.sleep(1)

