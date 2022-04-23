#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ryosuke mondo
#
# Created:     19/04/2022
# Copyright:   (c) ryosu 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import time
import pyperclip
import configparser

def main():
    driver = getWebDriver()
    config = configparser.ConfigParser()
    config.read('setting.ini')

    driver.get("https://facebook.com")
    url = pyperclip.paste()
    driver.get(url)

    all_comments = {}
    while True:
        now = int(time.time())
        commentsStr = execute_script(driver, "getComments.js") # to expand see more
        commentsStr = execute_script(driver, "getComments.js")
        if commentsStr == '':
            continue
        commentRows = commentsStr.split("\n")
        for commentRow in commentRows:
            row = commentRow.split(",")
            if len(row) < 2:
                print(commentRow)
            comment = Comment(now, row[0], row[1])

            if comment.comment_id in all_comments:
                pass
            else:
                all_comments[comment.comment_id] = comment
                if len(comment.comment_text) > 30:
                    n = 30
                    s = comment.comment_text
                    l = [s[i:i+n] for i in range(0,len(s), n)]
                    for line in l[1:]:
                        comment = Comment(now, comment.comment_id+line, line)
                        all_comments[comment.comment_id] = comment

            export_comments(all_comments,config['DEFAULT']['dst'])
        time.sleep(1)

def export_comments(all_comments, dst):
    output = [
        '<?xml version="1.0" encoding="utf-8"?><log>\n'
    ]
    for comment_id in all_comments.keys():
        output.append(all_comments[comment_id].to_xml())
    output.append('</log>')
    with open(dst, 'w', encoding="utf-8") as xml:
        xml.writelines(output)


class Comment:
    def __init__(self, epoch_time, comment_id, comment_text):
        self.epoch_time = epoch_time
        self.comment_id = comment_id
        self.comment_text = comment_text

    def to_xml(self):
        f = '\t<comment no="0" time="{0}" owner="0" service="youtubelive" handle="a">{1}</comment>\n'
        return f.format(self.epoch_time, self.comment_text)


def execute_script(driver, name):
    allText = ""
    with open(name) as f:
        allText = f.read()
    return driver.execute_script(allText)

def getWebDriver():
    options = webdriver.ChromeOptions()  # Configure options for Chrome.
    options = Options()
    path = sys.argv[0]
    #path = __file__

    PROFILE_PATH = os.path.dirname(path) + r'\UserData'
    if not os.path.exists(PROFILE_PATH):
        os.mkdir(PROFILE_PATH)
    options.add_argument('--user-data-dir=' + PROFILE_PATH)
    #options.add_argument('--profile-directory=Default')
    print(PROFILE_PATH)
    # Add wallet extension according to user choice
    options.add_argument('log-level=3')  # No logs is printed.
    options.add_argument('--mute-audio')  # Audio is muted.
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--lang=en-US')  # Set webdriver language
    options.add_argument(' --disable-dev-shm-usage')

    options.add_experimental_option(  # to English. - 2 methods.
        'prefs', {'intl.accept_languages': 'en,en_US'})
    options.add_experimental_option('excludeSwitches', [
        'enable-logging', 'enable-automation'])
    #driver = webdriver.Chrome(service=SC(  # DeprecationWarning using
    #    self.browser_path), options=options)  # executable_path.
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #driver.maximize_window()  # Maximize window to reach all elements.
    return driver

if __name__ == '__main__':
    main()
