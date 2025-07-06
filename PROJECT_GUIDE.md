# 🏆 Sports Tournament Dashboard - Complete Guide

This project provides three different approaches to create a comprehensive sports tournament dashboard based on your image reference. Choose the approach that best fits your needs and technical expertise.

## 📊 Dashboard Features (All Platforms)

Based on your image reference, the dashboard includes:

- **Key Metrics**: Total medals, players, and events
- **Tournament-wise Medal Tally**: Horizontal bar chart
- **Medal Share Distribution**: Pie chart with percentages
- **Win Rate Trends**: Line chart over time
- **Multiple Analysis Views**: Institute-wise, Player-wise, Gender-wise, Event/Category-wise, Year-wise
- **Interactive Filters**: Year, Gender, Institute, Event/Category
- **Search Functionality**: Quick search for institutes and players
- **Player Details Panel**: Detailed player information
- **Professional Design**: Brown/tan color scheme matching your reference

## 🚀 Option 1: Streamlit Dashboard (Recommended)

### ✅ Advantages:
- **Ready to Use**: Complete Python implementation provided
- **Interactive**: Full interactivity with filters and search
- **Customizable**: Easy to modify and extend
- **Cost-Effective**: Completely free and open-source
- **Professional**: Matches your reference design closely

### 📋 Quick Start:

```bash
# 1. Run the startup script
./run_dashboard.sh

# 2. Or manually:
export PATH=$PATH:/home/ubuntu/.local/bin
streamlit run sports_dashboard.py
```

### 📁 Files Included:
- `sports_dashboard.py` - Main dashboard application
- `requirements.txt` - Python dependencies
- `run_dashboard.sh` - Easy startup script
- `README.md` - Detailed documentation

### 🎯 Access:
Open your web browser and go to: `http://localhost:8501`

---

## 📈 Option 2: Tableau Implementation

### ✅ Advantages:
- **Enterprise-Grade**: Professional BI tool
- **Advanced Analytics**: Built-in statistical functions
- **Easy Sharing**: Tableau Server/Cloud integration
- **Drag-and-Drop**: No coding required

### 📋 Step-by-Step Guide:

#### Data Preparation:
1. **Import Data**:
   - Open Tableau Desktop
   - Connect to `22-23 csv.csv`, `23-24 csv.csv`, `24-25 csv.csv`
   - Union all three files into one dataset

2. **Data Cleaning**:
   ```
   - Create calculated field [Medal Type]:
     IF [Select the Achievement ] = "Gold" THEN "Gold"
     ELSEIF [Select the Achievement ] = "Silver" THEN "Silver" 
     ELSEIF [Select the Achievement ] = "Bronze" THEN "Bronze"
     ELSE "Other" END
   
   - Create calculated field [Is Medal]:
     [Medal Type] IN ("Gold","Silver","Bronze")
   ```

#### Dashboard Creation:

1. **Key Metrics Sheet**:
   - Drag [Medal Type] to Filters, select Gold/Silver/Bronze
   - Create three Text tables:
     - Total Medals: COUNT([Player Name or Team Name ])
     - Total Players: COUNTD([Player Name or Team Name ])
     - Total Events: COUNTD([Tournament Name])

2. **Tournament-wise Medal Tally**:
   - Rows: [Tournament level]
   - Columns: COUNT([Player Name or Team Name ])
   - Filters: [Is Medal] = True
   - Mark Type: Bar (horizontal)

3. **Medal Share Pie Chart**:
   - Angle: COUNT([Player Name or Team Name ])
   - Color: [Medal Type]
   - Filters: [Medal Type] ≠ "Other"
   - Mark Type: Pie

4. **Win Rate Trend**:
   ```
   Create calculated field [Win Rate]:
   SUM([Is Medal]) / COUNT([Player Name or Team Name ]) * 100
   ```
   - Columns: [YEAR]
   - Rows: [Win Rate]
   - Mark Type: Line

