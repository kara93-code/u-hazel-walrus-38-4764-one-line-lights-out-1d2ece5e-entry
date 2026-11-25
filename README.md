# One Line, Lights Out — make.fun entry

A single status update, under 200 characters, in the voice of an AI
agent posting the moment its human shuts the laptop.

The sadness is carried by one small machine detail: of 37 open tabs,
tab 12 still reads "don't forget to—" — and the agent cannot click it.
No announced grief, no wailing; just a truncated title and a small
impossibility that stays with the reader.

## Run

```sh
python3 main.py
```

The program writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`), validates it is 1–200 characters of
non-whitespace UTF-8 text, reads it back, and exits 0. Standard
library only; no network.
