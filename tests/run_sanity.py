from assignment_01_prime_checker import is_prime
from assignment_02_student_grade_system import get_grade
from assignment_03_array_statistics import sum_numbers, average, find_max, find_min
from assignment_05_fibonacci_sequence import generate_fibonacci, is_fibonacci
from assignment_09_simple_calculator import add, divide


def check(name, cond):
    print(f"{name}: {'PASS' if cond else 'FAIL'}")
    return cond


def main():
    ok = True
    ok = ok and check("prime 7", is_prime(7) is True)
    ok = ok and check("prime 10", is_prime(10) is False)
    ok = ok and check("grade 85", get_grade(85) == 'A')
    ok = ok and check("grade 110", get_grade(110) is None)
    nums = [4, 7, 2, 9, 1]
    ok = ok and check("sum", sum_numbers(nums) == 23)
    ok = ok and check("avg", abs(average(nums) - 4.6) < 1e-9)
    ok = ok and check("max", find_max(nums) == 9)
    ok = ok and check("min", find_min(nums) == 1)
    ok = ok and check("fib gen 7", generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8])
    ok = ok and check("is_fib 13", is_fibonacci(13) is True)
    ok = ok and check("is_not_fib 20", is_fibonacci(20) is False)
    ok = ok and check("add", add(2, 3) == 5)
    try:
        divide(5, 0)
        ok = ok and check("divide zero", False)
    except ZeroDivisionError:
        ok = ok and check("divide zero", True)

    print("ALL OK" if ok else "SOME TESTS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
