# Stream Shodan

Stream Shodan is a Python application that allows to Splunk manager to push data from Shodan Stream API endpoint to Splunk using Splunk HTTP Event Collector. For usage, requires a Splunk environment with HEC enabled.

## Installation

Download this package from GitHub or clone this repository to your destination folder using git clone command

## Configuration

Set config.ini file in config folder with following parameters:

```python
[default]
API_KEY = Your Shodan API Key
HEC_TOKEN = Your Splunk HTTP Event Collector token
URL = https://{Splunk_server}:8088/services/collector/event
PROCNAME = /your/root/folder/where/app/resides/Stream_Shodan/main.py
COMMAND1 = ps -Af
COMMAND2 = pkill -f
COMMAND3 = nohup python3 /your/root/folder/where/app/resides/Stream_Shodan/main.py > /your/root/folder/where/app/resides/Stream_Shodan/logs/main_log.outerr 2> /your/root/folder/where/app/resides/Stream_Shodan/logs/main_log.outerr &
```

The config file will allows the app to connect to Stream Shodan using the authorized API token, and allows the app to send data to Splunk endpoint. The PROCNAME & COMMAND1-2-3 lines will allows the shodanStatus app to restart main script.

Configure your own Cronjob to start "shodanStatus.py" file. Do not set a cronjob for main.py script, may cause multiple instances of the script and may consume a lot of resources from your environment

## Recommended environment

The app was developed on a Linux environment. It is fully recommended to use a Linux environment, for compatibility. In case you need to use a Windows environment, you will need to modify commands and PROCNAME lines, and set your folder based on Windows environment.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropiate.

## License

[MIT](https://choosealicense.com/licenses/mit)
