# Web3 Dashboard (Python + Flask + web3.py)

This project is a minimal Web3-enabled web interface built with **Python**, **Flask**, and **web3.py**.  
It allows users to enter an Ethereum address and retrieve its **ETH balance** from a blockchain node (Infura, Alchemy, or any RPC provider).

This repository serves as a starter template for building more advanced dApps, dashboards, or blockchain analytics tools in Python.

## Features

- Connects to any Ethereum-compatible RPC node  
- Validates Ethereum addresses  
- Converts balance from wei → ETH  
- Simple, clean web interface  
- Fully extensible (decentralized apps, tokens, NFTs, smart contract calls, etc.)

## Tech Stack

| Component | Description |
|----------|-------------|
| **Python 3.10+** | Backend runtime |
| **Flask** | Lightweight web framework |
| **web3.py** | Ethereum blockchain interaction |
| **dotenv** | Environment variable management |

## Project Structure

```
web3_app/
├─ app.py
├─ .env
├─ requirements.txt
└─ templates/
     └─ index.html
```

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd web3_app
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Configuration

Edit `.env`:

```
WEB3_RPC_URL=YOUR_ETHEREUM_RPC_URL
DEFAULT_ADDRESS=0x0000000000000000000000000000000000000000
```

## Running the App

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Extending

- ERC‑20 token balances  
- NFT (ERC‑721 / ERC‑1155) viewers  
- Smart contract calls (read/write)  
- Multi-network support  
- Authenticated dashboards  

## License

MIT License.
