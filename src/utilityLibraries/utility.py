import requests
import time
import logging



def read_urls_from_configfile(file_path):
    """
    This function reads list of http urls from the config file
    Args:
        file_path as string: config path as string
    Return:
        urls as List: List of urls present in configuration file
    """
    with open(file_path) as file:
        urls = []
        for line in file:
            tempLine = line.strip()
            if tempLine:
                urls.append(tempLine)
    return urls


def verifyContentRequiement(url, content_requirements):
    """
        This function triggers GET method to collect response data for each the URL and calculates 
        the response time of url and verifies the content requirement for each url , then logs the message in the log file
        Args:
            urls as List: List of http URL
            content_requirements as Dictionary: Dictionary for content requiremnet where key contains URL and value
            contains string content
            interval as Literal
        Return: N/A
        """
    try:
        # capture start time
        start_time = time.time()

        # Get reponse data for url
        response = requests.get(url, timeout=10)

        # capture end time
        end_time = time.time()

        # calculate response time
        elapsed_time = end_time - start_time

        # Verify that the page content matches the content requirements
        content = response.text

        # validate content requirement
        requirements = content_requirements.get(url, [])
        dataFound = True

        for data in requirements:
            if data not in content:
                dataFound = False
                break

        if dataFound            
            message = f'{url} is up and running. Response time: {elapsed_time:.2f}s'
            logging.info(message)
            print(message)
        else:
            message = f'{url} is up, but the content does not match the requirement.'
            logging.warning(message)
            print(message)

    except requests.exceptions.RequestException as e:
        message = f'{url} is down. Error message: {e}'
        logging.error(message)
        print(message)


def validateURLAndVerifyContentRequiement(urls, content_requirements, interval):
    """
    This function validates the URL and verifies the content requirement for each url
    Args:
        urls as List: List of http URL
        content_requirements as Dictionary: Dictionary for content requiremnet where key contains URL and value
        contains string content
        interval as Literal
    Return: N/A
    """
    for url in urls:
        verifyContentRequiement(url, content_requirements)
    time.sleep(interval)


def configureLogging(logFileName):
    """
    This function configure the logging file .
    Args:
        logFileName as string
    Returns:
        U/A
    """
    logging.basicConfig(filename=logFileName, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
