# chonosDDNSManager - ChonOS Dynamic DNS Client Manager

## DESCRIPTION
A client of the Chon DDNS Server. Access https://ddns.chon.group/ to register credentials to use the service.

List of options and arguments:

&nbsp;&nbsp;&nbsp;&nbsp; \--status - show the DDNS registration status.

&nbsp;&nbsp;&nbsp;&nbsp; \--update - update the DDNS registration.

&nbsp;&nbsp;&nbsp;&nbsp; -o conf - configures the Chon DDNS client.

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; -d \[domain\] - Chon DDNS domain name.

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; -u \[user\] - Chon DDNS user name.

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; -t \[token\] - Chon DDNS user token.

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; -a \[IPv4\] - IPv4 address.

## EXAMPLES

> sudo chonosDDNSManager -o conf -d myrobot -u \"ddns_user\" -t \"ddns_token\"

&nbsp;&nbsp;&nbsp;&nbsp; Configures the DDNS Server to resolve the FQDN myrobot.bot.chon.group address for the machine\'s local IPv4 address.

> sudo chonosDDNSManager -o conf -d myrobot -u \"ddns_user\" -t \"ddns_token\" -a "1.2.3.4"

&nbsp;&nbsp;&nbsp;&nbsp; Configures the DDNS Server to resolve the FQDN myrobot.bot.chon.group address for the IPv4 1.2.3.4.


The user credentials are _ddns_user_ and _ddns_token_.

## COPYRIGHT
Copyright © 2023 Chon Group http://chon.group. License GPLv3+: GNU GPL version 3 or later https://gnu.org/licenses/gpl.html. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.