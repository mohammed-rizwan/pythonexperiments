import newspaper

#cnn_paper = newspaper.build('https://edition.cnn.com/search/?q=nike')
#cnn_paper = newspaper.build('https://sneakernews.com/?s=nike')

sites = ['https://news.nike.com/search?search_terms=','https://weartesters.com/?s=','https://stockx.com/news/?s=','https://edition.cnn.com/search/?q=','https://sneakernews.com/?s='
		 'https://www.nicekicks.com/?s=', 'http://footwearnews.com/results/?q=', 'http://www.complex.com/search?q=','https://www.kicksonfire.com/?s=','https://solecollector.com/search?q=']

print (len(sites))

qString="air%20jordan"

articleCollection = []

for site in sites :
	qUrl = site + qString
	articleCollection.append(newspaper.build(qUrl))

print(len(articleCollection))

for art in articleCollection:
	print(len(art.articles))
	for article in art.articles:
		print(article.url)
