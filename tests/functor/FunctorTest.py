from functor.Functor import Functor
import unittest


class FunctorTest(unittest.TestCase):
    def test_of(self):
        with self.assertRaises(NotImplementedError) as e:
            Functor.of(42)
        self.assertEqual(e.msg, "Cannot instantiate Maybe directly.")


if __name__ == "__main__":
    unittest.main()
