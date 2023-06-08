#!/usr/bin/env python3

#Import common libraries
import requests
import urllib3
import json

#Import external libraries
from shodan import Shodan

#Import custom classes and functions
from utils.Exceptions import *
from utils.helper import *

#Set Disable Warnings for HTTPS URL's
urllib3.disable_warnings()

#Set Logger
LOGGER = logger("SHODAN_LOGGER")

#Get configurations from config file
config = read_config()

SPLUNK_URL = config["default"]["URL"]
API_KEY = config["default"]["API_KEY"]
HEC_TOKEN = config["default"]["HEC_TOKEN"]


#Set Authorization Header for Splunk
headers = {
    "Authorization": f"Splunk {HEC_TOKEN}"
}

#Base logic
try:
    LOGGER.info('Starting Shodan Stream')
    api = Shodan(API_KEY)
    for banner in api.stream.alert(aid=None, timeout=None, raw=False):
        if len(banner)>2:
            keys = banner.keys()
            if "ssl" in keys:
                LOGGER.info("SSL key was found. Removing...")
                del banner["ssl"]
            if "http" in keys:
                LOGGER.info("HTTP key was found. Removing...")
                try:
                    del banner["http"]["favicon"]["data"]
                except:
                    pass
                try:
                    del banner["http"]["html"]
                except:
                    pass
            LOGGER.info("Shodan Banner is ready")
            
            data = json.dumps({'host':'ShodanAPI','sourcetype':'shodan_monitoring','source':'ShodanAPI','event':banner})
            response = requests.post(url=SPLUNK_URL, headers=headers, data=data, verify=False)
            print(response.status_code)
except Exception as err:
    pass