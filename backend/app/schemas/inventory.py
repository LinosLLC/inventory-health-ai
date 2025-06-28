"""
Pydantic schemas for inventory management
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

from app.models.inventory import StockType

class InventoryLevelResponse(BaseModel):
    """Response schema for inventory levels"""
    id: int
    material_id: str
    plant_id: str
    storage_location: Optional[str] = None
    stock_type: StockType
    
    # Quantities
    available_quantity: float
    reserved_quantity: float
    total_quantity: float
    
    # Units
    unit_of_measure: str
    
    # ERP System Info
    erp_system: str
    erp_material_code: Optional[str] = None
    erp_plant_code: Optional[str] = None
    
    # Timestamps
    last_updated: datetime
    created_at: datetime
    
    # Additional metadata
    batch_number: Optional[str] = None
    shelf_life_expiry: Optional[datetime] = None
    quality_status: Optional[str] = None
    
    class Config:
        from_attributes = True

class InventoryLevelList(BaseModel):
    """Response schema for inventory level list"""
    items: List[InventoryLevelResponse]
    total_count: int
    page: int
    page_size: int

class InventoryTransactionResponse(BaseModel):
    """Response schema for inventory transactions"""
    id: int
    material_id: str
    plant_id: str
    
    # Transaction details
    transaction_type: str
    quantity: float
    unit_of_measure: str
    
    # Reference information
    reference_document: Optional[str] = None
    reference_number: Optional[str] = None
    
    # ERP System Info
    erp_system: str
    erp_transaction_id: Optional[str] = None
    
    # Timestamps
    transaction_date: datetime
    created_at: datetime
    
    # Additional metadata
    reason_code: Optional[str] = None
    notes: Optional[str] = None
    
    class Config:
        from_attributes = True

class InventoryAlertResponse(BaseModel):
    """Response schema for inventory alerts"""
    id: int
    material_id: str
    plant_id: str
    
    # Alert details
    alert_type: str
    severity: str
    message: str
    
    # Alert status
    is_active: bool
    acknowledged_by: Optional[str] = None
    acknowledged_at: Optional[datetime] = None
    
    # Timestamps
    created_at: datetime
    resolved_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class InventoryKPIs(BaseModel):
    """Response schema for inventory KPIs"""
    total_materials: int
    total_value: float
    low_stock_count: int
    overstock_count: int
    stock_out_risk: int
    last_updated: datetime

class InventorySummary(BaseModel):
    """Response schema for inventory summary"""
    summary_by_type: dict
    total_materials: int
    last_updated: datetime

class InventoryFilter(BaseModel):
    """Request schema for inventory filtering"""
    plant_id: Optional[str] = None
    material_id: Optional[str] = None
    stock_type: Optional[StockType] = None
    erp_system: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None 