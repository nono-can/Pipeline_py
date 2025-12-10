import pytest
from django.urls import reverse
from django.contrib.auth.models import User

# Utilisation d'une "fixture" Pytest qui donne accès à la base de données
# Le décorateur @pytest.mark.django_db est essentiel pour interagir avec la DB de Django
@pytest.mark.django_db 
def test_creation_utilisateur_db():
    """Vérifie qu'on peut créer un utilisateur dans la base de données de test."""
    
    # 1. Créer un objet dans la base de données
    user = User.objects.create_user(
        username='testuser', 
        email='test@example.com', 
        password='password123'
    )
    
    # 2. Vérifier que l'objet existe et que ses propriétés sont correctes
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.is_staff == False
    
    # 3. Vérifier que le nombre total d'utilisateurs est 1
    assert User.objects.count() == 1


def test_assertion_simple():
    """Un test simple sans base de données pour s'assurer que Pytest s'exécute."""
    a = 1 + 1
    assert a == 2