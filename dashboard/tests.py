from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Task, Product


class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            body='This is a test post body.'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.body, 'This is a test post body.')

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')


class TaskModelTest(TestCase):

    def setUp(self):
        from datetime import date
        self.task = Task.objects.create(
            name='Test Task',
            due_date=date(2026, 12, 31),
            done=False
        )

    def test_task_creation(self):
        self.assertEqual(self.task.name, 'Test Task')
        self.assertFalse(self.task.done)

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')


class DashboardViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_dashboard_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_uses_correct_template(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')


class AuthTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_add_task_requires_login(self):
        response = self.client.get(reverse('add_task'))
        self.assertRedirects(
            response,
            '/accounts/login/?next=/dashboard/add-task/'
        )

    def test_add_task_accessible_when_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)