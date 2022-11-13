from django.test import SimpleTestCase

# Create your tests here.

class SimpleTestCase(SimpleTestCase):

    def test_signup_page_uses_correct_templates(self):
        response = self.client.get('/signup')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_home_page_status_code(self):
        response= self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response= self.client.get('/about')
        self.assertEqual(response.status_code,200)

    def test_home_page_uses_correct_templates(self):
        response= self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_about_page_uses_correct_templates(self):
        response= self.client.get('/about/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_dev1_page_uses_correct_templates(self):
        response = self.client.get('/dev1/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'pages/dev1.html')

    def test_dev2_page_uses_correct_templates(self):
        response = self.client.get('/dev2/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'pages/dev2.html')