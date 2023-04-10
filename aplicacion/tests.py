from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

from aplicacion.models import User

# Create your tests here.

class CreateUserTest(APITestCase):
    def setUp (self):
        self.url = reverse("crear-usuario")
        self.data ={
                    "email":"admin34@admin.com",
                    "username":"admin137",
                    "password":"admin1234"
                    }
    def test_create_user(self):
        response = self.client.post(self.url,self.data)
        self.assertEqual(response.status_code,201)
        
class ListPersonasTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',email='admin@admin.com' ,password='testpassword')
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
    def test_list_personas(self):
        self.url = reverse("listar-personas")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.user.email,"admin@admin.com")
        
    
        
    
