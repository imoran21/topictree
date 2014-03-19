import json




def get_branch(slug):


	'''Grab data from json file '''
	JSON_FILE = '/tree.json'


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




