from flask import Flask, render_template, request
from web_scraperFOX import parse_html, download_page, DOWNLOAD_URL
from web_scraperCNN import parse_html1, download_page, DOWNLOAD_URL


app = Flask(__name__)
@app.route('/')
def index():  
   return render_template('index.html')


@app.route("/healthaggregator/", methods = ["GET"])
def aggregator():
      content = parse_html(download_page(DOWNLOAD_URL).read())
      content1 = parse_html1(download_page(DOWNLOAD_URL).read())
      return render_template ("healthaggregator.html",content = content, content1 = content1)

if __name__ == "__main__":
   app.run(debug=True)


