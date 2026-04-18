#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import urllib.parse
import urllib.request
from pathlib import Path


LOCAL_ENV_PATH = Path("/Users/sunray/codex/transcript_office/.env")
NEWSBOT_ENV_PATH = Path("/Users/sunray/newsbot/.env")


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def send_telegram_message(text: str) -> None:
    load_env(LOCAL_ENV_PATH)
    load_env(NEWSBOT_ENV_PATH)
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not bot_token or not chat_id:
        raise RuntimeError("TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID missing")

    payload = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text[:3500],
            "disable_web_page_preview": "true",
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30):
        pass


def build_default_message() -> str:
    transcript_root = Path("/Users/sunray/codex/transcript_handyrecorder/transcripts")
    source_dir = transcript_root / "wiki" / "sources"
    raw_count = len(list(transcript_root.glob("*.md")))
    source_count = len(list(source_dir.glob("*.md"))) if source_dir.exists() else 0
    return (
        "handyrecorder wiki update\n"
        f"raw files: {raw_count}\n"
        f"source notes: {source_count}\n"
        f"vault: {transcript_root}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a Telegram notification for handyrecorder wiki work.")
    parser.add_argument("--message", help="Custom Telegram message")
    args = parser.parse_args()
    send_telegram_message(args.message or build_default_message())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
