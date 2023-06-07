import  scrapping
import utils
from dotenv import dotenv_values

config = dotenv_values(".env")

def get_topics(url):
    parsed_data = scrapping.scrapping(url)
    articles_topics = parsed_data.find_all('h4')

    topics_list = []
    keys = ['name', 'url']

    for topic in articles_topics:
      topic_data = topic.find('a')
      if topic_data == None:
          continue
      topics_list.append(utils.create_dict(
          keys
          , [topic_data.get_text(), topic_data.get('href')]
          )
        )
    
    return topics_list


def get_articles_list(topics_list):
    keys = ['name', 'url', 'topic' ]
    articles_list = []
    for topic in topics_list:
      parsed_topic_data = scrapping.scrapping(topic['url'])
      articles_list.append(utils.create_dict(
         keys,
         [
            parsed_topic_data.find('h1').get_text(),
            topic['url'],
            topic['name']
          ]
        )
      )
      articles_html = parsed_topic_data.find('ul', id='lcp_instance_0').find_all('a')
      for article in articles_html:
          articles_list.append(utils.create_dict(
          keys,
          [ article.get_text(), article.get('href'), topic['name']]
          )
        )
    
    return articles_list
    

def get_articles(articles_frame):
  articles_data = []
  for index, row in articles_frame.iterrows():
      article_data = scrapping.scrapping(row['url'])
      #remove unecessary data
      target_text = f'Best {row.name} Books'
      target_element = article_data.find('h2', string=target_text)
      if target_element:
          next_siblings = target_element.find_next_siblings()
          for sibling in next_siblings:
              sibling.extract()
          target_element.extract()
      #get article as text    
      row['article'] = article_data.get_text()
      articles_data.append(row)

  return articles_data