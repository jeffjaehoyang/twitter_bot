from flask import Flask, render_template, request, redirect
import sentence, os, tweet_generator
import datetime
 
app = Flask(__name__)
timestamp = None 

@app.route('/')
def main():
    global timestamp
    return render_template('index.html', sentence=sentence.run(), timestamp=timestamp)

@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
    status = request.form['status']
    tweet_generator.tweet(status)
    currentDT = datetime.datetime.now()
    global timestamp
    timestamp = currentDT.strftime("%Y-%m-%d, %H:%M")
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)