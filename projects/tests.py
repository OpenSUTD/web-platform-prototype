from django.test import TestCase, Client
from django.urls import reverse
from django.test.utils import setup_test_environment

from projects.models import *
from projects.forms import *

import time

client = Client()

# length of base template, used to test for empty pages
LEN_BASE = 2600

# Create your tests here.


class BaseWebsiteTestCase(TestCase):
    def setUp(self):
        super()

    def test_homepage_load(self):
        url = reverse('projects:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_homepage_not_empty(self):
        url = reverse('projects:home')
        response = self.client.get(url)
        self.assertGreater(len(response.content), LEN_BASE)

    def test_project_list_load(self):
        url = reverse('projects:projects_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_project_list_not_empty(self):
        url = reverse('projects:projects_list')
        response = self.client.get(url)
        self.assertGreater(len(response.content), LEN_BASE)

    def test_project_search_load(self):
        url = reverse('projects:projects_list_filter')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_project_search_not_empty(self):
        url = reverse('projects:projects_list_filter')
        response = self.client.get(url)
        self.assertGreater(len(response.content), LEN_BASE)


class SecuredPageTestCase(TestCase):
    def setUp(self):
        super()

    def test_auth_approval_view(self):
        url = reverse('projects:approval')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_auth_submit_view(self):
        url = reverse('projects:submit_new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_auth_submit_reject(self):
        url = reverse('projects:reject', args=("rand",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_auth_submit_approve(self):
        url = reverse('projects:approve', args=("rand",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class SubmissionFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        um = OpenSUTDUserManager()
        um.create_user("tom", display_name="Tom Magnanti",
                       display_picture="https://via.placeholder.com/150",
                       graduation_year=2018, pillar="ISTD",
                       password="tompassword")

    def test_submission_form_entry(self):
        self.client.login(username='tom', password='tompassword')

        # test user can actually get to the page
        response = self.client.get(reverse('projects:submit_new'))
        self.assertEqual(response.status_code, 200)

        # test submission mechanism
        form = SubmissionForm({'project_name': "test",
                               'caption': "test caption",
                               'category': "ACAD",
                               'featured_image': "",
                               'github_url': "https://github.com/OpenSUTD/web-platform-prototype",
                               'poster_url': ""})


class LogintoSecuredPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        um = OpenSUTDUserManager()
        um.create_user("tom", display_name="Tom Magnanti",
                       display_picture="https://via.placeholder.com/150",
                       graduation_year=2018, pillar="ISTD",
                       password="tompassword")

    def test_login_approval_view(self):
        self.client.login(username='tom', password='tompassword')
        response = self.client.get(reverse('projects:approval'))
        self.assertEqual(response.status_code, 200)

    def test_login_submission_view(self):
        self.client.login(username='tom', password='tompassword')
        response = self.client.get(reverse('projects:submit_new'))
        self.assertEqual(response.status_code, 200)


class UserTestCase(TestCase):
    def setUp(self):
        um = OpenSUTDUserManager()
        um.create_user("tom", display_name="Tom Magnanti",
                       display_picture="https://via.placeholder.com/150",
                       graduation_year=2018, pillar="ISTD")

        um.create_user("jane", display_name="Jane Tan",
                       display_picture="https://via.placeholder.com/150",
                       graduation_year=2021, pillar="ESD")

    def test_user_get_name(self):
        tom = User.objects.get(username="tom")
        self.assertEqual(tom.display_name, "Tom Magnanti")

        jane = User.objects.get(username="jane")
        self.assertEqual(jane.display_name, "Jane Tan")

    def test_user_get_year(self):
        tom = User.objects.get(username="tom")
        self.assertEqual(tom.graduation_year, 2018)

        jane = User.objects.get(username="jane")
        self.assertEqual(jane.graduation_year, 2021)

    def test_user_get_pillar(self):
        tom = User.objects.get(username="tom")
        self.assertEqual(tom.pillar, "ISTD")

        jane = User.objects.get(username="jane")
        self.assertEqual(jane.pillar, "ESD")

    # test user profile page contents

    def test_user_page_load(self):
        url = reverse('projects:user', args=("tom",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse('projects:user', args=("jane",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_page_not_empty(self):
        url = reverse('projects:user', args=("tom",))
        response = self.client.get(url)
        self.assertGreater(len(response.content), LEN_BASE)

        url = reverse('projects:user', args=("jane",))
        response = self.client.get(url)
        self.assertGreater(len(response.content), LEN_BASE)

    def test_user_page_name(self):
        url = reverse('projects:user', args=("tom",))
        response = str(self.client.get(url).content)
        self.assertEqual("Tom Magnanti" in response, True)

        url = reverse('projects:user', args=("jane",))
        response = str(self.client.get(url).content)
        self.assertEqual("Jane Tan" in response, True)

    def test_user_page_year(self):
        url = reverse('projects:user', args=("tom",))
        response = str(self.client.get(url).content)
        self.assertEqual("2018" in response, True)

        url = reverse('projects:user', args=("jane",))
        response = str(self.client.get(url).content)
        self.assertEqual("2021" in response, True)

    def test_user_page_pillar(self):
        url = reverse('projects:user', args=("tom",))
        response = str(self.client.get(url).content)
        self.assertEqual("ISTD" in response, True)

        url = reverse('projects:user', args=("jane",))
        response = str(self.client.get(url).content)
        self.assertEqual("ESD" in response, True)

    def test_user_page_performance(self):
        start = time.time()

        for i in range(10):
            url = reverse('projects:user', args=("tom",))
            response = self.client.get(url)
            url = reverse('projects:user', args=("jane",))
            response = self.client.get(url)

        duration = time.time() - start
        self.assertLess(duration, 1.5)


class ProjectShowcaseTestCase(TestCase):
    def setUp(self):
        pm = OpenSUTDProjectManager()

        pm.create_project(project_uid="ACAD_00001",
                          title="OpenSUTD Web Platform",
                          caption="Sample project 1",
                          category="ACAD",
                          url="https://github.com/OpenSUTD/web-platform-prototype",
                          poster_url="https://via.placeholder.com/150",
                          featured_image="https://via.placeholder.com/150")

        um = OpenSUTDUserManager()

        um.create_user("tom", display_name="Tom Magnanti",
                       display_picture="https://via.placeholder.com/150",
                       graduation_year=2018, pillar="ISTD")

        um.create_user("jane", display_name="Jane Tan",
                       display_picture="https://via.placeholder.com/150",
                       graduation_year=2021, pillar="ESD")

    def test_project_properties(self):
        proj = Project.objects.get(project_uid="ACAD_00001")
        self.assertEqual(proj.title, "OpenSUTD Web Platform")

    def test_add_user_project(self):
        pm = OpenSUTDProjectManager()
        pm.add_user_to_project("ACAD_00001", "tom")
        proj = Project.objects.get(project_uid="ACAD_00001")
        self.assertEqual(len(proj.users.all()), 1)
        pm.add_user_to_project("ACAD_00001", "jane")
        self.assertEqual(len(proj.users.all()), 2)

    def test_add_tag_project(self):
        pm = OpenSUTDProjectManager()
        pm.add_tag_to_project("ACAD_00001", "rand1,rand2")
        proj = Project.objects.get(project_uid="ACAD_00001")
        self.assertEqual(len(proj.tags.all()), 2)

    def test_add_del_user_project(self):
        tom = User.objects.get(username="tom")
        jane = User.objects.get(username="jane")
        proj = Project.objects.get(project_uid="ACAD_00001")
        proj.users.add(tom)
        proj.users.add(jane)
        proj.users.remove(jane)
        self.assertEqual(len(proj.users.all()), 1)

    def test_project_page_not_approved(self):
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        #self.assertGreater(len(response.content), LEN_BASE)

    def test_project_page_approved(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), LEN_BASE)

    def test_project_page_name(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = str(self.client.get(url).content)
        self.assertEqual("OpenSUTD Web Platform" in response, True)

    def test_project_tag(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        pm.add_tag_to_project("ACAD_00001", "tag1,tag2")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = str(self.client.get(url).content)
        self.assertEqual("tag1" in response, True)
        self.assertEqual("tag2" in response, True)

    def test_project_page_contents(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = str(self.client.get(url).content)
        # print(response)
        # test top and bottom of contents
        # this does not pass on Travis for Pull Request builds
        # due to them disabling env variables for security reasons
        #self.assertEqual("Prototype for the Eventual OpenSUTD Web Platform" in response, True)
        #self.assertEqual("Data Model" in response, True)
        self.assertGreater(len(response), LEN_BASE)

    def test_project_page_load(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_project_page_not_empty(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = str(self.client.get(url).content)
        self.assertGreater(len(response), LEN_BASE)

    def test_project_author_name(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        pm.add_user_to_project("ACAD_00001", "tom")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = str(self.client.get(url).content)
        self.assertEqual("Tom Magnanti" in response, True)

    def test_project_author_pillar(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        pm.add_user_to_project("ACAD_00001", "tom")
        url = reverse('projects:project_page', args=("ACAD_00001",))
        response = str(self.client.get(url).content)
        self.assertEqual("ISTD" in response, True)

    def test_project_list_page(self):
        pm = OpenSUTDProjectManager()
        pm.set_project_status("ACAD_00001", "ACCEPT")
        url = reverse('projects:projects_list')
        response = str(self.client.get(url).content)
        self.assertEqual("OpenSUTD Web Platform" in response, True)
        self.assertEqual("Sample project 1" in response, True)

    def test_project_page_performance(self):
        start = time.time()

        for _ in range(10):
            url = reverse('projects:project_page', args=("ACAD_00001",))
            response = self.client.get(url)

        duration = time.time() - start
        self.assertLess(duration, 1.5)
