from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

NUM_OF_CONTAINERS = 1  # 10

print "starting ... "
GRID_URL = 'http://172.17.0.2:4444/wd/hub'

# Set tor profile and preferences
tor_profile = webdriver.FirefoxProfile()
tor_profile.set_preference('network.proxy.type', 1)
tor_profile.set_preference('network.proxy.socks', '127.0.0.1')
tor_profile.set_preference('network.proxy.socks_port', 9050)

try:
    print "configuring chrome driver... "
    chrome_driver = webdriver.Remote(command_executor=GRID_URL,
                                     desired_capabilities=DesiredCapabilities.CHROME)

    # print "configuring firefox driver... "
    # firefox_driver = webdriver.Remote(command_executor=GRID_URL,
    #                                   desired_capabilities=DesiredCapabilities.FIREFOX)

    print "configuring tor driver... "
    tor_driver = webdriver.Remote(command_executor=GRID_URL,
                                  desired_capabilities=DesiredCapabilities.FIREFOX, browser_profile=tor_profile)

    with open('sites.txt') as f:
        for line in f:
            for i in range(NUM_OF_CONTAINERS):
                print "chrome getting", line
                chrome_driver.get(line)

                # print "firefox getting", line
                # firefox_driver.get(line)

                print "tor getting", line
                tor_driver.get(line)

finally:
    print "closing windows ... "
    # chrome_driver.quit()
    # firefox_driver.quit()
    tor_driver.quit()

print "SUCCESS"
