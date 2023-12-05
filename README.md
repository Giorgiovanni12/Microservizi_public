The project aims to simulate the operation of a library.

By putting together 8 different microservices composed of these features: 

-AppBooks to perform CRUD operations on the db,it is also used as a kafka producer (it also sends an email when a new book is entered[use this one which is free https://app.brevo.com/])

-AppUsers always to perform CRUD operations to their db

-AppLenders always to perform CRUD operations to its own db

-DbBooks Db with all the books inside.

-DbUsers Db with all users inside.

-DbLoans Db with all loans inside.

-Kafka messaging broker with the purpose of alerting the user when certain operations are performed 

-AppConsumer is for the purpose of receiving notifications from the AppLibrary and printing them on the terminal

The project as a whole provides:

-CI/CD for publishing images directly to Docker-hub whenever a push is made to the repository and checking the code manually with pylint.

-Logging with the purpose of monitoring all actions by the container.The logs are saved inside the containers in a separate file.

-Testing through python's request library that tests each individual CRUD .

-Container use of dokcer and docker-compose to create all the individual containers.I also tried creating with kompose the configuration files but I have problems with vm :(

![Screenshot 2023-12-05 15 28 03](https://github.com/Giorgiovanni12/Microservizi_public/assets/129728209/d1c41600-1580-4a1c-877f-a97f0c2eb1ec)
