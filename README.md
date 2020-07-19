# Pi Groot
---

## Prerequisites

### Server

 * [Docker](https://docs.docker.com/install/linux/docker-ce/debian/)
 * Ports for ES should be opened. (default: 9200, 9300)


### Raspberry Pi

```bash
sudo apt install build-essential python-dev python-pip python3-pip libgpiod2
pip3 install virtualenv
```


## Getting Started

### Server

```bash
docker-compose up -d
```

### Raspberry Pi

```bash
virtualenv -p python3 venv
source venv/bin/activate
python ./setup.py install
pi_groot -c ./config.yml
```