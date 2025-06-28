"""
Material management endpoints
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.materials import Material, MaterialCategory

router = APIRouter()

@router.get("/")
async def get_materials(
    category: Optional[MaterialCategory] = Query(None, description="Filter by category"),
    material_group: Optional[str] = Query(None, description="Filter by material group"),
    is_active: Optional[bool] = Query(True, description="Filter by active status"),
    erp_system: Optional[str] = Query(None, description="Filter by ERP system"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get all materials with optional filtering"""
    
    query = db.query(Material)
    
    if category:
        query = query.filter(Material.category == category)
    if material_group:
        query = query.filter(Material.material_group == material_group)
    if is_active is not None:
        query = query.filter(Material.is_active == is_active)
    if erp_system:
        query = query.filter(Material.erp_system == erp_system)
    
    materials = query.all()
    return materials

@router.get("/{material_id}")
async def get_material(
    material_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get specific material details"""
    
    material = db.query(Material).filter(Material.material_id == material_id).first()
    if not material:
        return {"error": "Material not found"}
    
    return material

@router.get("/categories")
async def get_material_categories(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get all material categories"""
    
    categories = [category.value for category in MaterialCategory]
    return {"categories": categories} 