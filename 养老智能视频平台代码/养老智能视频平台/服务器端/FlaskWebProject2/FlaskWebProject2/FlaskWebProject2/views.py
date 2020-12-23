"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,render_template,Response,request
from FlaskWebProject2 import app
import base64

jpg=b''
move=''
lr=''
wendu=''
shidu=''
Light=''
du=10

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jpg',methods={'POST'})
def get_jpg():
    global jpg,move
    jpg=request.form['jpg']
    ml=move
    move=''
    return ml

def gen():
    global jpg
    while(1):
        jpg1=base64.b64decode(jpg)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+jpg1+b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control_left',methods={'POST','GET'})
def control_left():
    global move
    move='左转'
    print(move)
    return move

@app.route('/control_right',methods={'POST','GET'})
def control_right():
    global move
    move='右转'
    print(move)
    return move

@app.route('/wendu',methods={'POST'})
def wd():
    global wendu
    wendu=request.form['wendu']
    return '1'

@app.route('/getwendu',methods={'POST','GET'})
def wd1():
    return wendu

@app.route('/shidu',methods={'POST'})
def sd():
    global shidu
    shidu=request.form['shidu']
    return '1'

@app.route('/getshidu',methods={'POST','GET'})
def sd1():
    return shidu


@app.route('/time',methods={'POST'})
def tm():
    global time
    time=request.form['time']
    return '1'

@app.route('/gettime',methods={'POST','GET'})
def tm1():
    return time

@app.route('/Light',methods={'POST'})
def li():
    global Light
    Light=request.form['Light']
    return '1'

@app.route('/getLight',methods={'POST','GET'})
def li1():
    return Light

@app.route('/huoyan',methods={'POST'})
def hy():
    global huoyan
    huoyan=request.form['huoyan']
    return '1'

@app.route('/gethuoyan',methods={'POST','GET'})
def hy1():
    return huoyan

@app.route('/duqi',methods={'POST'})
def dq():
    global duqi
    duqi=request.form['duqi']
    return '1'

@app.route('/getduqi',methods={'POST','GET'})
def dq1():
    return duqi


@app.route('/Setduojijia',methods={'POST','GET'})
def duojijia():
    global du
    if(du < 160):
        du+=10
    return str(du)

@app.route('/Setduojijian',methods={'POST','GET'})
def duojijian():
    global du
    if(du > 10):
        du-=10
    return str(du)

@app.route('/Getduoji',methods={'POST','GET'})
def duoji1():
    return str(du)

##接收
#@socketio.on('request_for_response')
#def send_lr(message):
#    global lr
#    while(1):
#        emit('response',{'code':'200','msg':str(lr)})
#        lr+=1
