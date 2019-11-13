# NQueens

Solver for the N-Queens puzzle
[![Build Status](https://travis-ci.org/consvic/NQueens.svg?branch=master)](https://travis-ci.org/consvic/NQueens)

Reference code can be found here:
[N-Queen Solution](https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/)

## Description
What you'll find here is a somewhat basic implementation of the N-Queen puzzle, this version works with different Ns (not exclusively 8 as the original puzzle). 
- It prints the results numbered
- Uses *Postgresql* with *SQLAlchemy* to store the results in a DB but only if the results for that particular N haven't been previously stored
- The project is *Dockerized*
- It has some basic tests using *pytest* that test the functionality of some of the functions used (main thing is that it tests for several Ns, 8 ,4 ,7 & 9 to be precise)
- Tests are integrated with *TravisCI*

*** You need Docker to easily setup ***

## Code
### Let's setup first
First step (build docker images and list containers)

	docker-compose up --build -d && docker-compose ps

Now, let's go to the terminal shall we

	docker exec -it app bash

### Actual code
First you'll need to initialize the DB (very important!)

    python3 db.py

And now you can run the program

    python3 main.py


### Tests
If you want to run the tests run inside the container's terminal

    py.test