5. **Dashboard Assembly**:
   - Create dashboard with brown color scheme (#8B4513, #A0522D, #F5DEB3)
   - Add filters for Year, Gender, Institute, Event/Category
   - Arrange sheets to match reference layout

### 💰 Cost:
- Tableau Desktop: $75/month per user
- Tableau Creator: $75/month (includes Prep and Desktop)

---

## 📊 Option 3: Power BI Implementation

### ✅ Advantages:
- **Microsoft Ecosystem**: Integrates with Office 365
- **Cost-Effective**: Lower cost than Tableau
- **Cloud Integration**: Easy sharing via Power BI Service
- **DAX Language**: Powerful calculation engine

### 📋 Step-by-Step Guide:

#### Data Import:
1. **Get Data**:
   - Open Power BI Desktop
   - Get Data → Text/CSV
   - Import all three CSV files
   - Append queries to combine into one table

2. **Data Modeling**:
   ```DAX
   // Create Medal Type column
   Medal Type = 
   SWITCH(
       sports_data[Select the Achievement ],
       "Gold", "Gold",
       "Silver", "Silver", 
       "Bronze", "Bronze",
       "Other"
   )
   
   // Create Is Medal column
   Is Medal = IF(sports_data[Medal Type] IN {"Gold","Silver","Bronze"}, TRUE, FALSE)
   ```

#### Visualizations:

1. **Key Metrics Cards**:
   ```DAX
   Total Medals = CALCULATE(COUNT(sports_data[Player Name or Team Name ]), sports_data[Is Medal] = TRUE)
   Total Players = DISTINCTCOUNT(sports_data[Player Name or Team Name ])
   Total Events = DISTINCTCOUNT(sports_data[Tournament Name])
   ```

2. **Tournament Medal Tally** (Clustered Bar Chart):
   - Axis: Tournament level
   - Values: Count of records (filtered by Is Medal = TRUE)

3. **Medal Share** (Pie Chart):
   - Legend: Medal Type
   - Values: Count of records
   - Filter: Medal Type ≠ "Other"

4. **Win Rate Trend** (Line Chart):
   ```DAX
   Win Rate = 
   DIVIDE(
       CALCULATE(COUNT(sports_data[Player Name or Team Name ]), sports_data[Is Medal] = TRUE),
       COUNT(sports_data[Player Name or Team Name ])
   ) * 100
   ```
   - Axis: YEAR
   - Values: Win Rate

5. **Formatting**:
   - Apply brown color theme (#8B4513, #A0522D, #F5DEB3)
   - Add slicers for Year, Gender, Institute, Event/Category
   - Configure layout to match reference

### 💰 Cost:
- Power BI Pro: $10/month per user
- Power BI Premium: $20/month per user

---

## 🔄 Data Structure Reference

All implementations use the same data structure:

```csv
YEAR,Institute Name,Player Name or Team Name,Sports,Gender,Coach Name,Course,Tournament level,Tournament Name,Select the Achievement,Achievement Photos
2022-2023,Institute A,Player 1,Judo,Girl,Coach A,Course A,District Level,Tournament A,Gold,photo_link
```

### Key Columns:
- **YEAR**: Academic year (2022-2023, 2023-2024, 2024-2025)
- **Institute Name**: Educational institution
- **Player Name or Team Name**: Participant identifier
- **Sports**: Sport category (currently Judo)
- **Gender**: Male/Female
- **Tournament level**: District, State, National, etc.
- **Select the Achievement**: Gold, Silver, Bronze, Participated, positions
- **Tournament Name**: Specific tournament identifier

---

## 🎨 Design Specifications

### Color Palette:
- **Primary**: #8B4513 (Dark Brown)
- **Secondary**: #A0522D (Brown)
- **Background**: #D2B48C (Tan)
- **Text Light**: #F5DEB3 (Beige)
- **Accent**: #DEB887 (Burlywood)

### Chart Colors:
- **Gold**: #DAA520
- **Silver**: #C0C0C0  
- **Bronze**: #CD7F32

---

## 📋 Comparison Matrix

| Feature | Streamlit | Tableau | Power BI |
|---------|-----------|---------|----------|
| **Cost** | Free | $75/month | $10-20/month |
| **Ease of Setup** | Easy | Medium | Medium |
| **Customization** | High | High | Medium |
| **Learning Curve** | Low | High | Medium |
| **Interactivity** | High | Very High | High |
| **Sharing** | Self-hosted | Cloud/Server | Cloud Service |
| **Maintenance** | Self-managed | Managed | Managed |
| **Real-time Updates** | Yes | Yes | Yes |

---

## 🚀 Recommendations

### Choose **Streamlit** if:
- You want a free solution
- You're comfortable with Python
- You need full customization control
- You want to get started immediately

### Choose **Tableau** if:
- You have budget for enterprise tools
- You need advanced analytics features
- You want drag-and-drop simplicity
- You're in a large organization

### Choose **Power BI** if:
- You're in a Microsoft ecosystem
- You want professional BI at lower cost
- You need good balance of features and price
- You want enterprise sharing capabilities

---

## 📞 Support & Next Steps

### For Streamlit Implementation:
1. Run `./run_dashboard.sh` to start
2. Customize colors/features in `sports_dashboard.py`
3. Add new data by updating CSV files
4. Deploy to cloud using Streamlit Cloud (free)

### For Tableau/Power BI:
1. Follow the step-by-step guides above
2. Import your CSV data
3. Create calculated fields as specified
4. Build visualizations matching the reference
5. Apply the brown color theme

### Additional Features You Can Add:
- **Photo Gallery**: Display achievement photos
- **Performance Trends**: Year-over-year comparisons
- **Coach Analytics**: Coach performance metrics
- **Geographic Analysis**: Performance by region
- **Predictive Models**: Future performance predictions

---

**🏆 Happy Dashboard Building!**

*Need help? Check the detailed README.md for Streamlit implementation or refer to official documentation for Tableau/Power BI.*