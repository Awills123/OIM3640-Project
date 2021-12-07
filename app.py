from flask import Flask, render_template, request
from web_scraperFOX import return_FOX
from web_scraperCNN import return_CNN


app = Flask(__name__)
@app.route('/')
def index():  
   return render_template('index.html')


@app.route("/healthaggregator/", methods = ["GET"])
def aggregator():
      content = return_CNN()
      content1 = return_FOX()
      all_content = content + content1
      return render_template("healthaggregator.html",all_content = all_content)

@app.route("/search/")
def search():
      search_term = request.args.get("q" , default= " " , type = str)
      content = return_CNN()
      content1 = return_FOX()
      all_content = content + content1
      filtered_content = list(filter(lambda article: search_term.lower() in article[0].lower(), all_content))
      return render_template("search.html", filtered_content = filtered_content)
if __name__ == "__main__":
   app.run(debug=True)


