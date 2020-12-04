from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Author, Post
import json
# from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def posts(request):
    post = Post.objects.all()
    posts_serializers = serializers.serialize('json', post)
    post_json = json.loads(posts_serializers)
    data = json.dumps(post_json)
    return HttpResponse(data)
