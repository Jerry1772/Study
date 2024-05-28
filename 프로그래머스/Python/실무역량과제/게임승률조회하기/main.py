from flask import Flask, json, request

app = Flask(__name__)

DATA_DIR = "./data/input/"

def read_json_file(file_name):
    with open(DATA_DIR+file_name,"r") as f:
        record = json.load(f)
    return record

@app.route("/api/gamerecord/users", methods=["GET"])
def get_users():
    record = read_json_file("records.json")
    record.sort(key=lambda x: (x["username"], x["tag"]))
    return [{
                "username": r["username"], 
                "tag": r["tag"]} 
            for r in record]

@app.route("/api/gamerecord/winrate", methods=["GET"])
def get_winrate():
    record = read_json_file("records.json")

    username = request.args.get("username")
    tag = request.args.get("tag")

    if username is None or tag is None:
        return {"error": "Invalid data format"}, 401
    
    content = None
    for r in record:
        if r["username"]==username and r["tag"]==tag:
            content = r
            break
    
    if content is None:
        return {"error": "data not found"}, 404
    
    return {
        "winrate": int(content["win"]/(content["win"]+content["lose"]))}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678)
