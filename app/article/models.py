from app import db, ma


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=True)

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        pass


class ArticleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'content')
