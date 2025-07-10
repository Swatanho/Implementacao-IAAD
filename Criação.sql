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


-- PROGRAMAÇÃO DE FILMES -- 


-- Inserção dos dados na tabela Canal
INSERT INTO Canal (num_canal, nome) VALUES
(111, 'AXN'),
(222, 'HBO'),
(333, 'Cinemax'),
(444, 'TNT');

-- Inserção dos dados na tabela Filme
INSERT INTO Filme (num_filme, nome, ano, duracao) VALUES
(90001, 'Avatar', 2022, 164),
(90002, 'Titanic', 1997, 194),
(90003, 'Star Wars', 2019, NULL),
(90004, 'Vingadores Ultimato', 2019, 180),
(90005, 'Lilo & Stitch', 2025, 108);

-- Inserção dos dados na tabela Exibicao
INSERT INTO Exibicao (num_filme, num_canal, data_exibicao, hora_exibicao) VALUES
(90001, 222, '2025-06-27', '14:00:00'),
(90002, 111, '2025-06-27', '19:45:00'),
(90003, 333, '2025-06-28', '09:30:00'),
(90003, 333, '2025-06-28', '20:30:00'),
(90005, 222, '2025-08-03', '16:20:00'),
(90005, 333, '2025-08-03', '16:20:00');

-- Inserção dos dados na tabela Elenco
-- TRUE = personagem principal, FALSE = personagem secundário

INSERT INTO Elenco (num_filme, nome_ator, protagonista) VALUES
-- Elenco de Avatar
(90001, 'Sam Worthington', TRUE),
(90001, 'Zoe Saldana', TRUE),
(90001, 'Sigourney Weaver', FALSE),
-- Elenco de Titanic
(90002, 'Leonardo DiCaprio', TRUE),
(90002, 'Kate Winslet', TRUE),
(90002, 'Billy Zane', FALSE),
-- Elenco de Star Wars
(90003, 'Daisy Ridley', TRUE),
(90003, 'Adam Driver', TRUE),
(90003, 'John Boyega', FALSE),
-- Elenco de Vingadores Ultimato
(90004, 'Robert Downey Jr.', TRUE),
(90004, 'Chris Evans', TRUE),
(90004, 'Scarlett Johansson', TRUE),
(90004, 'Mark Ruffalo', FALSE),
-- Elenco de Lilo & Stitch
(90005, 'Chris Sanders', TRUE),  -- Voz do Stitch
(90005, 'Maia Kealoha', TRUE);
