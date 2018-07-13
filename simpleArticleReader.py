import newspaper
from newspaper import Article

#qUrl="https://solecollector.com/news/2018/05/off-white-air-jordan-1-i-unc-international-release-date-aq0818-148"
qUrl="https://solecollector.com/news/2018/02/nike-lebron-15-diamond-turf-deion-sanders"
article = Article(qUrl)

article.download()
article.parse()
print(article.authors)
print(article.text)

article.nlp()

print(article.keywords)
print(article.summary)

