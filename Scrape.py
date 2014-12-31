import urllib2
import os
import time
from bs4 import BeautifulSoup

subjects = []
allAllTRs = []
dryRun = False;

##Ok, here's the game plan:
## 1. Every hour/half hour/whatever, scrape the webpage.  Store the page locally (on server?)
## 2. after every scrape, use BS4 to grab current enrollment for ecach class
##        Note: store the enrollment in a seperate file for each subject.
## 3. Update the website, or pull directly from the db

## Folder system goes as follows:
## ROOT
## | Scrape python file
## | subject_tags.dat
## + Subject1
## | | HTML file
## | | Enrollment data file
## + Subject2
## | | HTML file
## | | Enrollment data file
##
## etc etc

## one folder for each subject.  Maybe just make it a DB later?


urlBase = "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=15W&subareasel="
headers = {'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}



def getSubjects():
    f = open("subject_tags.dat", 'r')
    if(len(subjects) == 0):
        for line in f:
            subjects.append(line)

def makeSubjectFolders():
    f = open("subject_tags.dat", 'r')
    storagePath = os.path.join(os.getcwd(), "storage")
    files = os.listdir(storagePath)
    for line in f:
        subTag = line[:-1]
        if subTag not in files:
            os.mkdir(os.path.join(storagePath, subTag))


def getAllHTML():
    if not subjects:
        getSubjects()
    for subject in subjects:
        subTag = subject[:-1]
        makeSubjectFolders()
        if(not dryRun):
            curURL = urlBase + subTag
            curDir = os.path.join(os.getcwd(), "storage", subTag)
            req = urllib2.Request(curURL, None, headers)
            try:
                response = urllib2.urlopen(req)
            except Exception as e:
                print "Url grab failed for " + subTag + "\n"
                sys.exit()

            code = response.getcode()
            if(code == "404"):
                html = ''
                print "grabbing " + subTag + " failed! 404\n"
            else:
                html = response.read()
                print "grabbing " + subTag + " successful!\n"

            soup = BeautifulSoup(html)
            f = open(os.path.join(curDir, "page.html"), 'w')
            f.write(str(soup))

        else:
            print subTag

def get1HTML():
    subjects = ["COM+SCI\n"]
    for subject in subjects:
        subTag = subject[:-1]
        makeSubjectFolders()
        if(not dryRun):
            curURL = urlBase + subTag
            curDir = os.path.join(os.getcwd(), "storage", subTag)
            req = urllib2.Request(curURL, None, headers)
            try:
                response = urllib2.urlopen(req)
            except Exception as e:
                print "Url grab failed for " + subTag + "\n"
                sys.exit()

            code = response.getcode()
            if(code == "404"):
                html = ''
                print "grabbing " + subTag + " failed! 404\n"
            else:
                html = response.read()
                print "grabbing " + subTag + " successful!\n"

            soup = BeautifulSoup(html)
            f = open(os.path.join(curDir, "page.html"), 'w')
            f.write(str(soup))

        else:
            print subTag

getAllHTML()