from django.http import HttpResponse
from django.shortcuts import render
import operator
def sun(request):
	return render(request,'homepage.html')
	
def count(request):
	fulltext=request.GET['fulltext']
	list1=fulltext.split()
	listdictionary={}
	for word in list1:
		if word in listdictionary:
			listdictionary[word]+=1
		else:
			listdictionary[word]=1
	sortlist=sorted(listdictionary.items(),key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'counttext':sortlist})
def about(request):
	return render(request,'about.html')
