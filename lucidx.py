#!/usr/bin/env python3
"""Backwards-compatible entry point — the real package lives in lucidx/.

Keep this module import-light: build tools may resolve the name
``lucidx`` against THIS file before the lucidx/ package.
"""
if __name__ == "__main__":
    from lucidx.cli import main

    raise SystemExit(main())
