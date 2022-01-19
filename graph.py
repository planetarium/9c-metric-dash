from __future__ import annotations
import pandas as pd
import plotly.express as px
from model import (
    BlockAppend, BlockEvaluation, BlockStates, TransactionStage, FindHashes
)

def get_block_append_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "appended at" in line]
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
    lines = [line for line in lines if "appended at" in line]
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
    mean = df["lag"].mean()
    median = df["lag"].median()
    std = df["lag"].std()
    text = f"mean: {mean:.2f}<br>median: {median:.2f}<br>std: {std:.2f}"
    fig.add_annotation(
        text=text,
        xref="paper",
        yref="paper",
        x=1.0,
        y=1.0,
        xanchor="right",
        yanchor="top",
        align="right",
        bordercolor="black",
        showarrow=False,
    )
    return fig

def get_block_evaluation_duration_figure(path: str, selection: str):
    with open(path, "r") as file:
        data = file.read()
    options = {
        "index": {
            "x": "index",
            "label": "index",
            "hover_data": ["hash", "tx_count"],
        },
        "tx_count": {
            "x": "tx_count",
            "label": "number of transactions",
            "hover_data": ["index", "hash"]
        }
    }
    option = options[selection]

    lines = data.strip().split("\n")
    lines = [line for line in lines if "evaluated in" in line]
    blocks = [BlockEvaluation(line) for line in lines]
    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "duration": [block.duration for block in blocks],
        "tx_count": [block.tx_count for block in blocks],
    })
    fig = px.scatter(
        df,
        x=option["x"],
        y="duration",
        labels={
            option["x"]: option["label"],
            "duration": "evaluation duration in milliseconds",
        },
        hover_data=option["hover_data"],
        title="Block evaluation duration",
    )
    if selection == "index":
        mean = df["duration"].mean()
        median = df["duration"].median()
        std = df["duration"].std()
        text = f"mean: {mean:.2f}<br>median: {median:.2f}<br>std: {std:.2f}"
        fig.add_annotation(
            text=text,
            xref="paper",
            yref="paper",
            x=1.0,
            y=1.0,
            xanchor="right",
            yanchor="top",
            align="right",
            bordercolor="black",
            showarrow=False,
        )
    return fig

def get_block_states_update_duration_figure(path: str, selection: str):
    with open(path, "r") as file:
        data = file.read()
    options = {
        "index": {
            "x": "index",
            "label": "index",
            "hover_data": ["hash", "key_count"],
        },
        "key_count": {
            "x": "key_count",
            "label": "number of keys",
            "hover_data": ["index", "hash"]
        }
    }
    option = options[selection]

    lines = data.strip().split("\n")
    lines = [line for line in lines if "updating the states" in line]
    blocks = [BlockStates(line) for line in lines]
    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "duration": [block.duration for block in blocks],
        "key_count": [block.key_count for block in blocks],
    })
    fig = px.scatter(
        df,
        x=option["x"],
        y="duration",
        labels={
            option["x"]: option["label"],
            "duration": "states update duration in milliseconds",
        },
        hover_data=option["hover_data"],
        title="Block states update duration",
    )
    if selection == "index":
        mean = df["duration"].mean()
        median = df["duration"].median()
        std = df["duration"].std()
        text = f"mean: {mean:.2f}<br>median: {median:.2f}<br>std: {std:.2f}"
        fig.add_annotation(
            text=text,
            xref="paper",
            yref="paper",
            x=1.0,
            y=1.0,
            xanchor="right",
            yanchor="top",
            align="right",
            bordercolor="black",
            showarrow=False,
        )
    return fig

def get_tx_lag_figure(path: str):
    with open(path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    lines = [line for line in lines if "staged at" in line]
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
    mean = df["lag"].mean()
    median = df["lag"].median()
    std = df["lag"].std()
    text = f"mean: {mean:.2f}<br>median: {median:.2f}<br>std: {std:.2f}"
    fig.add_annotation(
        text=text,
        xref="paper",
        yref="paper",
        x=1.0,
        y=1.0,
        xanchor="right",
        yanchor="top",
        align="right",
        bordercolor="black",
        showarrow=False,
    )
    return fig

def get_find_hashes_figure(path: str, selection: str):
    with open(path, "r") as file:
        data = file.read()
    options = {
        "chain_id_count": {
            "x": "chain_id_count",
            "label": "number of chain ids",
            "hover_data": ["hash_count"],
        },
        "hash_count": {
            "x": "hash_count",
            "label": "number of hashes",
            "hover_data": ["chain_id_count"]
        }
    }
    option = options[selection]

    lines = data.strip().split("\n")
    lines = [line for line in lines if "hashes from" in line]
    data = [FindHashes(line) for line in lines]
    df = pd.DataFrame({
        "hash_count": [x.hash_count for x in data],
        "chain_id_count": [x.chain_id_count for x in data],
        "duration": [x.duration for x in data],
    })

    fig = px.scatter(
        df,
        x=option["x"],
        y="duration",
        labels={
            option["x"]: option["label"],
            "duration": "hashes retrieval duration in milliseconds",
        },
        hover_data=option["hover_data"],
        title="Find hashes duration",
    )
    return fig
