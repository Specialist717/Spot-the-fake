# Spot The Fake

Spot The Fake is an engaging web-based game that challenges players to discern the truth from a sea of falsehoods. The game presents players with a series of statements, and their task is to determine whether each statement is true or false.

### Technologies Used
This project is built with Python and Flask, a lightweight and powerful web framework that is a joy to use. Flask's simplicity and flexibility allow it to adapt to projects of all sizes, and it has been a perfect fit for this game.

The game's user interface is built with HTML and CSS, technologies that form the backbone of the web. The clean and intuitive interface makes the game easy and fun to play.

JavaScript is used to enhance the interactivity of the game, providing immediate feedback to the player's choices and creating a dynamic gaming experience.

### Why Spot The Fake?
In an era of information overload, the ability to distinguish fact from fiction has never been more important. Spot The Fake not only provides a fun and engaging way to pass the time, but also helps to sharpen this critical skill.

Whether you're a trivia buff, a fan of brain teasers, or just someone looking for a fun way to challenge yourself, Spot The Fake is the game for you. So why wait? Jump in and see if you can spot the fake!


## Little demonstation

<p align="center">
  <img alt="Starting screen" src="./showcase pictures/StartScreen.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Good answe" src="./showcase pictures/GoodAnswer.png" width="45%">
</p>

## Project Structure

The project has the following structure:

- `app.py`: This is the main Python script that runs the web application.
- `statements.py`: This script contains the true and false statements used in the game.
- `templates/`: This directory contains the HTML templates for the game.
- `static/`: This directory contains static files like CSS and images.
- `instance/`: This directory contains instance-specific configuration files.
- `venv/`: This directory contains the Python virtual environment for the project.

## How to Run

1. Activate the virtual environment:
```source venv/Scripts/activate```
2. Run the application:
```python app.py```
3. The application will start on localhost:5000.

## How to Play
Navigate to the home page and click on 'Start Game'. You will be presented with a statement. Click the button with, in your opinion, a true statement. Test your ability to distinguish fact from falsehood. If you succeed your score will be increased.

## Plans for the future
- Adding statistics page.
- Expansion of the question base.
