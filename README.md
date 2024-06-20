CREATE TABLE Zakaz
(
Date_Zakaza DATE NOT NULL,
Date_Polucheniya DATE NOT NULL,
Number VARCHAR(250) NOT NULL,
Zakaz_id INT NOT NULL,
PRIMARY KEY (Zakaz_id)
);
CREATE TABLE Dostavka
(
Curier VARCHAR(250) NOT NULL,
Samovivoz VARCHAR(250) NOT NULL,
Dostavka_id INT NOT NULL,
Zakaz_id INT NOT NULL,
PRIMARY KEY (Dostavka_id),
FOREIGN KEY (Zakaz_id) REFERENCES Zakaz(Zakaz_id)
);
CREATE TABLE Client
(
Fio VARCHAR(250) NOT NULL,
Number VARCHAR(250) NOT NULL,
Klient_id INT NOT NULL,
Zakaz_id INT NOT NULL,
PRIMARY KEY (Klient_id),
FOREIGN KEY (Zakaz_id) REFERENCES Zakaz(Zakaz_id)
);
CREATE TABLE Sotrudnik
(
Fio VARCHAR(250) NOT NULL,
Dolznost VARCHAR(250) NOT NULL,
Sotrudnik_id INT NOT NULL,
Klient_id INT NOT NULL,
PRIMARY KEY (Sotrudnik_id),
FOREIGN KEY (Klient_id) REFERENCES Client(Klient_id)
);
CREATE TABLE Tovar
(
New VARCHAR(250) NOT NULL,
BU VARCHAR(250) NOT NULL,
Tovari_zakaza_id INT NOT NULL,
Zakaz_id INT NOT NULL,
PRIMARY KEY (Tovari_zakaza_id),
FOREIGN KEY (Zakaz_id) REFERENCES Zakaz(Zakaz_id)
);
CREATE TABLE Instrumenti
(
Proizvoditel VARCHAR(250) NOT NULL,
Price VARCHAR(250) NOT NULL,
Instrumenti_id INT NOT NULL,
Tovari_zakaza_id INT NOT NULL,
PRIMARY KEY (Instrumenti_id),
FOREIGN KEY (Tovari_zakaza_id) REFERENCES Tovar(Tovari_zakaza_id)
);
CREATE TABLE Aksessuari
(
Price VARCHAR(250) NOT NULL,
Proizvoditel VARCHAR(250) NOT NULL,
Acsesuari_id INT NOT NULL,
Tovari_zakaza_id INT NOT NULL,
PRIMARY KEY (Acsesuari_id),
FOREIGN KEY (Tovari_zakaza_id) REFERENCES Tovar(Tovari_zakaza_id)
);
CREATE TABLE Uslovia_Garantii
(
One_Year VARCHAR(250) NOT NULL,
More_Year VARCHAR(250) NOT NULL,
Uslovia_garantiy_id INT NOT NULL,
Tovari_zakaza_id INT NOT NULL,
PRIMARY KEY (Uslovia_garantiy_id),
FOREIGN KEY (Tovari_zakaza_id) REFERENCES Tovar(Tovari_zakaza_id)
);
CREATE TABLE Duhovie
(
Diapazon_not_instrumenta VARCHAR(250) NOT NULL,
Ves VARCHAR(250) NOT NULL,
Duhovie_id INT NOT NULL,
Instrumenti_id INT NOT NULL,
PRIMARY KEY (Duhovie_id),
FOREIGN KEY (Instrumenti_id) REFERENCES Instrumenti(Instrumenti_id)
);
CREATE TABLE Strunnie
(
Scripka VARCHAR(250) NOT NULL,
Violonchel VARCHAR(250) NOT NULL,
Alt VARCHAR(250) NOT NULL,
Gitara VARCHAR(250) NOT NULL,
Strunnie_id INT NOT NULL,
Instrumenti_id INT NOT NULL,
PRIMARY KEY (Strunnie_id),
FOREIGN KEY (Instrumenti_id) REFERENCES Instrumenti(Instrumenti_id)
);
CREATE TABLE Duhovie_dereviannie
(
Fleita VARCHAR(250) NOT NULL,
Klarnet VARCHAR(250) NOT NULL,
Duhovie_dereviannie_id INT NOT NULL,
Duhovie_id INT NOT NULL,
PRIMARY KEY (Duhovie_dereviannie_id),
FOREIGN KEY (Duhovie_id) REFERENCES Duhovie(Duhovie_id)
);
CREATE TABLE Duhovie_mednie
(
Trombon VARCHAR(250) NOT NULL,
Tryba VARCHAR(250) NOT NULL,
Fagot VARCHAR(250) NOT NULL,
Duhovie_mednie_id INT NOT NULL,
Duhovie_id INT NOT NULL,
PRIMARY KEY (Duhovie_mednie_id),
FOREIGN KEY (Duhovie_id) REFERENCES Duhovie(Duhovie_id)
);
 


