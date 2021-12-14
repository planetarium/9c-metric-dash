from __future__ import annotations
import pandas as pd
import plotly.express as px
from model import BlockAppend, BlockEvaluation, BlockStates, TransactionStage

def get_block_append_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "Block" in line]
    blocks = [BlockAppend(line) for line in lines]
    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "timestamp": [block.timestamp for block in blocks],
        "appended": [block.appended for block in blocks],
    })
    fig = px.scatter(
        df,
        x="timestamp",
        y="appended",
        labels={
            "timestamp": "block timestamp",
            "appended": "appended timestamp",
        },
        hover_data=["index", "hash"],
        title="Block timestamp vs appended timestamp",
    )
    return fig

def get_block_lag_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "Block" in line]
    blocks = [BlockAppend(line) for line in lines]
    df = pd.DataFrame({
        "appended": [block.appended for block in blocks],
        "lag": [(block.appended - block.timestamp).total_seconds() for block in blocks],
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

def get_block_absolute_evaluation_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "evaluated" in line]
    blocks = [BlockEvaluation(line) for line in lines]
    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "evaluation": [block.evaluation for block in blocks],
        "tx_count": [block.tx_count for block in blocks],
    })
    fig = px.scatter(
        df,
        x="index",
        y="evaluation",
        labels={
            "index": "index",
            "evaluation": "evaluation time in milliseconds",
        },
        hover_data=["hash", "tx_count"],
        title="Block evaluation time",
    )
    return fig

def get_block_relative_evaluation_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "evaluated" in line]
    blocks = [BlockEvaluation(line) for line in lines]
    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "evaluation": [block.evaluation for block in blocks],
        "tx_count": [block.tx_count for block in blocks],
    })
    fig = px.scatter(
        df,
        x="tx_count",
        y="evaluation",
        labels={
            "tx_count": "number of transactions",
            "evaluation": "evaluation time in milliseconds",
        },
        hover_data=["hash", "index"],
        title="Block evaluation time",
    )
    return fig

def get_block_absolute_states_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "states" in line]
    blocks = [BlockStates(line) for line in lines]
    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "states": [block.states for block in blocks],
        "key_count": [block.key_count for block in blocks],
    })
    fig = px.scatter(
        df,
        x="index",
        y="states",
        labels={
            "index": "index",
            "states": "states update time in milliseconds",
        },
        hover_data=["hash", "key_count"],
        title="Block states update time",
    )
    return fig

def get_block_relative_states_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "states" in line]
    blocks = [BlockStates(line) for line in lines]
    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "states": [block.states for block in blocks],
        "key_count": [block.key_count for block in blocks],
    })
    fig = px.scatter(
        df,
        x="key_count",
        y="states",
        labels={
            "key_count": "number of keys",
            "states": "states update time in milliseconds",
        },
        hover_data=["hash", "index"],
        title="Block states update time",
    )
    return fig

def get_tx_lag_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "Transaction" in line]
    txs = [TransactionStage(line) for line in lines]
    df = pd.DataFrame({
        "signer": [tx.signer for tx in txs],
        "id": [tx.id for tx in txs],
        "staged": [tx.staged for tx in txs],
        "lag": [(tx.staged - tx.timestamp).total_seconds() for tx in txs],
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
