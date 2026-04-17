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

    