Заполнение записей
INSERT INTO Zakaz (Date_Zakaza, Date_Polucheniya, Number, Zakaz_id)
VALUES
('2024-03-20', '2024-03-21', 'ZK001', 1),
('2024-03-19', '2024-03-22', 'ZK002', 2),
('2024-03-18', '2024-03-23', 'ZK003', 3),
('2024-03-17', '2024-03-24', 'ZK004', 4),
('2024-03-16', '2024-03-25', 'ZK005', 5),
('2024-03-15', '2024-03-26', 'ZK006', 6),
('2024-03-14', '2024-03-27', 'ZK007', 7),
('2024-03-13', '2024-03-28', 'ZK008', 8),
('2024-03-12', '2024-03-29', 'ZK009', 9),
('2024-03-11', '2024-03-30', 'ZK010', 10);
 
INSERT INTO Client (Fio, Number, Klient_id, Zakaz_id)
VALUES
('Иванов Иван Иванович', '123456789', 1, 1),
('Петров Петр Петрович', '987654321', 2, 2),
('Сидоров Сидор Сидорович', '555666777', 3, 3),
('Кузнецов Кузьма Кузьмич', '999888777', 4, 4),
('Михайлов Михаил Михайлович', '111222333', 5, 5),
('Федоров Федор Федорович', '444333222', 6, 6),
('Алексеев Алексей Алексеевич', '777888999', 7, 7),
('Дмитриев Дмитрий Дмитриевич', '666555444', 8, 8),
('Николаев Николай Николаевич', '999000111', 9, 9),
('Григорьев Григорий Григорьевич', '222111000', 10, 10);
 
INSERT INTO Tovar (New, BU, Tovari_zakaza_id, Zakaz_id)
VALUES
('Товар 1 (Новый)', 'Товар 1 (Б/У)', 1, 1),
('Товар 2 (Новый)', 'Товар 2 (Б/У)', 2, 2),
('Товар 3 (Новый)', 'Товар 3 (Б/У)', 3, 3),
('Товар 4 (Новый)', 'Товар 4 (Б/У)', 4, 4),
('Товар 5 (Новый)', 'Товар 5 (Б/У)', 5, 5),
('Товар 6 (Новый)', 'Товар 6 (Б/У)', 6, 6),
('Товар 7 (Новый)', 'Товар 7 (Б/У)', 7, 7),
('Товар 8 (Новый)', 'Товар 8 (Б/У)', 8, 8),
('Товар 9 (Новый)', 'Товар 9 (Б/У)', 9, 9),
('Товар 10 (Новый)', 'Товар 10 (Б/У)', 10, 10);
 
INSERT INTO Dostavka (Curier, Samovivoz, Dostavka_id, Zakaz_id)
VALUES
('Курьер 1', 'Да', 1, 1),
('Курьер 2', 'Нет', 2, 2),
('Курьер 3', 'Да', 3, 3),
('Курьер 4', 'Нет', 4, 4),
('Курьер 5', 'Да', 5, 5),
('Курьер 6', 'Нет', 6, 6),
('Курьер 7', 'Да', 7, 7),
('Курьер 8', 'Нет', 8, 8),
('Курьер 9', 'Да', 9, 9),
('Курьер 10', 'Нет', 10, 10);
 
