from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase

from .models import table, tableIncapables
from datetime import datetime, date, time
# Create your tests here.


class TestSick(TestCase):

    def test_sick(self):
        response = self.client.get('/sick_leave/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Accounting for sick leave', response.content.decode())

    def test_sick_neg(self):
        response = self.client.get('/sick_leave/')
        self.assertNotEqual(response.status_code, 300)

    def test_sick_incap(self):
        response = self.client.get('/sick_leave/incapable')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Disabled persons', response.content.decode())

    def test_sick_incap_neg(self):
        response = self.client.get('/sick_leave/incapable')
        self.assertNotEqual(response.status_code, 300)


    def test_sick_incap_cr(self):
        response = self.client.get('/sick_leave/create')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Form for adding sick leave', response.content.decode())

    def test_sick_incap_cr_neg(self):
        response = self.client.get('/sick_leave/create')
        self.assertNotEqual(response.status_code, 300)

    def test_sick_incap_cr_incapable(self):
        response = self.client.get('/sick_leave/createincapable')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Form for adding persons', response.content.decode())

    def test_sick_incap_cr_incapable_neg(self):
        response = self.client.get('/sick_leave/createincapable')
        self.assertNotEqual(response.status_code, 300)

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Dima', password='1', email='test@example.com')
        self.user.save()
        tableIncapables.objects.create(lastName = 'Germanovich', firstName = 'Dmitriy', patronymic = 'Sergeevich')
        incap = tableIncapables.objects.get(firstName = 'Dmitriy')
        table.objects.create(number_of_list = 123456789111, name_of_organization = 'BSU', work = 'Director',
                             ache = 'Headache', begin_date = '2022-10-12', end_date = '2022-12-10', incapable=incap)

    def test_correct(self):
        user = authenticate(username='Dima', password='1')
        self.assertTrue((user is not None) and user.is_authenticated)


    def test_wrong_username(self):
        user = authenticate(username='d', password='2')
        self.assertFalse(user is not None and user.is_authenticated)


    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_voditels_valid_value(self):
        incap = tableIncapables.objects.get(firstName = 'Dmitriy')
        link = table.objects.get(incapable=incap)
        self.assertEquals(incap.lastName, "Germanovich")
        self.assertNotEquals(incap.lastName, "dscds")
        self.assertEquals(incap.firstName, "Dmitriy")
        self.assertNotEquals(incap.firstName, "Dm")
        self.assertEquals(incap.patronymic, "Sergeevich")
        self.assertNotEquals(incap.patronymic, "dsc")
        self.assertEquals(link.work, 'Director')
        self.assertNotEquals(link.work, 'student')
        self.assertEquals(link.number_of_list, 123456789111)
        self.assertNotEquals(link.number_of_list, 21)
        self.assertEquals(link.name_of_organization, 'BSU')
        self.assertNotEquals(link.name_of_organization, 'BSUIR')
        self.assertEquals(link.ache, 'Headache')
        self.assertNotEquals(link.ache, 'fcvfdv')
        self.assertEquals(link.begin_date, date(2022, 10, 12))
        self.assertNotEquals(link.begin_date, '2022-11-12')
        self.assertEquals(link.end_date, date(2022, 12, 10))
        self.assertNotEquals(link.end_date, '2022-12-12')

    def test_get_absolute_sick_leave_url_with_id(self):
        obj = table.objects.get(id=1)
        self.assertEqual(obj.get_absolute_url(), "/sick_leave/1")

    def test_get_absolute_url_incapable_with_id(self):
        obj1 = tableIncapables.objects.get(id=1)
        self.assertEqual(obj1.get_absolute_url(), "/sick_leave/incapable/1")

    def test_string_method_car(self):
        incapable = tableIncapables.objects.get(id=1)
        expected_string = incapable.lastName + ' ' + incapable.firstName + ' ' + incapable.patronymic
        self.assertEqual(str(incapable), expected_string)














