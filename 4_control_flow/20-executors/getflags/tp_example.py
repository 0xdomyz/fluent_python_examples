#!/usr/bin/env python3.11

from concurrent import futures

import time
from pathlib import Path

import requests

POP20_CC = (
    "CN IN US ID BR PK NG BD RU JP " "MX PH VN ET EG DE IR TR CD FR"
).split()  # <2>

BASE_URL = "https://www.fluentpython.com/data/flags"  # <3>
DEST_DIR = Path("downloaded")  # <4>


def save_flag(img: bytes, filename: str) -> None:  # <5>
    (DEST_DIR / filename).write_bytes(img)


def get_flag(cc: str) -> bytes:  # <6>
    url = f"{BASE_URL}/{cc}/{cc}.gif".lower()
    resp = requests.get(url)
    return resp.content


def download_one(cc: str):  # <2>
    image = get_flag(cc)
    save_flag(image, f"{cc}.gif")
    print(cc, end=" ", flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor() as executor:  # <3>
        res = executor.map(download_one, sorted(cc_list))  # <4>

    return len(list(res))  # <5>


if __name__ == "__main__":
    DEST_DIR.mkdir(exist_ok=True)  # <14>
    t0 = time.perf_counter()  # <15>

    count = download_many(POP20_CC)

    elapsed = time.perf_counter() - t0
    print(f"\n{count} downloads in {elapsed:.2f}s")
