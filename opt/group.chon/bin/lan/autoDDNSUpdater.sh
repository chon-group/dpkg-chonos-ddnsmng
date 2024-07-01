#!/bin/sh

#executing at service start
sleep 15
/usr/bin/chonosDDNSManager --update

# monitoring changes in IPv4 address
/usr/bin/ip monitor address | while read -r line; do
    if echo "$line" | grep -q "inet "; then
        /usr/bin/chonos-task -t "sleep 10; /usr/bin/chonosDDNSManager --update"
    fi
done
