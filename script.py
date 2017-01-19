import urllib.request
import re

root = "http://www.freeviewnz.tv"
page = "/tvguide/whats-on/"
pattern = r''' data-original="(.*?)\?.*?"'''

print('Downloading '+root+page)
html = urllib.request.urlopen(root+page).read().decode('utf-8')
print('Finished Downloading')

resources = re.findall(pattern, html)

print('Downloading resources')
for resource in resources:
	filename = resource.split('/')[-1]
	print(filename)
	urllib.request.urlretrieve(root+resource, './downloads/'+filename)
print('Finished Downloading')

