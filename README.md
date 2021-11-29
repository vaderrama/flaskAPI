## Flask API REST + MongoDB  

## Index:
---

- [Install + Run](#install)
- [Description](#descrip)
- [Functions](#functions)
- [Urls ](#urls)
- [Login with Token](#login)
- [Testing with Postman](#test)


<a name="install"></a>
## Install + Run ( Linux )
---



To install it + run it : 

`./run.sh`

or use : 

- sudo apt get update
- sudo apt install python3-pip
- sudo apt install python3-flask
- pip3 install -r requirements.txt


To launch it we only have to use

    $Flask run 

and it will be launched on our internal server

We can access from [127.000.1:5000]()

Enjoy ! 

#### In some operating systems it will be necessary in case of error in the JWT libraries, add the following command : `pip3 install cryptography`

<a name="descrip"></a>
## Description and context
---
Rest API that returns different data in JSON of the inventory of Materials of a company

<a name="functions"></a>
## Functions
- **Insert one ( receive a "name" params )** -> Insert a material in the database

- **Insert many ( recieve a JSON param )** -> Insert several materials in the database, check that they are not previously
- **Update ( receive a "name" param + JSON param  )** -> Updates the content of a material in the database, checking that it previously exists
- **Get one ( receive a "name" param )** -> Returns the data of an existing material in the database
- **Get All ()** -> Returns the data of all the materials in the database
- **Search ( recieve a JSON param )** -> Returns the data of the materials corresponding to a search using a JSON
- **Delete one ( receive a "name" param )** -> Eliminate a material from the database obtained through its index name
- **Delete All ()** -> Delete all materials from a database
- **Login ( receive a JSON param with credentials - user - password )** -> Generates the login token obtained through the verification of a username and password sent by JSON

<a name="urls"></a>
## Urls
---
Different accessible urls of our rest API : 

- 127.000.1:5000/material/login
- 127.000.1:5000/material/search
- 127.000.1:5000/material/delete_all
- 127.000.1:5000/material/delete_one/<name> 
- 127.000.1:5000/material/update/<car>
- 127.000.1:5000/material/insert_one
- 127.000.1:5000/material/get_one/<car>
- 127.000.1:5000/material/get_all
- 127.000.1:5000/material/insert

<a name="login"></a>
## Login with Token
---

In this app we use the /login function with a JWT token for identification.

When you launch the route "127.000.000: 5000 / login" you must send it with a JSON object that includes the access credentials, if these are correct a message of this type will be returned:

    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODE5Mjg0MywianRpIjoiNmZmMTg3NTItZWUxYi00ZGMwLThhMWMtNmY5ODQ5ZWMyNzcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNvbnN0ZWxsYSIsIm5iZiI6MTYzODE5Mjg0MywiZXhwIjoxNjM4MTkzNzQzfQ.jSbVzwq914wUspEV7FSHRrBJjbakxWWmZbyRgJHZqUw",
    "user_id": "constella"
    }

This token has an expiration time, so you must login again after a while.

To include it in the requests, we add a field "Authorization" in Postman and in value = "Bearer <JWTtoken>", being this way:

    Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODE5Mjg0MywianRpIjoiNmZmMTg3NTItZWUxYi00ZGMwLThhMWMtNmY5ODQ5ZWMyNzcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNvbnN0ZWxsYSIsIm5iZiI6MTYzODE5Mjg0MywiZXhwIjoxNjM4MTkzNzQzfQ.jSbVzwq914wUspEV7FSHRrBJjbakxWWmZbyRgJHZqUw

<a name="test"></a>
## Testing with Postman 
---

In this repository `test-collection.postman_collection` file is included where the different urls already created come to make the requests and check their correct operation, only need to change the token in headers 


