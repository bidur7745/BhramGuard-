from __future__ import annotations

import re

import pandas as pd


def extract_web_features(value: object) -> dict[str, float]:
    text = "" if pd.isna(value) else str(value)
    lowered = text.lower()

    return {
        "char_length": len(text),
        "word_count": len(re.findall(r"\w+", text)),
        "link_count": len(re.findall(r"https?://|www\.", lowered)),
        "form_count": lowered.count("<form"),
        "password_count": lowered.count("password"),
        "input_count": lowered.count("<input"),
        "script_count": lowered.count("<script"),
        "iframe_count": lowered.count("<iframe"),
        "login_count": lowered.count("login"),
        "verify_count": lowered.count("verify"),
        "account_count": lowered.count("account"),
        "secure_count": lowered.count("secure"),
    }
