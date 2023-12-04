


USE Libri;

CREATE TABLE Libro(
ID int primary key,
Titolo varchar(255) ,
Autore varchar(255) ,
Editore varchar(255) ,
Genere varchar(255) ,
CopieDisponibili int 

);

INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (0, '1984', 'George Orwell', 'Feltrinelli', 'SperoFantascienza', 5);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (1, 'Le notti Bianche', 'Fëdor Dostoevskij', 'Tarantola', 'Romantico', 8);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (2, 'Memorie dal Sottosuolo', 'Fëdor Dostoevskij', 'Feltrinelli', 'Psicologico', 7);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (3, 'Il Giocatore', 'Fëdor Dostoevskij', 'Zanichelli', 'Romanzo', 17);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (4, 'Violence', 'Slavoj Žižek', 'Mondadori', 'Sociologia', 10);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (5, 'Thinking fast and Slow', 'Daniel Kahneman', 'Feltrinelli', 'Psicologia', 7);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (6, 'Il Libretto Rosso', 'Mao Tse-Tung', 'Fiori d Asia Editrice', 'Sociologia', 13);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (7, 'La Metamorfosi', 'Franz Kafka', 'Mondadori', 'Narrativa', 9);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (8, 'Signor Malaussène', 'Daniel Pennac', 'Feltrinelli', 'Romanzo', 5);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (9, 'La Locandiera', 'Carlo Goldoni', 'Rizzoli', 'Commedia', 3);
INSERT INTO Libro (ID, Titolo, Autore, Editore, Genere, CopieDisponibili) VALUES (10, 'Aforismi', 'Oscar Wilde', 'Newton', 'Opere Morali', 11);