from flask import Flask, render_template, request, flash
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

RPC_URL = os.getenv("WEB3_RPC_URL")
DEFAULT_ADDRESS = os.getenv("DEFAULT_ADDRESS", "")

web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.is_connected():
    raise RuntimeError("Could not connect to the blockchain node. Check WEB3_RPC_URL.")

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():
    balance_wei = None
    balance_eth = None
    address = DEFAULT_ADDRESS

    if request.method == "POST":
        address = request.form.get("address", "").strip()

        if not web3.is_address(address):
            flash("Invalid Ethereum address.", "error")
        else:
            address = web3.to_checksum_address(address)
            try:
                balance_wei = web3.eth.get_balance(address)
                balance_eth = web3.from_wei(balance_wei, "ether")
            except Exception as e:
                flash(f"Error fetching balance: {e}", "error")

    return render_template(
        "index.html",
        address=address,
        balance_wei=balance_wei,
        balance_eth=balance_eth,
        is_connected=web3.is_connected(),
        network_id=web3.net.version if web3.is_connected() else None,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
