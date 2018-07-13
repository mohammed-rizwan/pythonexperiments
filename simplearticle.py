import newspaper

#cnn_paper = newspaper.build('https://sneakernews.com/?s=air%20jordan')
cnn_paper = newspaper.build('https://sneakernews.com/?s=nike')

for article in cnn_paper.articles:
	print(article.url)
