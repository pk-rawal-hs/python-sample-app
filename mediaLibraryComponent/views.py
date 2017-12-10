from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt  

import mediaLibraryComponent.request as r
# Create your views here.

class MediaLibraryView(generic.View):

	def get(self, request):

		query    = request.GET.get('query', None)
		cursor 	 = request.GET.get('cursor', None)
		parentId = request.GET.get('parentId', None)
		payload = {'parentId': parentId, 'cursor': cursor, 'search': query}
		
		#getting data from Google Drive
		arrayData = r.fetchGoogleDriveData(payload)
		return JsonResponse(arrayData, safe=False)


