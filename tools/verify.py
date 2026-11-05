#!/usr/bin/env python3
"""Verify the released binary and bundle against manifest.json."""
import hashlib, json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
m = json.loads((root / "manifest.json").read_text())

def sha(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

pairs = [
    (root / m["engine"], m["engine_sha256"]),
    (root / m["bundle"], m["bundle_sha256"]),
]
bad = 0
for p, expect in pairs:
    if not p.is_file():
        print(f"MISSING  {p.relative_to(root)}"); bad += 1; continue
    got = sha(p)
    ok = got == expect
    print(f"{'OK     ' if ok else 'MISMATCH'} {p.relative_to(root)}  {got[:16]}…")
    if not ok: bad += 1

print(f"\nproduct : {m['product']}")
print(f"target  : {m['target']}")
print(f"result  : {'PASS' if bad == 0 else 'FAIL'}")
sys.exit(1 if bad else 0)
