from flask import Flask, render_template, request, redirect
import sentence, os, tweet_generator
 
app = Flask(__name__)

@app.route('/')
def main():
    last_tweet_at = tweet_generator.fetch_timestamp()
    return render_template('index.html', sentence=sentence.run(), timestamp=last_tweet_at)

@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
    status = request.form['status']
    tweet_generator.tweet(status)
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)