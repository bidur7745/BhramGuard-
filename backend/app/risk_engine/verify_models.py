from __future__ import annotations

from backend.app.risk_engine.predict import predict_text, predict_url, predict_web
from backend.app.risk_engine.risk_score import analyze_content


def main() -> None:
    samples = {
        "text": "Urgent: verify your account password now to avoid suspension.",
        "url": "http://secure-login-example.com/account/verify?token=123",
        "web": "<html><body><form><input type='password'>Verify your account login.</form></body></html>",
    }

    print("Text:", predict_text(samples["text"]))
    print("URL:", predict_url(samples["url"]))
    print("Web:", predict_web(samples["web"]))
    print("Combined:", analyze_content(text=samples["text"], url=samples["url"], web=samples["web"]))


if __name__ == "__main__":
    main()
