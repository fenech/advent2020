import sys
import unittest
import re


def parse_rule(rule):
    m = re.finditer(r"(\w+ \w+) bag", rule)
    return [s.group(1) for s in m]


class ParseRuleTestCase(unittest.TestCase):
    def test_parse_rule_one(self):
        self.assertEqual(
            parse_rule("bright white bags contain 1 shiny gold bag."),
            ["bright white", "shiny gold"],
        )

    def test_parse_rule_two(self):
        self.assertEqual(
            parse_rule(
                "light red bags contain 1 bright white bag, 2 muted yellow bags."
            ),
            ["light red", "bright white", "muted yellow"],
        )

    def test_parse_rule_none(self):
        self.assertEqual(
            parse_rule("dotted black bags contain no other bags."),
            ["dotted black", "no other"],
        )


def build_tree(rules):
    return {r[0]: set(r[1:]) for r in rules}


class BuildTreeTestCase(unittest.TestCase):
    def test_build_tree(self):
        rules = [
            ["light red", "bright white", "muted yellow"],
            ["dotted black", "no other"],
        ]
        self.assertEqual(
            build_tree(rules),
            {
                "light red": {"bright white", "muted yellow"},
                "dotted black": {"no other"},
            },
        )


def check_contents(count, rules_tree, bag, target):
    contents = rules_tree[bag]
    if contents == {"no other"}:
        return count
    if target in contents:
        return count + 1
    return count + any(
        check_contents(count, rules_tree, bag, target) for bag in contents
    )


def count_bags(rules_tree, target):
    return sum(
        check_contents(0, rules_tree, contents, target)
        for contents in rules_tree.keys()
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
            4,
        )


if __name__ == "__main__":
    tree = build_tree(map(parse_rule, sys.stdin.read().splitlines()))
    print(count_bags(tree, "shiny gold"))
