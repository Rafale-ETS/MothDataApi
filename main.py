from datetime import datetime
from deta import Deta
from flask import Flask, request

dta = Deta()

# This will get all items in the given db that match the query dict 
# See Deta Base fetch for query behaviour.
def get_all_items(db: dta.Base, query: dict = None) -> list[dict]:
    res = db.fetch(query)
    items = res.items

    while res.last:
        res = db.fetch(query, last=res.last)
        items += res.items

    return items

dta_db_races = dta.Base("MothRaces")
dta_db_data = dta.Base("MothData")

app = Flask(__name__)

#@app.route('/', methods=["GET"])
#def base_route():
#    return "Unauthorized", 401

@app.route('/race', methods=["GET", "POST"])
def race():
    if request.method == "GET":
        return list_races()
    elif request.method == "POST":
        return add_race()
    else:
        return "Unauthorised method", 401
    
def list_races():
    # TODO: enable pagination of the results
    return get_all_items(dta_db_races)

def add_race():
    data = request.json

    saved_at = datetime.utcnow().timestamp()
    data["saved_at"] = saved_at

    # TODO: do some sanity checks and format validation
    ret_race = dta_db_races.insert(data)

    return {"status": "success", "key": ret_race["key"], "msg": f"New race with id {ret_race['key']} added."}

@app.route('/race/<id>', methods=["GET", "POST"])
def race_id(id):
    if request.method == "GET":
        return list_datapoints(id)
    elif request.method == "POST":
        return add_datapoint(id)
    else:
        return "Unauthorised method", 401

def list_datapoints(id):
    # TODO: enable pagination of the results
    return get_all_items(dta_db_data)

def add_datapoint(id):
    data = request.json

    data["race_id"] = id
    saved_at = datetime.utcnow().timestamp()
    data["saved_at"] = saved_at

    # TODO: do some sanity checks and format validation
    ret_data = dta_db_data.insert(data)

    return {"status": "success", "key": ret_data["key"], "race_id": ret_data["race_id"], "msg": f"New data for race with id {ret_data['race_id']} added."}

@app.route('/race/<id>/<data_id>', methods=["GET"])
def get_datapoint(id, data_id):
    return dta_db_data.get(data_id)
