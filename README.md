# 🏆 Sports Medals Dashboard

A comprehensive Streamlit dashboard for analyzing sports tournament data from the past 3 years. This dashboard provides interactive visualizations and analytics for medal distribution, player performance, institute rankings, and tournament statistics.

## Features

### 📊 Key Visualizations
- **Total Statistics**: Overview of total medals, players, and events
- **Tournament-wise Medal Tally**: Horizontal bar chart showing medal distribution by tournament level
- **Medal Share**: Pie chart displaying gold, silver, and bronze medal percentages
- **Win Rate Trend**: Line chart showing performance trends over years

### 🔍 Interactive Filters
- **Year Filter**: Select specific years (2022-2023, 2023-2024, 2024-2025)
- **Gender Filter**: Filter by Male/Female participants
- **Institute Filter**: Choose specific institutes
- **Event/Category Filter**: Filter by sport type

### 📈 Multi-Tab Analysis
1. **Institute-wise**: Analyze performance by educational institution
2. **Player-wise**: Individual player statistics and achievements
3. **Gender-wise**: Gender-based performance analysis
4. **Event/Category-wise**: Sport-specific performance metrics
5. **Year-wise**: Temporal analysis of performance trends

### 🎨 Design Features
- **Dark Theme**: Professional brown/tan color scheme matching the original design
- **Responsive Layout**: Optimized for different screen sizes
- **Search Functionality**: Quick search for institutes and players
- **Export Options**: Download data as CSV or summary reports
- **Player Details Panel**: Detailed information about selected players

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Step 1: Clone or Download
```bash
# If using git
git clone <repository-url>
cd sports-dashboard

# Or download the files directly
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Data Files
Ensure you have the following CSV files in the project directory:
- `22-23 csv.csv`
- `23-24 csv.csv`
- `24-25 csv.csv`
- `main data sheet cleaned.xlsx` (optional)

### Step 4: Run the Dashboard
```bash
streamlit run sports_dashboard.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`

## Usage Guide

### Navigation
1. **Sidebar Filters**: Use the left sidebar to filter data by year, gender, institute, and event category
2. **Main Dashboard**: View key metrics and visualizations
3. **Tabs**: Switch between different analysis views
4. **Search**: Use search boxes to find specific institutes or players
5. **Export**: Download filtered data or summary reports

### Key Metrics
- **Total**: Total number of medals won
- **Total Players**: Number of unique players
- **Total Events**: Number of unique tournaments/events

### Chart Interactions
- **Hover**: Hover over charts to see detailed information
- **Zoom**: Use plotly controls to zoom in/out on charts
- **Pan**: Click and drag to pan across charts

## Data Structure

The dashboard expects CSV files with the following columns:
- `YEAR`: Academic year (e.g., 2022-2023)
- `Institute Name`: Educational institution name
- `Player Name or Team Name`: Participant name
- `Sports`: Sport category (e.g., Judo)
- `Gender`: Male/Female
- `Coach Name/College Sports In charge Name`: Coach information
- `Course`: Academic course details
- `Tournament level`: Competition level (District, State, National, etc.)
- `Tournament Name`: Specific tournament name
- `Select the Achievement`: Medal type (Gold, Silver, Bronze, Participated)
- `Achievement or team photographs`: Photo links (optional)

## Customization

### Colors and Themes
You can customize the dashboard colors by modifying the CSS variables in `sports_dashboard.py`:
- `#8B4513`: Primary brown color
- `#A0522D`: Secondary brown color
- `#F5DEB3`: Light beige color
- `#D2B48C`: Tan color

### Adding New Visualizations
To add new charts or analysis:
1. Create a new function in `sports_dashboard.py`
2. Add it to the appropriate tab section
3. Update the layout as needed

### Filters
To add new filters:
1. Add the filter widget in the sidebar section
2. Include the filter in the data filtering logic
3. Update the `filtered_df` variable

## Troubleshooting

### Common Issues

1. **Module Not Found Error**
   ```bash
   pip install streamlit pandas plotly numpy openpyxl
   ```

2. **Data Loading Error**
   - Ensure CSV files are in the correct directory
   - Check file names match exactly
   - Verify CSV file format and encoding

3. **Chart Not Displaying**
   - Check if filtered data is empty
   - Verify column names in the CSV files
   - Ensure data types are correct

4. **Performance Issues**
   - Large datasets may take time to load
   - Consider using `@st.cache_data` for heavy operations
   - Filter data to reduce processing time

### File Structure
```
sports-dashboard/
├── sports_dashboard.py      # Main dashboard application
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── 22-23 csv.csv          # Data file for 2022-2023
├── 23-24 csv.csv          # Data file for 2023-2024
├── 24-25 csv.csv          # Data file for 2024-2025
└── main data sheet cleaned.xlsx  # Optional Excel file
```

## Alternative Platforms

### Tableau
If you prefer Tableau:
1. Import the CSV files into Tableau
2. Create calculated fields for medal types
3. Build similar visualizations using Tableau's drag-and-drop interface
4. Set up filters and parameters for interactivity

### Power BI
For Power BI implementation:
1. Load data using Power BI Desktop
2. Create relationships between tables if needed
3. Build visuals using Power BI's visualization pane
4. Add slicers for filtering functionality

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your Python and package versions
3. Ensure data files are properly formatted
4. Check the Streamlit documentation for advanced features

## License

This project is open-source and available under the MIT License.

---

**Happy Analyzing! 🏆📊**