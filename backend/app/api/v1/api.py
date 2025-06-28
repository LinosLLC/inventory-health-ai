"""
Main API router for v1 endpoints
"""

from fastapi import APIRouter

from app.api.v1.endpoints import inventory, plants, materials, ai, analytics, auth

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
api_router.include_router(plants.router, prefix="/plants", tags=["plants"])
api_router.include_router(materials.router, prefix="/materials", tags=["materials"])
api_router.include_router(ai.router, prefix="/ai", tags=["artificial intelligence"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"]) 