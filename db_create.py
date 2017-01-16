from app import db
from models import Post

# create database and tables
db.create_all()

#insert

db.session.add(Post(title="The Chess Flamenguist", description="A new Chess Legen has born"))
db.session.add(Post(title="FSND", description="Full Stack Web Developer Nanodegree"))

db.session.commit()
