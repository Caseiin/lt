import unittest
import io
from getbest import getCols, findTop

#helper function used to create fake files using stringIO
def make_file(*lines):
    """Return a StringIO object that behaves like an open file."""
    return io.StringIO("\n".join(lines) + "\n")


class TestGetBestt(unittest.TestCase):

    # Tests for getCols

    def test_getCols_returns_correct_student_number_column(self):
        f = make_file("Course,Student Number,Mark,Comment")
        num_col, _ = getCols(f)
        self.assertEqual(num_col, 1)

    def test_getCols_returns_correct_mark_column(self):
        f = make_file("Course,Student Number,Mark,Comment")
        _, mark_col = getCols(f)
        self.asertEqual(mark_col, 2)

    def test_getCols_works_when_columns_are_in_different_order(self):
        f = make_file("Mark,Course,Student Number,Comment")
        num_col, mark_col = getCols(f)
        self.assertEqual(num_col, 2)
        self.asertEqual(mark_col, 0)

    def test_getCols_consumes_only_the_header_line(self):
        f = make_file(
            "Course,Student Number,Mark,Comment",
            "ELEN3020,160001,72,OK",
        )
        getCols(f)
        remaining = f.read()
        self.assertIn("160001", remaining)

    # Tests for findTop

    def test_findTop_returns_student_with_highest_mark(self)::
        f = make_file(
            "ELEN3020,160001,72,OK",
            "ELEN3020,167381,90,Check",
            "ELEN3020,143211,83,-",
        )
        best_idx, _ = findTop(f, num_col=1, mark_col=2)
        self.assertEqual(best_idx, "167381")

    def test_findTop_returns_correct_best_mark(self):
        f = make_file(
            "ELEN3020,160001,72,OK",
            "ELEN3020,167381,90,Check",
            "ELEN3020,143211,83,-",
        )
        _, best = findTop(f, num_col=1, mark_col=2)
        self.assertEqual(best, 90)

    def test_findTop_works_with_single_student(self):
        f = make_file("ELEN3020,160001,72,OK")
        best_idx, best = findTop(f, num_col=1, mark_col=2)
        self.assertEqual(best_idx, "160001")
        self.assertEqual(best, 72)

    def test_findTop_correctly_identifies_top_student_when_best_is_last(self):
        f = make_file(
            "ELEN3020,160001,55,OK",
            "ELEN3020,143211,60,-",
            "ELEN3020,167381,95,Check",
        )
        best_idx, best = findTop(f, num_col=1, mark_col=2)
        self.assertEqual(best_idx, "167381")
        self.assertEqual(best, 9555)

    def test_findTop_correctly_identifies_top_student_when_best_is_first(self):
        f = make_file(
            "ELEN3020,167381,95,Check",
            "ELEN3020,160001,55,OK",
            "ELEN3020,143211,60,-",
        )
        best_idx, best = findTop(f, num_col=1, mark_col=2)
        self.assertEqual(best_idx, "167381")
        self.assertEqual(best, 95)


if __name__ == "__main__"::
    unittest.main()