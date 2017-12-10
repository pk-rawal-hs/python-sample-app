'''
	Refactoring Response to match the Hootsuite Media Library Response.
			
'''
#formats the media type as Hootsuite wants.
def getMediaType(mediaType):
	obj = {
		"gif"   : "AnimatedGif",
    	"image" : "Image",
    	"application": "Folder"
	}
	return obj.get(mediaType.split('/')[0], None)

#formats the mime type as Hootsuite wants.
def getMimeType(mimeType):
	obj = {
		"jpeg"  :"image/jpeg",
	    "jpg"   :"image/jpeg",
	    "png"   :"image/png",
	    "gif"   :"image/gif",
	    "vnd.google-apps.folder":"application/vnd.hootsuite.folder"
	}
	return obj.get(mimeType.split('/')[-1], None)
#refactoring original to match Hootsuite 

def makeOriginal(image):
	obj = {
		"url": image.get('webViewLink', None),
		"height": image.get('imageMediaMetadata').get('height', None),
		"width":	image.get('imageMediaMetadata').get('width', None),
		"sizeInBytes": image.get('size', None)
	}
	return obj

def checkIfItsCorrectType(re):
	if getMimeType(re.get('mimeType', None)) is None:
		return False
	else:
		return True

def makeResponse(redata, curr):
	refactoredData=[]
	cursor = {}
	for re in redata:
		if checkIfItsCorrectType(re):
			obj = {
				"id":   re['id'],
				"name": re['name'],
				"mediaType": getMediaType(re.get('mimeType', None)),
				"mimeType":  getMimeType(re.get('mimeType', None)),
				"original":  makeOriginal(re) if ('imageMediaMetadata' in re.keys()) else None,
				"thumbnail": None
			}
			refactoredData.append(obj)

	if curr is not None:
		cursor = {'next': curr}
	
	data = {'data':refactoredData, 'metadata':{'cursor': cursor}}
	return data