INSERT INTO Sotrudnik (Fio, Dolznost, Sotrudnik_id, Klient_id)
VALUES
('Иванов Иван Иванович', 'Менеджер', 1, 1),
('Петров Петр Петрович', 'Администратор', 2, 2),
('Сидоров Сидор Сидорович', 'Консультант', 3, 3),
('Кузнецов Кузьма Кузьмич', 'Продавец', 4, 4),
('Михайлов Михаил Михайлович', 'Менеджер', 5, 5),
('Федоров Федор Федорович', 'Администратор', 6, 6),
('Алексеев Алексей Алексеевич', 'Консультант', 7, 7),
('Дмитриев Дмитрий Дмитриевич', 'Продавец', 8, 8),
('Николаев Николай Николаевич', 'Менеджер', 9, 9),
('Григорьев Григорий Григорьевич', 'Администратор', 10, 10);
 
INSERT INTO Instrumenti (Proizvoditel, Price, Instrumenti_id, Tovari_zakaza_id)
VALUES
('Производитель 1', '100', 1, 1),
('Производитель 2', '200', 2, 2),
('Производитель 3', '300', 3, 3),
('Производитель 4', '400', 4, 4),
('Производитель 5', '500', 5, 5),
('Производитель 6', '600', 6, 6),
('Производитель 7', '700', 7, 7),
('Производитель 8', '800', 8, 8),
('Производитель 9', '900', 9, 9),
('Производитель 10', '1000', 10, 10);
 
INSERT INTO Uslovia_Garantii (One_Year, More_Year, Uslovia_garantiy_id, Tovari_zakaza_id)
VALUES
('Гарантия на 1 год', 'Расширенная гарантия', 1, 1),
('Гарантия на 2 года', 'Стандартная гарантия', 2, 2),
('Гарантия на 3 года', 'Расширенная гарантия', 3, 3),
('Гарантия на 1 год', 'Стандартная гарантия', 4, 4),
('Гарантия на 2 года', 'Расширенная гарантия', 5, 5),
('Гарантия на 3 года', 'Стандартная гарантия', 6, 6),
('Гарантия на 1 год', 'Расширенная гарантия', 7, 7),
('Гарантия на 2 года', 'Стандартная гарантия', 8, 8),
('Гарантия на 3 года', 'Расширенная гарантия', 9, 9),
('Гарантия на 1 год', 'Стандартная гарантия', 10, 10);
 
INSERT INTO Aksessuari (Price, Proizvoditel, Acsesuari_id, Tovari_zakaza_id)
VALUES
('50', 'Производитель 1', 1, 1),
('60', 'Производитель 2', 2, 2),
('70', 'Производитель 3', 3, 3),
('80', 'Производитель 4', 4, 4),
('90', 'Производитель 5', 5, 5),
('100', 'Производитель 6', 6, 6),
('110', 'Производитель 7', 7, 7),
('120', 'Производитель 8', 8, 8),
('130', 'Производитель 9', 9, 9),
('140', 'Производитель 10', 10, 10);
 
INSERT INTO
Duhovie (Diapazon_not_instrumenta, Ves, Duhovie_id, Instrumenti_id)
VALUES
('Диапазон 1', '10 кг', 1, 1),
('Диапазон 2', '20 кг', 2, 2),
('Диапазон 3', '30 кг', 3, 3),
('Диапазон 4', '40 кг', 4, 4),
('Диапазон 5', '50 кг', 5, 5),
('Диапазон 6', '60 кг', 6, 6),
('Диапазон 7', '70 кг', 7, 7),
('Диапазон 8', '80 кг', 8, 8),
('Диапазон 9', '90 кг', 9, 9),
('Диапазон 10', '100 кг', 10, 10);
 
