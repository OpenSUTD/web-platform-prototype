from django.test import TestCase, Client
from django.urls import reverse
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from .forms import RegistrationForm

from projects.models import *

import time

client = Client()

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(user_id="tom",
                            display_name="Tom Magnanti",
                            graduation_year=2018,
                            pillar="ISTD",
                            contact_email="tom@sutd.edu.sg",
                            personal_links="tommagnanti")

        User.objects.create(user_id="jane",
                            display_name="Jane Tan",
                            graduation_year=2021,
                            pillar="ESD",
                            contact_email="jane.sutd.edu.sg",
                            personal_links="janetan.com")

    def test_user_basic_info(self):
        tom = User.objects.get(user_id="tom")
        self.assertEqual(tom.pillar, "ISTD")
        self.assertEqual(tom.graduation_year, 2018)
        self.assertEqual(tom.display_name, "Tom Magnanti")
        self.assertEqual(tom.contact_email, "tom@sutd.edu.sg")
        self.assertEqual(tom.personal_links, "tommagnanti")

        jane = User.objects.get(user_id="jane")
        self.assertEqual(jane.pillar, "ESD")
        self.assertEqual(jane.graduation_year, 2021)
        self.assertEqual(jane.display_name, "Jane Tan")
        self.assertEqual(jane.contact_email, "jane.sutd.edu.sg")
        self.assertEqual(jane.personal_links, "janetan.com")

    def test_user_page(self):
        url = reverse('projects:user', args=("tom",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), 10)

        url = reverse('projects:user', args=("jane",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), 10)

    def test_valid_email(self):
        tom = User.objects.get(user_id="tom")
        self.assertTrue(User.valid_email(tom.contact_email))
        jane = User.objects.get(user_id="jane")
        self.assertTrue(User.valid_email(jane.contact_email))

    def test_valid_links(self):
        tom = User.objects.get(user_id="tom")
        self.assertTrue(User.valid_links(tom.personal_links))
        jane = User.objects.get(user_id="jane")
        self.assertTrue(User.valid_links(jane.personal_links))

    def test_user_page_performance(self):
        start = time.time()
        
        for i in range(10):
            url = reverse('projects:user', args=("tom",))
            response = self.client.get(url)
            url = reverse('projects:user', args=("jane",))
            response = self.client.get(url)
        
        duration = time.time() - start
        self.assertLess(duration, 1.0)

class ProjectShowcaseTestCase(TestCase):
    def setUp(self):
        Project.objects.create(title="OpenSUTD Web Platform",
                                project_uid="ACAD_00001",
                                caption="Sample project 1",
                                category="ACAD",
                                url="https://github.com/OpenSUTD/web-platform-prototype",
                                status="ACCEPT")

        User.objects.create(user_id="tom",
                            display_name="Tom Magnanti",
                            graduation_year=2018,
                            pillar="ISTD")

        User.objects.create(user_id="jane",
                            display_name="Jane Tan",
                            graduation_year=2021,
                            pillar="ESD")
        
    def test_add_user_project(self):
        tom = User.objects.get(user_id="tom")
        jane = User.objects.get(user_id="jane")

        proj = Project.objects.get(project_uid="ACAD_00001")
        proj.users.add(tom)
        proj.users.add(jane)

        self.assertEqual(len(proj.users.all()), 2)

    def test_add_del_user_project(self):
        tom = User.objects.get(user_id="tom")
        jane = User.objects.get(user_id="jane")

        proj = Project.objects.get(project_uid="ACAD_00001")
        proj.users.add(tom)
        proj.users.add(jane)

        proj.users.remove(jane)

        self.assertEqual(len(proj.users.all()), 1)

    def test_project_page(self):
        url = reverse('projects:showcase', args=("ACAD_00001",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), 10)

    def test_project_page_performance(self):
        start = time.time()
        
        for i in range(20):
            url = reverse('projects:showcase', args=("ACAD_00001",))
            response = self.client.get(url)
        
        duration = time.time() - start
        self.assertLess(duration, 1.0)



class TestRegistrationForm(TestCase):

  #https://www.agiliq.com/blog/2018/05/django-unit-testing/#writing-tests-for-forms

  def test_registration_form(self):
    # test invalid data
    invalid_data = {
      "username": "user@test.com",
      "password": "secret",
      "confirm": "not secret"
    }
    form = RegistrationForm(data=invalid_data)
    form.is_valid()
    self.assertTrue(form.errors)

    # test valid data
    valid_data = {
      "username": "user@test.com",
      "password": "secret",
      "confirm": "secret"
    }

    form = RegistrationForm(data=valid_data)
    form.is_valid()
    self.assertFalse(form.errors)


class TestUserRegistrationView(TestCase):

  def setUp(self):
    self.client = Client()

  def test_registration(self):
    url = reverse('register')
    
    # test req method GET
    response = self.client.get(url)
    self.assertEqual(response.status, 200)

    # test req method POST with empty data
    response = self.client.post(url, {})
    self.assertEqual(response.status, 200)
    exp_data = {
      'error': True,
      'errors': {
        'username': 'This field is required',
        'password': 'This field is required',
        'confirm': 'This field is required',
      }
    }
    self.asssertEqual(exp_data, response.json())
    
    # test req method POST with invalid data
    req_data = {
      'username': 'user@test.com',
      'password': 'secret',
      'confirm': 'secret1',
    }
    response = self.client.post(url, req_data)
    self.assertEqual(response.status, 200)
    exp_data = {
      'error': True,
      'errors': {
        'confirm': 'Passwords mismatched'
      }
    }
    self.asssertEqual(exp_data, response.json())

    # test req method POST with valid data
    req_data = {
      'username': 'user@test.com',
      'password': 'secret',
      'confirm': 'secret',
    }
    response = self.client.post(url, req_data)
    self.assertEqual(response.status, 200)
    exp_data = {
      'error': False,
      'message': 'Success, Please login'
    }
    self.asssertEqual(exp_data, response.json())
    self.assertEqual(User.objects.count(), 1)


