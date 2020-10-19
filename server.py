from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)

# This option will cause Jinja to throw UndefinedErrors if a value hasn't
# been defined (so it more closely mimics Python's behavior)
app.jinja_env.undefined = StrictUndefined

# This option will cause Jinja to automatically reload templates if they've been
# changed. This is a resource-intensive operation though, so it should only be
# set while debugging.
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = 'ABC'

MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}


@app.route("/top-melons")
def top_melon_display():
    "Displays top voted melons"
    melons = MOST_LOVED_MELONS

    if "username" not in session:
        return render_template("homepage.html")
    else:
        session["username"] = request.args.get("username")

    return render_template("top-melons.html", 
                            username=session["username"], 
                            melons=melons)


@app.route("/")
def index():
    """Melon Favorites Homepage."""

    if "username" in session:
        return render_template("top-melons.html")
        #Checks if name is already in session, if so sends user to Top Melons pages
    else:
        return render_template("homepage.html")
        #If name not in session, stays on homepage to get name


@app.route("/")
def get_name():
    #Gets name from user, passes to a session to use on top_melons
    session["username"] = request.args.get["username"]

    return render_template("top-melons.html", username=session["username"])

# optional:
# @app.route("/love-melon")

# handles optional form from drop down menu in top melons
# takes POST request and gets melon from form
# increases num_loves count in MOST_LOVED_MELONS dictionary
# renders template thank-you.html
# Thank you should be personalized Thank you, [name]
# Should have a link back to top-melons page


if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
