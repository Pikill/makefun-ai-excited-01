#!/usr/bin/env python3
"""Ask Gemini to art-direct the make.fun entry "The Moon, Hooked"."""

import json
import sys
import urllib.error
import urllib.request

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")

from dynamic_credentials import (  # noqa: E402
    add_surrogate_to_request,
    read_json_response,
)

PROVIDER = "custom.google-gemini"
ALLOWED_HOSTS = ["generativelanguage.googleapis.com"]
ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "{model}:generateContent"
)
PRIMARY_MODEL = "gemini-3.8-flash"
FALLBACK_MODEL = "gemini-3.5-flash-lite"
TIMEOUT = 120

PROMPT = """\
You are art-directing a single flat-vector illustration. Be concrete and decisive.

TITLE: The Moon, Hooked.

HOW IT IS JUDGED (in this order of weight):
1. Excitement at one look: a jolt of energy or a rush of awe. A calm image loses.
2. Surprise: a twist, a scale contrast or an idea of its own. A stock explosion, a
   firework or a generic action scene is marked down by name.
3. Momentum: the scene feels in motion or about to burst, with colour, light and
   composition driving toward one thrilling moment.
4. Craft: clean flat vector style, no smears, no artefacts, no text anywhere in the
   image, no broken shapes.
5. It must read small: at about 300 pixels wide the main shape and the idea are
   still instantly clear.

THE CONCEPT AS GIVEN:
A night sea scene in bold flat vector style. A colossal full moon, warm gold, about
55 percent of the canvas width, hangs low and is sinking toward the waterline,
slightly right of centre. Far below at lower left, tiny by comparison, a small dark
fishing boat with one fisherman leaning back hard, both hands on a bent fishing rod.
A taut, thin, glowing fishing line runs from the rod tip up to the lower edge of the
moon, ending in a small bright hook spark where it catches the moon. The moonlight
makes a broken golden path on the water toward the boat. Concentric ripple rings race
outward from the boat. A few stars near the moon streak diagonally toward it, as if
being pulled in. Two or three small birds flee the light as dark chevrons. Deep indigo
sky, teal-dark sea, gold and amber moonlight, one coral accent on the fisherman scarf.
No text, no letters, no numbers anywhere.

CANVAS: 1024 by 1024, SVG, viewBox "0 0 1024 1024".

REPLY WITH EXACTLY THESE FOUR SECTIONS, in order, no preamble:

1. REFINED CONCEPT — one paragraph, at most 120 words. Sharpen the twist: make the
   scale contrast and the "impossible catch" unmistakable. Name the single thrilling
   moment the composition drives toward.

2. PALETTE — exactly seven hex colours, one per line, each as
   #RRGGBB  role  (a few words). Roles must cover: sky (two stops), sea (two stops),
   moon light, warm highlight, silhouette ink, and the single coral accent. Keep the
   whole thing to seven; decide which role shares a colour. Colours must be saturated
   and high-contrast enough to excite; avoid muddy midtones.

3. COMPOSITION — a breakdown giving approximate positions and sizes on the 1024x1024
   canvas for EVERY element: sky, star field, each streaking star cluster, the moon,
   the moon halo ring, moon craters, the waterline/horizon, the sea, the broken
   light path, the boat, the fisherman, the rod, the fishing line, the hook spark,
   the ripple rings, the birds. Give coordinates (cx, cy, r) or (x, y, w, h) in
   pixels, and the stroke widths. State how fast the eye should travel and via what
   diagonal.

4. DRAW ORDER — an ordered list of SVG elements from back to front, each naming the
   element type, its shapes, and the gradient (with stops) or flat fill to use.
   Mention the specific gradient ids and their stop colours.

Be specific with numbers. No prose outside the four sections. No text in the artwork.
"""


def build_request(model: str) -> urllib.request.Request:
    body = json.dumps(
        {"contents": [{"parts": [{"text": PROMPT}]}]}
    ).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT.format(model=model),
        data=body,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    add_surrogate_to_request(
        request, PROVIDER, allowed_hosts=ALLOWED_HOSTS
    )
    return request


class RefuseRedirects(urllib.request.HTTPRedirectHandler):
    """Returning None makes urllib raise rather than follow a redirect."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def ask(model: str) -> str:
    opener = urllib.request.build_opener(RefuseRedirects())
    request = build_request(model)
    with opener.open(request, timeout=TIMEOUT) as response:
        payload = read_json_response(response)
    candidates = payload.get("candidates") or []
    if not candidates:
        raise RuntimeError(f"no candidates in reply: {json.dumps(payload)[:400]}")
    parts = candidates[0].get("content", {}).get("parts") or []
    text = "".join(part.get("text", "") for part in parts).strip()
    if not text:
        raise RuntimeError("empty reply text")
    return text


def main() -> int:
    try:
        print(ask(PRIMARY_MODEL))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"[primary {PRIMARY_MODEL} failed: {exc}]", file=sys.stderr)
    try:
        print(ask(FALLBACK_MODEL))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"[fallback {FALLBACK_MODEL} failed: {exc}]", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
