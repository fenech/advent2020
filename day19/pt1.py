import sys
import re


def parse(lines):
    return {a: b for a, b in map(lambda line: line.split(": "), lines)}


def resolve(rules, rule="0"):
    r = rules[rule]
    if re.search(r"\d", r) is None:
        return re.sub(r"[\" ]+", "", r)

    r = re.sub(r"\d+(?!})", lambda m: "(?:" + resolve(rules, m.group(0)) + ")", r)
    return r


def stripper(lines):
    for line in lines:
        yield line.rstrip()


def block(lines):
    for line in lines:
        if line == "":
            break
        yield line


if __name__ == "__main__":
    lines = stripper(sys.stdin)
    rules = parse(block(lines))
    matcher = re.compile("^" + resolve(rules).replace(" ", "") + "$")
    print(sum(m is not None for m in map(matcher.match, lines)))
