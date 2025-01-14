from flask import Flask,jsonify,request

app=Flask(__name__)

# initial data in tdl
items=[
    {"id":1,"name":"item1","description":"this is item1"},
    {"id":2,"name":"item2","description":"this is item2"}
]

@app.route("/")
def home():
    return "welcome to the sample todo list"

@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

# get:retreive specific item by id
@app.route("/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item=next((for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"message":"item not found"})
    return jsonify(item)

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id":len(it

if __name__ == "__main__":
    app.run(debug=True)
