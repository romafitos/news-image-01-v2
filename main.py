"""news-image-01 round 2 entry: copy the staged news image to the output dir.

The image ("The World in One Day", three-band news poster for Friday
13 November 2026) ships in this repository as entry.png. This program
copies it, byte for byte, to $MAKEFUN_OUTPUT_DIR/entry.png (default
/output/entry.png) and checks the copy before it exits: the file must
be present, at most 1 MiB, a PNG or JPEG by its magic bytes, and the
copy must be identical to the source. Standard library only.
"""

import hashlib
import os
import shutil
import sys

MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def _is_image_magic(head):
    """True when the leading bytes name a PNG or a JPEG file."""
    return head.startswith(PNG_MAGIC) or head.startswith(JPEG_MAGIC)


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        print("entry.png missing from repository", file=sys.stderr)
        return 1
    if os.path.getsize(source) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    with open(source, "rb") as handle:
        head = handle.read(len(PNG_MAGIC))
    if not _is_image_magic(head):
        print("entry.png is neither PNG nor JPEG", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)
    if _sha256(source) != _sha256(target):
        print("copy differs from source", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)"
          % (target, os.path.getsize(target), _sha256(target)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
