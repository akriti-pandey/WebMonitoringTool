.. F-Secure Web Monitoring Tool documentation master file, created by
   sphinx-quickstart on Mon May 15 23:41:55 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to F-Secure Web Monitoring Tool's documentation!
========================================================
This tool is intended as a monitoring tool for web site administrators for detecting problems on their sites.

Main functions:

* Reads a list of web pages (HTTP URLs) from a configuration file.
* Periodically makes an HTTP request to each page.
* Measures the time it took for the web server to complete the whole request.
* Verifies that the page content received from the server matches the content requirements (e.g., certain string in the web page).
* Writes a log file that shows the progress of the periodic checks.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Prerequiste
==================

set_python_path.bat need to be run in order to configure the python path

Requirements
==================

-Python 3.x
-utility library
-OS
-time
-requests
-logging

Installation
==================

Clone the project repository.
Installation Clone the repository: git clone https://github.com/your-username/url-monitor.git


Navigate to the project directory: cd url-monitor
Install the required dependencies: 
-OS
-time
-requests
-logging
-utility

Install the required dependencies by running "pip Install" command



Usage
==================
1) Set the configuration parameters:

   config_file_path: The path to the configuration file containing the list of URLs.
   log_file_name: The path and filename for the log file where URL response times will be logged.
   interval: The time interval (in seconds) between each URL verification.
   maxDuration: The maximum duration (in seconds) for monitoring the URLs.

   example:
   in Windows:

   config_file_path = "src\\resource\\config.txt"
   log_file_name = "src\\log\\monitor.log"
   interval = 20
   maxDuration = 90

2)Define the content requirements for each URL
   example:
   content_requirements = {
      'https://www.facebook.com': 'User',
      'https://www.google.com': 'Google',
      'https://www.instagram.com': 'insta',
      'https://www.amazon.com': 'amazon',
   }

3.Configure the logging file for monitoring URL response times using function configureLogging

   example
   lib.configureLogging(log_file_name)

4. Run the script using cmd "python web_monitoring_tool.py"

