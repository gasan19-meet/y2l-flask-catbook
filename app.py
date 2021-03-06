from flask import Flask
from flask import render_template
from database import get_all_cats, get_cat_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cats(id):
	cat = get_cat_by_id(id)
	return render_template(
		'cat.html',cat=cat)
if __name__ == '__main__':
   app.run(debug = True)
@app.route('/create_cat')
def create_page():
	if request.method == 'GET':
		return render_template('create_cat.html')
	else:
		name=request.form['name']
		cats=get_all_cats()
		return reder_template('home.html',cats=cats)