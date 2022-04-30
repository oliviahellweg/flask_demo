from flask import Flask
from flask import render_template, request

app = Flask(_name_)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float (form['radius'])
        height = float (form['height'])
        PI=3.14
        Labor=15
        Material=25

        TankTop=PI*(radius*radius)
        TankSides=(PI*(radius*height)*2)
        TotalAreaIn=TankTop+TankSides
        TotalSqft=TotalAreaIn/144

        MaterialCost=TotalSqft*Material
        LaborCost=TotalSqft*Labor

        estimate=MaterialCost+LaborCost
        return render_template('index.html', data=estimate)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
