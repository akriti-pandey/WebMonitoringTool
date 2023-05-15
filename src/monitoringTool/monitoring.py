
import os
import subprocess
import sys
file_path = "\\src\\Resource\\config.txt"
log_file_name ="monitor.log"

import utilityLibraries.utility as utility

if __name__ == '__main__':

    urls = utility.read_urls_from_file(file_path)

    content_requirements = {
        'http://example.com': 'Example Domain',
        'http://google.com': 'Google',
        'http://reddit.com': 'reddit',
        # add more URLs and content requirements here
    }

    interval = 20

    utility.configureLogging(log_file_name)

    utility.validateURLAndVerifyContentRequiement(urls, content_requirements, interval)   