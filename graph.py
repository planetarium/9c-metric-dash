from __future__ import annotations
import pandas as pd
import plotly.express as px
from model import Block, Transaction

def get_block_lag_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "Block" in line]
    blocks = [Block(line) for line in lines]
    df = pd.DataFrame({
        "appended": [block.appended for block in blocks],
        "lag": [(block.appended - block.created).total_seconds() for block in blocks],
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
    })
    fig = px.scatter(
        df,
        x="appended",
        y="lag",
        labels={
            "appended": "appended timestamp",
            "lag": "lag in seconds",
        },
        hover_data=["index", "hash"],
        title="Block propagation time",
    )
    return fig

def get_tx_lag_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "Transaction" in line]
    txs = [Transaction(line) for line in lines]
    df = pd.DataFrame({
        "staged": [tx.staged for tx in txs],
        "lag": [(tx.staged - tx.created).total_seconds() for tx in txs],
        "signer": [tx.signer for tx in txs],
        "id": [tx.id for tx in txs],
    })
    fig = px.scatter(
        df,
        x="staged",
        y="lag",
        labels={
            "staged": "staged timestamp",
            "lag": "lag in seconds",
        },
        hover_data=["signer", "id"],
        title="Transaction propagation time",
    )
    return fig
