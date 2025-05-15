from types import FunctionType
from functor.Maybe import Maybe, Just, Nothing
import unittest


class MaybeTest(unittest.TestCase):
    def test_of_01(self):
        x = Maybe.of(42)
        self.assertIsInstance(x, Just)
        self.assertIsInstance(x.value, int)
        self.assertEqual(x.value, 42)

    def test_of_02(self):
        x = Maybe.of(None)
        self.assertEqual(x, Nothing.of())


class JustTest(unittest.TestCase):
    def test_of_01(self):
        x = Just.of(42)
        self.assertIsInstance(x, Just)
        self.assertIsInstance(x.value, int)
        self.assertEqual(x.value, 42)

    def test_of_02(self):
        def inc(x: int) -> int:
            return x + 1

        x = Just.of(inc)
        self.assertIsInstance(x, Just)
        self.assertIsInstance(x.value, FunctionType)
        self.assertEqual(x.value, inc)
        self.assertEqual(x.value(10), 11)

    def test_fmap_01(self):
        x = Just.of(5)
        y = x.fmap(lambda n: n + 10)
        self.assertIsInstance(y, Just)
        self.assertEqual(y.value, 15)

        self.assertNotEqual(id(x), id(y))

        z = x.fmap(str)
        self.assertEqual(z.value, "5")
        self.assertIsInstance(z.value, str)

    def test_fmap_02(self):
        x = Just.of(5)
        y = x.fmap(lambda _: None)
        self.assertEqual(y, Nothing.of())

        z = x.fmap(str)
        self.assertEqual(z.value, "5")
        self.assertIsInstance(z.value, str)


class NothingTest(unittest.TestCase):
    def test_of(self):
        x = Nothing.of()
        y = Nothing.of()
        self.assertEqual(x, y)

    def test_fmap(self):
        x = Nothing.of()
        y = x.fmap(lambda n: n + 10)
        self.assertEqual(y, Nothing())


if __name__ == "__main__":
    unittest.main()
