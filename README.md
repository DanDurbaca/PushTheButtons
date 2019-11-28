# PushTheButtons
Repo for push the button game

Intro:

This is an overview of a PI (raspberry PI) project that we intend building inside our highscool. 
Our deadline is set for the open days (March 2020).


Description:

We would like to build a large push-buttons panel that are randomly turned on and then off by the user when he/she pushes them.
The aim of the game is to measure user’s reaction time: how many buttons can one turn off within a minute!


Implementation overview:

We intend using a raspberry PI that controls a set of LEDs and buttons through its GPIO connectors. Furthermore, we would like to log the user’s results into a database and display the historical results into a webpage. 


Database:

Our database should contain the following information: the user (some string up to 10 characters) that played the game, the number of buttons that he pressed and the date and time when he played. 
Extra fields may be added as the game evolves: at this point we only play the game for a 1 minute; later, we could play the game in a different mode – for two minutes for example. 

[Database Updates]
- The database dbms is SQLite to keep it neater and simpler than having to install Postgres or such. https://www.sqlite.org/download.html

- Added scores table - query `CREATE TABLE scores (score_ID INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(500), total_score INT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);`
- Added button logs table - query [TBA]


19th of dec - THIS video: https://www.youtube.com/watch?v=T1jdjmbe1mM&feature=youtu.be&t=2m38s 
does what we want to do with an Arduino Mega.

However, they have the same problem as us (LED not beeing too bright) - given that they turn off the lights when testing ++++

21st of dec - we would like to replace the LED from the Adafruit BigDome pushbutton with this LED - https://www.reichelt.de/led-5-mm-bedrahtet-warmweiss-11000-mcd-30-led-5-8000-ww-p107236.html?&trstct=pos_2 - notice the 11K mcd !


Details on the software implementation:

As of beginning of November we checked and managed to light up an LED, using raspberry PI. The code should be available soon enough in this github repository.


DB Library usage:
.. code:: py

    import dblib

    buttonHandler = buttonDBLib() # do this once
    buttonHandler.handleButton(BUTTON_ID)
    buttonHandler.handleButton(BUTTON_ID2)
    buttonHandler.handleButton(BUTTON_ID3)
    buttonHandler.endConnection() # run this when no longer needed
