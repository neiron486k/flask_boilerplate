from flask import Blueprint, request, jsonify
from app.article.models import Article
from app import db

article = Blueprint('article', __name__)


@article.route('/')
def index():
    return 'home'


@article.route('/articles/<int:article_id>', methods=['GET'])
def get(article_id: int):
    art: Article = Article.query.get(article_id)

    if art is None:
        return jsonify({'message': 'not found'}), 404

    return jsonify(art.to_dict())


@article.route('/articles', methods=['GET'])
def collection():
    return jsonify([art.to_dict() for art in Article.query.all()])


@article.route('/articles', methods=['POST'])
def post():
    data = request.get_json()
    art: Article = Article(data)
    db.session.add(art)
    db.session.commit()
    return jsonify(art.to_dict())


@article.route('/articles/<int:article_id>', methods=['PATCH'])
def update(article_id):
    art = Article.query.get(article_id)
    data = request.get_json()
    art.from_dict(data)
    db.session.commit()
    return jsonify(art.to_dict())


@article.route('/articles/<int:article_id>', methods=['DELETE'])
def delete(article_id: int):
    art: Article = Article.query.get(article_id)

    if art is None:
        return jsonify({'message': 'not found'}), 404

    db.session.delete(art)
    db.session.commit()
    return jsonify(art.to_dict())
