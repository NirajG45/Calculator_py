from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    expression = ""
    error = None
    if request.method == 'POST':
        expression = request.form.get('expression')
        try:
            # Eval se calculation
            result = eval(expression)
        except:
            error = "Invalid Expression"
    return render_template('index.html', result=result, expression=expression, error=error)

if __name__ == '__main__':
    app.run(debug=True)
