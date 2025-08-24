from __future__ import annotations

from unittest import mock
import pytest

from airflow_provider_ibm_db2.hooks.db2 import Db2Hook


def test_get_uri_uses_connection(monkeypatch):
    hook = Db2Hook()
    class FakeConn:
        host="localhost"; port=50000; schema="SAMPLE"; login="user"; password="pwd"
        extra_dejson={}
    monkeypatch.setattr(Db2Hook, "get_connection", lambda self, _: FakeConn())
    uri = hook.get_uri()
    assert uri.startswith("db2://")
