from app import app
# import sys
# sys.path.insert(1,"C:\\Users\\vicky\\Flask\\iCode")
@app.route("/")
def maintenance():
    return "<h1>Under maintenance. Visit us again after 01-Oct-2020</h1>"