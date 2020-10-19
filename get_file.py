import requests
import openpyxl
import pandas as pd
import schedule
import datetime
from constants import *
import urllib
import time
import subprocess
from bs4 import BeautifulSoup
import urllib.parse

def update():
    with open("schedule_page.html", "w") as f:
        sched_page = requests.get(url)
        f.write(sched_page.text)
        sched_page = str(sched_page.text)
        sched_page = BeautifulSoup(sched_page,"lxml")

        link = sched_page.find_all("a")[132]
        link = str(link['href'])
        linkloc = link[46::]
        linkloc = urllib.parse.quote(linkloc)
        link = link[0:46]
        f.close
    link += linkloc
    urllib.request.urlretrieve(link, "sched.xlsx")  # For Python 3
    subprocess.Popen(['python3', "work_with_file.py"])

now = (datetime.datetime.now())
date = "%d" % now.hour
sec = "%d" % now.second
minut = "%d" % now.minute
if date == "6" and sec == "0" and minut == "0":
    update()

# urllib.urlretrieve(dls, "test.xls")  # For Python 2

# table = requests.get(url)
# xl = pd.ExcelFile(table.text)
# df1 = xl.parse("ИИТ_1к_20-21_осень")
# writer = xl.ExcelWriter("sched.xlsx",engine='xlsxwriter')
# xl.to_excel(writer,'ss')
# writer.save()

