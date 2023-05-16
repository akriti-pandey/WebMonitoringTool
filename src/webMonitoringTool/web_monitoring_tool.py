#This script is designed to retrieve URLs from a specified configuration file, configure logging settings,
#and periodically verify the presence of specific content requirements on each URL. 
#The script utilizes a utility library (utility.py) to perform these operations.
#Author : Akriti Pandey

import time
import utility as utilLibrary


config_file_path = "src\\resource\\config.txt"
print("Config file path is {config_file_path}")

timestamp = time.strftime("%Y%m%d%H%M%S")
log_file_name = f"src\\log\\monitor_{timestamp}.log"
print("Monitor log file name is {config_file_path}")

interval = 20
maxDuration = 90
content_requirements = {
    'https://www.facebook.com': 'User',
    'https://www.google.com': 'Google',
    'https://www.instagram.com': 'insta',
    'https://www.amazon.com': 'insta',
}

if __name__ == '__main__':

    # reads urls from config file
    urls = utilLibrary.read_urls_from_configfile(config_file_path)

    # configures the logging file
    utilLibrary.configureLogging(log_file_name)

    # verifies the content for url and logs data in the log the periodic checks
    utilLibrary.validateURLAndVerifyContentRequiement(urls, content_requirements, interval, maxDuration)