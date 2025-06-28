"""
Inventory management endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.inventory import InventoryLevel, InventoryTransaction, InventoryAlert, StockType
from app.schemas.inventory import (
    InventoryLevelResponse,
    InventoryLevelList,
    InventoryTransactionResponse,
    InventoryAlertResponse,
    InventoryKPIs
)

router = APIRouter()

@router.get("/levels", response_model=List[InventoryLevelResponse])
async def get_inventory_levels(
    plant_id: Optional[str] = Query(None, description="Filter by plant ID"),
    material_id: Optional[str] = Query(None, description="Filter by material ID"),
    stock_type: Optional[StockType] = Query(None, description="Filter by stock type"),
    erp_system: Optional[str] = Query(None, description="Filter by ERP system"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get current inventory levels with optional filtering"""
    
    query = db.query(InventoryLevel)
    
    if plant_id:
        query = query.filter(InventoryLevel.plant_id == plant_id)
    if material_id:
        query = query.filter(InventoryLevel.material_id == material_id)
    if stock_type:
        query = query.filter(InventoryLevel.stock_type == stock_type)
    if erp_system:
        query = query.filter(InventoryLevel.erp_system == erp_system)
    
    inventory_levels = query.all()
    return inventory_levels

@router.get("/levels/{plant_id}", response_model=List[InventoryLevelResponse])
async def get_inventory_by_plant(
    plant_id: str,
    stock_type: Optional[StockType] = Query(None, description="Filter by stock type"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get inventory levels for a specific plant"""
    
    query = db.query(InventoryLevel).filter(InventoryLevel.plant_id == plant_id)
    
    if stock_type:
        query = query.filter(InventoryLevel.stock_type == stock_type)
    
    inventory_levels = query.all()
    return inventory_levels

@router.get("/transactions", response_model=List[InventoryTransactionResponse])
async def get_inventory_transactions(
    plant_id: Optional[str] = Query(None, description="Filter by plant ID"),
    material_id: Optional[str] = Query(None, description="Filter by material ID"),
    transaction_type: Optional[str] = Query(None, description="Filter by transaction type"),
    start_date: Optional[datetime] = Query(None, description="Start date for filtering"),
    end_date: Optional[datetime] = Query(None, description="End date for filtering"),
    limit: int = Query(100, description="Number of records to return"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get inventory transaction history"""
    
    query = db.query(InventoryTransaction)
    
    if plant_id:
        query = query.filter(InventoryTransaction.plant_id == plant_id)
    if material_id:
        query = query.filter(InventoryTransaction.material_id == material_id)
    if transaction_type:
        query = query.filter(InventoryTransaction.transaction_type == transaction_type)
    if start_date:
        query = query.filter(InventoryTransaction.transaction_date >= start_date)
    if end_date:
        query = query.filter(InventoryTransaction.transaction_date <= end_date)
    
    transactions = query.order_by(InventoryTransaction.transaction_date.desc()).limit(limit).all()
    return transactions

@router.get("/alerts", response_model=List[InventoryAlertResponse])
async def get_inventory_alerts(
    plant_id: Optional[str] = Query(None, description="Filter by plant ID"),
    material_id: Optional[str] = Query(None, description="Filter by material ID"),
    alert_type: Optional[str] = Query(None, description="Filter by alert type"),
    severity: Optional[str] = Query(None, description="Filter by severity"),
    is_active: Optional[bool] = Query(True, description="Filter by active status"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get active inventory alerts"""
    
    query = db.query(InventoryAlert)
    
    if plant_id:
        query = query.filter(InventoryAlert.plant_id == plant_id)
    if material_id:
        query = query.filter(InventoryAlert.material_id == material_id)
    if alert_type:
        query = query.filter(InventoryAlert.alert_type == alert_type)
    if severity:
        query = query.filter(InventoryAlert.severity == severity)
    if is_active is not None:
        query = query.filter(InventoryAlert.is_active == is_active)
    
    alerts = query.order_by(InventoryAlert.created_at.desc()).all()
    return alerts

@router.get("/kpis", response_model=InventoryKPIs)
async def get_inventory_kpis(
    plant_id: Optional[str] = Query(None, description="Filter by plant ID"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get inventory KPIs for executive dashboard"""
    
    query = db.query(InventoryLevel)
    if plant_id:
        query = query.filter(InventoryLevel.plant_id == plant_id)
    
    inventory_levels = query.all()
    
    # Calculate KPIs
    total_materials = len(inventory_levels)
    total_value = sum(level.total_quantity for level in inventory_levels)
    low_stock_count = len([level for level in inventory_levels if level.available_quantity < 10])
    overstock_count = len([level for level in inventory_levels if level.total_quantity > 1000])
    
    # Calculate stock-out risk
    stock_out_risk = len([level for level in inventory_levels if level.available_quantity == 0])
    
    return InventoryKPIs(
        total_materials=total_materials,
        total_value=total_value,
        low_stock_count=low_stock_count,
        overstock_count=overstock_count,
        stock_out_risk=stock_out_risk,
        last_updated=datetime.now()
    )

@router.get("/summary")
async def get_inventory_summary(
    plant_id: Optional[str] = Query(None, description="Filter by plant ID"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get inventory summary for executive dashboard"""
    
    query = db.query(InventoryLevel)
    if plant_id:
        query = query.filter(InventoryLevel.plant_id == plant_id)
    
    inventory_levels = query.all()
    
    # Group by stock type
    summary_by_type = {}
    for level in inventory_levels:
        stock_type = level.stock_type.value
        if stock_type not in summary_by_type:
            summary_by_type[stock_type] = {
                "count": 0,
                "total_quantity": 0,
                "total_value": 0
            }
        
        summary_by_type[stock_type]["count"] += 1
        summary_by_type[stock_type]["total_quantity"] += level.total_quantity
        summary_by_type[stock_type]["total_value"] += level.total_quantity  # Simplified value calculation
    
    return {
        "summary_by_type": summary_by_type,
        "total_materials": len(inventory_levels),
        "last_updated": datetime.now()
    } 