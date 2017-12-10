import requests
import httplib2

import mediaLibraryComponent.utils as u
import googleDrive.credentials as google

from apiclient import discovery
from oauth2client import client

#get google drive data
def getGoolgeDriveData(parentId):
	q=''
	if parentId is not None:
		q = "\'{}\' in parents".format(str(parentId))
	return q 

#search google drive data
def searchGoogleDriveData(search):
	q=''
	if search is not None:
		q = q + "name contains \'{}\'".format(search)
	return q

def sendRequest(query, cursor):
	credentials = google.get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('drive', 'v3', http=http)
	results = service.files().list(q=query, fields='*', pageToken=cursor).execute()
	curr = results.get('nextPageToken', None)
	items = results.get('files', [])
	print(items)
	refactoredData = u.makeResponse(items, curr)
	return refactoredData

def fetchGoogleDriveData(payload):
	search = payload.get('search')
	cursor = payload.get('cursor')
	parentId = payload.get('parentId')

	parent_q = getGoolgeDriveData(parentId)
	search_q = searchGoogleDriveData(search)

	if (parent_q != '') and (search_q != ''):
		query = parent_q + ' and ' + search_q
	elif parent_q != '':
		query = parent_q
	elif search_q != '':
		query = search_q
	else:
		query = ''

	return sendRequest(query, cursor)



