# -*- coding: utf-8 -*-
from functools import wraps
import numpy as np
import json
import codecs
from flask import jsonify, make_response


def jsonize(f):
    @wraps(f)
    def _(*args, **kwargs):
        r = f(*args, **kwargs)
        data, code = r if isinstance(r, tuple) else (r, 200)
        return jsonify(data), code
    return _


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


def err_msg(code, msg: str):
    return jsonify({"errcode": f'{code}', "errmsg": str(msg)})


def ok_msg():
    return jsonify({"errcode": "0", "errmsg": "success"})


def ok_msg_with(data):
    body = {"errcode": "0", "errmsg": "success"}
    body["data"] = data
    return jsonify(body)


def ok_msg_make_response(data: dict):
    body = {"errcode": "0", "errmsg": "success"}
    body["data"] = data
    res = make_response(codecs.decode(json.dumps(
        body, cls=NpEncoder, default=str), "unicode_escape"), 200)
    res.headers['content-type'] = 'application/json'
    return res


def err_msg_make_response(code: str, msg: str, data: dict):
    body = {"errcode": code, "errmsg": str(msg)}
    body["data"] = data
    res = make_response(codecs.decode(json.dumps(
        body, cls=NpEncoder), "unicode_escape"), 200)
    res.headers['content-type'] = 'application/json'
    return res
