import re
import requests

def  info():
	print("""
		-------------------------------
		-- Extract Emails from a URL --
		-------------------------------
		Example:-------------------------------------------
		import extract_email                            ---
		email = extract_email.extract(URL)              ---	
		# it will return a list containing all Emails   ---
		# present in the page at the URL provided.      ---
		---------------------------------------------------
		""")

def  extract(url):
	if url == '': return []
	res = requests.get(url)
	data = str(res.text)
	emails = []
	raw_emails = re.findall('\w+@\w+\.\w+', data)
	#removing duplicates

	for e in raw_emails:
		if (not e in emails):
			emails.append(e)
	print('Found ' + str(len(emails)) + ' Emails!')
	return emails