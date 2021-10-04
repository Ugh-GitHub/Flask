# Python REST API Server

Now that you have a handle on basic syntax, we're going to look more closely at how to apply that to making a server-side REST API that connects to a database. We will to build our server side in our new language, while our front-end client continues to be JavaScript.

## Objectives

  - explore server side frameworks for a new language
  - create a REST API in a new language
  - connect to and utilize a postgres database in a new language
  - document and share what you've learned in GitHub readme

## Web Stuff

Most programming languages aren't designed just to work on the web. 

While a simple command line Hello World is a great first step, getting a web application up is generally requires some extra libraries or packages. This is similar to like JavaScript requires Node and something like Express to run server-side. 

While there are generally many options for how to do this, we suggest you take a look at [Flask](http://flask.pocoo.org/)

Look for tutorials that help you to build a REST API. Specifically you'll need to know how to:

 - Make GET/POST/PUT/Delete requests
 - Get data from a POST body
 - Use parameters to send an id with PUT/DELETE
 
 > Focus on the server code, using Postman for testing your routes. 


## Databases

The last thing that we'll need to do is work with a database. Look for tutorials that show you how to connect to a Postgres database in your assigned language. Some tutorials will use an ORM (Object Relational Mapping) library. These are great tools to build some experience with.

Take a look at `psycopg2` for DB connection and queries.

Try to connect to a database and get some data. Use an existing database from an old class project, or create a simple database with a single table. 


## GitHub

Create a GitHub repository to share your basic API & database example. Make sure to comment the code to help others understand what is going on. Also include a Readme file with information on how to setup the database and run the project. You should also note any tutorials or resources you found helpful in the Readme.

When you are done, complete the assignment on the portal with your GitHub repo. 


