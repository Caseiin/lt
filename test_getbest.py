import unittest;
import io;
from getbest import getCols, findTop

#helper function used to create fake files using stringIO

def make_file(*lines):
    return io.StringIO("\n" .join(lines) + "\n")


#class
class TestGetBest(unittest.TestCase):
    # Tests for getCols

    def test_getCols_return_correct_student_number_column(self):
        f = make_file("Course,Student Number,Mark,Comment")
        num_col, _ = getCols(f)
        self.assertEqual(num_col,1)

    def test_getCols_returns_correct_mark_column(self):
        f = make_file("Course,Student Number,Mark,Comment")
        _, mark_col = getCols(f)
        self.assertEqual(mark_col,2)

    def test_getCols_different_order(self):
        f = make_file("Mark,Course,Student Number,Comment")
        num_col, mark_col = getCols(f)

        self.assertEqual(num_col, 2)
        self.assertEqual(mark_col, 0)

    # def test_getCols_only_reads_header(self):
    #     f = make_file(
    #         "Course,Student Number,Mark,Comment",
    #         "ELEN3020,160001,72,OK",
    #     )

    #     getCols(f)
    #     remaining = f.read()

    #     self.assertIn("160001", remaining)

    # Tests for findTop

    def test_findTop_highest_student(self):
        f = make_file(
            "ELEN3020,160001,72,OK",
            "ELEN3020,167381,90,Check",
            "ELEN3020,143211,83,-",
        )

        best_idx, _ = findTop(f, num_col=1, mark_col=2)

        self.assertEqual(best_idx, "167381")

    def test_findTop_single_student(self):
        f = make_file("ELEN3020,160001,72,OK")

        best_idx, best = findTop(f, num_col=1, mark_col=2)

        self.assertEqual(best_idx, "160001")
        self.assertEqual(best, 72)

    def test_findTop_last_row_best(self):
        f = make_file(
            "ELEN3020,160001,55,OK",
            "ELEN3020,143211,60,-",
            "ELEN3020,167381,95,Check",
        )

        best_idx, best = findTop(f, num_col=1, mark_col=2)

        self.assertEqual(best_idx, "167381")
        self.assertEqual(best, 95)

    def test_findTop_first_row_best(self):
        f = make_file(
            "ELEN3020,167381,95,Check",
            "ELEN3020,160001,55,OK",
            "ELEN3020,143211,60,-",
        )

        best_idx, best = findTop(f, num_col=1, mark_col=2)

        self.assertEqual(best_idx, "167381")
        self.assertEqual(best, 95)


