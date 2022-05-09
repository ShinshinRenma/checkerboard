from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template("index.html", x=8, y=8)

@app.route('/<x>/')
def modify_x_only(x):
    print(x)
    return render_template("index.html", column=int(x), row=8)

@app.route('/<x>/<y>')
def modify_xy(x,y):
    print(x)
    print(y)
    return render_template("index.html", column=int(x), row=int(y))


@app.route('/<x>/<y>/<color1>/<color2>')
def modify_xycolor(x,y, color1, color2):
    print(x)
    print(y)
    return render_template("index.html", column=int(x), row=int(y), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)