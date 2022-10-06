from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a sample Python Web App running on Flask Framework!! Random testing is a black-box software testing technique where programs are tested by generating random, independent inputs. Results of the output are compared against software specifications to verify that the test output is pass or fail.[1] In case of absence of specifications the exceptions of the language are used which means if an exception arises during test execution then it means there is a fault in the program, it is also used as a way to avoid biased testing."


