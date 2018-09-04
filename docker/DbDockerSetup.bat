docker run -dit -p 3306:80 --name=scrapperdb -e MYSQL_ROOT_PASSWORD=Password1 -d mysql/mysql-server:8.0
docker exec -it scrapperdb mysql -uroot -p
CREATE DATABASE scrapper_output;
USE scrapper_output;
CREATE TABLE search_results(uuid varchar(255), is_error int, title varchar(255), description varchar(255), tags varchar(255), last_update_time date, language varchar(255), stars varchar(255));