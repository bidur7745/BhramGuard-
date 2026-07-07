from __future__ import annotations

import ipaddress
import re
from types import SimpleNamespace
from urllib.parse import urlparse

import pandas as pd


def parse_url(value: object):
    url = "" if pd.isna(value) else str(value).strip()
    candidate = url if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url) else "http://" + url

    try:
        return url, urlparse(candidate), 0
    except ValueError:
        fallback = SimpleNamespace(scheme="", hostname="", path="", query="")
        return url, fallback, 1


def safe_url_part(parsed: object, part_name: str) -> str:
    try:
        return getattr(parsed, part_name) or ""
    except ValueError:
        return ""


def hostname_is_ip(hostname: str) -> int:
    if not hostname:
        return 0
    try:
        ipaddress.ip_address(hostname)
        return 1
    except ValueError:
        return 0


def extract_url_features(value: object) -> dict[str, float]:
    url, parsed, parse_error = parse_url(value)
    lowered = url.lower()
    hostname = safe_url_part(parsed, "hostname")
    path = safe_url_part(parsed, "path")
    query = safe_url_part(parsed, "query")
    suspicious_words = ["login", "verify", "secure", "account", "update", "confirm", "bank", "wallet", "password"]

    return {
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(path),
        "query_length": len(query),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "slash_count": url.count("/"),
        "question_count": url.count("?"),
        "equals_count": url.count("="),
        "at_count": url.count("@"),
        "percent_count": url.count("%"),
        "digit_count": sum(char.isdigit() for char in url),
        "has_https": int(safe_url_part(parsed, "scheme") == "https"),
        "has_ip_hostname": hostname_is_ip(hostname),
        "subdomain_count": max(hostname.count(".") - 1, 0),
        "suspicious_word_count": sum(1 for word in suspicious_words if word in lowered),
        "parse_error": parse_error,
    }
