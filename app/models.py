from app import db

class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = False)
    lastName = db.Column(db.String(100), unique = False)

    def __str__(self):
        return f'{self.name} {self.lastName}'

    def __repr__(self):
        return f'{self.name} {self.lastName}'