from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
@app.route("/")
def home2():
  return render_template("homepage.html")
@app.route('/form', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       first_name = request.form.get("fname")
       last_name = request.form.get("lname")
       return "Your name is "+first_name +" "+ last_name
    return render_template("form.html")
if __name__ == "__main__":
  app.run()