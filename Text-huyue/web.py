from flask import Flask,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from sql_mine import sql
import requests
import json


app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap = Bootstrap(app)
mysql=sql('data.db')
mysql.settable(people)
book_name=''
publish_date=''
writter=''
publisher=''

class say(FlaskForm):
    name = StringField('what is your name?',validators=[Required()])
    whatsay = StringField('what do you want to say?',validators=[Required()])
    number = StringField('你的学号',validators=[Required()])
    possward = StringField('你的密码（身份证后六位）',validators=[Required()])
    submit = SubmitField('submit')

class reseach(FlaskForm)
    youwant = StringField('what is your want?',validators=[Required()])

@app.route('/',methods = ['GET','POST'])
def index():
    name = None
    whatsay = None
    number = None
    possward = None
    youwant = None
    form = say()
    reseach = reseach()
    if form.validate_on_submit():
        name = form.name.data
        whatsay = form.whatsay.data
        number = form.number.data
        possward = form.possward.data
        youwant = form.youwant.data
        getbook(youwant)
        b=[]
        if yanzhen(number,possward):
            flash('用户名或密码错误')
        else:
            b=mysql.select("comment","book_name",book_name)
            mysql.insert("name,student_id,book_name,publish_date,writter,publisher,comment",name + number+book_name+publish_date+writter+publisher+whatsay)
        return redirect(url_for('index'))
    return render_template('index.html',form=form,reseach=reseach,comments=b,book_name=book_name,publish_date=publish_date,writter=writter,publisher=publisher)


def topeople(a):
    a["commnet_data"]=mysql.select("name,comment","book_name",a["book_data"]["book_name"])
    return a


def yanzhen(username,password):
    #验证用户名
    url = 'https://os.ncuos.com/api/user/token'
    data={
        'username':username,
        'password':password}
    headers = {'content-type': 'application/json'}
    r = requests.post(url,data=json.dumps(data),headers=headers)
    b =False
    if r.json()['message']=='获取成功'：
        b = True
    return b

def getbook(book_name):
    #该功能未完成

if __name__ == '__main__':
    app.run()
