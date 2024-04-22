from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
from statements import true_statements, false_statements

app = Flask(__name__) 

score = 0

def picking_statements(true_statements, false_statements):
    true_s = random.choice(true_statements)
    false_s = random.choice(false_statements)
    true_statements.remove(true_s)
    false_statements.remove(false_s)
    return [true_s, false_s]

def statment_order():
    order_top = random.randint(0, 1)
    if order_top == 0:
        order_bottom = 1
    else:
        order_bottom = 0
    return order_top, order_bottom  

@app.route('/')
def index():
    return render_template('start_page.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    global score
    if request.method == 'GET':
        statements = picking_statements(true_statements, false_statements)
        order_top, order_bottom = statment_order()
        return render_template('game_page.html', score=score, statements = statements, order_top = order_top, order_bottom = order_bottom)
    elif request.method == 'POST':
        if request.form.get('submit') == 'True':
            score = score + 1
        else:
            score = 0
        order_top, order_bottom = statment_order()
        statements = picking_statements(true_statements, false_statements)
    return render_template('game_page.html', score = score, statements = statements, order_top = order_top, order_bottom = order_bottom)

@app.route('/stats', methods=['GET'])
def stats():
    return render_template('stats_page.html')

if __name__ == '__main__':
    app.run(debug=True)