📌 Backend - API de Registro de Usuarios

API REST desarrollada con FastAPI que permite registrar usuarios validando email, contraseña y almacenando la contraseña de forma segura usando hash.

🛠 Tecnologías utilizadas
1️⃣ fastapi

Framework moderno y rápido para crear APIs con Python.

Manejo de rutas

Validación automática de datos

Documentación automática (Swagger)

Soporte para tipado fuerte

2️⃣ uvicorn

Servidor ASGI que ejecuta la aplicación FastAPI.

Permite:

Levantar el servidor

Recarga automática con --reload

Manejar peticiones HTTP

3️⃣ sqlalchemy

ORM (Object Relational Mapper) para interactuar con la base de datos.

Permite:

Crear modelos como clases Python

Realizar consultas sin escribir SQL directo

Manejar sesiones de base de datos

4️⃣ bcrypt

Librería para hashear contraseñas de forma segura.


Protege contraseñas antes de guardarlas

Previene almacenamiento en texto plano

5️⃣ email-validator

Valida que el correo tenga un formato correcto.

Se usa internamente junto con Pydantic para validar el campo EmailStr.

🗄 Base de datos

Se utiliza SQLite.

Base de datos ligera

No requiere servidor

Ideal para proyectos pequeños o escolares

El archivo users.db se crea automáticamente al ejecutar el proyecto.

📂 Estructura del proyecto
backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   └── utils/
│
├── requirements.txt
└── README.md

🚀 Instalación y ejecución
1️⃣ Clonar el repositorio
```bash
git clone <url-del-repo>
cd backend
```

2️⃣ Crear entorno virtual
```bash
python -m venv venv
```

Activar entorno:
```bash
venv\Scripts\activate
```

3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

4️⃣ Ejecutar el servidor
```bash
python -m uvicorn app.main:app --reload
```

🌐 Probar la API

Una vez levantado el servidor, abrir en el navegador:
```bash
http://127.0.0.1:8000/docs

```

Aquí encontrarás la documentación automática con Swagger UI.

📌 Endpoints disponibles
```bash
🔹 POST /register
```

Registra un nuevo usuario.

Validaciones:

El email debe tener formato válido

La contraseña debe tener entre 8 y 10 caracteres

El email no debe existir previamente

Ejemplo de request:

```json
{
  "email": "test@gmail.com",
  "password": "12345678"
}
```

```bash
🔹 GET /users
```

Devuelve la lista de usuarios registrados.

Ejemplo de respuesta:

```json
[
  {
    "id": 1,
    "email": "test@gmail.com",
    "paswword": "$2$dHidu8B6dnK"
  }
]
```

🔐 Seguridad

Las contraseñas se almacenan hasheadas usando bcrypt.

Nunca se guardan en texto plano.