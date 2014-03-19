from django.shortcuts import render


import json


import os

JSON_FILE = 'tree.json'
def get_branch(slug):


	'''Grab data from json file '''


	def retrieve_json(file_name):
		jdata = open(file_name)
		data = json.load(jdata)
		jdata.close()
		return data



	data = retrieve_json(JSON_FILE)
	count = 0

	def find_slug_data(slug, dump):


		
		if isinstance(dump,list):

			for x in dump:
				if not find_slug_data(slug, x) == None:
					return find_slug_data(slug, x)
		if isinstance(dump,dict):

			if dump['slug'] == slug:
				return dump
			elif 'children' in dump.keys():
				return find_slug_data(slug, dump['children'])
			else:
				pass

		else:
			return None



	return find_slug_data(slug, data)





# Create your views here.
def home(request):
	return render(request,'myapp/home.html')





def slug(request, slug):

	slug_branch = get_branch(slug)
	if 'children' in slug_branch.keys():
		kids_tittle = [x['title'] for x in slug_branch['children']]
		kids_slug = [x['slug'] for x in slug_branch['children']]
		slug_branch.update({'kids_title':kids_tittle})
		slug_branch.update({'kids_slug':kids_slug})
		return render(request, 'myapp/topical.html', slug_branch)
	elif 'content' in slug_branch.keys():
		return render(request, 'myapp/content.html', slug_branch)
	else:
		return redirect('home')

