import utility as lib
config_file_path = "src\\resource\\config.txt"
log_file_name ="src\\log\\monitor.log"
interval = 20
maxDuration =90
if __name__ == '__main__':

    urls = lib.read_urls_from_configfile(config_file_path)

    content_requirements = {
        'https://www.facebook.com': 'User',
        'https://www.google.com': 'Google',
        'https://www.instagram.com': 'insta',
        'https://www.amazon.com': 'insta',
    }

    #configures the logging file log urls response time
    lib.configureLogging(log_file_name)

    #verifies the content for url and logs the periodic checks
    lib.validateURLAndVerifyContentRequiement(urls, content_requirements,interval,maxDuration)   