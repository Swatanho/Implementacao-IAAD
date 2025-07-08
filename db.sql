CREATE TABLE Canal (
num_canal INT NOT NULL PRIMARY KEY,
nome varchar(25)
);

CREATE TABLE Filme(
num_filme INT NOT NULL PRIMARY KEY,
nome varchar(255),
ano INT,
duracao INT NULL
);

CREATE TABLE Exibição (
FOREIGN KEY (num_filme) REFERENCES Filme(num_filme),
FOREIGN KEY (num_canal) REFERENCES Canal(num_canal),
data_exibição DATE,
hora_exibição TIMESTAMP
);

CREATE TABLE Elenco(
FOREIGN KEY (num_filme) REFERENCES Filme(num_filme),
nome_ator varchar(255),
protagonista bool
)