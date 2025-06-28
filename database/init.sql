-- Database initialization script for Inventory Health AI
-- This script creates sample data for demonstration purposes

-- Create sample plants
INSERT INTO plants (plant_code, plant_name, plant_type, country, region, city, erp_system, is_active) VALUES
('PLANT001', 'North Manufacturing', 'Manufacturing', 'USA', 'Northeast', 'Boston', 'SAP', true),
('PLANT002', 'South Distribution', 'Distribution', 'USA', 'Southeast', 'Atlanta', 'Oracle', true),
('PLANT003', 'West Production', 'Manufacturing', 'USA', 'West', 'Los Angeles', 'SAP', true),
('PLANT004', 'Central Warehouse', 'Warehouse', 'USA', 'Central', 'Chicago', 'SAP', true),
('PLANT005', 'European Hub', 'Manufacturing', 'Germany', 'Bavaria', 'Munich', 'SAP', true);

-- Create sample materials
INSERT INTO materials (material_id, material_name, material_description, category, material_group, base_unit, erp_system, is_active) VALUES
('MAT001', 'Steel Sheet 2mm', 'High-grade steel sheet 2mm thickness', 'raw_material', 'Metals', 'PCS', 'SAP', true),
('MAT002', 'Electronic Circuit Board', 'PCB for control systems', 'semi_finished', 'Electronics', 'PCS', 'SAP', true),
('MAT003', 'Finished Product A', 'Complete assembled product A', 'finished_good', 'Products', 'PCS', 'SAP', true),
('MAT004', 'Motor Bearing', 'Precision motor bearing', 'spare_part', 'Mechanical', 'PCS', 'SAP', true),
('MAT005', 'Lubricating Oil', 'Industrial lubricating oil', 'consumable', 'Chemicals', 'L', 'SAP', true),
('MAT006', 'Plastic Container', 'Storage container 20L', 'packaging', 'Packaging', 'PCS', 'SAP', true);

-- Create sample inventory levels
INSERT INTO inventory_levels (material_id, plant_id, storage_location, stock_type, available_quantity, reserved_quantity, total_quantity, unit_of_measure, erp_system) VALUES
('MAT001', 'PLANT001', 'WH-A1', 'raw_material', 150.0, 25.0, 175.0, 'PCS', 'SAP'),
('MAT002', 'PLANT001', 'WH-B2', 'semi_finished', 75.0, 10.0, 85.0, 'PCS', 'SAP'),
('MAT003', 'PLANT001', 'WH-C3', 'finished_good', 200.0, 50.0, 250.0, 'PCS', 'SAP'),
('MAT004', 'PLANT002', 'WH-D4', 'spare_part', 45.0, 5.0, 50.0, 'PCS', 'Oracle'),
('MAT005', 'PLANT002', 'WH-E5', 'consumable', 500.0, 0.0, 500.0, 'L', 'Oracle'),
('MAT006', 'PLANT003', 'WH-F6', 'packaging', 300.0, 75.0, 375.0, 'PCS', 'SAP'),
('MAT001', 'PLANT003', 'WH-A1', 'raw_material', 200.0, 30.0, 230.0, 'PCS', 'SAP'),
('MAT002', 'PLANT004', 'WH-B2', 'semi_finished', 60.0, 15.0, 75.0, 'PCS', 'SAP'),
('MAT003', 'PLANT005', 'WH-C3', 'finished_good', 180.0, 40.0, 220.0, 'PCS', 'SAP');

-- Create sample inventory transactions
INSERT INTO inventory_transactions (material_id, plant_id, transaction_type, quantity, unit_of_measure, reference_document, reference_number, erp_system, transaction_date) VALUES
('MAT001', 'PLANT001', 'IN', 50.0, 'PCS', 'PO', 'PO-2024-001', 'SAP', NOW() - INTERVAL '1 day'),
('MAT001', 'PLANT001', 'OUT', 25.0, 'PCS', 'SO', 'SO-2024-001', 'SAP', NOW() - INTERVAL '2 days'),
('MAT002', 'PLANT001', 'IN', 30.0, 'PCS', 'PO', 'PO-2024-002', 'SAP', NOW() - INTERVAL '3 days'),
('MAT003', 'PLANT001', 'OUT', 40.0, 'PCS', 'SO', 'SO-2024-002', 'SAP', NOW() - INTERVAL '4 days'),
('MAT004', 'PLANT002', 'IN', 20.0, 'PCS', 'PO', 'PO-2024-003', 'Oracle', NOW() - INTERVAL '5 days');

-- Create sample inventory alerts
INSERT INTO inventory_alerts (material_id, plant_id, alert_type, severity, message, is_active) VALUES
('MAT001', 'PLANT001', 'LOW_STOCK', 'medium', 'Steel Sheet 2mm stock level is below reorder point', true),
('MAT004', 'PLANT002', 'STOCK_OUT', 'high', 'Motor Bearing is out of stock', true),
('MAT005', 'PLANT002', 'OVERSTOCK', 'low', 'Lubricating Oil stock level is above maximum', true);

-- Create sample users
INSERT INTO users (username, email, full_name, hashed_password, role, company, department, is_active, is_verified) VALUES
('admin', 'admin@company.com', 'System Administrator', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.s5u.Gi', 'admin', 'Company Inc', 'IT', true, true),
('executive', 'executive@company.com', 'Executive User', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.s5u.Gi', 'executive', 'Company Inc', 'Executive', true, true),
('manager', 'manager@company.com', 'Operations Manager', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.s5u.Gi', 'manager', 'Company Inc', 'Operations', true, true);

-- Note: The hashed password above is for 'admin123' - change in production! 