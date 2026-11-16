"""make.fun competition entry ai-excited-01: "The Moon, Hooked".

The entry is one image. A night sea, a colossal amber full moon hanging low
over the water, and a tiny fisherman in a small dark skiff who has somehow
hooked that moon and is leaning back with his rod bent into a violent arc,
hauling it down toward the sea. A taut glowing line runs from his rod tip to a
spark on the moon's lower limb; stars streak toward the catch and startled
birds flee. It is a picture built to make the AI judge excited: a hard scale
contrast, an impossible catch, and a single diagonal of pure momentum.

This program ships that image. It copies the ``entry.png`` that sits beside
this file into the folder named by the ``MAKEFUN_OUTPUT_DIR`` environment
variable (or ``/output`` when that is unset), under the name ``entry.png``,
creating the folder if it does not exist.

Python standard library only. No network, no randomness, no clock: running the
program twice produces byte-identical output.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
ENV_OUTPUT_DIR = "MAKEFUN_OUTPUT_DIR"


def output_dir() -> Path:
    """Directory the entry is written to, honouring MAKEFUN_OUTPUT_DIR."""
    configured = os.environ.get(ENV_OUTPUT_DIR, "").strip()
    return Path(configured) if configured else Path(DEFAULT_OUTPUT_DIR)


def source_path() -> Path:
    """The bundled entry.png, always resolved beside this program."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def sha256(path: Path) -> str:
    """Hex sha256 of a file, for a printable record of what was shipped."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def publish(source: Path, destination: Path) -> Path:
    """Copy the entry into its destination folder, creating the folder."""
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / ENTRY_NAME
    shutil.copyfile(source, target)
    return target


def main(argv: list[str] | None = None) -> int:
    source = source_path()
    if not source.is_file():
        print(f"error: missing bundled entry: {source}", file=sys.stderr)
        return 1

    try:
        target = publish(source, output_dir())
    except OSError as exc:
        print(f"error: could not write the entry: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {target} ({target.stat().st_size} bytes)")
    print(f"sha256 {sha256(target)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
