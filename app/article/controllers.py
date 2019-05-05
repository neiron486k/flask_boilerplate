from flask import Blueprint, request, jsonify
from app.article.models import Article, ArticleSchema
from app import db

article = Blueprint('article', __name__)
articles_schema = ArticleSchema(many=True)
article_schema = ArticleSchema()


@article.route('/')
def index():
    return 'home'


@article.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    return str(id)


@article.route('/articles', methods=['POST'])
def create_article():
    data = request.get_json()
    art = Article(data['title'], data['content'])
    db.session.add(art)
    db.session.commit()
    return article_schema.jsonify(art)


@article.route('/articles', methods=['GET'])
def get_articles():
    all_articles = Article.query.all()
    result = articles_schema.dump(all_articles)
    return jsonify(result.data)
