# Test task for MadDevs

Project for data collection and analysis using API exchanges Binance and Bitfinex.

![chart](/assets/RSI.png)

## 🏗️ Architecture and Technologies

The backend is built using Python. Connection to exchanges is carried out via the WebSocket protocol. Graphana is used for visualization.

### 📚 Technology Stack:

- [Python](https://python.org/) - project language
- [Pydantic](https://docs.pydantic.dev/latest/) - data validation library for parsing data returned by exchanges
- [Pandas](https://pandas.pydata.org/) - mathematical tool for data analysis and processing
- [Aiohttp](https://docs.aiohttp.org/en/stable/index.html) - asynchronous http client, used to connect to the Bitfinex exchange
- [Python Binance](https://github.com/sammchardy/python-binance) - library for connecting to the Binance exchange
- [InfluxDB](https://www.influxdata.com/) - time series database for storing and accessing data obtained from exchanges
- [Grafana](https://grafana.com/grafana/) - a tool for visualizing data and building dashboards

## 🛠️ Getting Started

### ⚙️ Configuration:

Copy `.env` file and replace variables with your preferred values:

```bash
cp deploy/config/env/.env.sample deploy/config/env/.env
```

### 🔍 Run in development environment:

Create a virtual environment:

```bash
cd src && python3 -m venv .venv && source ./venv/bin/activate
```

Install dependencies:

```bash
poetry install
```

Run project:

```bash
python3 main.py
```

### 🚀 Run in production environment:

Run docker compose project:

```bash
cd deploy && docker compose up -d --build
```

## 📁 Usage

### 📝 Text logs:

Text logs can be viewed directly from the container:

```bash
docker compose logs backend --since 1m -f
```

### 🧐 InfluxDB:

The InfluxDB interface for working with the received data is available at http://localhost:8086, the login and password to log in are specified in the environment variables. You can use `admin` : `ZJC2s2zgx36rCne9` by default.

### 🧪 Grafana:

Grafana provide convenient dashboards that are updated in real time. You can see dashboards here: http://localhost:3000/dashboards, the login and password to log in are specified in the environment variables. You can use `admin` : `ZJC2s2zgx36rCne9` by default.
