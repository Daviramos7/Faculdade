CREATE DATABASE MedicamentosDB;
USE MedicamentosDB;

CREATE TABLE Cliente (
    Cod_cli INT PRIMARY KEY,
    Nom_cli VARCHAR(255),
    Ende_cli VARCHAR(255)
);

CREATE TABLE Motoqueiro (
    Cod_moto INT PRIMARY KEY,
    Nom_moto VARCHAR(255)
);

CREATE TABLE Area (
    Cod_area INT PRIMARY KEY,
    Nome_are VARCHAR(255),
    Valor DECIMAL(10,2)
);

CREATE TABLE Farmaceutica (
    Cod_forma INT PRIMARY KEY,
    Nome_farma VARCHAR(255),
    End_farma VARCHAR(255),
    Cont_farma VARCHAR(20),
    Tele_farna VARCHAR(20)
);

CREATE TABLE Medicamento (
    Codigo_med INT PRIMARY KEY,
    Nome_Med VARCHAR(255),
    Composicao TEXT,
    Unidade VARCHAR(50),
    Preco DECIMAL(10,2),
    Generico BOOLEAN,
    Original BOOLEAN
);

CREATE TABLE Fabrica (
    Codigo_med INT,
    Cod_forma INT,
    PRIMARY KEY (Codigo_med, Cod_forma),
    FOREIGN KEY (Codigo_med) REFERENCES Medicamento(Codigo_med),
    FOREIGN KEY (Cod_forma) REFERENCES Farmaceutica(Cod_forma)
);

CREATE TABLE Pedido (
    Seq_pedi INT PRIMARY KEY,
    Data_ped DATE,
    Data_ent DATE,
    Status_ped VARCHAR(50),
    Valor_ped DECIMAL(10,2),
    Form_pag VARCHAR(50),
    Cod_cli INT,
    FOREIGN KEY (Cod_cli) REFERENCES Cliente(Cod_cli)
);

CREATE TABLE Pedido_Medicamento (
    Seq_pedi INT,
    Codigo_med INT,
    Qtd_ped INT,
    Preco_ped DECIMAL(10,2),
    PRIMARY KEY (Seq_pedi, Codigo_med),
    FOREIGN KEY (Seq_pedi) REFERENCES Pedido(Seq_pedi),
    FOREIGN KEY (Codigo_med) REFERENCES Medicamento(Codigo_med)
);

CREATE TABLE Pedido_Area (
    Seq_pedi INT,
    Cod_area INT,
    PRIMARY KEY (Seq_pedi, Cod_area),
    FOREIGN KEY (Seq_pedi) REFERENCES Pedido(Seq_pedi),
    FOREIGN KEY (Cod_area) REFERENCES Area(Cod_area)
);

CREATE TABLE Pedido_Entrega (
    Seq_pedi INT,
    Cod_moto INT,
    PRIMARY KEY (Seq_pedi, Cod_moto),
    FOREIGN KEY (Seq_pedi) REFERENCES Pedido(Seq_pedi),
    FOREIGN KEY (Cod_moto) REFERENCES Motoqueiro(Cod_moto)
);
