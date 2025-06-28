# Inventory Health AI

An AI-driven inventory management application designed for executive leadership to gain comprehensive insights across multiple ERP systems including SAP and other enterprise systems.

## 🚀 Features

- **Multi-ERP Integration**: Seamlessly connect to SAP, Oracle, and other ERP systems
- **AI-Powered Analytics**: Machine learning insights for inventory optimization
- **Executive Dashboard**: High-level KPIs and visualizations for leadership
- **Plant-Level Views**: Granular inventory tracking across manufacturing facilities
- **Material & SKU Management**: Comprehensive item-level tracking
- **Stock Type Analysis**: Raw materials, WIP, finished goods, and spare parts
- **Predictive Analytics**: Demand forecasting and stock-out prevention
- **Real-time Monitoring**: Live inventory levels and alerts

## 🏗️ Architecture

```
inventory-health-ai/
├── backend/                 # FastAPI backend with AI services
├── frontend/               # React dashboard for executives
├── ai_services/           # Machine learning models and analytics
├── database/              # Database schemas and migrations
├── docs/                  # Documentation and API specs
└── deployment/            # Docker and deployment configs
```

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.11+
- **Frontend**: React 18, TypeScript, Material-UI
- **Database**: PostgreSQL with TimescaleDB for time-series data
- **AI/ML**: scikit-learn, TensorFlow, pandas
- **Integration**: SAP RFC, REST APIs, ETL pipelines
- **Deployment**: Docker, Kubernetes, GitHub Actions

## 📊 Key Capabilities

### Executive Dashboard
- Real-time inventory KPIs
- Cross-plant comparison views
- Stock-out risk indicators
- Cost optimization insights
- Demand forecasting trends

### AI-Powered Features
- **Inventory Optimization**: ML-based reorder point calculations
- **Demand Forecasting**: Time-series analysis for accurate predictions
- **Anomaly Detection**: Identify unusual inventory patterns
- **Cost Analysis**: AI-driven cost optimization recommendations
- **Risk Assessment**: Predictive stock-out and overstock alerts

### Multi-ERP Support
- **SAP Integration**: RFC connections, BAPI calls
- **Oracle ERP**: REST API integration
- **Other ERPs**: Extensible connector framework
- **Data Harmonization**: Unified data model across systems

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Docker & Docker Compose

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-org/inventory-health-ai.git
cd inventory-health-ai
```

2. **Start with Docker**
```bash
docker-compose up -d
```

3. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Manual Setup

1. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

2. **Frontend Setup**
```bash
cd frontend
npm install
npm start
```

3. **Database Setup**
```bash
cd database
psql -U postgres -d inventory_health_ai -f schema.sql
```

## 📈 Usage

### Executive Dashboard
1. Navigate to the dashboard at http://localhost:3000
2. Select your company and plant locations
3. View real-time inventory KPIs and trends
4. Explore AI-powered insights and recommendations

### API Integration
```python
import requests

# Get inventory levels
response = requests.get("http://localhost:8000/api/v1/inventory/levels")
inventory_data = response.json()

# Get AI predictions
response = requests.get("http://localhost:8000/api/v1/ai/forecast")
forecast_data = response.json()
```

## 🔧 Configuration

### ERP Connections
Configure your ERP systems in `config/erp_config.yaml`:

```yaml
sap:
  host: your-sap-host
  client: 100
  user: your-username
  password: your-password

oracle:
  base_url: https://your-oracle-instance.com
  api_key: your-api-key
```

### AI Model Configuration
Adjust AI parameters in `config/ai_config.yaml`:

```yaml
forecasting:
  model_type: "lstm"
  lookback_period: 90
  prediction_horizon: 30

optimization:
  min_stock_level: 0.1
  max_stock_level: 0.9
  reorder_frequency: 7
```

## 📊 API Documentation

Comprehensive API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Key Endpoints

- `GET /api/v1/inventory/levels` - Current inventory levels
- `GET /api/v1/inventory/plants` - Plant information
- `GET /api/v1/inventory/materials` - Material catalog
- `GET /api/v1/ai/forecast` - Demand forecasts
- `GET /api/v1/ai/optimization` - Optimization recommendations
- `GET /api/v1/analytics/kpis` - Executive KPIs

## 🤖 AI Features

### Demand Forecasting
- LSTM neural networks for time-series prediction
- Seasonal decomposition and trend analysis
- Confidence intervals for forecast accuracy

### Inventory Optimization
- Multi-objective optimization algorithms
- Cost-benefit analysis for stock levels
- Dynamic reorder point calculations

### Anomaly Detection
- Statistical process control (SPC) methods
- Machine learning-based outlier detection
- Real-time alert generation

## 🔒 Security

- JWT-based authentication
- Role-based access control (RBAC)
- API rate limiting
- Data encryption at rest and in transit
- Audit logging for compliance

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- Documentation: [docs/](docs/)
- Issues: [GitHub Issues](https://github.com/your-org/inventory-health-ai/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/inventory-health-ai/discussions)

## 🗺️ Roadmap

- [ ] Advanced ML models for demand forecasting
- [ ] Mobile application for executives
- [ ] Integration with more ERP systems
- [ ] Real-time streaming analytics
- [ ] Advanced reporting and BI features
- [ ] Machine learning model explainability
- [ ] Integration with supply chain systems

---

Built with ❤️ for executive leadership to make data-driven inventory decisions. 