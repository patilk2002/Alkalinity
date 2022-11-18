# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        vol = request.form.get("vol")
        vol2 = request.form.get("vol2")

        # getting input with name = lname in HTML form
        # last_name = request.form.get("lname")
        #  return "Your name is "+first_name + last_name

        return "<div style='text-align:center;height:100px;width:500px;padding:50px 100px;border:2px solid;border-radius:10px;margin:0 auto;margin-top:200px;'><h2>The Alkalinity is : "+str((int(vol2)*0.02*50*1000)/int(vol))+" mg/L of CaCO3 </h2></div>"

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
