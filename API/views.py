
import os
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from unauth.models import AuthModel
from .models import UrlModel
from .serializers import UrlSerializer


"""The view for redirect a short url to the original one"""
@api_view(['GET'])  
def Redirect(request, url):
        
        try:
            original_url = get_object_or_404(UrlModel, short_url=url).original_url
            return HttpResponseRedirect(redirect_to=original_url)
        except Http404:
            try:
                original_url = get_object_or_404(AuthModel, short_url=url).original_url
                return HttpResponseRedirect(redirect_to=original_url)
            except Http404:
                return render(request, "users/404.html")


@api_view(['POST'])  
def Shorten(request):

    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        returned_data = serializer.data.get('short_url')
        
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)