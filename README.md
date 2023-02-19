**0x00. AirBnB clone**

The goal of the project is to deploy a simple copy of the AirBnB website.

![logo airbnb clone](https://user-images.githubusercontent.com/111267046/217175544-dd115555-0e7f-43ed-b6e4-46b1bb80964e.png)


The web application is composed of:
 1. _A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)_
 2. _A website (the front-end) that shows the final product: static and dynamic_
 3. _A database or files that store data (data = objects)_
 4. _An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)_

**Description of the console**

 ![console image](https://user-images.githubusercontent.com/111267046/217175653-a1baa628-1aa2-40bb-a032-ff815e0f300d.png)

  
  This is the initial stage of the project whereby we aim to establish a method for managing the objects to be used by our web page through the implementation of a database in JSON format. We will apply object-oriented programming, data translation with Python, and command-line logic, we aim to develop a local database that can be modified via commands.
 
 **Prerequisites**

 Python3.4+ has to be installed if you desire to use the console:
  
  sudo apt-get install python3
  
 **Installation**
 
 To have access to the console use the following command:

 git@github.com:bjeptum/AirBnB_clone.git
  
 **Run**
  
 If you want to execute the console use: 
 python3 console.py or ./console.py
 
**How to start it**
*Interactive Mode*
$ ./console.py

Now you are on interactive mode and you will see the prompt (hbnb) input a command:

(hbnb) create User
the id of the created model will be visible in the standard output, if you do:

(hbnb) show User [id]
All the attributes of the created model will be in your screen.

use:

(hbnb) help
For a list of usable commands, to exit press Ctrl+D or type the command quit.

*Non-Interactive Mode*

The console can also be used in non-interactive mode:

$ echo "create User" | ./console.py
