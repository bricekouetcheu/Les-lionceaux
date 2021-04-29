from drf_yasg2 import openapi

username = openapi.Parameter(
    'username',
    openapi.IN_QUERY,
    description="Username",
    required=True,
    type=openapi.TYPE_STRING
)
password = openapi.Parameter(
    'password',
    openapi.IN_QUERY,
    description="Mot de passe de l'utilisateur",
    required=True,
    type=openapi.TYPE_STRING
)

login_schema = [username, password]

nom = openapi.Parameter(
    'nom',
    openapi.IN_QUERY,
    description="Nom",
    required=True,
    type=openapi.TYPE_STRING
)
prenom = openapi.Parameter(
    'prenom',
    openapi.IN_QUERY,
    description="Prénom",
    required=True,
    type=openapi.TYPE_STRING
)
email = openapi.Parameter(
    'email',
    openapi.IN_QUERY,
    description="Email",
    required=True,
    type=openapi.TYPE_STRING
)
message = openapi.Parameter(
    'message',
    openapi.IN_QUERY,
    description="Message",
    required=True,
    type=openapi.TYPE_STRING
)
telephone = openapi.Parameter(
    'telephone',
    openapi.IN_QUERY,
    description="Téléphone",
    required=True,
    type=openapi.TYPE_INTEGER
)

contact_schema = [nom, prenom, email, message, telephone]