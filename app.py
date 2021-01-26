import random
import string
from flask import Flask, request, render_template, flash, escape, send_from_directory, url_for
from werkzeug.exceptions import HTTPException
from MonteCarlo_Calculator import MonteCarlo
from helpers import is_valid_number

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=30))


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        mode = request.form.get("radio")
        monte_carlo_N = escape(request.form.get("MonteCarlo_N"))

        # Confirm both forms are filled
        if (mode is not None) and (monte_carlo_N is not None):
            # Confirm both values are valid
            if is_valid_number(monte_carlo_N) and (mode in set(["integer", "decimal"])):
                monte_carlo_N = int(monte_carlo_N)
                if mode == "decimal":
                    mode = 0
                elif mode == "integer":
                    mode = 1
                else:  # Generally not happen
                    mode = 1
                estimated_pi, figdata = MonteCarlo(monte_carlo_N, mode)
                return render_template(
                                        "result.html",
                                        estimated_pi=estimated_pi,
                                        monte_carlo_N=monte_carlo_N,
                                        figdata=figdata
                                      )
            else:
                flash("入力された値が不正です。", category="alert alert-danger")
        else:
            flash("値を入力してください。", category="alert alert-danger")

    return render_template("index.html")


@app.errorhandler(HTTPException)
def error_handler(e):
    print(f"HTTP Error: {e.code} {e.name}")
    return render_template("http_error.html", error_name=e.name, status_code=e.code)


if __name__ == "__main__":
    app.run(debug=0)
