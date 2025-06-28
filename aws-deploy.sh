#!/bin/bash

# AWS Deployment Script for Inventory Health AI

echo "🚀 Deploying Inventory Health AI to AWS..."

# Install Docker if not present
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    sudo usermod -aG docker $USER
fi

# Install Docker Compose if not present
if ! command -v docker-compose &> /dev/null; then
    echo "Installing Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

# Clone repository
if [ ! -d "inventory-health-ai" ]; then
    git clone https://github.com/LinosLLC/inventory-health-ai.git
    cd inventory-health-ai
else
    cd inventory-health-ai
    git pull origin main
fi

# Set environment variables
export DATABASE_URL="postgresql://postgres:password@localhost:5432/inventory_health_ai"
export SECRET_KEY="your-production-secret-key"
export DEBUG="False"

# Start services
echo "Starting services with Docker Compose..."
docker-compose up -d

echo "✅ Deployment complete!"
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs" 