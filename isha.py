import requests,pprint
from bs4 import BeautifulSoup
a=requests.get('https://www.ishavidhya.org/photo-video/photos/category/4-nagercoil.html')
print (a)
b=BeautifulSoup(a.text,'html.parser')
image=b.findAll('div',class_='phocagallery-box-file')
celeb=[]

# details={'celebration':'','image_url':''}
for i in range(len(image)):
	details={'celebration':'','image_url':''}

	details['image_url']= ('https://ishavidhya.org/'+image[i].a['href'])

	name=b.findAll('div',class_='phocaname')
	celeb.append(name[i-1].text)
	
	details['celebration']=celeb[i]
	# pprint.pprint(details)
	pprint.pprint(details)