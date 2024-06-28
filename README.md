# ChonOS Dynamic DNS Client Manager 

|![chonos-ddns](https://github.com/chon-group/dpkg-chonos-ddnsmng/assets/32855001/cf909ae3-7efa-47f1-8e32-d15a7a9d6808)|
|:--:|
|ChonOS DDNS implements a Dynamic DNS Client accountable for maintaining the embedded system's _Fully Qualified Domain Name_ updated. So, the designer can access the system directly through its name without worrying about discovering the IP address when changing networks.|
|Moreover, this module implements a _Simple Service Discovery Protocol_ server to announce the cognitive device into the local area network. So, the embedded multi-agent system can exchange information about themselves and the services they provide to others.|

## How to Install?
1) In a terminal run the commands below:

```console
echo "deb [trusted=yes] http://packages.chon.group/ chonos main" | sudo tee /etc/apt/sources.list.d/chonos.list
sudo apt update
sudo apt install chonos-ddnsmng
```

### DESCRIPTION

List of options and arguments:
|Argument|Description|
|-|-|
|\--status|show the DDNS registration status|
|\--update|update the DDNS registration|
|-o conf|configures the Chon DDNS client|
|-d \[domain\]|Chon DDNS domain name|
|-u \[user\]|Chon DDNS user name|
|-t \[token\]|Chon DDNS user token|
|-a \[IPv4\]|IPv4 address|

### EXAMPLES

The user credentials are _ddns_user_ and _ddns_token_.
Access https://ddns.chon.group/ to register credentials to use the service.

1. Configures the DDNS Server to resolve the FQDN myrobot.bot.chon.group address for the machine\'s local IPv4 address.
```sh
sudo chonosDDNSManager -o conf -d myrobot -u "ddns_user" -t "ddns_token"
```

2. Configures the DDNS Server to resolve the FQDN myrobot.bot.chon.group address for the IPv4 1.2.3.4.
```sh
sudo chonosDDNSManager -o conf -d myrobot -u "ddns_user" -t "ddns_token" -a "1.2.3.4"
```


## COPYRIGHT
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />The Chonos-Log is part of the [_Cognitive Hardware on Networks Operating
System (chonOS)_](http://os.chon.group/) and is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The licensor cannot revoke these freedoms as long as you follow the license terms:

* __Attribution__ — You must give __appropriate credit__ like below:

LAZARIN, Nilson Mori; PANTOJA, Carlos Eduardo; VITERBO, José. Towards a Toolkit for Teaching AI Supported by Robotic-agents: Proposal and First Impressions. In: WORKSHOP SOBRE EDUCAÇÃO EM COMPUTAÇÃO (WEI), 31. , 2023, João Pessoa/PB. Anais [...]. Porto Alegre: Sociedade Brasileira de Computação, 2023 . p. 20-29. ISSN 2595-6175. DOI: https://doi.org/10.5753/wei.2023.229753.


<details>
<summary> Bibtex citation format</summary>

```
@inproceedings{chonOS,
 author = {Nilson Lazarin and Carlos Pantoja and José Viterbo},
 title = { Towards a Toolkit for Teaching AI Supported by Robotic-agents: Proposal and First Impressions},
 booktitle = {Anais do XXXI Workshop sobre Educação em Computação},
 location = {João Pessoa/PB},
 year = {2023},
 issn = {2595-6175},
 pages = {20--29},
 publisher = {SBC},
 address = {Porto Alegre, RS, Brasil},
 doi = {10.5753/wei.2023.229753},
 url = {https://sol.sbc.org.br/index.php/wei/article/view/24887}
}

```
</details>
