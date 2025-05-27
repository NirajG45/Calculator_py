from flask import Flask, render_template, request, session, jsonify
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key'

# Allowed characters for safe evaluation
allowed_chars_pattern = re.compile(r'^[0-9+\-*/. ()minmax,]+$')

# Custom evaluation with minmax function
def custom_eval(expr):
    def eval_minmax(args):
        return max(args) - min(args)

    # Process all minmax() instances
    while 'minmax' in expr:
        start = expr.find('minmax')
        open_paren = expr.find('(', start)
        close_paren = expr.find(')', open_paren)
        args_str = expr[open_paren + 1:close_paren]
        args = [float(x.strip()) for x in args_str.split(',')]
        val = eval_minmax(args)
        expr = expr[:start] + str(val) + expr[close_paren + 1:]
    
    # Evaluate final expression safely
    return eval(expr, {"__builtins__": None}, {})

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    expression = ""
    error = None

    # Initialize session history if not present
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        expression = request.form.get('expression', '').strip()

        if not expression:
            error = "Please enter an expression."
        elif not allowed_chars_pattern.match(expression):
            error = "Invalid characters in expression."
        else:
            try:
                result = str(custom_eval(expression))
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                session['history'].append({
                    'expression': expression,
                    'result': result,
                    'timestamp': timestamp
                })
                session.modified = True
                expression = result
            except Exception as e:
                print(f"Eval error: {e}")
                error = "Invalid mathematical expression or function."

    return render_template(
        'index.html',
        result=result,
        expression=expression,
        error=error,
        history=session.get('history', [])
    )

@app.route('/clear-history', methods=['POST'])
def clear_history():
    session['history'] = []
    return render_template(
        'index.html',
        result=None,
        expression="",
        error=None,
        history=[]
    )

@app.route('/get-history', methods=['GET'])
def get_history():
    return jsonify(session.get('history', []))

if __name__ == '__main__':
    app.run(debug=True)
