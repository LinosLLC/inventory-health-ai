"""
Configuration settings for Inventory Health AI
"""

from pydantic_settings import BaseSettings
from typing import List, Optional
import os

class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "Inventory Health AI"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/inventory_health_ai"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 30
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "https://your-domain.com"
    ]
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # SAP Configuration
    SAP_HOST: Optional[str] = None
    SAP_CLIENT: Optional[str] = None
    SAP_USER: Optional[str] = None
    SAP_PASSWORD: Optional[str] = None
    SAP_ASHOST: Optional[str] = None
    SAP_SYSNR: Optional[str] = None
    
    # Oracle Configuration
    ORACLE_BASE_URL: Optional[str] = None
    ORACLE_API_KEY: Optional[str] = None
    ORACLE_USERNAME: Optional[str] = None
    ORACLE_PASSWORD: Optional[str] = None
    
    # AI Model Configuration
    AI_MODEL_PATH: str = "./models"
    FORECAST_LOOKBACK_DAYS: int = 90
    FORECAST_HORIZON_DAYS: int = 30
    MIN_STOCK_LEVEL: float = 0.1
    MAX_STOCK_LEVEL: float = 0.9
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    
    # Monitoring
    ENABLE_METRICS: bool = True
    METRICS_PORT: int = 9090
    
    # File Upload
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    UPLOAD_DIR: str = "./uploads"
    
    # Cache
    CACHE_TTL: int = 300  # 5 minutes
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings() 