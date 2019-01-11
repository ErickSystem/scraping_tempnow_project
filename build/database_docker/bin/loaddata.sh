#!/bin/sh

eval $(jq -r '. | to_entries | .[] | .key + "=\"" + (.value|tostring) + "\""' postgrator.json)

for file in $(find "$fakeDirectory" -type f | sort); do
    echo -n "processing $file"
    mysql --protocol=tcp -h "$host" -P $port -u "$username" --password="$password" "$database" < "$file"
    echo " ... done"
done