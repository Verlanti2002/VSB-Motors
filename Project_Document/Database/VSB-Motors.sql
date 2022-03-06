create database VSB-Motors; 
use VSB-Motors
create table cliente
(    
idCliente varchar(5) not null auto_increment,
nome varchar(25) not null, 
cognome varchar(45) not null,
data_di_nascita date not null,
telefono varchar(10) not null,
email varchar(50) not null,
password varchar(100) not null,
primary key (idCliente),
unique key (email)
); 

create table concessionaria
(
idConcessionaria varchar(5) not null auto_increment,
ragione_sociale varchar(45) not null,
partita_iva varchar(11) not null, 
indirizzo varchar(45) not null,
CAP varchar(5) not null,
città varchar(45) not null,
telefono varchar(10) null,
email varchar(50) not null,
password varchar(100) not null,
primary key (idConcessionaria),
unique key (email) 
); 

create table marca
(
idMarca varchar(5) not null auto_increment,
nome varchar(30) not null,
primary key(idMarca) 
); 

create table carburante
(
idCarburante varchar(5) not null auto_increment,
nome varchar(45) not null CHECK (nome='Diesel' OR  nome='Benzina' OR nome='Metano' OR nome='GPL' OR nome='Elettrico'),
primary key(idCarburante) 
); 

create table automobile
(  
idAutomobile varchar(5) not null auto_increment,
targa varchar(7) not null,
modello varchar(25) not null, 
cilindrata int not null CHECK (cilindrata>'750'), 
cavalli int not null CHECK (cavalli>'39'),
potenza int not null CHECK (potenza>'25'), 
stato varchar (45) not null CHECK (stato='Usato' OR stato='Nuovo'), 
km_percorsi int not null CHECK (km_percorsi>0), 
anno_produzione int not null CHECK (anno_prudzione>='1950'),
numero_proprietari int CHECK(numero_proprietari>0),   
prezzo int not null CHECK (prezzo < 0),
cod_marca varchar(30) not null, 
cod_venditore int(5) not null, 
cod_carburante varchar(45) not null CHECK (cod_carburante='Diesel' OR  cod_carburante='Benzina' OR cod_carburante='Metano' OR cod_carburante='GPL' OR cod_carburante='Elettrico'),
primary key(idAutomobile),
foreign key (cod_marca) references marca(nome), 
foreign key (cod_carburante) references carburante(nome),
foreign key (cod_venditore) references venditore(id)
); 

create table ordine
( 
idOrdine int(5) not null auto_increment, 
data date not null,
cod_automobile int(5) not null, 
cod_cliente int(5) not null,
primary key(idOrdine), 
foreign key (cod_automobile) references automobile(idAutomobile),
foreign key (cod_cliente) references cliente(idCliente),
unique key (cod_automobile),
unique key (cod_cliente),
unique key (cod_venditore)
);  
