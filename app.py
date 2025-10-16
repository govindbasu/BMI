from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height')) / 100  # Convert cm to meters
        
        if weight <= 0 or height <= 0:
            return jsonify({'error': 'Weight and height must be positive numbers'}), 400
            
        bmi = weight / (height * height)
        
        if bmi < 18.5:
            category = 'Underweight'
            category_class = 'underweight'
        elif 18.5 <= bmi < 25:
            category = 'Normal weight'
            category_class = 'normal'
        elif 25 <= bmi < 30:
            category = 'Overweight'
            category_class = 'overweight'
        else:
            category = 'Obese'
            category_class = 'obese'
            
        return jsonify({
            'bmi': round(bmi, 1),
            'category': category,
            'category_class': category_class
        })
        
    except (ValueError, TypeError):
        return jsonify({'error': 'Please enter valid numbers'}), 400

if __name__ == '__main__':
    app.run(debug=True)
