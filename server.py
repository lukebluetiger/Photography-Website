from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


# using a special post id for specifics in links
@app.route("/")
def index():
    # templates are used for rendering html files, and need to be placed in the template folder
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/photos/landscapes")
def landscapes():
    return render_template('landscapes.html')


@app.route("/photos/portraits")
def portraits():
    return render_template('portraits.html')


@app.route("/thankyou")
def thankyou():
    return render_template('thankyou.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou")
    else:
        return 'something went wrong. please try again'

# using our dictionary of data to write to a file containing our data


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        name = data["name"]
        email = data["email"]  # collecting data from dict
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)  # using csv to write our data
        csv_writer.writerow([name, email, message])


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):

    # defining function
    return render_template("404.html")
