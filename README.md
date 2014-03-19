topictree
=========

Topic Tree


Project live @ topictree.herokuapp.com
_____________________________________________________________________________________________________________________________________________________________________________________________


The Task

You will create a Django project that allows the user to navigate around a hierarchical “topic tree”.  An example (small) topic tree could be something like:

The structure of the topic tree and content is stored in a “JSON” data structure, with the following format:
	
	
	{
	    "kind": "Topic",
	    "title": "Stories & Literature",
	    "slug": "stories-and-literature",
	    "children": [
	        {
	            "kind": "Topic",
	            "title": "Fairy Tales",
	            "slug": "fairy-tales",
	            "children": [
	                {
	                    "kind": "Text",
	                    "title": "Little Red Riding Hood",
	                    "slug": "little-red-riding-hood",
	                    "content": "Once upon a time there lived in a certain village…”
	                },
	                {
	                    "kind": "Text",
	                    "title": "The Emperor’s New Clothes",
	                    "slug": "emperors-new-clothes",
	                    "content": "Many years ago there was an Emperor…”
	                },
	{

        
        
The app should start by displaying the root node with a link to its children  (in the case of the example, the “Stories and Literature” node). Clicking through that link will display that node’s children, with links to its children etc. up until it reaches the leaf nodes where you display the content.
The full JSON file to use for your testing can be downloaded from here or viewed here. The “slug” field can be used to build URLs for the pages, and the “content” field is what gets displayed on the content page.
Note that this is a small topic tree; later, we will be testing your same code with larger topic trees, and it should be designed to work well for them too, without confusing the user or being slow.
Tip: You can use Python’s “json” module to load the contents of the topic tree file into a python structure (of dicts and lists).

_____________________________________________________________________________________________________________________________________________________________________________________________



I will highlight the main points of the code in my solution:

1) Get data from JSON dictionary
    I used a recursive function that takes in a slug value and returns the dictionary containing the slug value.
    
Here is this function

#views.py
---------------------------------------------------------------------------------------
'''get branch takes in a slug value and returns the dictionary it lives in'''
def get_branch(slug):


	'''Grab data from json file '''
	def retrieve_json(file_name):
		jdata = open(file_name)
		data = json.load(jdata)
		jdata.close()
		return data

	data = retrieve_json(JSON_FILE)


  # wrapper function to support importing without loading json data
	def find_slug_data(slug, dump):
    # if this is true then we are looking at a list of children dicts.
		if isinstance(dump,list):

			for x in dump:
			  # Find out if each child has the slug being passed
				if not find_slug_data(slug, x) == None:
					return find_slug_data(slug, x)
					
		if isinstance(dump,dict):
			if dump['slug'] == slug:
			  #success, exit recursion
				return dump
			elif 'children' in dump.keys():
				return find_slug_data(slug, dump['children'])
		else:
		  #no slug with that value exists
			return None

	return find_slug_data(slug, data)

-----------------------------------------------------------------

2) I  pass the dictionary returned by this function into my template. I use the slug value passed through my urls into my view.

In regards to design, I just linked to some external bootstrap CDNs and added a basic homepage+nav bar.

Any feedback is much appreciated

Thanks!
-Imran


