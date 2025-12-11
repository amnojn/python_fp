def count_nested_levels(nested_documents, target_document_id, level=1):
    # Loop through each document id
    for document_id, sub_docs in nested_documents.items():

        # Case 1: document ditemukan di level ini
        if document_id == target_document_id:
            return level

        # Case 2: jika masih ada nested dictionary, rekursi
        if isinstance(sub_docs, dict):
            result = count_nested_levels(sub_docs, target_document_id, level + 1)

            # Jika rekursi menemukan target
            if result != -1:
                return result

    # Case 3: tidak ditemukan sama sekali
    return -1



# Example usage :
run_cases = [
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 2, 2),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 9, 4),
]

submit_cases = run_cases + [
    ({}, 1, -1),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 5, 4),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 20, -1),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Input tree: {input1}")
    print(f"Input document id: {input2}")
    print(f"Expected: {expected_output}")
    result = count_nested_levels(input1, input2)
    print(f"Actual:   {result}")
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