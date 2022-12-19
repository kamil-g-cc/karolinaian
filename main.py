from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/api/get_actor/<id>")
def get_actor(id):
    #data_manager.get_actor(id)
    result = {"id":id, "name": "Emily Clark", "age" : 37}
    return json.dumps(result)

@app.route("/")
def index():
    return """<h1>Welcome</h1>
    
    <script>
        function get_actor_details(id){
            fetch("/api/get_actor/"+id).then(response=>response.json()).then(response=>{
                //console.log(response)
                document.getElementById("actor").innerHTML=response.name+", "+response.age;
            })    
        }
    </script>

    <input type="button" onclick="get_actor_details(1234)" value="get data">
    <div id="actor">
    </div>
    
    """
