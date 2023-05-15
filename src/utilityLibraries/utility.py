import requests
import time
import logging

file_path = "C:\\Users\\theak\\OneDrive\\Desktop\\fsecure_akriti\\Resource\\config.txt"

def read_urls_from_file(file_path):
    with open(file_path) as file:
        urls =[]
        for line in file:
            tempLine = line.strip()
            if tempLine:
                urls.append(tempLine)    
    return urls

def verifyContentRequiement(url, content_requirements):
    try:
        # capture start time
        start_time = time.time()

        #Get reponse data for url
        response = requests.get(url, timeout=10)
        
        # capture end time
        end_time = time.time()

        #calculate response time
        elapsed_time = end_time - start_time

        # Verify that the page content matches the content requirements
        content = response.text

        #validate content requirement
        if all(requirement in content for requirement in content_requirements.get(url, [])):
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
        for url in urls:
            verifyContentRequiement(url, content_requirements)
        time.sleep(interval)

def configureLogging(logFileName):
    logging.basicConfig(filename=logFileName, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
