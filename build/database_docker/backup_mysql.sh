#!/bin/bash
BKP_DATE=`date +%Y%m%d`
BKP_NAME="tempnow_${BKP_DATE}.sql"

if [ $# -eq 0 ]; then
	echo "ERROR: please provide a username to connect to production database"
	echo "USAGE: $0 <database user>"
	exit 1
fi

DB_USER=${1}

mysqldump --routines --quick --single-transaction -h $MYSQL_HOST -u ${DB_USER} -p $MYSQL_DATABASE > /tmp/${BKP_NAME}
rm -f backups/mysql/*.sql.gz
mv /tmp/${BKP_NAME} backups/mysql/ && gzip -9 backups/mysql/${BKP_NAME}
echo "backup done with succesfully"
