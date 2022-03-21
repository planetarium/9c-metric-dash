from __future__ import annotations
import json
import pandas as pd
import plotly.express as px
from model import (
    BlockAppend, BlockEvaluation, BlockStates, BlockRender,
    TransactionStage, FindHashes, OutboundMessage, InboundMessage, Sockets
)
from model.message import InboundMessage

def line_to_dict(line: str) -> dict:
    try:
        return json.loads(line.strip())
    except:
        return {}

def read_file(path: str) -> list[dict]:
    with open(path, "r") as file:
        data = [
            elem for elem in [line_to_dict(line) for line in file.readlines()]
                if elem and "Subtag" in elem
        ]
    return data

def get_block_append_figure(path: str):
    blocks = [
        BlockAppend(elem) for elem in read_file(path)
            if elem["Subtag"] == "BlockAppendTimestamp"
    ]
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
    blocks = [
        BlockAppend(elem) for elem in read_file(path)
            if elem["Subtag"] == "BlockAppendTimestamp"
    ]
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
    count = len(df.index)
    mean = df["lag"].mean()
    median = df["lag"].median()
    std = df["lag"].std()
    text = f"count: {count}<br>mean: {mean:.2f}<br>median: {median:.2f}<br>std: {std:.2f}"
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
    blocks = [
        BlockEvaluation(elem) for elem in read_file(path)
            if elem["Subtag"] == "BlockEvaluationDuration"
    ]
    options = {
        "index": {
            "x": "index",
            "label": "index",
            "hover_data": ["pre_eval_hash", "tx_count"],
        },
        "tx_count": {
            "x": "tx_count",
            "label": "number of transactions",
            "hover_data": ["index", "pre_eval_hash"]
        }
    }
    option = options[selection]

    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "pre_eval_hash": [block.pre_eval_hash for block in blocks],
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
            "pre_eval_hash": "pre-evaluation hash"
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
    blocks = [
        BlockStates(elem) for elem in read_file(path)
            if elem["Subtag"] == "StateUpdateDuration"
    ]
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
    txs = [
        TransactionStage(elem) for elem in read_file(path)
            if elem["Subtag"] == "TxStageTimestamp"
    ]
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
    count = len(df.index)
    mean = df["lag"].mean()
    median = df["lag"].median()
    std = df["lag"].std()
    text = f"count: {count}<br>mean: {mean:.2f}<br>median: {median:.2f}<br>std: {std:.2f}"
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

def get_outbound_message_report_figure(path: str, selection: str):
    messages = [
        OutboundMessage(elem) for elem in read_file(path)
            if elem["Subtag"] == "OutboundMessageReport"
    ]

    options = {
        "duration": {
            "y": "duration",
            "label": "duration in milliseconds",
            "hover_data": ["message", "duration", "timeout", "received", "expected", "success"],
        },
        "ratio": {
            "y": "ratio",
            "label": "duration / timeout",
            "hover_data": ["message", "duration", "timeout", "received", "expected", "success"],
        }
    }
    option = options[selection]

    df = pd.DataFrame({
        "message": [message.message for message in messages],
        "timestamp": [message.timestamp for message in messages],
        "timeout": [message.timeout for message in messages],
        "duration": [message.duration for message in messages],
        "received": [message.received for message in messages],
        "expected": [message.expected for message in messages],
        "success": [message.success for message in messages],
        "ratio": [message.ratio for message in messages],
    })

    fig = px.scatter(
        df,
        x="timestamp",
        y=option["y"],
        color="message",
        symbol="success",
        symbol_map= {
            True: 0,    # o
            False: 4,   # x
        },
        hover_data=option["hover_data"],
        title="Outbound message report",
    )
    return fig

def get_inbound_message_report_figure(path: str):
    messages = [
        InboundMessage(elem) for elem in read_file(path)
            if elem["Subtag"] == "InboundMessageReport"
    ]
    df = pd.DataFrame({
        "message": [message.message for message in messages],
        "timestamp": [message.timestamp for message in messages],
    })

    fig = px.strip(
        df,
        x="timestamp",
        y="message",
        color="message",
        title="Inbound message report",
    )
    return fig

def get_socket_count_figure(path: str):
    socket_counts = [
        Sockets(elem) for elem in read_file(path)
            if elem["Subtag"] == "SocketCount"
    ]

    df = pd.DataFrame({
        "timestamp": [sockets.timestamp for sockets in socket_counts],
        "count": [sockets.count for sockets in socket_counts],
    })
    fig = px.area(
        df,
        x="timestamp",
        y="count",
        labels={
            "timestamp": "log timestamp",
            "count": "number of sockets open",
        },
        title="Number of sockets open",
    )
    return fig

def get_find_hashes_figure(path: str, selection: str):
    data = [
        FindHashes(elem) for elem in read_file(path)
            if elem["Subtag"] == "FindHashesDuration"
    ]

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

def get_block_render_duration_figure(path: str, selection: str):
    blocks = [
        BlockRender(elem) for elem in read_file(path)
            if elem["Subtag"] == "BlockRenderDuration"
    ]

    options = {
        "index": {
            "x": "index",
            "label": "index",
            "hover_data": ["hash", "render_count"],
        },
        "render_count": {
            "x": "render_count",
            "label": "number of renders",
            "hover_data": ["index", "hash"]
        }
    }
    option = options[selection]

    df = pd.DataFrame({
        "index": [block.index for block in blocks],
        "hash": [block.hash for block in blocks],
        "duration": [block.duration for block in blocks],
        "render_count": [block.render_count for block in blocks],
    })
    fig = px.scatter(
        df,
        x=option["x"],
        y="duration",
        labels={
            option["x"]: option["label"],
            "duration": "render duration in milliseconds",
        },
        hover_data=option["hover_data"],
        title="Block render duration",
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
