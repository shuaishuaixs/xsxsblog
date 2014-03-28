# -*- coding:utf-8 -*-

from django.http import HttpResponse,Http404
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404,redirect
from blog.models import Post,Tag
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

recent_post = ''
tag_list = ''

def get_right_content(func):
	def wrap(*args,**kwargs):
			global recent_post,tag_list
			recent_post = Post.objects.order_by('-pub_time')[:5]
			tag_list = Tag.objects.order_by('-id')
			return func(*args,**kwargs)
	return wrap		
		
	
def hello(request):
	raise Http404
	#return HttpResponse('hello world!')
	#return render_to_response('404.html')

@get_right_content
def home(request):
	'''home'''
	global post_list
	post_list = Post.objects.order_by('-pub_time')[:10]

	return render_to_response('home.html',{'recent_post':recent_post,'tag_list':tag_list,'post_list':post_list})


@get_right_content
def archive(request):	
	'''archive'''
	global post_list
	post_list = Post.objects.order_by('-pub_time')

	return render_to_response('archive.html',{'recent_post':recent_post,'tag_list':tag_list,'post_list':post_list})


@get_right_content
def project(request):
	'''project'''

	return render_to_response('project.html',{'recent_post':recent_post,'tag_list':tag_list})
	
	
@get_right_content
def about(request):
	'''about'''

	return render_to_response('about.html',{'recent_post':recent_post,'tag_list':tag_list})
	
@get_right_content
def tag(request, name):
	try:
		tag_info = Tag.objects.get(name = str(name).strip('/').decode('utf-8'))
	except Tag.DoesNotExist:
		raise Http404
	#code = sys.getfilesystemencoding()
	post_list = Tag.objects.get(name = str(name).strip('/').decode('utf-8')).post_set.all()


	return render_to_response('tag.html',{'recent_post':recent_post,'tag_list':tag_list,'post_list':post_list})
	
@get_right_content
def post(request,pid):
	global post
	post = get_object_or_404(Post,pk = pid.strip('/'))
	post = Post.objects.get(id = pid.strip('/'))

	return render_to_response('post.html',{'recent_post':recent_post,'tag_list':tag_list,'post':post})


def handler404(request):
	return render_to_response('404.html')

def handler500(request):
	return render_to_response('500.html')
