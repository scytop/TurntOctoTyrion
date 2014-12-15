import urllib2
import os
import time
from bs4 import BeautifulSoup

subjects = []
allAllTRs = []
dryRun = False;


urlBase = "http://www.registrar.ucla.edu/schedule/detmain.aspx?termsel=15W&subareasel="
headers = {'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}



def getSubjects():
	f = open("subject_tags.dat", 'r')
	if(len(subjects) == 0):
		for line in f:
			subjects.append(line)

def getAllHTML():
	if not subjects:
		getSubjects()
	for subject in subjects:
		if(not dryRun):
			curURL = urlBase + subject
			req = urllib2.Request(curURL, None, headers)
			try:
				response = urllib2.urlopen(req)
			except Exception as e:
				print "Url grab failed for " + subject + "\n"
				sys.exit()

			code = response.getcode()
			if(code == "404"):
				html = ''
				print "grabbing " + subject + "failed! 404\n"
			else:
				html = response.read()
				print "grabbing " + subject + "successful!\n"

			soup = BeautifulSoup(html)
			allTRs = soup.find_all('tr', 'dgdClassDataEnrollCap')
			allAllTRs.append(allTRs)

		else:
			print subject
	print allAllTRs

def get1HTML():
	subjects = ["COM+SCI"]
	for subject in subjects:
		if(not dryRun):
			curURL = urlBase + subject
			req = urllib2.Request(curURL, None, headers)
			try:
				response = urllib2.urlopen(req)
			except Exception as e:
				print "Url grab failed for " + subject + "\n"
				sys.exit()

			code = response.getcode()
			if(code == "404"):
				html = ''
				print "grabbing " + subject + "failed! 404\n"
			else:
				html = response.read()
				print "grabbing " + subject + "successful!\n"

			soup = BeautifulSoup(html)
			allAllTRs.append(soup)

		else:
			print subject
	print allAllTRs

get1HTML()