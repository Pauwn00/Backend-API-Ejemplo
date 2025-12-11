from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.database import engine, Base
from app.routers import auth

settings = get_settings()

# Inicializar FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    description="Backend ejemplo con FastAPI para aplicación móvil y panel de administrador",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_event():
    """
    Crear las tablas en la base de datos al iniciar
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Base de datos conectada y tablas creadas")
    except Exception as e:
        print(f"⚠️  Error al conectar con la base de datos: {e}")
        print("La API iniciará pero las operaciones de BD fallarán")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix=settings.API_V1_PREFIX)


@app.get("/")
async def root():
    return {
        "message": "Bienvenido a Backend Ejemplo API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