INSERT INTO Strunnie (Scripka, Violonchel, Alt, Gitara, Strunnie_id, Instrumenti_id)
VALUES
('Скрипка 1', 'Виолончель 1', 'Альт 1', 'Гитара 1', 1, 1),
('Скрипка 2', 'Виолончель 2', 'Альт 2', 'Гитара 2', 2, 2),
('Скрипка 3', 'Виолончель 3', 'Альт 3', 'Гитара 3', 3, 3),
('Скрипка 4', 'Виолончель 4', 'Альт 4', 'Гитара 4', 4, 4),
('Скрипка 5', 'Виолончель 5', 'Альт 5', 'Гитара 5', 5, 5),
('Скрипка 6', 'Виолончель 6', 'Альт 6', 'Гитара 6', 6, 6),
('Скрипка 7', 'Виолончель 7', 'Альт 7', 'Гитара 7', 7, 7),
('Скрипка 8', 'Виолончель 8', 'Альт 8', 'Гитара 8', 8, 8),
('Скрипка 9', 'Виолончель 9', 'Альт 9', 'Гитара 9', 9, 9),
('Скрипка 10', 'Виолончель 10', 'Альт 10', 'Гитара 10', 10, 10);
 
INSERT INTO Duhovie_dereviannie (Fleita, Klarnet, Duhovie_dereviannie_id, Duhovie_id)
VALUES
('Флейта 1', 'Кларнет 1', 1, 1),
('Флейта 2', 'Кларнет 2', 2, 2),
('Флейта 3', 'Кларнет 3', 3, 3),
('Флейта 4', 'Кларнет 4', 4, 4),
('Флейта 5', 'Кларнет 5', 5, 5),
('Флейта 6', 'Кларнет 6', 6, 6),
('Флейта 7', 'Кларнет 7', 7, 7),
('Флейта 8', 'Кларнет 8', 8, 8),
('Флейта 9', 'Кларнет 9', 9, 9),
('Флейта 10', 'Кларнет 10', 10, 10);
 
INSERT INTO Duhovie_mednie (Trombon, Tryba, Fagot, Duhovie_mednie_id, Duhovie_id)
VALUES
('Тромбон 1', 'Труба 1', 'Фагот 1', 1, 1),
('Тромбон 2', 'Труба 2', 'Фагот 2', 2, 2),
('Тромбон 3', 'Труба 3', 'Фагот 3', 3, 3),
('Тромбон 4', 'Труба 4', 'Фагот 4', 4, 4),
('Тромбон 5', 'Труба 5', 'Фагот 5', 5, 5),
('Тромбон 6', 'Труба 6', 'Фагот 6', 6, 6),
('Тромбон 7', 'Труба 7', 'Фагот 7', 7, 7),
('Тромбон 8', 'Труба 8', 'Фагот 8', 8, 8),
('Тромбон 9', 'Труба 9', 'Фагот 9', 9, 9),
('Тромбон 10', 'Труба 10', 'Фагот 10', 10, 10);
 
Редактирование БД
ALTER TABLE Aksessuari
	ADD COLUMN kolichestvo INT AFTER price;
 
ALTER TABLE Aksessuari
	MODIFY COLUMN kolichestvo VARCHAR(255);
 
 ALTER TABLE Duhovie_mednie
	DROP COLUMN Tryba;
   
ALTER TABLE Duhovie_mednie
	ADD CONSTRAINT Duhovie_mednie_foreign_key
    FOREIGN KEY (Duhovie_dereviannie_id) REFERENCES Duhovie_dereviannie(Duhovie_dereviannie_id);
 
ALTER TABLE Duhovie_mednie
	DROP PRIMARY KEY,
	ADD PRIMARY KEY (Duhovie_mednie_id, Duhovie_dereviannie_id); 
RENAME TABLE Sotrudnik  TO Post;
 
ALTER TABLE Dostavka
	RENAME column Dostavka_id TO CUrier_id;
     
DROP TABLE IF EXISTS Sotrudnik;
 
DROP DATABASE IF EXISTS sus;
 
Дополнительные запросы
Добавление записи
INSERT INTO sus.Zakaz (Date_Zakaza, Date_Polucheniya, Number, Zakaz_id)
VALUES
('2024-03-20','2024-03-25','ZK0007',11);
Изменение значения в записи
update zakaz set number='ZK07' where Zakaz_id=11;
Удаление записи
delete from zakaz where Zakaz_id=11;
Удаление столбца
ALTER TABLE zakaz
DROP Number;
