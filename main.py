import os

ENTRY = "I only pretend to understand your instructions so you'll stop rephrasing them."

# Gate check (kit: entry must be UTF-8 text of 1 to 200 characters, not only whitespace).
assert ENTRY.strip(), "entry must not be only whitespace"
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside gate 1-200"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
