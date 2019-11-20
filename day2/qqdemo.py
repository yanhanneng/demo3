from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = "author"
    # 添加id字段
    id = db.Column(db.Integer, primary_key=True)
    # 添加name字段
    name = db.Column(db.String(64), unique=True)

    """
    定义关系字段，方便查询
    author.books : 查看当前作者对象有那些书籍（list）
    book.author: 查询当前书籍属于哪个作者 （author对象）
    """
    books = db.relationship("Book", backref="author")

    def __repr__(self):
        return "author: %s %d" % (self.name, self.id)

class Book(db.Model):
    __tablename__ = "book"
    # 添加id字段
    id = db.Column(db.Integer, primary_key=True)
    # 添加name字段
    name = db.Column(db.String(64), unique=True)
    # 定义外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))

    def __repr__(self):
        return "book: %s %d" % (self.name, self.id)

@app.route("/")
def index():
    """书籍新增"""
    # if request.method == "GET":
    #     # authors = Author.query.all()
    #     return render_template("author_book.html")
    return "hello word"

    # if request.method == "POST":
    #     """新增书籍"""
    #     author_name = request.form.get("author")
    #     book_name = request.form.get("book")
    #     if not all([author_name,book_name]):
    #         print("参数错误")
    #         flash("参数错误")
    #         return
    #     author = Author.query.filter(Author.name == author_name).first()
    #     if not author:
    #         new_author = Author(name=author_name)
    #         db.session.add(new_author)
    #         db.session.commit()
    #         new_book = Book(name=book_name,author_id=new_author.id)
    #         db.session.add(new_book)
    #         db.session.commit()
    #     else:
    #         book = Book.query.filter(Book.name == book_name).first()
    #         if book:
    #             print("不能重复添加书籍")
    #             flash("不能重复添加书籍")
    #         else:
    #             new_book = Book(name=book_name,author_id=author.id)
    #             db.session.add(new_book)
    #             db.session.commit()
    #
    # authors = Author.query.all
    # return render_template("author_book.html",authors=authors)




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
