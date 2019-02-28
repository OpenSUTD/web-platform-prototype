from django.test import TestCase, Client
from django.urls import reverse
from django.test.utils import setup_test_environment

from projects.models import *

client = Client()

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(user_id="tom",
                            display_name="Tom Magnanti",
                            graduation_year=2018,
                            pillar="ISTD")

        User.objects.create(user_id="jane",
                            display_name="Jane Tan",
                            graduation_year=2021,
                            pillar="ESD")

    def test_user_basic_info(self):
        tom = User.objects.get(user_id="tom")
        self.assertEqual(tom.pillar, "ISTD")
        self.assertEqual(tom.graduation_year, 2018)
        self.assertEqual(tom.display_name, "Tom Magnanti")

        jane = User.objects.get(user_id="jane")
        self.assertEqual(jane.pillar, "ESD")
        self.assertEqual(jane.graduation_year, 2021)
        self.assertEqual(jane.display_name, "Jane Tan")

    def test_user_page(self):
        url = reverse('projects:user', args=("tom",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), 10)

        url = reverse('projects:user', args=("jane",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), 10)


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

    

