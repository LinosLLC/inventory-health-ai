"""
Analytics and reporting endpoints
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/kpis")
async def get_executive_kpis(
    plant_id: Optional[str] = Query(None, description="Plant ID for KPIs"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get executive-level KPIs"""
    
    kpis = {
        "inventory_turnover": 4.2,
        "days_of_inventory": 87,
        "stock_out_rate": 0.023,
        "overstock_rate": 0.156,
        "inventory_accuracy": 0.987,
        "cost_of_inventory": 1250000.00,
        "last_updated": datetime.now()
    }
    
    return kpis

@router.get("/trends")
async def get_inventory_trends(
    plant_id: Optional[str] = Query(None, description="Plant ID for trends"),
    days: int = Query(30, description="Number of days for trend analysis"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get inventory trends over time"""
    
    trends = {
        "total_inventory": [
            {"date": "2024-01-01", "value": 1200000},
            {"date": "2024-01-15", "value": 1180000},
            {"date": "2024-02-01", "value": 1250000}
        ],
        "stock_outs": [
            {"date": "2024-01-01", "count": 5},
            {"date": "2024-01-15", "count": 3},
            {"date": "2024-02-01", "count": 7}
        ],
        "last_updated": datetime.now()
    }
    
    return trends

@router.get("/comparison")
async def get_plant_comparison(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get comparison data across plants"""
    
    comparison = {
        "plants": [
            {
                "plant_id": "PLANT001",
                "plant_name": "North Manufacturing",
                "inventory_value": 450000,
                "turnover_rate": 4.5,
                "stock_out_rate": 0.018
            },
            {
                "plant_id": "PLANT002", 
                "plant_name": "South Distribution",
                "inventory_value": 320000,
                "turnover_rate": 5.2,
                "stock_out_rate": 0.025
            }
        ],
        "last_updated": datetime.now()
    }
    
    return comparison 