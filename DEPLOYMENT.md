# 🚀 Deployment Guide - Inventory Health AI

This guide provides multiple options to deploy your AI-driven inventory management application.

## 📋 **Quick Start Options**

### **Option 1: Deploy with Docker (Recommended)**

#### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

#### Deploy
```bash
# Clone the repository
git clone https://github.com/LinosLLC/inventory-health-ai.git
cd inventory-health-ai

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

---

### **Option 2: Deploy to Railway (Easiest)**

#### Steps
1. **Sign up** at [Railway.app](https://railway.app)
2. **Connect** your GitHub repository
3. **Deploy** automatically from the main branch
4. **Set environment variables**:
   - `DATABASE_URL`: Your PostgreSQL connection string
   - `SECRET_KEY`: A secure secret key
   - `DEBUG`: False

#### Benefits
- Automatic deployments from GitHub
- Built-in PostgreSQL database
- Free tier available
- HTTPS by default

---

### **Option 3: Deploy to Heroku**

#### Steps
1. **Install Heroku CLI**:
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   ```

2. **Login and create app**:
   ```bash
   heroku login
   heroku create your-inventory-app
   ```

3. **Add PostgreSQL**:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   ```

5. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set DEBUG="False"
   ```

---

### **Option 4: Deploy to AWS**

#### Using AWS EC2
1. **Launch EC2 instance** (Ubuntu 20.04 LTS)
2. **SSH into instance**:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Run deployment script**:
   ```bash
   # Download and run the AWS deployment script
   curl -fsSL https://raw.githubusercontent.com/LinosLLC/inventory-health-ai/main/aws-deploy.sh | bash
   ```

#### Using AWS ECS
1. **Build and push Docker images**:
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account.dkr.ecr.us-east-1.amazonaws.com
   docker build -t inventory-health-ai-backend ./backend
   docker tag inventory-health-ai-backend:latest your-account.dkr.ecr.us-east-1.amazonaws.com/inventory-health-ai-backend:latest
   docker push your-account.dkr.ecr.us-east-1.amazonaws.com/inventory-health-ai-backend:latest
   ```

2. **Create ECS cluster and services** using AWS Console or CLI

---

### **Option 5: Deploy to Google Cloud Platform**

#### Using Google Cloud Run
1. **Install Google Cloud SDK**
2. **Enable required APIs**:
   ```bash
   gcloud services enable run.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   ```

3. **Deploy backend**:
   ```bash
   cd backend
   gcloud run deploy inventory-health-ai-backend \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

4. **Deploy frontend**:
   ```bash
   cd frontend
   gcloud run deploy inventory-health-ai-frontend \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

---

### **Option 6: Deploy to Azure**

#### Using Azure Container Instances
1. **Install Azure CLI**
2. **Login and create resource group**:
   ```bash
   az login
   az group create --name inventory-health-ai --location eastus
   ```

3. **Deploy with Azure Container Instances**:
   ```bash
   az container create \
     --resource-group inventory-health-ai \
     --name inventory-health-ai-backend \
     --image your-registry.azurecr.io/inventory-health-ai-backend:latest \
     --dns-name-label inventory-health-ai-backend \
     --ports 8000
   ```

---

## 🔧 **Environment Configuration**

### **Required Environment Variables**

Create a `.env` file in the backend directory:

```env
# Application
APP_NAME=Inventory Health AI
DEBUG=False
SECRET_KEY=your-super-secret-key-change-in-production

# Database
DATABASE_URL=postgresql://username:password@host:port/database

# Redis
REDIS_URL=redis://localhost:6379/0

# CORS
ALLOWED_ORIGINS=["http://localhost:3000", "https://your-domain.com"]

# AI Configuration
AI_MODEL_PATH=./models
FORECAST_LOOKBACK_DAYS=90
FORECAST_HORIZON_DAYS=30

