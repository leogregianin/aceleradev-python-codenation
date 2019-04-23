from main import filter_email
import unittest


class EmailValidTests(unittest.TestCase):
    def test_one(self):
        emails = [
            'lara@codenation.com',
            'brian-23@codenation.com.br',
            'britts_54@codenation.com'
        ]
        self.assertEqual(len(filter_email(emails)), 3)

    def test_two(self):
        emails = [
            'lara@gmail',
            'brian-23@codenation.br'
        ]
        self.assertEqual(len(filter_email(emails)), 1)

    def test_three(self):
        emails = [
            'dheeraj-234@gmail.com',
            'itsallcrap',
            'harsh_1234@red2iff.in',
            'kunal_shin@iop.az',
            'matt23@@india.in'
        ]
        self.assertEqual(len(filter_email(emails)), 3)

    def test_four(self):
        emails = [
            'fjladfk_iasdfad234@sdlkjf23335.in',
            'ha@git@int.cz',
            'prashant24_@gmail.com'
        ]
        self.assertEqual(len(filter_email(emails)), 2)

if __name__ == '__main__':
    unittest.main()
