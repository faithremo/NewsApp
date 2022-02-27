from app import app
from flask import render_template    


from .utils import get_latest_news 

@app.route('/')
def say_hello():
    user = {"name": "New User"}
    return render_template("index.html", user=user)    



@app.route('/news')
def news_headlines():
    news_articles = get_latest_news()
    return render_template("news.html", news_articles=news_articles)







    