from app import app
from app.forms import PlayAgain
from flask import Flask, render_template, redirect, request, url_for
import random
import sys

def RPS(user_choice, computer_choice):
    if (user_choice == computer_choice):
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win! :)"
    elif (computer_choice == "Rock" and user_choice == "Scissors") or (computer_choice == "Paper" and user_choice == "Rock") or (computer_choice == "Scissors" and user_choice == "Paper"):
        return "Computer Wins. :("
    
def ResultsImageUser(user_choice):
    jpg = ".jpg"
    filename = ""
    images = ["Rock", "Paper", "Scissors"]
    i = 0
    for choice in images:
        if images[i] == user_choice:
            images = user_choice
            filename = user_choice.lower()
            filename += jpg
        i += 1
    return filename

def ResultsImageComputer(computer_choice):
    jpg = ".jpg"
    filename = ""
    images = ["Rock", "Paper", "Scissors"]
    i = 0
    for choice in images:
        if images[i] == computer_choice:
            images = computer_choice
            filename = computer_choice.lower()
            filename += jpg
        i += 1
    return filename

@app.route('/results', methods=['GET', 'POST'])
def results():
    form = PlayAgain()
    if request.method == 'POST':
        if request.form.get('Rock') == 'Rock':
            user_choice = 'Rock'
        elif request.form.get('Paper') == 'Paper':
            user_choice = 'Paper'
        elif request.form.get('Scissors') == 'Scissors':
            user_choice = 'Scissors'
    results_title = "Results"
    rps=["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(rps)
    user_image = ResultsImageUser(user_choice)
    computer_image = ResultsImageComputer(computer_choice)
    results = RPS(user_choice, computer_choice)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('results.html', computer_choice=computer_choice, results_title=results_title, user_choice=user_choice, results=results, user_image=user_image, computer_image=computer_image, form=form)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    index_title = "Welcome to Rock, Paper, Scissors!"
    return render_template('index.html', index_title=index_title)

