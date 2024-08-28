
## DictDB - A CLI Database 

A Python CLI project. 

DictDB uses Pyton Dictionary to mimic MySQL like Database. 



### Features 

It can handle the below SQL-like operations: 

- SELECT     - Fetch Data 
- SELECTALL  - Get All Data
- INSERT     - Insert INT/STR
- INSERTLIST - Insert List 
- INCREMENT  - Increment INT
- APPEND     - Append List in Existing List 
- DELETE     - Delete Any Key 
- UPDATE     - Update INT/STR 
- UPDATELIST - Update List 
- STATUS     - All Command Status 


### Learnings 

Implemented the knowledge of SQL/MySQL to develope a CLI project to mimic the MySQL internals. It was super benefitial for to in my initial days 
of learning SQL. As I had to learn a lot of MySQL internals to build the project, I also gained super handson knowledge and data manipulation on Python.  


### How To Run 

Please clone the repository, and and run `python dict_db.py`. 


### Commands 

* Dict_DB needs three `semicolon` in the command.
<br>


      Command Lists.  Commands are case-insensitive. 

      Data Types - INT, STR, LIST 

      Key Only Commands: SELECT, DELETE  [Example: command;key;; ]

      Key, Value Commands: INSERT, UPDATE, INCREMENT, DECREMENT, INSERTLIST, APPEND, UPDATELIST  [Example: command;key;value;data_type]

      Non Parameter Command: STATUS (all commands runtime status) [Example: status;;;]

      Note: Put three " ; " in the command. Do not give space after seimicolon. 

      Correct Command:  insert;name;My nam is Mahboob Alam.;str 

      Incorrect Command: insert;  name;  My nam is Mahboob Alam;  str | Notice the space after semicolon. Bad Command. 
      
 
<br>

- SELECT:      `select;key;;`
  
- SELECTALL:   `selectall;;;`
  
- INSERT:      `insert;key;value;datatype` `(INT/STR)`

- INSERTLIST:  `insertlist;key;value,value,value;list`
  
- INCREMENT:   `increment;key;value;int`
  
- APPEND:      `append;key;value,value,value;list`
  
- DELETE:      `delete;key;;`
 
- UPDATE:      `update;key;value;datatype` `(INT/STR)`
  
- UPDATELIST:  `updatelist;key;value,value,value;list`
   
- STATUS:       `status;;;`

<br>

### Image 

<br>

![Screenshot from 2024-08-28 09-18-57](https://github.com/user-attachments/assets/f732bbf3-8352-4cd5-9c54-d956fa89140a)

<br><br>
