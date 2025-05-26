from flask import Flask, render_template, request, session
import re

app = Flask(__name__)
app.secret_key = 'super-secret-key'

allowed_chars_pattern = re.compile(r'^[0-9+\-*/. ()minmax,]+$')

def custom_eval(expr):
    def eval_minmax(args):
        return max(args) - min(args)
    while 'minmax' in expr:
        start = expr.find('minmax')
        open_paren = expr.find('(', start)
        close_paren = expr.find(')', open_paren)
        args_str = expr[open_paren + 1:close_paren]
        args = [float(x.strip()) for x in args_str.split(',')]
        val = eval_minmax(args)
        expr = expr[:start] + str(val) + expr[close_paren + 1:]
    return eval(expr, {"__builtins__": None}, {})

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    expression = ""
    error = None
    if 'history' not in session:
        session['history'] = []
    if request.method == 'POST':
        expression = request.form.get('expression', '').strip()
        print("Expression received:", expression)
        if not expression:
            error = "Please enter an expression."
        elif not allowed_chars_pattern.match(expression):
            error = "Invalid characters in expression."
        else:
            try:
                result = str(custom_eval(expression))
                session['history'].append(f"{expression} = {result}")
                session.modified = True
                expression = result
            except Exception:
                error = "Invalid mathematical expression or function."
    return render_template('index.html', result=result, expression=expression, error=error, history=session.get('history', []))

@app.route('/clear-history', methods=['POST'])
def clear_history():
    session['history'] = []
    return render_template('index.html', result=None, expression="", error=None, history=[])

if __name__ == '__main__':
    app.run(debug=True)
