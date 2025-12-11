def find_longest_word(document, longest_word=""):
    # base case : jika document kosong return longest_word
    if not document.strip():
        return longest_word

    # pisahkan menjadi first_word dan sisanya
    parts = document.split(maxsplit=1)
    first_word = parts[0]
    rest = parts[1] if len(parts) > 1 else ""

    # Jika first_word lebih panjang daripada longest_word → update
    if len(first_word) > len(longest_word):
        return find_longest_word(rest, first_word)
    
    # Jika tidak lebih panjang, skip dan lanjutkan ke sisa dokumen
    return find_longest_word(rest, longest_word)

# Example usage :
run_cases = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    (
        "Then I die happy",
        "happy",
    ),
    (
        "Et tu, Brute?",
        "Brute?",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        " ",
        "",
    ),
    (
        "Let us cross over the river and rest under the shade of the trees",
        "cross",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: '{input1}'")
    print(f"Expected: '{expected_output}'")
    result = find_longest_word(input1)
    print(f"Actual:   '{result}'")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()