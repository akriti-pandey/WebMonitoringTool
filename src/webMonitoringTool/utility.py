import requests
import time
import logging



def read_urls_from_configfile(file_path: str):
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
            url = line.strip()
            if url:
                urls.append(url)
    return urls


def verifyContentRequiement(url: str, content_requirement: str):
    """
        This function triggers GET method to collect response data for URL and calculates 
        the response time and verifies the content requirement for the url, then logs the message in the log file
        Args:
            url as string: http URL
            content_requirements as Dictionary: Dictionary for content requiremnet where key contains URL and value
            contains string content
        Return: N/A
        """
    try:
        # capture start time
        start_time = time.time()

        # Get reponse data for url
        logging.info(f"Triggering GET request for URL: {url}")
        response = requests.get(url, timeout=10)

        # capture end time
        end_time = time.time()

        # calculate response time
        elapsed_time = end_time - start_time

        # Verify that the page content matches the content requirements
        responseContent = response.text

        if content_requirement in responseContent:              
            message = f'{url} is up and running. Response time: {elapsed_time:.2f}s. {content_requirement} is found'
            logging.info(message)
            print(message)
        else:
            message = f'{url} is up, but the content does not match the requirement.'
            logging.error(message)
            print(message)

    except requests.exceptions.RequestException as e:
        message = f'{url} is down. Error message: {e}'
        logging.error(message)
        print(message)


def validateURLAndVerifyContentRequiement(urls: list, content_requirements: dict, interval: int, maxDuration: int):
    """
    This function validates the URL and verifies the content requirement for each url
    Args:
        urls as List: List of http URL
        content_requirements as Dictionary: Dictionary for content requiremnet where key contains URL and value
        contains string content
        interval as int: wait time in seconds
        maxDuration as int: total execution time in seconds
    Return: N/A
    """
    duration = 0
    while duration<= maxDuration:
        for url in urls:
            verifyContentRequiement(url, content_requirements[url])
        time.sleep(interval)
        duration += interval
        


def configureLogging(logFileName: str):
    """
    This function configure the logging file .
    Args:
        logFileName as string
    Returns:
        U/A
    """
    logging.basicConfig(filename=logFileName, level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
