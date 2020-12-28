import sys
import re
from pt1 import stripper, block, parse, resolve

if __name__ == "__main__":
    lines = stripper(sys.stdin)
    rules = parse(block(lines))

    r42 = resolve(rules, "42")
    r31 = resolve(rules, "31")
    rules["8"] = "(?:" + r42 + ")+"
    rules["11"] = (
        "(?:"
        + "|".join(
            [
                "(?:(?:" + r42 + "){" + str(i) + "}(?:" + r31 + "){" + str(i) + "})"
                for i in range(1, 40)
            ]
        )
        + ")"
    )
    matcher = re.compile("^" + resolve(rules).replace(" ", "") + "$")
    print(sum(m is not None for m in map(matcher.match, lines)))
