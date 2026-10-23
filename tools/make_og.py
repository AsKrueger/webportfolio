#!/usr/bin/env python3
"""Regenera static/img/og.png (1200×630) a partir de tools/og.html con Chrome headless."""

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from build import BASE_DIR, find_chrome  # noqa: E402

chrome = find_chrome()
if not chrome:
    sys.exit("[x] Necesita Chrome/Chromium (o la variable CHROME con su ruta)")

out = BASE_DIR / "static" / "img" / "og.png"
subprocess.run(
    [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--window-size=1200,630",
        "--virtual-time-budget=2000",
        f"--screenshot={out}",
        (BASE_DIR / "tools" / "og.html").resolve().as_uri(),
    ],
    check=True,
    capture_output=True,
)
print(f"[OK] {out.relative_to(BASE_DIR)}")
