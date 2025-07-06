#!/bin/bash

# Sports Dashboard Startup Script
echo "🏆 Starting Sports Medals Dashboard..."

# Add local bin to PATH
export PATH=$PATH:/home/ubuntu/.local/bin

# Check if required CSV files exist
if [ ! -f "22-23 csv.csv" ] || [ ! -f "23-24 csv.csv" ] || [ ! -f "24-25 csv.csv" ]; then
    echo "❌ Error: Required CSV files not found!"
    echo "Please ensure the following files are in the current directory:"
    echo "  - 22-23 csv.csv"
    echo "  - 23-24 csv.csv" 
    echo "  - 24-25 csv.csv"
    exit 1
fi

echo "✅ CSV files found"

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