# Logging
LOG_LEVEL=INFO
```

### **Production Security Checklist**

- [ ] Change default `SECRET_KEY`
- [ ] Set `DEBUG=False`
- [ ] Configure proper `ALLOWED_ORIGINS`
- [ ] Use HTTPS in production
- [ ] Set up proper database credentials
- [ ] Configure backup strategy
- [ ] Set up monitoring and logging
- [ ] Configure rate limiting
- [ ] Set up SSL certificates

---

## 📊 **Database Setup**

### **PostgreSQL Setup**

1. **Install PostgreSQL**:
   ```bash
   # Ubuntu/Debian
   sudo apt-get install postgresql postgresql-contrib
   
   # macOS
   brew install postgresql
   ```

2. **Create database**:
   ```bash
   sudo -u postgres psql
   CREATE DATABASE inventory_health_ai;
   CREATE USER inventory_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE inventory_health_ai TO inventory_user;
   ```

3. **Run migrations**:
   ```bash
   cd backend
   alembic upgrade head
   ```

### **Using Cloud Databases**

#### **AWS RDS**
```bash
aws rds create-db-instance \
  --db-instance-identifier inventory-health-ai \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password your-password \
  --allocated-storage 20
```

#### **Google Cloud SQL**
```bash
gcloud sql instances create inventory-health-ai \
  --database-version=POSTGRES_14 \
  --tier=db-f1-micro \
  --region=us-central1
```

---

## 🔍 **Monitoring and Logging**

### **Health Checks**

The application includes health check endpoints:
- Backend: `GET /health`
- Database connectivity
- Redis connectivity

### **Logging**

Configure structured logging:
```python
# In your deployment environment
export LOG_LEVEL=INFO
export LOG_FORMAT=json
```

### **Metrics**

The application exposes Prometheus metrics at `/metrics`:
- Request counts
- Response times
- Error rates
- Custom business metrics

---

## 🚀 **CI/CD Pipeline**

### **GitHub Actions**

The repository includes a GitHub Actions workflow that:
1. **Tests** the application
2. **Builds** Docker images
3. **Deploys** to your chosen platform

### **Configure Secrets**

In your GitHub repository settings, add these secrets:
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password
- `DEPLOY_KEY`: SSH key for deployment
- `DATABASE_URL`: Production database URL

---

## 🔒 **Security Best Practices**

### **Network Security**
- Use HTTPS in production
- Configure proper firewall rules
- Use VPC for cloud deployments
- Implement API rate limiting

### **Application Security**
- Regular security updates
- Input validation
- SQL injection prevention
- XSS protection
- CSRF protection

### **Data Security**
- Encrypt data at rest
- Encrypt data in transit
- Regular backups
- Access control and audit logs

---

## 📈 **Scaling Considerations**

### **Horizontal Scaling**
- Use load balancers
- Implement database connection pooling
- Use Redis for caching
- Consider microservices architecture

### **Vertical Scaling**
- Monitor resource usage
- Scale up when needed
- Use auto-scaling groups

### **Database Scaling**
- Read replicas for read-heavy workloads
- Database sharding for large datasets
- Connection pooling
- Query optimization

---

## 🆘 **Troubleshooting**

### **Common Issues**

1. **Database Connection Errors**
   - Check database URL
   - Verify network connectivity
   - Check firewall rules

2. **Port Conflicts**
   - Change default ports in docker-compose.yml
   - Check for running services

3. **Memory Issues**
   - Increase container memory limits
   - Optimize application code
   - Use connection pooling

### **Logs and Debugging**

```bash
# View application logs
docker-compose logs -f backend

# View database logs
docker-compose logs -f postgres

# Check application health
curl http://localhost:8000/health
```

---

## 📞 **Support**

For deployment issues:
1. Check the [GitHub Issues](https://github.com/LinosLLC/inventory-health-ai/issues)
2. Review the [API Documentation](docs/API_DOCUMENTATION.md)
3. Check the application logs
4. Verify environment configuration

---

## 🎯 **Next Steps**

After successful deployment:
1. **Configure ERP integrations** (SAP, Oracle)
2. **Set up monitoring** and alerting
3. **Train AI models** with your data
4. **Customize dashboards** for your business
5. **Set up user management** and permissions
6. **Configure backup** and disaster recovery
7. **Plan for scaling** as your business grows 