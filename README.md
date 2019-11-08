# PushTheButtons
Repo for push the button game

Intro:

This is an overview of a PI (raspberry PI) project that we intend building inside LPEM. 
Our deadline is set for the open days (March 2020).


Description:

We would like to build a large push-buttons panel that are randomly turned on and then off by the user when he/she pushes the it.
The aim of the game is to measure user’s reaction time: how many buttons can one turn off within a minute!


Implementation overview:

We intend using a raspberry PI that controls a set of LEDs and buttons through its GPIO connectors. Furthermore, we would like to log the user’s results into a database and display the historical results into a webpage. 


Database:

Our database should contain the following information: the user (some string up to 10 characters) that played the game, the number of buttons that he pressed and the date and time when he played. 
Extra fields may be added as the game evolves: at this point we only play the game for a 1 minute; later, we could play the game in a different mode – for two minutes for example. 


Details on the software implementation:

As of beginning of November we checked and managed to light up an LED, using raspberry PI. The code should be available soon enough in this github repository.

