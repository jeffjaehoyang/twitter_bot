from flask import Flask, render_template, request, redirect, url_for
import sentence, os, tweet_generator
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', sentence=sentence.run())

@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
    status = request.form['status']
    tweet_generator.tweet(status)
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)