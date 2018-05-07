from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def add(weight, height):
    bmi = (int(weight)) / (int(height) * int(height))
    if bmi < 16:
        return str(bmi), "Severely underweight"
    elif 16 <= bmi < 18.5:
        return str(bmi), "Underweight"
    elif 18.5 <= bmi < 25:
        return str(bmi), "Normal"
    elif 25 <= bmi < 30:
        return str(bmi), "Overweight"
    else:
        return str(bmi), "Obese"

if __name__ == '__main__':
  app.run(debug=True)
