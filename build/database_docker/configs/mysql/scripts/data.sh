#!/bin/bash
echo -n "# Restoring production data into LOCAL MYSQL..."
mkdir -p /proddata
rm -rf /proddata/*
cp -f /backup/*.gz /proddata/
cd /proddata
gunzip *.gz

CMD="mysql -u root -pabc123"

${CMD} -e "DROP DATABASE IF EXISTS tempnow;" >/dev/null 2>&1
${CMD} -e "CREATE DATABASE tempnow;" >/dev/null 2>&1
${CMD} tempnow < *.sql >/dev/null 2>&1

echo "done"
exit 0
