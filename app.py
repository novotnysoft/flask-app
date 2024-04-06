from flask import Flask, render_template

app = Flask(__name__)

# pages index, kontakt atd...
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', nadpis='Blog')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html', nadpis='Kontakt')

# errors page urls 404, 500 atd....
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':  
   app.run()