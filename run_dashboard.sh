#!/bin/bash

# Sports Dashboard Startup Script
echo "🏆 Starting Sports Medals Dashboard..."

# Add local bin to PATH
export PATH=$PATH:/home/ubuntu/.local/bin

# Check if required Excel file exists
if [ ! -f "main data sheet cleaned.xlsx" ]; then
    echo "❌ Error: Required Excel file not found!"
    echo "Please ensure the following file is in the current directory:"
    echo "  - main data sheet cleaned.xlsx"
    exit 1
fi

echo "✅ Excel file found"

# Check if streamlit is available
if ! command -v streamlit &> /dev/null; then
    echo "❌ Error: Streamlit not found!"
    echo "Please install dependencies first:"
    echo "pip install --break-system-packages streamlit pandas plotly numpy openpyxl"
    exit 1
fi

echo "✅ Streamlit found"

# Start the dashboard
echo "🚀 Launching dashboard..."
echo "📊 Dashboard will be available at: http://localhost:8501"
echo "Press Ctrl+C to stop the dashboard"

streamlit run sports_dashboard.py
