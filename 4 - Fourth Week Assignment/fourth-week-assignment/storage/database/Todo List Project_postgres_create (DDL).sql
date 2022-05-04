 CREATE DATABASE todo_list_project_db;

 CREATE TABLE task (
	id_task serial NOT NULL,
	id_todolist integer NOT NULL,
	title VARCHAR(255) NOT NULL,
	content VARCHAR(255) NOT NULL,
	id_tag integer NOT NULL,
	id_status integer NOT NULL,
	CONSTRAINT task_pk PRIMARY KEY (id_task)
);



CREATE TABLE todo (
	id_todo serial NOT NULL,
	title VARCHAR(255) NOT NULL UNIQUE,
	CONSTRAINT todo_pk PRIMARY KEY (id_todo)
);


CREATE TABLE status (
	id_status serial NOT NULL,
	status_name VARCHAR(15) NOT NULL,
	CONSTRAINT status_pk PRIMARY KEY (id_status)
);


CREATE TABLE tag (
	id_tag serial NOT NULL,
	tag_name VARCHAR(255) NOT NULL UNIQUE,
	CONSTRAINT tag_pk PRIMARY KEY (id_tag)
);


ALTER TABLE task ADD CONSTRAINT task_fk0 FOREIGN KEY (id_todolist) REFERENCES todo(id_todo);
ALTER TABLE task ADD CONSTRAINT task_fk1 FOREIGN KEY (id_tag) REFERENCES tag(id_tag);
ALTER TABLE task ADD CONSTRAINT task_fk2 FOREIGN KEY (id_status) REFERENCES status(id_status);


INSERT INTO status (status_name) VALUES('unassigned');
INSERT INTO status (status_name) VALUES('pending');
INSERT INTO status (status_name) VALUES('accepted');
INSERT INTO status (status_name) VALUES('started');
INSERT INTO status (status_name) VALUES('completed');