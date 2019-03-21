from flask import Flask, request, render_template
import controller
import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def indexPost():
    text = request.form['text']
    noSentences = request.form['Sentences']
    links = request.form['links']
    keyword = text.upper()
    response = controller.controller(keyword,int(links))
    content = summarizer.summController(noSentences)
    meta = []
    with open('meta.txt') as f:
        meta = f.read().splitlines()
        
    if response == "done":
        return render_template('index.html', keyword = keyword ,contents = content, meta = meta)
    else:
        return render_template('index.html', contents = "error")

if __name__=="__main__":
    app.run(debug=True)