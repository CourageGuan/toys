drop table if exists info;
create table info (
	id integer primary key autoincrement,
	url string not null,
	keyword string not null,
	mail string not null
);
