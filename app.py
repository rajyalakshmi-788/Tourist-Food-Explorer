from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Data
data = {
    "Hyderabad": [
        {"name": "Hyderabadi Biryani", "rating": "⭐⭐⭐⭐⭐"},
        {"name": "Haleem", "rating": "⭐⭐⭐⭐"},
        {"name": "Irani Chai", "rating": "⭐⭐⭐⭐"}
    ],

    "Delhi": [
        {"name": "Chole Bhature", "rating": "⭐⭐⭐⭐⭐"},
        {"name": "Jalebi", "rating": "⭐⭐⭐⭐"},
        {"name": "Butter Chicken", "rating": "⭐⭐⭐⭐⭐"}
    ],

    "Mumbai": [
        {"name": "Vada Pav", "rating": "⭐⭐⭐⭐"},
        {"name": "Pav Bhaji", "rating": "⭐⭐⭐⭐⭐"},
        {"name": "Bombay Sandwich", "rating": "⭐⭐⭐⭐"}
    ],

    "Chennai": [
        {"name": "Masala Dosa", "rating": "⭐⭐⭐⭐⭐"},
        {"name": "Idli", "rating": "⭐⭐⭐⭐"}
    ]
}

# API
@app.route("/foods/<city>")
def foods(city):
    return jsonify(data.get(city, []))

# Webpage
@app.route("/")
def home():
    return render_template_string("""

<!DOCTYPE html>
<html>
<head>
<title>Tourist Food Explorer</title>

<style>
body{
font-family:Arial;
background:linear-gradient(135deg,#1f4037,#99f2c8);
display:flex;
justify-content:center;
align-items:center;
height:100vh;
}

.app{
background:white;
padding:20px;
border-radius:15px;
width:320px;
}

button,select{
width:100%;
padding:10px;
margin-top:10px;
}

.food{
background:#f2f2f2;
padding:10px;
margin-top:10px;
border-radius:10px;
}
</style>

</head>

<body>

<div class="app">

<h2>🍽 Tourist Food Explorer</h2>

<select id="city">
<option value="">Select City</option>
<option>Hyderabad</option>
<option>Delhi</option>
<option>Mumbai</option>
<option>Chennai</option>
</select>

<button onclick="loadFoods()">Show Foods</button>

<div id="foods"></div>

</div>

<script>

async function loadFoods(){

let city=document.getElementById("city").value
let foodsDiv=document.getElementById("foods")

foodsDiv.innerHTML=""

if(city==="") return

let res=await fetch("/foods/"+city)
let data=await res.json()

data.forEach(food=>{

let div=document.createElement("div")
div.className="food"

div.innerHTML="<h3>"+food.name+"</h3><p>"+food.rating+"</p>"

foodsDiv.appendChild(div)

})

}

</script>

</body>
</html>

""")

if __name__ == "__main__":
    app.run(debug=True)