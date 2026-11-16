"""make.fun competition entry ai-excited-01: "The Moon, Hooked".

The entry is one image, made to excite the AI judge. A night sea under a sky
full of stars; a colossal amber full moon hangs low over the water, too big
and too close for the horizon to hold. A tiny fisherman in a small dark skiff
has hooked that moon: his rod is bent into a violent arc, a taut glowing line
runs from the rod tip to a spark on the moon's lower limb, and he is leaning
back with his whole body, pulling the moon down toward the sea.

It is built on a hard scale contrast -- one small human against a body larger
than the sky -- and on a single unbroken diagonal of momentum from the boat
through the line to the catch. The impossible catch is the point: the judge
should feel the pull, the tension, and the audacity of the thing.

This program ships that image. It copies the ``entry.png`` that sits beside
this file into the folder named by the ``MAKEFUN_OUTPUT_DIR`` environment
variable (or ``/output`` when that variable is unset), under the name
``entry.png``, creating the folder if it does not already exist.

Python standard library only. No network, no randomness, no clock: two runs
produce byte-identical output.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
ENV_OUTPUT_DIR = "MAKEFUN_OUTPUT_DIR"


def output_dir() -> Path:
    """The folder the entry is written to, honouring MAKEFUN_OUTPUT_DIR."""
    configured = os.environ.get(ENV_OUTPUT_DIR, "").strip()
    if configured:
        return Path(configured)
    return Path(DEFAULT_OUTPUT_DIR)


def source_path() -> Path:
    """The bundled entry.png, always resolved beside this program."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def publish(source: Path, destination: Path) -> Path:
    """Copy the entry into ``destination``, creating the folder if needed."""
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / ENTRY_NAME
    shutil.copyfile(source, target)
    return target


def main(argv: list[str] | None = None) -> int:
    """Write the entry and report where it landed. Returns a process code."""
    source = source_path()
    if not source.is_file():
        print(f"error: missing bundled entry: {source}", file=sys.stderr)
        return 1

    try:
        target = publish(source, output_dir())
    except OSError as exc:
        print(f"error: could not write the entry: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
