from flask import Flask, render_template, request
import eng_to_ipa as p

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":

        text = request.form["text"]
        
        if text == "":
            return render_template("index.html", result="No text entered")
        
        result = p.convert(text)
        return render_template("index.html", result=result)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)