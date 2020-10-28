# pitch-App
## Author

[Jeff-Mwai](https://github.com/Jeff-Mwai)

# Description
Pitch App is an application that is developed using flask, and its main aim is to allow the users to register and create new pitches. The users can also comment on the pitches that are already there, like and dislike them. 

## Live Link
[View Site](https://pitches2020.herokuapp.com/)

## Figma Link
https://www.figma.com/file/y4fss7Vj4mN7N5RjsUjnqQ/Pitches?node-id=0%3A1

## User Story

* Register and login users.
* See the pitches posted by other uses.
* Select the different categories of pitches.
* Comment on the different pitches posted py other uses.
* Like a pitch by upvoting.
* Dislike a pitch by downvoting.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| The page loads | **On page load** | The user chooses between register and login|
| Select Register| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Email** and **password** | Redirect to home where one can choose between the different pitch categories|
| Select comment button | **Comment** | The user inputs a comment|
| Click on comment |  | Redirect to all comments tamplate with your comment and other comments|

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/Jeff-Mwai/Pitch-App.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Pitch-App
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.6 manage.py runserver
  ```
5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

In case of any issues, kindly email me at [jeffmwai3@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2019 **Jeffrey Mwai**