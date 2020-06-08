
# Mashov Private API

[![](https://img.shields.io/badge/MashovAPI-Donate!-brightgreen?style=for-the-badge&logo=paypal)](https://paypal.me/xiddoc)

A Python wrapper for the Mashov private API. Supports both the app and web APIs.

## Overview

MashovAPI is a Python module which replicates the Mashov Private API, and turns the confusing mess into a simple module.
This project was mainly started in order to access Mashov's API, after concluding that no modules already exist for doing so. Simple tasks like erasing unneeded emails, marking notifications as read, and justifying wrongful behavior requests are all a hassle to do manually, so this module was built to assist with just that.

## Features

Almost everything the app has to offer! This includes emails, grades, logging in, and much more. More features are being added to Mashov, and in similar parallel, this module is also expanding to capture all of the new features. A few features might still be missing, but they will soon be added to the module!

## Install

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install MashovAPI.

How to install with pip:

``py -m pip install mashovapi``

To update:

``py -m pip install --upgrade mashovapi``

## Documentation

This module makes it super simple to use the Mashov API in Python! This is an example on how to get your birth date as a datetime object:
```python
# Import modules
from MashovAPI import MashovAPI

# Initialize MashovAPI class
mashov = MashovAPI("myStudentID", "myPassword", "mySchoolName")

# Log In
mashov.login()

# Check if logged in
if mashov.isLoggedIn == True:
    print("Logged In!")
else:
    print("Not logged in!")
    exit(1)

# Get birth date
returnData = mashov.getBirthday()["birthDate"]

# Turn string into datetime object
date = mashov.toDate(returnData)

# I was born on 1/1/2004
print("I was born on {}/{}/{}".format(date.day, date.month, date.year))
```

The ``MashovAPI(username, password, school)`` class has a lot of features, methods, and helpful tricks, including extra aliases for some methods. Here are most, if not all, of the methods that the MashovAPI class has to offer:
```python
def login():

# Attempts to log in to Mashov, returns True or False based on whether it is logged in after the function ends.

def isLoggedIn():

# Returns True or False based on whether the current object is logged in or not.

def getSession():

# Returns the Session object.

def setSession(session):

# Sets the object's Session to the inputted Session object.

def getUsername():

# Returns the user's username in plaintext.

def getPassword():

# Returns the user's password in plaintext.

def getSchoolIDByName(school):

# Returns the school's ID if found

def getSchoolID():

# Returns the user's school's Mashov ID

def getYear():

# Returns the current year.

def getUserID():

# Returns the user's authentication identity / code.

def getSchoolSite():

# Returns the link to the user's school's official website.

def getMoodleSite():

# Returns the link to the user's school's Moodle website.

def getSchoolName():

# Returns the user's school's full name.

def getFirstName():

# Returns the user's first name.

def getLastName():

# Returns the user's last name.

def getClassName():

# Returns the user's full class name.

def getLastPasswordChange():

# Returns the time string representing the timestamp of the last password change.

def getLastLogin():

# Returns the time string representing the timestamp of the last login.

def getSchoolYears():

# Returns an array of years for which the user's account has been activated.

def getCSRFToken():

# Returns the user's CSRF Token in plaintext.

def getChildren():

# Returns an array of the user's children, including themselves.

def clearSession():

# Clears the session, effectively logging out and rendering the current object useless until another log in.

def getMailCount():

# Returns a lot of different numbers about your mail, including- full mail count, deleted mail, and unread mail. 

def getBirthday():

# Returns the birth date as a dictionary, can be converted to a datetime object with the toDate() function.

def getBells():

# Returns the bell data, including their start and end time.

def getSchools():

# Returns a list of all the schools registered on the website.

def getClassmates():

# Returns lots of data on classmates, including their userID, phone number, and address.

def getPicture():

# Returns the picture data from your profile picture.

def getNotifications():

#

def getPrivateLessons():

# Returns private lesson history, vouched by teachers.

def getPrivateLessonTypes():

# Returns all the different high-leveled or school-based justifications.

def getClasses():

# Returns data on all subjects and classes in which the user takes or participates in.

def getBehavior():

#

def getGrades():

# Returns data on the user's grades.

def getMoodleGrades():

#

def getHatamot():

# Returns the list of scholar adjustments that the user has.

def getDrafts():

# Returns data on the user's written draft emails.

def getConversation(mailID):

#

def createDraft():

# Creates a new draft and returns data about it, including ID.

def getTeachers():

# Returns data on all emailable teachers, administrators, and other such workers.

def attachFile(mailID, fileName):

# WIP.

def toDate(dateString):

# Returns a datetime object built from the inputted time string.

def getDate():

# Returns a time string representing the current timestamp.

```
## Legal

Disclaimer: This is not affliated, endorsed or certified by Mashov. This is an independent and unofficial API. Strictly **not for spam**. Use at your own risk.

## License
[MIT](https://choosealicense.com/licenses/mit/)