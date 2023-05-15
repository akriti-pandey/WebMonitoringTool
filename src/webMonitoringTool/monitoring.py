import Resource as res
import utilityLibraries.utility as utility

if __name__ == '__main__':

    urls = utility.read_urls_from_configfile(res.config_file_path)

    content_requirements = {
        'http://example.com': 'Example Domain',
        'http://google.com': 'Google',
        'http://reddit.com': 'reddit',
    }

    #configures the logging file log urls response time
    utility.configureLogging(res.log_file_name)

    #verifies the content for url and logs the periodic checks
    utility.validateURLAndVerifyContentRequiement(urls, content_requirements,res.interval)   