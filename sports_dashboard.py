import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Medals Dashboard",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #8B4513;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #8B4513 0%, #A0522D 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 1.2rem;
        color: #F5DEB3;
    }
    
    .filter-section {
        background: #8B4513;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .filter-title {
        color: #F5DEB3;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .chart-container {
        background: #D2B48C;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .chart-title {
        color: #8B4513;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .player-card {
        background: #8B4513;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    
    .player-name {
        font-size: 1.5rem;
        font-weight: bold;
        color: #F5DEB3;
    }
    
    .player-details {
        color: #DEB887;
        margin-top: 0.5rem;
    }
    
    .stSelectbox > div > div {
        background-color: #F5DEB3;
        color: #8B4513;
    }
    
    .stMultiSelect > div > div {
        background-color: #F5DEB3;
        color: #8B4513;
    }
    
    .stDataFrame {
        background-color: #F5DEB3;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #8B4513;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #A0522D;
        color: #F5DEB3;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load data from the main Excel file"""
    try:
        # Load Excel file
        df = pd.read_excel('main data sheet cleaned.xlsx')
        
       # Clean column names
df.columns = df.columns.str.strip()

# Directly reference the known column name after stripping
achievement_col = "Select the Achievement"
if achievement_col not in df.columns:
    st.error(f"Column '{achievement_col}' not found in the data")
    return pd.DataFrame()

# Standardize achievement values
df['Achievement'] = df[achievement_col].astype(str).str.strip().str.title()

# Map known values to standardized labels
df['Achievement'] = df['Achievement'].replace({
    'Gold': 'Gold',
    'Silver': 'Silver',
    'Bronze': 'Bronze',
    'Participated': 'Participated'
    '5th Position': '5th Position'
    '7th Position': '7th Position'
})

        #Create medal type column
        df['Medal_Type'] = df['Achievement'].str.lower().map({
            'gold': 'Gold',
            'silver': 'Silver',
            'bronze': 'Bronze'
        }).fillna('Participated')
        
        # Handle gender column - look for variations
        gender_col = None
        for col in df.columns:
            if 'gender' in col.lower():
                gender_col = col
                break
        
        if gender_col:
            df['Gender'] = df[gender_col].astype(str).str.strip().str.lower()
                        # Map 'boy' → 'Male', 'girl' → 'Female'
             df['Gender'] = df['Gender'].replace({
                 'boy': 'Male',
                 'girl': 'Female',
                 'male': 'Male',
                 'female': 'Female'
             })
             df['Gender'] = df['Gender'].where(df['Gender'].isin(['Male', 'Female']), 'Unknown')
        else:
            df['Gender'] = 'Unknown'
        
        # Handle institute names - look for variations
            df.columns = df.columns.str.strip()

              # Use the known column name
            institute_col = "Institute Name"

            if institute_col in df.columns:
                 df['Institute'] = df[institute_col].astype(str).str.strip()
            else:
                 df['Institute'] = 'Unknown'
        
        # Handle player names - look for variations
           df.columns = df.columns.str.strip()

           if "Player Name or Team Name" in df.columns:
                 df = df.rename(columns={"Player Name or Team Name": "Player/Team_Name"})
                 df['Player/Team_Name'] = df['Player/Team_Name'].astype(str).str.strip()
           else:
                 df['Player/Team_Name'] = 'Unknown'

        
        # Handle sports - look for variations
        sport_col = None
        for col in df.columns:
            if 'sport' in col.lower():
                sport_col = col
                break
        
        if sport_col:
            df['Sport'] = df[sport_col].astype(str).str.strip()
        else:
            df['Sport'] = 'Unknown'
        
        # Handle tournament level - look for variations
        tournament_level_col = None
        for col in df.columns:
            if 'tournament' in col.lower() and 'level' in col.lower():
                tournament_level_col = col
                break
        
        if tournament_level_col:
            df['Tournament_Level'] = df[tournament_level_col].astype(str).str.strip()
        else:
            df['Tournament_Level'] = 'Unknown'
        
        # Handle tournament name - look for variations
        tournament_name_col = None
        for col in df.columns:
            if ('tournament' in col.lower() and 'name' in col.lower()) or ('tournament' in col.lower() and 'title' in col.lower()):
                tournament_name_col = col
                break
        
        if tournament_name_col:
            df['Tournament Name'] = df[tournament_name_col].astype(str).str.strip()
        else:
            # Use tournament level as tournament name if specific name not found
            df['Tournament Name'] = df['Tournament_Level']
        
        # Handle year - look for variations
        year_col = None
        for col in df.columns:
            if 'year' in col.lower():
                year_col = col
                break
        
        if year_col:
            df['YEAR'] = df[year_col].astype(str).str.strip()
        else:
            df['YEAR'] = '2024-2025'  # Default year
        
        # Remove rows with missing essential data
        # Clean string fields
            df['Player_Name'] = df['Player_Name'].astype(str).str.strip()
            df['Achievement'] = df['Achievement'].astype(str).str.strip()
      # Remove rows with missing essential data
            df = df.dropna(subset=['Player_Name', 'Achievement'])
            df = df[df['Player_Name'].str.lower() != 'unknown']
            df = df[~df['Achievement'].str.lower().eq('nan')]
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()
#EDITED AND CHECKED TILL HERE (EXCEPT HTML PART) - AYUSH
def create_medal_tally_chart(df):
    """Create tournament-wise medal tally bar chart"""
    medal_counts = df[df['Medal_Type'].isin(['Gold', 'Silver', 'Bronze'])].groupby('Tournament_Level').size().reset_index(name='Count')
    
    fig = px.bar(
        medal_counts, 
        x='Count', 
        y='Tournament_Level',
        orientation='h',
        title='Tournament-wise Medal Tally',
        color='Count',
        color_continuous_scale='brwnyl'
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#8B4513'),
        title_font=dict(size=16, color='#8B4513'),
        height=300
    )
    
    return fig

def create_medal_share_chart(df):
    """Create medal share pie chart"""
    medal_counts = df[df['Medal_Type'].isin(['Gold', 'Silver', 'Bronze'])]['Medal_Type'].value_counts()
    
    colors = ['#DAA520', '#C0C0C0', '#CD7F32']  # Gold, Silver, Bronze colors
    
    fig = px.pie(
        values=medal_counts.values,
        names=medal_counts.index,
        title='Medal Share',
        color_discrete_sequence=colors
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#8B4513'),
        title_font=dict(size=16, color='#8B4513'),
        height=300
    )
    
    return fig

def create_win_rate_chart(df):
    """Create win rate trend chart"""
    # Calculate win rate by year
    yearly_stats = df.groupby('YEAR').agg({
        'Medal_Type': lambda x: sum(x.isin(['Gold', 'Silver', 'Bronze'])),
        'Player_Name': 'count'
    }).reset_index()
    
    yearly_stats['Win_Rate'] = (yearly_stats['Medal_Type'] / yearly_stats['Player_Name']) * 100
    
    fig = px.line(
        yearly_stats,
        x='YEAR',
        y='Win_Rate',
        title='Win Rate Trend',
        markers=True
    )
    
    fig.update_traces(line=dict(color='#8B4513', width=3))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#8B4513'),
        title_font=dict(size=16, color='#8B4513'),
        height=300,
        xaxis=dict(gridcolor='#DEB887'),
        yaxis=dict(gridcolor='#DEB887')
    )
    
    return fig

def main():
    # Load data
    df = load_data()
    
    if df.empty:
        st.error("No data available. Please check your Excel file: 'main data sheet cleaned.xlsx'")
        return
    
    # Main header
    st.markdown('<div class="main-header">🏆 Medals Dashboard</div>', unsafe_allow_html=True)
    
    # Sidebar filters
    st.sidebar.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="filter-title">FILTERS</div>', unsafe_allow_html=True)
    
    # Year filter
    years = sorted(df['YEAR'].unique())
    selected_years = st.sidebar.multiselect('Year', years, default=years)
    
    # Gender filter
    genders = sorted(df['Gender'].unique())
    selected_genders = st.sidebar.multiselect('Gender', genders, default=genders)
    
    # Institute filter
    institutes = sorted(df['Institute'].unique())
    selected_institutes = st.sidebar.multiselect('Institute', institutes, default=institutes[:5])
    
    # Event/Category filter
    sports = sorted(df['Sport'].unique())
    selected_sports = st.sidebar.multiselect('Event / Category', sports, default=sports)
    
    # Reset filters button
    if st.sidebar.button('Reset Filters'):
        st.rerun()
    
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    # Filter data
    filtered_df = df[
        (df['YEAR'].isin(selected_years)) &
        (df['Gender'].isin(selected_genders)) &
        (df['Institute'].isin(selected_institutes)) &
        (df['Sport'].isin(selected_sports))
    ]
    
    # Top metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_medals = len(filtered_df[filtered_df['Medal_Type'].isin(['Gold', 'Silver', 'Bronze'])])
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{total_medals}</div>
            <div class="metric-label">Total</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        total_players = filtered_df['Player_Name'].nunique()
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{total_players}</div>
            <div class="metric-label">Total Players</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        total_events = filtered_df['Tournament Name'].nunique()
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{total_events}</div>
            <div class="metric-label">Total Events</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Charts row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_medal_tally_chart(filtered_df), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_medal_share_chart(filtered_df), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_win_rate_chart(filtered_df), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Tabs for different views
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Institute-wise', 'Player-wise', 'Gender-wise', 'Event/Category-wise', 'Year-wise'])
    
    with tab1:
        st.markdown('<div class="chart-title">Institute-wise Analysis</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Institute-wise table
            institute_stats = filtered_df.groupby('Institute').agg({
                'Player_Name': 'nunique',
                'Medal_Type': lambda x: sum(x.isin(['Gold', 'Silver', 'Bronze'])),
                'Gender': lambda x: ', '.join(x.unique())[:20] + '...' if len(', '.join(x.unique())) > 20 else ', '.join(x.unique()),
                'Tournament Name': 'nunique'
            }).reset_index()
            
            institute_stats.columns = ['Institute', 'Players', 'Medals', 'Gender', 'Tournaments']
            institute_stats = institute_stats.sort_values('Medals', ascending=False)
            
            # Search functionality
            search_term = st.text_input("🔍 Search Institute", placeholder="Search institute...")
            if search_term:
                institute_stats = institute_stats[institute_stats['Institute'].str.contains(search_term, case=False)]
            
            st.dataframe(institute_stats, use_container_width=True, hide_index=True)
            
            # Pagination info
            st.markdown(f"<div style='color: #8B4513; text-align: center; margin-top: 1rem;'>1-{len(institute_stats)} of {len(institute_stats)}</div>", unsafe_allow_html=True)
        
        with col2:
            # Player details panel
            if not institute_stats.empty:
                selected_institute = institute_stats.iloc[0]['Institute']
                selected_players = filtered_df[filtered_df['Institute'] == selected_institute]
                
                if not selected_players.empty:
                    player_info = selected_players.iloc[0]
                    st.markdown(f'''
                    <div class="player-card">
                        <div class="player-name">{player_info['Player_Name']}</div>
                        <div class="player-details">
                            <strong>Institute:</strong> {player_info['Institute']}<br>
                            <strong>Gender:</strong> {player_info['Gender']}<br>
                            <strong>Events played:</strong> {player_info['Sport']}<br>
                            <strong>Medals won:</strong> {player_info['Achievement']}<br>
                            <strong>Total Events:</strong> {len(selected_players)}
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="chart-title">Player-wise Analysis</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Player-wise table
            player_stats = filtered_df.groupby('Player_Name').agg({
                'Institute': 'first',
                'Gender': 'first',
                'Medal_Type': lambda x: sum(x.isin(['Gold', 'Silver', 'Bronze'])),
                'Achievement': 'first',
                'Tournament Name': 'nunique'
            }).reset_index()
            
            player_stats.columns = ['Player Name', 'Institute', 'Gender', 'Medals', 'Achievement', 'Tournaments']
            player_stats = player_stats.sort_values('Medals', ascending=False)
            
            # Search functionality
            search_player = st.text_input("🔍 Search Player", placeholder="Search player...")
            if search_player:
                player_stats = player_stats[player_stats['Player Name'].str.contains(search_player, case=False)]
            
            st.dataframe(player_stats, use_container_width=True, hide_index=True)
            
            # Pagination info
            st.markdown(f"<div style='color: #8B4513; text-align: center; margin-top: 1rem;'>1-{len(player_stats)} of {len(player_stats)}</div>", unsafe_allow_html=True)
        
        with col2:
            # Player details panel
            if not player_stats.empty:
                selected_player_name = player_stats.iloc[0]['Player Name']
                selected_player_data = filtered_df[filtered_df['Player_Name'] == selected_player_name]
                
                if not selected_player_data.empty:
                    player_info = selected_player_data.iloc[0]
                    medals_won = selected_player_data[selected_player_data['Medal_Type'].isin(['Gold', 'Silver', 'Bronze'])]
                    
                    st.markdown(f'''
                    <div class="player-card">
                        <div class="player-name">{player_info['Player_Name']}</div>
                        <div class="player-details">
                            <strong>Institute:</strong> {player_info['Institute']}<br>
                            <strong>Gender:</strong> {player_info['Gender']}<br>
                            <strong>Events played:</strong> {player_info['Sport']}<br>
                            <strong>Medals won:</strong> {len(medals_won)}<br>
                            <strong>Total Events:</strong> {len(selected_player_data)}
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="chart-title">Gender-wise Analysis</div>', unsafe_allow_html=True)
        
        # Gender-wise statistics
        gender_stats = filtered_df.groupby('Gender').agg({
            'Player_Name': 'nunique',
            'Medal_Type': lambda x: sum(x.isin(['Gold', 'Silver', 'Bronze'])),
            'Tournament Name': 'nunique'
        }).reset_index()
        
        gender_stats.columns = ['Gender', 'Players', 'Medals', 'Tournaments']
        
        # Gender-wise medal distribution chart
        gender_medal_dist = filtered_df[filtered_df['Medal_Type'].isin(['Gold', 'Silver', 'Bronze'])].groupby(['Gender', 'Medal_Type']).size().reset_index(name='Count')
        
        fig = px.bar(
            gender_medal_dist,
            x='Gender',
            y='Count',
            color='Medal_Type',
            title='Medal Distribution by Gender',
            color_discrete_map={'Gold': '#DAA520', 'Silver': '#C0C0C0', 'Bronze': '#CD7F32'}
        )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#8B4513'),
            title_font=dict(size=16, color='#8B4513')
        )
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.dataframe(gender_stats, use_container_width=True, hide_index=True)
    
    with tab4:
        st.markdown('<div class="chart-title">Event/Category-wise Analysis</div>', unsafe_allow_html=True)
        
        # Event-wise statistics
        event_stats = filtered_df.groupby('Sport').agg({
            'Player_Name': 'nunique',
            'Medal_Type': lambda x: sum(x.isin(['Gold', 'Silver', 'Bronze'])),
            'Tournament Name': 'nunique'
        }).reset_index()
        
        event_stats.columns = ['Sport', 'Players', 'Medals', 'Tournaments']
        event_stats = event_stats.sort_values('Medals', ascending=False)
        
        # Event-wise medal chart
        fig = px.bar(
            event_stats,
            x='Sport',
            y='Medals',
            title='Medals by Sport',
            color='Medals',
            color_continuous_scale='brwnyl'
        )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#8B4513'),
            title_font=dict(size=16, color='#8B4513')
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(event_stats, use_container_width=True, hide_index=True)
    
    with tab5:
        st.markdown('<div class="chart-title">Year-wise Analysis</div>', unsafe_allow_html=True)
        
        # Year-wise statistics
        year_stats = filtered_df.groupby('YEAR').agg({
            'Player_Name': 'nunique',
            'Medal_Type': lambda x: sum(x.isin(['Gold', 'Silver', 'Bronze'])),
            'Tournament Name': 'nunique'
        }).reset_index()
        
        year_stats.columns = ['Year', 'Players', 'Medals', 'Tournaments']
        
        # Year-wise trend chart
        fig = px.line(
            year_stats,
            x='Year',
            y='Medals',
            title='Medal Trend Over Years',
            markers=True
        )
        
        fig.update_traces(line=dict(color='#8B4513', width=3))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#8B4513'),
            title_font=dict(size=16, color='#8B4513')
        )
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.dataframe(year_stats, use_container_width=True, hide_index=True)
    
    # Export functionality
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("📊 Export to CSV"):
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"sports_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    
    with col2:
        if st.button("📋 Download Summary"):
            summary = f"""
            Sports Dashboard Summary
            =======================
            
            Total Records: {len(filtered_df)}
            Total Players: {filtered_df['Player_Name'].nunique()}
            Total Medals: {len(filtered_df[filtered_df['Medal_Type'].isin(['Gold', 'Silver', 'Bronze'])])}
            Total Events: {filtered_df['Tournament Name'].nunique()}
            
            Medal Distribution:
            - Gold: {len(filtered_df[filtered_df['Medal_Type'] == 'Gold'])}
            - Silver: {len(filtered_df[filtered_df['Medal_Type'] == 'Silver'])}
            - Bronze: {len(filtered_df[filtered_df['Medal_Type'] == 'Bronze'])}
            
            Top Performing Institute: {filtered_df.groupby('Institute')['Medal_Type'].apply(lambda x: sum(x.isin(['Gold', 'Silver', 'Bronze']))).idxmax()}
            """
            
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name=f"sports_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
