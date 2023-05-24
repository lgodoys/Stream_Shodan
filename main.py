from utils.Exceptions import *
from utils.helper import *
from shodan import Shodan
import requests
import urllib3
import json

urllib3.disable_warnings()

config = read_config()

SPLUNK_URL = config["default"]["URL"]
API_KEY = config["default"]["API_KEY"]
HEC_TOKEN = config["default"]["HEC_TOKEN"]
LOGGER = logger("SHODAN_LOGGER")

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
        headers = {
            "Authorization": "Splunk "+HEC_TOKEN
        }
        data = json.dumps({'host':'ShodanAPI','sourcetype':'shodan_monitoring','source':'ShodanAPI','event':banner})
        response = requests.post(url=SPLUNK_URL, headers=headers, data=data, verify=False)
        print(response.status_code)
