# potentially missing packages:
pip3 install datetime forex-python MIMEText MIMEMultipart xlrd

# how it works:
main script runChecker.sh periodically runs priceCheckOTE.sh, which downloads xls file from OTE page and calls for ote_warning.py, which sends email, if the price is above some value

# setup is simple, just run
    nohup ./runChecker.sh &

set it to autorun on computer startup

# possible issues: 
    1) change of page, xls file names
    2) firewall blocks wget or sending of email