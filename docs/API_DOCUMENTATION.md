# Inventory Health AI - API Documentation

## Overview

The Inventory Health AI API provides comprehensive endpoints for managing inventory across multiple ERP systems, including SAP and Oracle. The API is built with FastAPI and provides real-time inventory data, AI-powered analytics, and executive insights.

## Base URL

- Development: `http://localhost:8000`
- Production: `https://your-domain.com`

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

### Login

**POST** `/api/v1/auth/login`

Request body:
```json
{
  "username": "admin",
  "password": "admin123"
}
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "user": {
    "username": "admin",
    "role": "executive",
    "full_name": "Executive User"
  }
}
```

## Inventory Management

### Get Inventory Levels

**GET** `/api/v1/inventory/levels`

Query Parameters:
- `plant_id` (optional): Filter by plant ID
- `material_id` (optional): Filter by material ID
- `stock_type` (optional): Filter by stock type (raw_material, wip, finished_good, spare_part, consumable)
- `erp_system` (optional): Filter by ERP system (SAP, Oracle, etc.)

Response:
```json
[
  {
    "id": 1,
    "material_id": "MAT001",
    "plant_id": "PLANT001",
    "storage_location": "WH-A1",
    "stock_type": "raw_material",
    "available_quantity": 150.0,
    "reserved_quantity": 25.0,
    "total_quantity": 175.0,
    "unit_of_measure": "PCS",
    "erp_system": "SAP",
    "erp_material_code": "10000001",
    "erp_plant_code": "1000",
    "last_updated": "2024-01-15T10:30:00Z",
    "created_at": "2024-01-01T00:00:00Z",
    "batch_number": "BATCH001",
    "shelf_life_expiry": "2024-12-31T00:00:00Z",
    "quality_status": "GOOD"
  }
]
```

### Get Inventory by Plant

**GET** `/api/v1/inventory/levels/{plant_id}`

Response: Same as above, filtered by plant.

### Get Inventory Transactions

**GET** `/api/v1/inventory/transactions`

Query Parameters:
- `plant_id` (optional): Filter by plant ID
- `material_id` (optional): Filter by material ID
- `transaction_type` (optional): Filter by transaction type (IN, OUT, TRANSFER, ADJUSTMENT)
- `start_date` (optional): Start date for filtering
- `end_date` (optional): End date for filtering
- `limit` (optional): Number of records to return (default: 100)

Response:
```json
[
  {
    "id": 1,
    "material_id": "MAT001",
    "plant_id": "PLANT001",
    "transaction_type": "IN",
    "quantity": 50.0,
    "unit_of_measure": "PCS",
    "reference_document": "PO",
    "reference_number": "PO-2024-001",
    "erp_system": "SAP",
    "erp_transaction_id": "TXN001",
    "transaction_date": "2024-01-15T10:30:00Z",
    "created_at": "2024-01-15T10:30:00Z",
    "reason_code": "PURCHASE",
    "notes": "Regular stock replenishment"
  }
]
```

### Get Inventory Alerts

**GET** `/api/v1/inventory/alerts`

Query Parameters:
- `plant_id` (optional): Filter by plant ID
- `material_id` (optional): Filter by material ID
- `alert_type` (optional): Filter by alert type
- `severity` (optional): Filter by severity (LOW, MEDIUM, HIGH, CRITICAL)
- `is_active` (optional): Filter by active status (default: true)

Response:
```json
[
  {
    "id": 1,
    "material_id": "MAT001",
    "plant_id": "PLANT001",
    "alert_type": "LOW_STOCK",
    "severity": "medium",
    "message": "Steel Sheet 2mm stock level is below reorder point",
    "is_active": true,
    "acknowledged_by": null,
    "acknowledged_at": null,
    "created_at": "2024-01-15T10:30:00Z",
    "resolved_at": null
  }
]
```

### Get Inventory KPIs

**GET** `/api/v1/inventory/kpis`

Query Parameters:
- `plant_id` (optional): Filter by plant ID

