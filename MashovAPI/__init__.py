#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import modules
import requests
import datetime
import json

class MashovAPI:
	def __init__(self, username, **kwargs):
		# MashovAPI("201234567", password = "myPass", schoolID = 52110, schoolData = {...}, schoolName = "הכפר")
		self.url = "https://web.mashov.info/api/{}/"
		self.session = requests.Session()
		self.session.headers.update({'Accept': 'application/json, text/plain, */*',
									'Referer': 'https://web.mashov.info/students/login',
									'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
									'Content-Type': 'application/json'})
		self.username = username
		self.authID = 0
		# Kwargs password
		if "password" in kwargs:
			self.password = kwargs["password"]
		else:
			self.password = False
		# Kwargs schoolData
		if "schoolData" in kwargs:
			self.schoolData = kwargs["schoolData"]
		else:
			self.schoolData = False
		# Kwargs schoolID
		if "schoolID" in kwargs:
			self.schoolID = kwargs["schoolID"]
		elif not self.schoolData:
			self.schoolData = self.getSchools()
			self.schoolID = self.getSchoolIDByName(kwargs["schoolName"])
		self.currentYear = datetime.datetime.now().year

	def login(self):
		if not self.password:
			return False
		self.loginData = {'semel': self.schoolID,
							'username': self.username,
							'password': self.password,
							'year': self.currentYear,
							'appName': 'info.mashov.students',
							'apiVersion': '3.20200528',
							'appVersion': '3.20200528',
							'appBuild': '3.20200528',
							'deviceUuid': 'chrome',
							'devicePlatform': 'chrome',
							'deviceManufacturer': 'win',
							'deviceModel': 'desktop',
							'deviceVersion': '83.0.4103.61'}
		self.retData = self.send("login", "post", self.loginData)
		self.retText = json.loads(self.retData.text)
		if self.retData.status_code == 200:
			self.isLoggedIn = True
			self.authID = self.retText["credential"]["userId"]
			self.userID = self.authID
			self.uid = self.authID
			self.uID = self.authID
			self.guid = self.authID
			self.guID = self.authID
			self.schoolSite = self.retText["accessToken"]["schoolOptions"]["schoolSite"]
			self.moodleSite = self.retText["accessToken"]["schoolOptions"]["moodleSite"]
			self.schoolName = self.retText["accessToken"]["schoolOptions"]["schoolName"]
			self.lastName = self.retText["accessToken"]["children"][0]["familyName"]
			self.firstName = self.retText["accessToken"]["children"][0]["privateName"]
			self.className = str(self.retText["accessToken"]["children"][0]["classNum"]) + str(self.retText["accessToken"]["children"][0]["classCode"])
			self.lastPass = self.retText["accessToken"]["lastPassSet"]
			self.lastLogin = self.retText["accessToken"]["lastLogin"]
			self.schoolYears = self.retText["accessToken"]["userSchoolYears"]
			self.csrfToken = self.retData.cookies["Csrf-Token"]
			self.session.headers.update({"x-csrf-token" : self.csrfToken})
			self.userChildren = self.retText["accessToken"]["children"]
			return self.isLoggedIn
		else:
			self.isLoggedIn = False
			return self.isLoggedIn

	def getSchoolData(self):
		return self.schoolData

	def updateSchoolData(self):
		self.schoolData = self.formReturn(self.send("schools", "get"))
		return True

	def getSchools(self):
		self.updateSchoolData()
		return self.getSchoolData()

	def sendOTP(self, phoneNumber):
		if self.send("user/otp", "post", {"cellphone" : phoneNumber, "semel" : self.schoolID, "username" : self.username}).status_code == 200:
			return True
		else:
			return False

	def isLoggedIn(self):
		return self.isLoggedIn

	def getSession(self):
		return self.session

	def getUsername(self):
		return self.username

	def getPassword(self):
		return self.password

	def setSession(self, session):
		self.session = session
		return True

	def setUsername(self, username):
		self.username = username
		return True

	def setPassword(self, password):
		self.password = password
		return True
	
	def getSchoolIDByName(self, school):
		if self.schoolData:
			schoolData = self.schoolData
		else:
			schoolData = self.updateSchoolData()
		for schools in schoolData:
			if schools["name"].find(school) == 0:
				return schools["semel"]

	def getSchoolID(self):
		return self.schoolID
	
	def getYear(self):
		return self.currentYear

	def getUserID(self):
		return self.getAuthID()

	def getAuthID(self):
		return self.authID

	def getSchoolSite(self):
		return self.schoolSite
	
	def getMoodleSite(self):
		return self.moodleSite

	def getSchoolName(self):
		return self.schoolName

	def getFirstName(self):
		return self.firstName

	def getLastName(self):
		return self.lastName

	def getClassName(self):
		return self.className

	def getLastPasswordChange(self):
		return self.getLastPass()
		
	def getLastPass(self):
		return self.lastPass

	def getLastLogin(self):
		return self.lastLogin
	
	def getSchoolYears(self):
		return self.schoolYears

	def getCSRF(self):
		return self.getCSRFToken()

	def getCSRFToken(self):
		return self.csrfToken
	
	def getChildren(self):
		return self.userChildren

	def clearSession(self):
		return self.formReturn(self.send("clearSession", "get"))

	def getMailCount(self):
		return self.formReturn(self.send("mail/counts", "get"))

	def getBirthDate(self):
		return self.getBirthday()

	def getBirthdate(self):
		return self.getBirthday()

	def getBirth(self):
		return self.getBirthday()

	def getBirthday(self):
		return self.formReturn(self.send("user/{}/birthday".format(self.authID), "get"))

	def getBells(self):
		return self.formReturn(self.send("bells", "get"))

	def getClassmates(self):
		return self.formReturn(self.send("students/{}/alfon".format(self.authID), "get"))

	def getPicture(self):
		return self.send("user/{}/picture".format(self.authID), "get").content

	def getNotifications(self):
		return self.formReturn(self.send("user/notifications", "get", {"skip" : 0, "take" : "500"}))

	def getSpecialLessons(self):
		return self.getPrivateLessons()

	def getPrivateLessons(self):
		return self.formReturn(self.send("students/{}/specialHoursLessons".format(self.authID), "get"))

	def getPrivateLessonTypes(self):
		return self.formReturn(self.send("lessonsTypes", "get"))

	def getClasses(self):
		return self.getGroups()

	def getGroups(self):
		return self.formReturn(self.send("students/{}/groups".format(self.authID), "get"))

	def getBehave(self):
		return self.getBehavior()

	def getBehavior(self):
		return self.formReturn(self.send("students/{}/behave".format(self.authID), "get"))

	def getMashovGrades(self):
		return self.getGrades()

	def getGrades(self):
		return self.formReturn(self.send("students/{}/grades".format(self.authID), "get"))

	def getMoodleGrades(self):
		return self.formReturn(self.send("students/{}/moodle/assignments/grades".format(self.authID), "get"))

	def getAdjustments(self):
		return self.getHatamot()

	def getHatamot(self):
		return self.formReturn(self.send("students/{}/hatamot".format(self.authID), "get"))

	def getDrafts(self):
		return self.formReturn(self.send("mail/draft/conversations", "get", {"skip" : "0", "take" : "500"}))

	def getConversation(self, mailID):
		return self.getMailWithID(mailID)

	def getMailWithID(self, mailID):
		return self.formReturn(self.send("mail/conversations/{}".format(mailID), "get"))

	def createDraft(self):
		return self.formReturn(self.send("mail/conversations/draft", "put", {"isNew" : "true", "isDeleted" : "false", "body" : ""}))

	def getTeachers(self):
		return self.getRecipents()

	def getRecipents(self):
		return self.formReturn(self.send("mail/recipients", "get"))

	def attachFile(self, mailID, fileName):
		return self.mailAttach(mailID, fileName)

	def attachMail(self, mailID, fileName):
		return self.mailAttach(mailID, fileName)

	def mailAttach(self, mailID, fileName):
		return self.formReturn(self.send("lessonsTypes", "post", {}, {'file': open(fileName, 'rb')}))

	def toDate(self, dateString):
		return self.createDate(dateString)

	def createDate(self, dateString):
		return datetime.datetime.strptime(dateString, "%Y-%m-%dT%H:%M:%S")

	def getDate(self):
		return datetime.datetime.now().isoformat(timespec='seconds')

	def formReturn(self, response):
		if response.status_code != 200:
			return False
		else:
			try:
				return json.loads(response.text)
			except:
				return response.text

	def send(self, url, method = "get", params = {}, files = {}):
		return getattr(self.session, str(method).strip().lower())(self.url.format(url), data = json.dumps(params), files = files)

	def toString(self):
		return json.dumps({
		"MashovAPI" : {
			"url" : self.url,
			"sessionH" : dict(self.session.headers),
			"sessionC" : self.session.cookies.get_dict(),
			"username" : self.username,
			"password" : self.password,
			"schoolData" : self.schoolData,
			"schoolID" : self.schoolID,
			"currentYear" : self.currentYear,
			"loginData" : self.loginData,
			"isLoggedIn" : self.isLoggedIn,
			"authID" : self.authID,
			"userID" : self.userID,
			"uid" : self.uid,
			"uID" : self.uID,
			"guid" : self.guid,
			"guID" : self.guID,
			"schoolSite" : self.schoolSite,
			"moodleSite" : self.moodleSite,
			"schoolName" : self.schoolName,
			"lastName" : self.lastName,
			"firstName" : self.firstName,
			"className" : self.className,
			"lastPass" : self.lastPass,
			"lastLogin" : self.lastLogin,
			"schoolYears" : self.schoolYears,
			"csrfToken" : self.csrfToken,
			"userChildren" : self.userChildren
		}})

	def fromString(objString):
		# mashov = Mashov.fromString(stringFromToStringMethod)
		objDict = json.loads(objString)["MashovAPI"]
		username = objDict["username"]
		password = objDict["password"]
		schoolID = objDict["schoolID"]
		newObj = MashovAPI(username, password = password, schoolID = schoolID)
		newObj.url = objDict["url"]
		newObj.session = requests.Session()
		newObj.session.headers.update(objDict["sessionH"])
		newObj.session.cookies.update(objDict["sessionC"])
		newObj.schoolName = objDict["schoolName"]
		newObj.schoolData = objDict["schoolData"]
		newObj.currentYear = objDict["currentYear"]
		newObj.loginData = objDict["loginData"]
		newObj.isLoggedIn = objDict["isLoggedIn"]
		newObj.authID = objDict["authID"]
		newObj.userID = objDict["userID"]
		newObj.uid = objDict["uid"]
		newObj.uID = objDict["uID"]
		newObj.guid = objDict["guid"]
		newObj.guID = objDict["guID"]
		newObj.schoolSite = objDict["schoolSite"]
		newObj.moodleSite = objDict["moodleSite"]
		newObj.lastName = objDict["lastName"]
		newObj.firstName = objDict["firstName"]
		newObj.className = objDict["className"]
		newObj.lastPass = objDict["lastPass"]
		newObj.lastLogin = objDict["lastLogin"]
		newObj.schoolYears = objDict["schoolYears"]
		newObj.csrfToken = objDict["csrfToken"]
		newObj.userChildren = objDict["userChildren"]
		return newObj