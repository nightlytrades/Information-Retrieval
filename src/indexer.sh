#!/bin/sh python3
chmod +x ./indexer.sh
echo "Enter number of pages to crawl: "
read readNumPages
python3 crawler.py seedurl.txt $readNumPages
