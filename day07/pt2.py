import sys
import unittest
import re


def parse_rule(rule):
    m = re.match(r"\w+ \w+", rule)
    container = m.group(0)

    m = re.finditer(r"(\d+) (\w+ \w+) bag", rule[m.end() :])
    return container, {s.group(2): int(s.group(1)) for s in m}


class ParseRuleTestCase(unittest.TestCase):
    def test_parse_rule_one(self):
        self.assertEqual(
            parse_rule("bright white bags contain 1 shiny gold bag."),
            ("bright white", {"shiny gold": 1}),
        )

    def test_parse_rule_two(self):
        self.assertEqual(
            parse_rule(
                "light red bags contain 1 bright white bag, 2 muted yellow bags."
            ),
            ("light red", {"bright white": 1, "muted yellow": 2}),
        )

    def test_parse_rule_none(self):
        self.assertEqual(
            parse_rule("dotted black bags contain no other bags."),
            ("dotted black", {}),
        )


def build_tree(rules):
    return {b: r for b, r in rules}


class BuildTreeTestCase(unittest.TestCase):
    def test_build_tree(self):
        rules = [
            ("light red", {"bright white": 1, "muted yellow": 2}),
            ("dotted black", {}),
        ]
        self.assertEqual(
            build_tree(rules),
            {"light red": {"bright white": 1, "muted yellow": 2}, "dotted black": {}},
        )


def count_bags(rules, bag, count=0):
    if rules[bag] == {}:
        return count
    return count + sum(
        n + n * count_bags(rules, bag, count) for bag, n in rules[bag].items()
    )


class CountBagsTestCase(unittest.TestCase):
    def setUp(self):
        self.input = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags.",
        ]
        self.rules = map(parse_rule, self.input)
        self.tree = build_tree(self.rules)
        print(self.tree)

    def test_count_bags(self):
        self.assertEqual(
            count_bags(self.tree, "shiny gold"),
            32,
        )


if __name__ == "__main__":
    tree = build_tree(map(parse_rule, sys.stdin.read().splitlines()))
    print(count_bags(tree, "shiny gold"))
