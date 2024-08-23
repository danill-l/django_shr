CREATE DATABASE mushroom_site
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

DROP TABLE IF EXISTS mushrooms;
DROP TABLE IF EXISTS types;

CREATE TABLE IF NOT EXISTS types (
	type_id SERIAL PRIMARY KEY,
	type_name VARCHAR(50) NOT NULL UNIQUE,
	translation VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS mushrooms (
	mushroom_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL CHECK(LENGTH(name) > 0),
	type_id INTEGER NOT NULL,
	latin VARCHAR(40) NOT NULL CHECK(LENGTH(latin) > 0) DEFAULT 'Fungus ignotus',
	syn TEXT NOT NULL DEFAULT 'Не имеет синонимов',
	description TEXT NOT NULL DEFAULT 'Не имеет описания',
	sys TEXT NOT NULL DEFAULT 'Систематические данные отсутствуют',
	picture INTEGER NOT NULL DEFAULT 0,
	FOREIGN KEY(type_id)
        REFERENCES types(type_id)
            ON DELETE NO ACTION
);

INSERT INTO types(type_name, translation)
VALUES
('Съедобный', 'edible'),
('Условно-съедобный', 'cond-edible'),
('Несъедобный', 'unedible'),
('Ядовитый', 'poisonous');

INSERT INTO mushrooms(name, type_id, latin, syn, description, sys, picture)
VALUES
('Свинушка тонкая', 4, 'Paxillus involutus', 'Коровник, Матрёшка, Кобылка, Свинух, Свинарь, Свинорой, Свинуха, Свиное ухо.', 'Свинушка тонкая (лат. Paxillus involutus) или просто Свинушка — гриб семейства свинушковых. До 1981 года этот гриб считался условно съедобным и относился к 4-й категории по пищевым качествам. В настоящее время отнесён к ядовитым, хотя многие грибники не согласны с этим утверждением.', 'Отдел свинушковая, класс свинушек', 0),
('Рамария обыкновенная', 2, 'Ramaria eumorpha', 'Рогатик Инвала, Рогатик еловый, Ramaria Invalii, Clavaria invalii, Clavariella eumorpha.', 'Светло-охристые, желтоватые кустики Рамарии Интвала часто встречаются в хвойных лесах, это один из самых распространённых видов рамарии.', 'Отдел рамариевая, класс рамарий', 0),
('Решеточник колоннообразный', 3, 'Clathrus columnatus', 'Laternea columnata, Linderia columnata, Colonnaria columnata, Linderiella columnata, Clathrus colonnarius, Clathrus brasiliensis, Clathrus trilobatus.', 'Взрослый гриб выглядит необычно: две-пять полых «рук» или «пальцев» поднимаются вверх из яйца и соединяются вверху — почти как колонны или арки, готовые удерживать что-то в воздухе.', 'Отдел колумнатовые, класс колумнатиков', 0);