# Railway Deployment Guide

## Option 1: Native Python Deployment (Recommended)

This approach avoids Docker build issues by using Railway's native Python support.

### Step 1: Configure Railway for Native Python
1. In your Railway project dashboard, go to Settings
2. Set the following environment variables:
   ```
   PYTHON_VERSION=3.11
   ```

### Step 2: Deploy Using Nixpacks
1. Railway will automatically detect the Python project
2. It will use the `requirements-railway.txt` file for dependencies
3. The `railway.json` configuration will handle the deployment

### Step 3: Set Environment Variables
Add these environment variables in Railway dashboard:
```
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key_here
ENVIRONMENT=production
```

## Option 2: Optimized Docker Deployment

If you prefer Docker deployment, use the optimized Dockerfile.

### Step 1: Update Railway Configuration
1. In Railway dashboard, go to Settings
2. Set the build command to:
   ```
   docker build -f backend/Dockerfile -t inventory-health-ai ./backend
   ```

### Step 2: Set Build Context
Make sure Railway is building from the root directory, not the backend directory.

## Option 3: Manual Deployment Steps

### Step 1: Connect Repository
1. Go to Railway dashboard
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository: `LinosLLC/inventory-health-ai`

### Step 2: Configure Build Settings
1. Set Root Directory to: `backend`
2. Set Build Command to: `pip install -r requirements-railway.txt`
3. Set Start Command to: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 3: Add PostgreSQL Database
1. In Railway dashboard, click "New" → "Database" → "PostgreSQL"
2. Copy the connection string
3. Add as environment variable: `DATABASE_URL`

### Step 4: Set Environment Variables
```
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key_here
ENVIRONMENT=production
CORS_ORIGINS=https://your-frontend-domain.com
```

## Troubleshooting

### Build Timeout Issues
- Use `requirements-railway.txt` instead of `requirements.txt`
- The simplified requirements file excludes heavy packages like TensorFlow
- Consider using Railway's native Python support instead of Docker

### Database Connection Issues
- Ensure PostgreSQL is provisioned in Railway
- Check that `DATABASE_URL` is correctly set
- Verify the connection string format

### Port Issues
- Railway automatically sets the `$PORT` environment variable
- Make sure your app listens on `0.0.0.0:$PORT`

### Health Check Failures
- The app includes a `/health` endpoint
- Railway will use this for health checks
- Ensure the endpoint returns a 200 status

## Monitoring Deployment

1. Check Railway logs for build progress
2. Monitor the deployment status in the dashboard
3. Test the health endpoint: `https://your-app.railway.app/health`
4. Access API docs: `https://your-app.railway.app/docs`

## Post-Deployment

1. Test all API endpoints
2. Verify database connections
3. Check environment variables
4. Monitor application logs
5. Set up custom domain if needed

## Rollback Strategy

If deployment fails:
1. Check Railway logs for specific errors
2. Verify environment variables
3. Test locally with the same configuration
4. Consider using the simplified requirements file
5. Use Railway's native Python support as fallback 