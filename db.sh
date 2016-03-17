mysql -uroot -e "create database ask_db"
mysql -uroot -e "create user 'django'@'localhost' identified by 'ask_user'"
mysql -uroot -e "grant all on ask_db.* to 'django'@'localhost'"
