from app import db


class Article(db.Model):
    __tablename__: str = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=True)

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
        }