Response:
```json
{
  "total_materials": 1250,
  "total_value": 1250000.0,
  "low_stock_count": 23,
  "overstock_count": 45,
  "stock_out_risk": 7,
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Get Inventory Summary

**GET** `/api/v1/inventory/summary`

Query Parameters:
- `plant_id` (optional): Filter by plant ID

Response:
```json
{
  "summary_by_type": {
    "raw_material": {
      "count": 450,
      "total_quantity": 12500,
      "total_value": 450000
    },
    "finished_good": {
      "count": 300,
      "total_quantity": 8500,
      "total_value": 600000
    }
  },
  "total_materials": 1250,
  "last_updated": "2024-01-15T10:30:00Z"
}
```

## Plant Management

### Get All Plants

**GET** `/api/v1/plants`

Query Parameters:
- `country` (optional): Filter by country
- `plant_type` (optional): Filter by plant type
- `is_active` (optional): Filter by active status (default: true)

Response:
```json
[
  {
    "id": 1,
    "plant_code": "PLANT001",
    "plant_name": "North Manufacturing",
    "plant_type": "Manufacturing",
    "country": "USA",
    "region": "Northeast",
    "city": "Boston",
    "address": "123 Manufacturing St, Boston, MA",
    "contact_person": "John Smith",
    "contact_email": "john.smith@company.com",
    "contact_phone": "+1-555-0123",
    "erp_system": "SAP",
    "erp_plant_code": "1000",
    "is_active": true,
    "capacity_utilization": 0.85,
    "production_capacity": 10000,
    "capacity_unit": "PCS",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
]
```

### Get Plant Details

**GET** `/api/v1/plants/{plant_id}`

Response: Single plant object as above.

### Get Storage Locations

**GET** `/api/v1/plants/{plant_id}/storage-locations`

Response:
```json
[
  {
    "id": 1,
    "plant_id": 1,
    "location_code": "WH-A1",
    "location_name": "Warehouse A - Section 1",
    "location_type": "Warehouse",
    "storage_capacity": 1000,
    "capacity_unit": "PCS",
    "current_utilization": 0.75,
    "erp_system": "SAP",
    "erp_location_code": "A001",
    "is_active": true,
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
]
```

## Material Management

### Get All Materials

**GET** `/api/v1/materials`

Query Parameters:
- `category` (optional): Filter by category
- `material_group` (optional): Filter by material group
- `is_active` (optional): Filter by active status (default: true)
- `erp_system` (optional): Filter by ERP system

Response:
```json
[
  {
    "id": 1,
    "material_id": "MAT001",
    "material_name": "Steel Sheet 2mm",
    "material_description": "High-grade steel sheet 2mm thickness",
    "category": "raw_material",
    "material_group": "Metals",
    "material_type": "Sheet Metal",
    "base_unit": "PCS",
    "weight_unit": "KG",
    "weight_per_unit": 2.5,
    "volume_unit": "M3",
    "volume_per_unit": 0.001,
    "length": 1000,
    "width": 500,
    "height": 2,
    "dimension_unit": "MM",
    "standard_cost": 15.50,
    "currency": "USD",
    "erp_system": "SAP",
    "erp_material_code": "10000001",
    "erp_material_group": "METALS",
    "is_active": true,
    "is_obsolete": false,
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
]
```

### Get Material Details

**GET** `/api/v1/materials/{material_id}`

Response: Single material object as above.

### Get Material Categories

**GET** `/api/v1/materials/categories`

Response:
```json
{
  "categories": [
    "raw_material",
    "semi_finished",
    "finished_good",
    "spare_part",
    "consumable",
    "packaging"
  ]
}
```

## AI and Analytics

### Get Demand Forecast

**GET** `/api/v1/ai/forecast`

Query Parameters:
- `material_id` (optional): Material ID for forecasting
- `plant_id` (optional): Plant ID for forecasting
- `horizon_days` (optional): Forecast horizon in days (default: 30)

Response:
```json
{
  "material_id": "MAT001",
  "plant_id": "PLANT001",
  "forecast_horizon_days": 30,
  "forecast_data": [
    {
      "date": "2024-01-16",
      "predicted_demand": 105.2,
      "confidence_lower": 94.7,
      "confidence_upper": 115.7
    }
  ],
  "model_accuracy": 0.87,
  "confidence_level": 0.95,
  "last_updated": "2024-01-15T10:30:00Z",
  "model_version": "v1.0"
}
```

### Get Inventory Optimization

**GET** `/api/v1/ai/optimization`

Query Parameters:
- `plant_id` (optional): Plant ID for optimization

Response:
```json
{
  "plant_id": "PLANT001",
  "optimization_score": 0.78,
  "potential_savings": 125000,
  "recommendations": [
    {
      "type": "reorder_point_optimization",
      "materials_affected": 23,
      "potential_impact": "Reduce stock-outs by 15%",
      "priority": "high"
    }
  ],
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Get Anomaly Detection

**GET** `/api/v1/ai/anomaly-detection`

Query Parameters:
- `plant_id` (optional): Plant ID for anomaly detection

Response:
```json
{
  "anomalies": [],
  "total_detected": 0,
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Get AI Insights

**GET** `/api/v1/ai/insights`

Query Parameters:
- `plant_id` (optional): Plant ID for insights

Response:
```json
{
  "key_insights": [
    "Inventory turnover rate is 15% below industry average",
    "Stock-out risk is high for 23 materials"
  ],
  "recommendations": [
    "Implement dynamic reorder points for high-demand items",
    "Review safety stock levels for critical materials"
  ],
  "last_updated": "2024-01-15T10:30:00Z"
}
```

## Analytics and Reporting

### Get Executive KPIs

**GET** `/api/v1/analytics/kpis`

Query Parameters:
- `plant_id` (optional): Plant ID for KPIs

Response:
```json
{
  "inventory_turnover": 4.2,
  "days_of_inventory": 87,
  "stock_out_rate": 0.023,
  "overstock_rate": 0.156,
  "inventory_accuracy": 0.987,
  "cost_of_inventory": 1250000.00,
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Get Inventory Trends

**GET** `/api/v1/analytics/trends`

Query Parameters:
- `plant_id` (optional): Plant ID for trends
- `days` (optional): Number of days for trend analysis (default: 30)

Response:
```json
{
  "total_inventory": [
    {
      "date": "2024-01-01",
      "value": 1200000
    }
  ],
  "stock_outs": [
    {
      "date": "2024-01-01",
      "count": 5
    }
  ],
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### Get Plant Comparison

**GET** `/api/v1/analytics/comparison`

Response:
```json
{
  "plants": [
    {
      "plant_id": "PLANT001",
      "plant_name": "North Manufacturing",
      "inventory_value": 450000,
      "turnover_rate": 4.5,
      "stock_out_rate": 0.018
    }
  ],
  "last_updated": "2024-01-15T10:30:00Z"
}
```

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden
```json
{
  "detail": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Rate Limiting

The API implements rate limiting to ensure fair usage:
- 100 requests per minute per authenticated user
- 1000 requests per hour per authenticated user

Rate limit headers are included in responses:
- `X-RateLimit-Limit`: Request limit per window
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Time when the rate limit resets

## Pagination

For endpoints that return lists, pagination is supported:

Query Parameters:
- `page` (optional): Page number (default: 1)
- `page_size` (optional): Items per page (default: 100, max: 1000)

Response headers:
- `X-Total-Count`: Total number of items
- `X-Page`: Current page number
- `X-Page-Size`: Items per page
- `X-Total-Pages`: Total number of pages

## WebSocket Support

Real-time updates are available via WebSocket connections:

**WebSocket URL**: `ws://localhost:8000/ws`

Events:
- `inventory_update`: Real-time inventory level changes
- `alert_created`: New inventory alerts
- `kpi_update`: KPI value updates

Example WebSocket message:
```json
{
  "event": "inventory_update",
  "data": {
    "material_id": "MAT001",
    "plant_id": "PLANT001",
    "new_quantity": 150.0,
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
``` 