from flask import Flask,render_template, send_from_directory, request

app = Flask(__name__)


@app.route('/')
@app.route('/index.html/')
def index():
	return render_template("index.html")

    
@app.route('/<passcode>/')
def test(passcode):
        if passcode=="1":
		c1="This is 1st clue "
                return render_template("treasure_hunt.html" , data=c1)
	if passcode=="2":
		c2="This is 2nd clue"
		return render_template("treasure_hunt.html" , data=c2)
        
if __name__ == '__main__':
    app.run(debug=True)
