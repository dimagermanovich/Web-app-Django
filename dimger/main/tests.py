from django.test import TestCase


class TestMain(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_about_text(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Про нас', response.content.decode())


    # def test_index_neg(self):
    #     response = self.client.get('')
    #     self.assertEqual(response.status_code, 300)


    # def test_index_about_neg(self):
    #     response = self.client.get('/about')
    #     self.assertEqual(response.status_code, 300)


    def test_index_contacts(self):
        response = self.client.get('/contacts')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Contacts', response.content.decode())

    # def test_index_contacts_neg(self):
    #     response = self.client.get('/contacts')
    #     self.assertEqual(response.status_code, 300)


    def test_reg(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Registration', response.content.decode())

    # def test_reg_neg(self):
    #     response = self.client.get('/register/')
    #     self.assertEqual(response.status_code, 300)

    def test_log(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Log in', response.content.decode())

    # def test_log_neg(self):
    #     response = self.client.get('/login/')
    #     self.assertEqual(response.status_code, 300)

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)


    # def test_logout_neg(self):
    #     response = self.client.get('/logout/')
    #     self.assertEqual(response.status_code, 202)










