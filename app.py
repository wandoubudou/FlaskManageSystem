from flask import Flask,render_template,send_file,request
from utils.register_check import check
from utils.login_check import login_check
from utils.reset_pwd import reset_pwd
from utils.get_staff_info import get_staff_detail
from utils.set_chart_data import set_data
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

@app.route('/charts')
def charts():
    total_data = set_data(False)

    return render_template('charts.html',
                           labels=total_data['labels'],
                           data=total_data['data'],
                           bar_labels=total_data['bar_labels'],
                           bar_data = total_data['bar_data'],
                           pie_labels  = total_data['pie_labels'],
                           pie_color = total_data['pie_color'],
                           pie_data = total_data['pie_data'],
                           )

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot-password.html',res="tnull")

@app.route('/login')
def login():
    return render_template('login.html',res="tnull")

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/register')
def register():
    return render_template('register.html',res="tnull")

@app.route('/tables')
def tables():
    data = get_staff_detail()
    return render_template('tables.html',data = data)



@app.route('/do_register',methods=['POST'])
def do_register():
    FirstName = request.form.get('FirstName')
    LastName = request.form.get('LastName')
    EmailAddress = request.form.get('EmailAddress')
    Password = request.form.get('Password')
    ConfirmPassword = request.form.get('ConfirmPassword')
    res = check(FirstName,LastName,EmailAddress,Password,ConfirmPassword)
    print("注册结果为 : ",res)
    if res=="Register Success...":
        return render_template("login.html", res=res)
    else:
        return render_template("register.html",res=res)


@app.route('/do_login', methods=["POST"])
def do_login():
    EmailAddress = request.form.get("EmailAddress")
    Password = request.form.get("Password")
    res = login_check(EmailAddress,Password)
    print("登陆结果为: " , res)
    if res == "Success...":
        return render_template('index.html')
    else:
        return render_template("login.html",res=res)


@app.route('/do_forget_password',methods=['POST'])
def do_forget_password():
    EmailAddress = request.form.get("EmailAddress")
    Password = request.form.get("Password")
    res = reset_pwd(EmailAddress,Password)
    if res=="Success...":
        return render_template("login.html",res=res)
    else:
        return render_template("forgot-password.html",res=res)


if __name__ == '__main__':
    app.run(port=5000, debug=True)