# WebMonitoringTool
URL Monitor
This tool is designed to retrieve URLs from a specified configuration file, configure logging settings, and periodically verify the presence of specific content requirements on each URL. The script utilizes a utility library (utility.py) to perform these operations.

**Author**
Akriti Pandey

1) Installation
Clone the repository:
git clone https://github.com/your-username/url-monitor.git

2) Navigate to the project directory:
cd url-monitor
Install the required dependencies:
pip install -r requirements.txt

3)Configuration
Before running the script, make sure to configure the following settings in the config.txt file located in the src/resource directory:

plaintext
https://www.facebook.com
https://www.google.com
https://www.instagram.com
https://www.amazon.com
Each URL should be listed on a separate line.

4)Usage
To start monitoring the URLs and verifying the content requirements, run the following command:

python main.py

The script will read the URLs from the configuration file, configure the logging file, and periodically check the content requirements for each URL. The monitoring process will run every 20 seconds for a maximum duration of 90 seconds.

5)Logs
The monitoring logs will be saved in the src/logs directory with the filename format monitor_{timestamp}.log, where {timestamp} represents the current date and time in the format YYYYMMDDHHMMSS.

License
This project is licensed under the MIT License.
