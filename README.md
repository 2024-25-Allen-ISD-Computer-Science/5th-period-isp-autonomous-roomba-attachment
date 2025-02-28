[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UcZhcxPD)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16671865)
# Linewriter - Drawing Robot
Drawing robot that uses an arduino, steppers, servos, and 3d printed parts. 
Follows an SVG as input. 
Code follows these steps:
1. Pulls svg data and parses it.
2. Tokenizes all the data 
3. Converts the svg commands into g-code commands
4. Uses a built in arduino function to makes the arduino follow the g-code.
