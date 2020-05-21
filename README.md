# Minotaur

An automated scanning tool using Dockers & RabbitMQ to help with bug bounties

The whole setup is based on workflows:

1. Passive Subdomains Enumeration -> Dedup & keep new ones -> shuffleDNS -> httprobe -> dirsearch
2. IP or Subnet -> Masscan -> Nmap Services -> Dirsearch http/https ports

## Tools

- RabbitMQ
- Amass / Assetfinder / Findomain / Subfinder
- Massdns / Nmap
- Dnsgen
- httprobe / anew
- Dirsearch

## To Do

- [x] Add Dirsearch implementation
- [x] Add Rapid7 Sonar via Crobat
- [ ] Pull fresh Resolvers (via cronjob)
- [x] Scan IP found from Massdns step for Open Ports (masscan / nmap)
- [x] Add shuffleDNS & dnsvalidator tools to wrap arround Massdns
- [ ] Add waybackmachine/commoncrawl results

## Instructions

1. git clone the repo
2. Put resolvers.txt in the docker/input/ directory, which you can get through a daily run of dnsvalidator
3. Put wordlist.txt in the docker/input/ directory, which is the list dirsearch will use

Build using `--compatibility` mode due to the use of replicas for dirsearch.

```
docker-compose --compatibility up --build
```

Finally, at the moment you can run this using:

```
python app/send.py assetfinder domain.com
```

### Extra

- Dirsearch runs with 3 replicas, you can edit to add more or less.

### Rabbitmq

Useful commands

Use `docker-compose exec rabbitmq bash` to get into the rabbitmq container
Use `rabbitmqctl list_queues
Use `rabbitmqadmin get queue=dir-scan count=100` to list the last 100 entries in the dir-scan queue


