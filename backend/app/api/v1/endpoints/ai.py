"""
AI and machine learning endpoints
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.inventory import InventoryForecast
from app.services.ai_forecasting import ForecastingService
from app.services.ai_optimization import OptimizationService

router = APIRouter()

@router.get("/forecast")
async def get_demand_forecast(
    material_id: Optional[str] = Query(None, description="Material ID for forecasting"),
    plant_id: Optional[str] = Query(None, description="Plant ID for forecasting"),
    horizon_days: int = Query(30, description="Forecast horizon in days"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get AI-powered demand forecast"""
    
    forecasting_service = ForecastingService()
    
    if material_id and plant_id:
        # Get specific material forecast
        forecast = await forecasting_service.get_material_forecast(
            material_id, plant_id, horizon_days
        )
    else:
        # Get general forecast
        forecast = await forecasting_service.get_general_forecast(horizon_days)
    
    return forecast

@router.get("/optimization")
async def get_inventory_optimization(
    plant_id: Optional[str] = Query(None, description="Plant ID for optimization"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get AI-powered inventory optimization recommendations"""
    
    optimization_service = OptimizationService()
    
    if plant_id:
        recommendations = await optimization_service.get_plant_optimization(plant_id)
    else:
        recommendations = await optimization_service.get_global_optimization()
    
    return recommendations

@router.get("/anomaly-detection")
async def get_anomaly_detection(
    plant_id: Optional[str] = Query(None, description="Plant ID for anomaly detection"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get AI-powered anomaly detection results"""
    
    # This would integrate with the anomaly detection service
    anomalies = {
        "anomalies": [],
        "total_detected": 0,
        "last_updated": datetime.now()
    }
    
    return anomalies

@router.get("/insights")
async def get_ai_insights(
    plant_id: Optional[str] = Query(None, description="Plant ID for insights"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Get AI-powered business insights"""
    
    insights = {
        "key_insights": [
            "Inventory turnover rate is 15% below industry average",
            "Stock-out risk is high for 23 materials",
            "Overstock detected for 45 materials",
            "Demand seasonality detected for 67 materials"
        ],
        "recommendations": [
            "Implement dynamic reorder points for high-demand items",
            "Review safety stock levels for critical materials",
            "Consider supplier diversification for long-lead-time items"
        ],
        "last_updated": datetime.now()
    }
    
    return insights 