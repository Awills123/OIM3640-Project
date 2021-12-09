from flask import Flask, render_template, request
from web_scraperFOX import return_FOX
from web_scraperCNN import return_CNN


app = Flask(__name__)
"""creates the homepage for our website"""
@app.route('/')
def index():  
   return render_template('index.html')

"""creates a page with all the content layed out"""
@app.route("/healthaggregator/", methods = ["GET"])
def aggregator():
      """uses the automated function to return all the data from CNN"""
      content = return_CNN()
      """uses the automated function to return all the data from FOX"""
      content1 = return_FOX()
      """adds both contents into one"""
      all_content = content + content1
      """prints all the content into the html page"""
      return render_template("healthaggregator.html",all_content = all_content)

"""creates a seperate page where the user can search a word in the title"""
@app.route("/search/")
def search():
      """This line creates the request for the user to input a search term"""
      search_term = request.args.get("q" , default= " " , type = str)
      content = return_CNN()
      content1 = return_FOX()
      all_content = content + content1
      """this line basically creates an anonymous function that filters all the content so that all words are lowercase and can be searchable"""
      filtered_content = list(filter(lambda article: search_term.lower() in article[0].lower(), all_content))
      return render_template("search.html", filtered_content = filtered_content)
if __name__ == "__main__":
   app.run(debug=True)


