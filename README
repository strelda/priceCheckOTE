### setup is simple, just run
    nohup ./runChecker.sh &

set it to run on computer startup

### how it works:
main script runChecker.sh periodically runs priceCheckOTE.sh, which downloads xls file from OTE page and calls for ote_warning.py, which sends email, if the price is above some value

### possible issues: 
    - change of page, xls file names
    - firewall blocks wget or sending of email
    - potentially missing packages: pip3 install datetime forex-python MIMEText MIMEMultipart xlrd