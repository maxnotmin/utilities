#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.phantomjs.webdriver import WebDriver as PJSWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from collections import OrderedDict
import getpass
import re
import sys
import os
import time
import typing


# ---------- GLOBAL ----------

# when DEBUG is set to TRUE, use THE_USER
# and THE_PASS regardless of user input
DEBUG = False
THE_USER = ''
THE_PASS = ''

# PATH TO BROWSERS
# PhantomJS is no longer being mantained
#PHANTOMJS_PATH = os.path.dirname(os.path.realpath(__file__)) + '\\phantomjs-2-1-1\\bin\\phantomjs.exe'

CHROME_PATH = ''
FIREFOX_PATH = ''


class QualysBase(object):


    HEADERS = OrderedDict()

    def __init__(self):
        """
        Constructor. Used to initialize all members.
        """
        """
        Constructor. Used to initialize all members.
        """
        self.auth_user = ''
        self.auth_pass = ''
        self.browser_type = None
        self.driver = None
        self.is_logged_in = False
        self.master_info = []  # type: list[dict[str, str]]
        self.user_id_list = []
        #determine desired capabilites
        self.d_cap = None
        self.d_cap = None
        self.determine_driver()

    #RUN AT INIT TO DETERMINE Desired Capabilites for Browser
    def determine_driver(self):
        if self.browser_type.lower() == 'chrome':
            pass
        elif self.browser_type.lower() == 'chrome_headless':
            pass
        elif self.browser_type.lower() == 'firefox':
            pass
        elif self.browser_type.lower() == 'firefox_headless':
            pass
        elif self.browser_type.lower() == 'ie':
            pass
        elif self.browser_type.lower() == 'ie_headless':
            pass
        elif self.browser_type.lower() == 'brave':
            pass
        elif self.browser_type.lower() == 'brave_headless':
            pass
        elif self.browser_type.lower() == 'phantomjs':
            self.d_cap = dict(desired_capabilities.DesiredCapabilities.PHANTOMJS)
            self.d_cap['phantomjs.page.settings.userAgent'] = (
                "Mozilla/46 (X11; Linux x86_64) AppleWebKit/53 " +
                "(KHTML, like Gecko) Chrome/50"
            )
        else:
            print("The Browser you listed is not configured for this Selenium Class")

        return self

    def __str__(self):
        """
        Usage:
        Returns:
        """
        main_string = 'Base Selenium Dict: {} {} {} {}'.format()
        return main_string

    def __repr__(self):
        """

        :return:
        """
        return
