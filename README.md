# Hackathon
Hackathon simulation  
This project is meant for me to expand my knowledge with mySql databases and connecting databases to Python scripts.  

This project is a simulation of a hackathon with separate areas for participants and developers.  

The participants can input the names of files that they submit for solutions. In an expanded version of this, the participants would have a webpage that they could upload files through and these files would be screened through a security process. The Python script then runs the file in a subprocess environment and analyzes the output to see if the solution is correct.  

The developers can input problems and solutions into a database. The Python script takes the input from the developers and uploads those into a SQL database. These inputs have been structured to prevent common forms of SQL injecting. In an expanded version of this project, the developers would have another webpage to upload files into.  

The SQL script appears as so:  
<img width="442" height="316" alt="image" src="https://github.com/user-attachments/assets/e8674920-b3bd-43c4-85ba-bd61e2aa6066" />
