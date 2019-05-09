from app import db


class Article(db.Model):
    __tablename__: str = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=True)

    def __init__(self, data: dict = None):
        if data is not None:
            self.from_dict(data)

        self.from_dict(data)

    def __repr__(self):
        return f'<Article {self.id} {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

    def from_dict(self, data: dict):
        for key, value in data.items():
            if key != 'id' and value != '':
                setattr(self, key, value)
