#!/bin/bash

rm *.xls

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

# day=$(day)
# month=$(month)
# year=$(year)

wget https://www.ote-cr.cz/pubweb/attachments/$(tomorrow)/$(year)/month$(month)/day$(day)/$(day)_$(month)_$(year)_EN.xls &&
python3 ote_warning.py
