from django.test import TestCase


# Create your tests here.
class PassingTest(TestCase):
    def test(self):
        self.assertTrue(True)


class FailingTest(TestCase):
    def test(self):
        self.assertTrue(False)
