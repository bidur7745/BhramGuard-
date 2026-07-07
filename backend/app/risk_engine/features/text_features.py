from __future__ import annotations

import re

import pandas as pd


def extract_text_features(value: object) -> dict[str, float]:
    text = "" if pd.isna(value) else str(value)
    lowered = text.lower()
    words = text.split()

    urgency_words = ["hurry", "urgent", "immediately", "act now", "limited time", "expire", "act fast"]
    reward_words = ["free", "win", "winner", "prize", "discount", "offer", "guarantee", "cash"]
    threat_words = ["suspend", "verify", "confirm", "account", "password", "security", "unauthorized"]
    authority_words = ["bank", "paypal", "microsoft", "google", "admin", "support", "team", "irs", "tax"]
    caps_words = [word for word in words if word.isupper() and len(word) > 1]

    return {
        "char_length": len(text),
        "word_count": len(words),
        "urgency_count": sum(1 for word in urgency_words if word in lowered),
        "reward_count": sum(1 for word in reward_words if word in lowered),
        "threat_count": sum(1 for word in threat_words if word in lowered),
        "authority_count": sum(1 for word in authority_words if word in lowered),
        "caps_ratio": len(caps_words) / len(words) if words else 0,
        "exclamation_count": text.count("!"),
        "question_count": text.count("?"),
        "link_count": len(re.findall(r"https?://|www\.", lowered)),
        "email_count": len(re.findall(r"[\w.%-]+@[\w.-]+\.[A-Za-z]{2,}", text)),
        "money_count": len(re.findall(r"[$]\s?\d+|\d+\s?(usd|dollars|rs|npr)", lowered)),
        "elongation_count": len(re.findall(r"([a-zA-Z])\1{3,}", text)),
    }
