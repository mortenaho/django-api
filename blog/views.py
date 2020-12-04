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


@csrf_exempt
def post_insert(request):
    try:
        post = Post()
        post.title = request.POST.get("title")
        post.description = request.POST.get("description")
        post.author = Author.objects.get(pk=request.POST.get("author"))
        post.thumb = request.POST.get("thumb")
        post.save()
        return HttpResponse("200")
    except NameError:
        return HttpResponse("500")


@csrf_exempt
def post_edit(request):
    try:
        post = Post()
        post.id = request.POST.get("id")
        post.title = request.POST.get("title")
        post.description = request.POST.get("description")
        Post.objects.filter(id=post.id).update(title=post.title, description=post.description)
        return HttpResponse("200")
    except NameError:
        return HttpResponse("500")


@csrf_exempt
def post_delete(request):
    try:
        id = request.POST.get("id")
        Post.objects.filter(id=id).delete()
        return HttpResponse("200")
    except NameError:
        return HttpResponse("500")
