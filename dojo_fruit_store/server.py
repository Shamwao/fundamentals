from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    num_of_strawberries = request.form['strawberry']
    num_of_raspberries = request.form['raspberry']
    num_of_apples = request.form['apple']
    return render_template("checkout.html", first_name =first_name, last_name =last_name, student_id = student_id, num_of_apples = num_of_apples, num_of_strawberries = num_of_strawberries, num_of_raspberries = num_of_raspberries)
    count = int(num_of_apples) + int(num_of_raspberries)+ int(num_of_strawberries)
    print ("Charging " + request.form['first_name']+ "for" + count)
    
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    