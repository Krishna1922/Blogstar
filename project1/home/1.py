import requests

#the required first parameter of the 'get' method is the 'url':
#x = requests.get('https://api.currentsapi.services/v1/latest-news')
r = requests.get('https://api.currentsapi.services/v1/latest-news', headers={'Authorization': '8D9YgSnRhndn-SCHsf8TMv4chnY3Xqe2IF6r_4gtuEDmKO7N'})
#print the response text (the content of the requested file):
d = r.json()
#print(dir(r))
news = d['news']
#print(news[0]['image'])
print(news[0]['category'])
print(news[1]['category'])
print(news[2]['category'])
print(news[3]['category'])
print(news[4]['category'])
print(news[5]['category'])
print(news[6]['category'])
print(news[7]['category'])
print(news[8]['category'])
print(news[9]['category'])
print(news[10]['category'])
