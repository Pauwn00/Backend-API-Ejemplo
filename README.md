# Backend Ejemplo API

Backend en FastAPI para aplicación móvil y panel de administrador con autenticación JWT y base de datos SQLite.

## Características

- 🚀 FastAPI framework
- 🔐 Autenticación JWT con hasheo de contraseñas (bcrypt)
- 🗄️ Base de datos SQLite con SQLAlchemy ORM (fácil migración a PostgreSQL/MySQL)
- 👤 Sistema de usuarios con niveles de skate (1-5)
- 📝 Endpoints de Login y Signup
- 📚 Documentación automática con Swagger UI

## Requisitos

- Python 3.8+
- MySQL 5.7+ o MariaDB
- pip

## Instalación

1. **Clonar el repositorio** (si aplica)

2. **Crear entorno virtual**

```bash
python -m venv venv
```

3. **Activar entorno virtual**

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

5. **Configurar base de datos**

Crear base de datos en MySQL:

```sql
CREATE DATABASE tricklabz_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

6. **Configurar variables de entorno**

Copiar `.env.example` a `.env` y configurar:

```bash
cp .env.example .env
```

Editar `.env` con tus credenciales:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=tricklabz_db

SECRET_KEY=tu-clave-secreta-super-segura-cambiar-en-produccion
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Importante**: Genera una SECRET_KEY segura. Puedes usar:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## Ejecutar la aplicación

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: `http://localhost:8000`

## Documentación

Una vez iniciada la aplicación, accede a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

### Autenticación

#### POST `/api/v1/auth/signup`

Registrar nuevo usuario

**Body:**

```json
{
  "email": "usuario@example.com",
  "nombre": "Juan Pérez",
  "password": "contraseña123",
  "nivel_skate": 3
}
```

**Response:**

```json
{
  "id": 1,
  "email": "usuario@example.com",
  "nombre": "Juan Pérez",
  "nivel_skate": 3,
  "created_at": "2025-12-11T10:00:00",
  "updated_at": null
}
```

#### POST `/api/v1/auth/login`

Iniciar sesión

**Body:**

```json
{
  "email": "usuario@example.com",
  "password": "contraseña123"
}
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### GET `/api/v1/auth/me`

Obtener información del usuario autenticado

**Headers:**

```
Authorization: Bearer {token}
```

**Response:**

```json
{
  "id": 1,
  "email": "usuario@example.com",
  "nombre": "Juan Pérez",
  "nivel_skate": 3,
  "created_at": "2025-12-11T10:00:00",
  "updated_at": null
}
```

## Estructura del Proyecto

```
Tricklabz/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación principal
│   ├── config.py            # Configuración
│   ├── database.py          # Conexión a base de datos
│   ├── models/              # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/             # Esquemas Pydantic
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routers/             # Endpoints
│   │   ├── __init__.py
│   │   └── auth.py
│   └── utils/               # Utilidades
│       ├── __init__.py
│       └── security.py      # Hasheo y JWT
├── .env                     # Variables de entorno (no versionar)
├── .env.example             # Ejemplo de variables
├── .gitignore
├── requirements.txt         # Dependencias
└── README.md
```

## Modelo de Usuario

```python
class User:
    id: int                  # ID único
    email: str               # Email único
    nombre: str              # Nombre del usuario
    hashed_password: str     # Contraseña hasheada con bcrypt
    nivel_skate: int         # Nivel de 1 a 5
    created_at: datetime     # Fecha de creación
    updated_at: datetime     # Fecha de actualización
```

## Seguridad

- ✅ Contraseñas hasheadas con bcrypt
- ✅ Tokens JWT con expiración
- ✅ Validación de datos con Pydantic
- ✅ Protección contra SQL injection (SQLAlchemy ORM)
- ✅ CORS configurado (ajustar para producción)

## Próximos pasos

- [ ] Agregar más endpoints para gestión de usuarios
- [ ] Implementar roles (usuario, admin)
- [ ] Agregar refresh tokens
- [ ] Implementar recuperación de contraseña
- [ ] Agregar tests unitarios
- [ ] Configurar logging
- [ ] Dockerizar la aplicación

## Licencia

MIT
