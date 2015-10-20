from __future__ import print_function, absolute_import
from flask import Flask, url_for, request

# Bind app to a Flask instance
app = Flask(__name__)


@app.route('/')  # the URL which triggers this function
def hello_world():
    return("Hello <i>you</i>. :-}")


# We can define variables in the arg. to `@app.route`
# syntax: `<[conv:]var>`
# Where `conv` is an optional converter function which is applied to `var`
# Existing converters are: `int`, `float` (self explanatory) and
# `path`, which also accepts slashes (`/`)
@app.route('/mirror/<var>')
def var_test(var):
    return var


@app.route('/slashend/')
def slashend():
    return "This also works without the slash at the end."


@app.route('/noslash')
def noslash():
    return "This doesn't work <i>with</i> a slash."

# `url_for(page)` "builds" the URL for `page`.
# This is a confusing way of saying that it figures out and returns
# the url for `page`. It doesn't create an url and doesn't allow us to bypass
# the hard-coding of urls in calls to the `route` decorator.
# It saves us from having to hard-code the URL for `page` elsewhere in the
# application, however.


@app.route('/method_page/', methods=['GET', 'POST'])
def methodz():
    # We can do different things depending on the HTTP request type.
    # The tutorial/quickstart guide uses the `request` object here but doesn't
    # mention that you need to import it from `flask`

    # We can't access the keyword arg. `methods` (given to the `route`
    # decorator) in here.
    if request.method == "GET":
        wut = dir(app)
        print(wut)
        # If we try returning 'wut' the app crashes with
        # 'list object not callable'. Returning `str(wut)` works fine, however.
        # > wut?
        return str(wut)
    else:
        return "This isn't the post office."


@app.route('/statics/')
def statics():
    # They've hard-coded the 'static' arg as a special case which makes it
    # go look in `static/`. Other strings get interpreted as page names.
    # (Which it looks for amongst the directory of the app I guess?)
    return url_for('static', filename='butts')


if __name__ == '__main__':
    # Run the application if this script was executed by the Python interpreter
    app.debug = True  # Don't do this in production.
    app.run()
