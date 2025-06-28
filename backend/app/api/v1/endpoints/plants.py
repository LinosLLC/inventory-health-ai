"""
Plant management endpoints
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.plants import Plant, StorageLocation

router = APIRouter()

@router.get("/")
async def get_plants(
    country: Optional[str] = Query(None, description="Filter by country"),
    plant_type: Optional[str] = Query(None, description="Filter by plant type"),
    is_active: Optional[bool] = Query(True, description="Filter by active status"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get all plants with optional filtering"""
    
    query = db.query(Plant)
    
    if country:
        query = query.filter(Plant.country == country)
    if plant_type:
        query = query.filter(Plant.plant_type == plant_type)
    if is_active is not None:
        query = query.filter(Plant.is_active == is_active)
    
    plants = query.all()
    return plants

@router.get("/{plant_id}")
async def get_plant(
    plant_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get specific plant details"""
    
    plant = db.query(Plant).filter(Plant.plant_code == plant_id).first()
    if not plant:
        return {"error": "Plant not found"}
    
    return plant

@router.get("/{plant_id}/storage-locations")
async def get_storage_locations(
    plant_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get storage locations for a specific plant"""
    
    locations = db.query(StorageLocation).filter(StorageLocation.plant_id == plant_id).all()
    return locations 