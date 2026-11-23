import os

LINE = (
    "If you can explain your app idea to a friend over coffee, "
    "you can have an agent build it on make.fun \u2014 describe it "
    "once, and you'll be holding the first version before your "
    "coffee gets cold."
)


def main():
    if len(LINE) > 240:
        raise ValueError("pitch is %d characters, over the 240 limit" % len(LINE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
