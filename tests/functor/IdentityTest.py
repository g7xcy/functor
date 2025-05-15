from types import FunctionType
from functor.Identity import Identity
import unittest


class IdentityTest(unittest.TestCase):
    def test_of_01(self):
        x = Identity.of(42)
        self.assertIsInstance(x, Identity)
        self.assertIsInstance(x.value, int)
        self.assertEqual(x.value, 42)

    def test_of_02(self):
        x = Identity.of(None)
        self.assertIsInstance(x, Identity)
        self.assertIsInstance(x.value, None.__class__)
        self.assertEqual(x.value, None)

    def test_of_03(self):
        def inc(x: int) -> int:
            return x + 1

        x = Identity.of(inc)
        self.assertIsInstance(x, Identity)
        self.assertIsInstance(x.value, FunctionType)
        self.assertEqual(x.value, inc)
        self.assertEqual(x.value(10), 11)

    def test_fmap(self):
        x = Identity.of(5)
        y = x.fmap(lambda n: n + 10)
        self.assertIsInstance(y, Identity)
        self.assertEqual(y.value, 15)

        self.assertNotEqual(id(x), id(y))

        z = x.fmap(str)
        self.assertEqual(z.value, "5")
        self.assertIsInstance(z.value, str)


if __name__ == "__main__":
    unittest.main()
