from app import db
from models import Post

# create database and tables
db.create_all()

#insert

db.session.add(Post(title="The Chess Flamenguist", content="A new Chess Legen has born"))
db.session.add(Post(title="FSND", content="Full Stack Web Developer Nanodegree"))

db.session.commit()
