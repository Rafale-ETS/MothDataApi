from deta import Deta
from flask import Flask

#TODO: Move this to it's own module/file that handles database access
#       and data formatting.
dta = Deta()
dta_db = dta.Base("MothRaces")

app = Flask(__name__)

@app.route('/', methods=["GET"])
def base_route():
    return "Unauthorized", 401

@app.route('/race', methods=["GET"])
def list_races():
    return "TODO: return a list of the races"

@app.route('/race', methods=["POST"])
def add_update_race():
    return "TODO: add or update race in the database, return race_id."

@app.route('/race/<id>', methods=["GET"])
def list_datapoints(id):
    return f"TODO: return a list of datapoints for this {id} race."

@app.route('/race/<id>', methods=["POST"])
def add_datapoint(id):
    return f"TODO: add a datapoint to the database for the race {id}."

@app.route('/race/<id>/<data_id>', methods=["GET"])
def get_datapoint(id, data_id):
    return f"TODO: return the data for this specific race {id} and datapoint {data_id}."
