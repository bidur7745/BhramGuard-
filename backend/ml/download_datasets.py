from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import requests


DATASET_REPO_ID = "ealvaradob/phishing-dataset"
DATASET_BASE_URL = f"https://huggingface.co/datasets/{DATASET_REPO_ID}/resolve/main"
DATASET_FILES = {
    "texts": "texts.json",
    "urls": "urls.json",
    "webs": "webs.json",
}


def default_dataset_dir() -> Path:
    return Path(__file__).resolve().parent / "datasets"


def json_records_to_csv(json_path: Path, csv_path: Path) -> None:
    with json_path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if not records:
        csv_path.write_text("", encoding="utf-8")
        return

    fieldnames = list(records[0].keys())
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def download_file(url: str, destination: Path, force: bool = False) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)

    remote_size = None
    head_response = requests.head(url, allow_redirects=True, timeout=(30, 60))
    if head_response.ok and head_response.headers.get("content-length"):
        remote_size = int(head_response.headers["content-length"])

    existing_size = destination.stat().st_size if destination.exists() else 0
    if force and destination.exists():
        destination.unlink()
        existing_size = 0

    if remote_size is not None and existing_size == remote_size:
        print(f"{destination} already exists; using local raw file")
        return

    headers = {}
    mode = "wb"
    if existing_size and (remote_size is None or existing_size < remote_size):
        headers["Range"] = f"bytes={existing_size}-"
        mode = "ab"
        print(f"Resuming {destination.name} from byte {existing_size}")

    with requests.get(url, stream=True, timeout=(30, None), headers=headers) as response:
        response.raise_for_status()
        with destination.open(mode) as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)


def download_dataset(name: str, dataset_dir: Path, force: bool = False) -> Path:
    filename = DATASET_FILES[name]
    csv_path = dataset_dir / f"{name}.csv"
    raw_dir = dataset_dir / "raw"
    raw_path = raw_dir / filename

    if csv_path.exists() and not force:
        print(f"{csv_path} already exists; skipping")
        return csv_path

    url = f"{DATASET_BASE_URL}/{filename}"
    download_file(url, raw_path, force)
    print(f"Downloaded {filename} to {raw_path}")

    json_records_to_csv(raw_path, csv_path)
    print(f"Saved {csv_path}")
    return csv_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download BhramGuard phishing datasets.")
    parser.add_argument(
        "datasets",
        nargs="*",
        choices=sorted(DATASET_FILES),
        default=["texts", "urls", "webs"],
        help="Dataset names to download and convert.",
    )
    parser.add_argument(
        "--dataset-dir",
        type=Path,
        default=default_dataset_dir(),
        help="Directory where CSV files should be saved.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download and overwrite existing CSV files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for dataset in args.datasets:
        download_dataset(dataset, args.dataset_dir, args.force)


if __name__ == "__main__":
    main()
