from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    response = requests.get(f'https://api.deezer.com/search/track?q={search_term}')
    data = response.json()
    tracks = data['data']
    return render_template('search_results.html', tracks=tracks, search_term=search_term)

if __name__ == '__main__':
    app.run(debug=True)
