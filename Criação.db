CREATE TABLE Canal (
    num_canal INT NOT NULL PRIMARY KEY,
    nome VARCHAR(25)
);

CREATE TABLE Filme(
    num_filme INT NOT NULL PRIMARY KEY,
    nome VARCHAR(255),
    ano INT,
    duracao INT
);

CREATE TABLE Exibicao (
    id_exibicao INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    num_filme INT NOT NULL,
    num_canal INT NOT NULL,
    data_exibicao DATE,
    hora_exibicao TIME,
    FOREIGN KEY (num_filme) REFERENCES Filme(num_filme),
    FOREIGN KEY (num_canal) REFERENCES Canal(num_canal),
    UNIQUE KEY (num_filme, num_canal, data_exibicao, hora_exibicao)
);

CREATE TABLE Elenco(
    id_elenco INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    num_filme INT NOT NULL,
    nome_ator VARCHAR(255),
    protagonista BOOLEAN,
    FOREIGN KEY (num_filme) REFERENCES Filme(num_filme)
);
