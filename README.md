# Pi Groot
---

## Prerequisites

### Server

 * [Docker](https://docs.docker.com/install/linux/docker-ce/debian/)
 * Ports for ES should be opened. (default: 9200, 9300)


### Raspberry Pi

```bash
sudo apt install build-essential python-dev python-pip python3-pip libgpiod2 git
pip3 install virtualenv
```


## Getting Started

### Server

```bash
docker-compose up -d
```

### Raspberry Pi

Download source code, then install python packages for your environment.

This step is required only the first time while setup this project on your Raspberry Pi.

```bash
git clone https://github.com/skyducks/pi-groot.git
cd pi-groot
virtualenv -p python3 venv
source venv/bin/activate
python ./setup.py install
```

Customize [config.yml](./config.yml) for your environment.

Then you can start farm management with your Raspberry Pi.

```bash
cd pi-groot
source venv/bin/activate
python ./setup.py install
pi_groot -c ./config.yml
```