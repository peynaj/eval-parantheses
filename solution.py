OPEN, CLOSE = "(", ")"


def eval_par(s: str) -> int:
    indexes_map = {}
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c == OPEN:
            stack.append(i)
        elif c == CLOSE:
            opened = stack.pop()
            indexes_map[opened] = i

    def recursive(open_index: int) -> int:
        if open_index not in indexes_map:
            return 0
        close_index = indexes_map[open_index]
        if close_index - open_index == 1:
            # sequential mode
            return 1 + recursive(close_index + 1)
        if (open_index + 1) in indexes_map:
            # depth mode
            return 2 ** recursive(open_index + 1) + recursive(close_index + 1)

    return recursive(0)


raw_tests = """
() => 1
()() => 2
()()() => 3
(()()()) => 8
(()) => 2
(()()) => 4
()(())() => 4
(()()()) => 8
(()()())()()() => 11
"""


def run_tests():
    tests = raw_tests.splitlines()
    tests = filter(bool, tests)
    tests = list(map(lambda line: line.split(" => "), tests))

    success = 0
    for s, expected in tests:
        expected = int(expected)
        actual = eval_par(s)
        if actual != expected:
            print(f"[Failed!] {s=} {expected=} {actual=}")
        else:
            success += 1

    print(f"Finished! {success}/{len(tests)} tests are successful.")


if __name__ == "__main__":
    run_tests()
