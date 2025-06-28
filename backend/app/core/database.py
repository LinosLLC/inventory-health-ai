"""
Database configuration and connection management
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import structlog
from typing import AsyncGenerator
import asyncio

from app.core.config import settings

logger = structlog.get_logger()

# Database engine
engine = create_engine(
    settings.DATABASE_URL,
    poolclass=StaticPool,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,
    echo=settings.DEBUG
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Metadata
metadata = MetaData()

async def init_db():
    """Initialize database tables"""
    try:
        # Import all models to ensure they are registered
        from app.models import inventory, plants, materials, users
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
        
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_db_async() -> AsyncGenerator:
    """Get async database session"""
    # For now, using sync session in async context
    # In production, consider using async SQLAlchemy
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 