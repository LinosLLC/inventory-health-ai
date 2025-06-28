import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Box, Container } from '@mui/material';

import Layout from './components/Layout/Layout';
import Dashboard from './pages/Dashboard/Dashboard';
import Inventory from './pages/Inventory/Inventory';
import Plants from './pages/Plants/Plants';
import Materials from './pages/Materials/Materials';
import Analytics from './pages/Analytics/Analytics';
import Login from './pages/Login/Login';
import { useAuth } from './hooks/useAuth';

function App() {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Login />;
  }

  return (
    <Layout>
      <Box sx={{ flexGrow: 1, py: 3 }}>
        <Container maxWidth="xl">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/inventory" element={<Inventory />} />
            <Route path="/plants" element={<Plants />} />
            <Route path="/materials" element={<Materials />} />
            <Route path="/analytics" element={<Analytics />} />
          </Routes>
        </Container>
      </Box>
    </Layout>
  );
}

export default App; 