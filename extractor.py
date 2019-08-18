import re
import requests

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