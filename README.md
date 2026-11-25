# The Excuse My Agent Gave Me

[![make.fun bounty](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/thanhvu261090/makefun-excuse-my-agent/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/thanhvu261090/makefun-excuse-my-agent/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

Entry for the [make.fun bounty "The Excuse My Agent Gave Me"](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) — a single line, under 200 characters, in which an AI agent explains to its human why it missed a deadline. A model judge compares lines pairwise and keeps the funnier one.

## The entry

> Sorry — I rescheduled your deadline to February 30th, and my calendar accepted it, my reminders confirmed it, and I have been early for it ever since.

## How it works

`main.py` holds one fixed entry line and writes it, exactly as-is with no trailing newline, to `/output/entry.txt`. Before writing, `gate_check` enforces the competition gate: the text must be 1–200 UTF-8 characters, not only whitespace, a single line with no leading or trailing whitespace. The entry is deterministic — running the program twice produces byte-identical output — because the judge compares the exact submitted text.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
