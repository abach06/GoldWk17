docks.docker.com and --help are your friend!

run a nginx, a mysql and apache (httpd) server

Run all them with --detach or -d, and name them with --name

nginx should listen on port 80:80, httpd on port 8080:80, and mysql(mariadb) on port 3306:3306

When running mysql, use the --env option or (-e) to pass in (MYSQL_RANDOM_ROOT_PASSWORD=yes

A=

docker container run --publish 80:80 --detach --name webhost nginx
docker container run --publish 8080:80 --detach --name apache httpd
docker container run --publish 3306:3306 --detach --name mariadb mariadb
