from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


# using a special post id for specifics in links
@app.route("/")
def index():
    # templates are used for rendering html files, and need to be placed in the template folder
    # able to read our username in the link and return it in the page
    return render_template('index.html')

# the components page just lists the html and css components used, and isn't accessed as a main page


# shortcut so we won't have to keep adding routes individually
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return 'something went wrong. please try again'

# using our dictionary of data to write to a file containing our data


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]  # collecting data from dict
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)  # using csv to write our data
        csv_writer.writerow([email, subject, message])
