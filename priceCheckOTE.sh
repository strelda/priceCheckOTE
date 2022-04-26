#!/bin/bash

function day() {
	date -d today '+%d'       
}
function tomorrow() {
	date -d tomorrow '+%d'
}
function month() {
	date -d today '+%m'       
}
function year() {
	date -d today '+%Y'       
}

curl 'https://www.ote-cr.cz/en/short-term-markets/electricity/intra-day-market?date=$(year)-$(month)-$(day)&set_language=en' > temp_dailyMarketPage

FILENAME=$(grep "/pubweb/attachments/" temp_dailyMarketPage | awk -F '"' '{print $2}')
wget https://www.ote-cr.cz/${FILENAME} -O temp_dailyMarketStats.xls

python3 ote_warning.py
