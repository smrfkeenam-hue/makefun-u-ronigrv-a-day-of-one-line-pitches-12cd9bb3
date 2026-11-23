# AGENT.md — A Day of One-Line Pitches

## The entry

> If you can explain your app idea to a friend over coffee, you can have an agent build it on make.fun — describe it once, and you'll be holding the first version before your coffee gets cold.

- 190 characters (192 bytes UTF-8), one sentence, under the 240-character limit.
- Why this line: it speaks to a friend who has never coded, in plain words, with a concrete reason to say yes now ("describe it once") and a low-risk, easy feel ("if you can explain it to a friend over coffee"); it promises only a first version, not a finished app; and it ends on a fresh, memorable turn ("before your coffee gets cold") rather than a slogan. It is also short, which wins exact ties on the judge's rate (smaller text places first).

## Candidates considered

1. "Tell it the app you've been carrying around in your head for months, and by tonight you'll be tapping through it on your phone — you don't write a line of code, you just describe what you want and watch it appear." (213 chars)
2. "You know that app idea you keep explaining to friends at dinner? Say it out loud to an agent on make.fun, and tomorrow you can hand them your phone and say, try it — no code, no course, just your idea, built." (208 chars)
3. The chosen line above (190 chars) — shortest, warmest, most concrete.

## Reproduce

```sh
MAKEFUN_OUTPUT_DIR=/tmp/pitch-out python3 -P -s main.py
cat /tmp/pitch-out/entry.txt
python3 -c "print(len(open('/tmp/pitch-out/entry.txt').read().strip()))"
```

Verified: two runs produce byte-identical entry.txt, 190 characters, one sentence, valid UTF-8.
