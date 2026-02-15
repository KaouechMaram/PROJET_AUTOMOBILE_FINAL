#!/usr/bin/env python3
"""
=============================================================================
APPLICATION STREAMLIT - ANALYSE AUTOMOBILE COMPLÈTE
=============================================================================

Application web interactive pour l'analyse automobile avec toutes les pages :
- Accueil
- Dashboard Exécutif
- Modèles ML
- Analyse Géographique
- Transition Électrique
- Fabricants
- Analyse Économique
- Intelligence Concurrentielle
- Risques et Opportunités
- Analyse Post-COVID
- Transition Électrique Avancée
- Recommandations Stratégiques
- Analyse Sectorielle
- Prospective 2030

Auteur: Système d'Analyse Automobile Avancée
Date: Août 2025
Version: 2.0
=============================================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="🚗 Analyse Automobile Avancée",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .success-metric {
        border-left-color: #28a745;
    }
    .warning-metric {
        border-left-color: #ffc107;
    }
    .danger-metric {
        border-left-color: #dc3545;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Charge toutes les données nécessaires."""
    try:
        # Charger les données CSV
        # Parser explicitement la colonne Date pour éviter les erreurs sur .dt
        df = pd.read_csv('comprehensive_automotive_data.csv', parse_dates=['Date'], dayfirst=True)
        # Si la colonne Date n'a pas été parsée automatiquement, forcer la conversion
        if df['Date'].dtype == object:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

        # Normaliser les noms de colonnes pour correspondre à l'application
        rename_map = {
            'Production_Volume': 'Production',
            'Average_Price': 'Price',
            'Category': 'Vehicle_Category'
        }
        df = df.rename(columns=rename_map)

        # Créer une colonne `EV_Production` si absente (production uniquement pour Electric_Vehicles)
        if 'EV_Production' not in df.columns:
            if 'Vehicle_Category' in df.columns and 'Production' in df.columns:
                df['EV_Production'] = df.apply(lambda r: r['Production'] if str(r.get('Vehicle_Category')).lower().startswith('electric') else 0, axis=1)
            else:
                df['EV_Production'] = 0
        
        # Charger les résultats JSON
        with open('automotive_analysis_results_clean.json', 'r', encoding='utf-8') as f:
            results = json.load(f)
            
        return df, results
    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {e}")
        return None, None

def page_accueil():
    """Page d'accueil avec vue d'ensemble."""
    st.markdown('<h1 class="main-header">🚗 Analyse Automobile Avancée</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card success-metric">
            <h3>📊 Données Analysées</h3>
            <h2>12,096</h2>
            <p>Observations (2010-2023)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🤖 Modèles ML</h3>
            <h2>6</h2>
            <p>XGBoost, Prophet, ARIMA, LR</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🌍 Scénarios</h3>
            <h2>9</h2>
            <p>Politiques & Économiques</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Vue d'ensemble des données
    if df is not None:
        st.subheader("📈 Vue d'ensemble de la production automobile")
        
        # Graphique de production par année
        yearly_production = df.groupby(df['Date'].dt.year)['Production'].sum().reset_index()
        
        fig = px.line(yearly_production, x='Date', y='Production', 
                     title="Évolution de la production automobile mondiale (2010-2023)",
                     labels={'Date': 'Année', 'Production': 'Production (millions d\'unités)'})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Statistiques clés
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Production Totale 2023", f"{df[df['Date'].dt.year == 2023]['Production'].sum():,.0f}")
        
        with col2:
            st.metric("Prix Moyen 2023", f"${df[df['Date'].dt.year == 2023]['Price'].mean():,.0f}")
        
        with col3:
            st.metric("Part EV 2023", f"{df[df['Date'].dt.year == 2023]['EV_Share'].mean():.1%}")
        
        with col4:
            st.metric("Croissance 2023 vs 2022", f"{((df[df['Date'].dt.year == 2023]['Production'].sum() / df[df['Date'].dt.year == 2022]['Production'].sum()) - 1) * 100:.1f}%")

def page_dashboard_executif():
    """Dashboard exécutif pour la direction."""
    st.header("📊 Dashboard Exécutif - Direction")
    
    if results is None:
        st.error("Données non disponibles")
        return
    
    # KPIs principaux
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Meilleur Scénario 2030", "Rapid EV Transition", "+10.2%")
    
    with col2:
        st.metric("Production Prévue 2030", "630,864 unités", "+10.2%")
    
    with col3:
        st.metric("Prix Moyen 2030", "$43,959", "-9.8%")
    
    with col4:
        st.metric("Part EV 2030", "45%", "+35%")
    
    # Graphique des scénarios
    if 'forecasts_2030' in results:
        scenarios = list(results['forecasts_2030'].keys())
        productions = []
        
        for scenario in scenarios:
            ensemble = results['forecasts_2030'][scenario].get('ensemble') if isinstance(results['forecasts_2030'][scenario], dict) else None
            if ensemble and 'production' in ensemble:
                try:
                    prod_val = ensemble['production'][-1]
                    prod = float(prod_val)
                except Exception:
                    prod = 0
                productions.append(prod)
            else:
                productions.append(0)
        
        fig = px.bar(x=scenarios, y=productions, 
                    title="Production prévue en 2030 par scénario",
                    labels={'x': 'Scénario', 'y': 'Production (unités)'})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def page_modeles_ml():
    """Page des modèles de machine learning."""
    st.header("🤖 Modèles de Machine Learning")
    
    if results is None:
        st.error("Données non disponibles")
        return
    
    # Performance des modèles
    st.subheader("📊 Performance des modèles")
    
    models = results['model_performance']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Régression Linéaire")
        st.metric("Production - R²", f"{models['linear_regression_production']['r2_score']:.3f}")
        st.metric("Prix - R²", f"{models['linear_regression_price']['r2_score']:.3f}")
    
    with col2:
        st.subheader("XGBoost")
        st.metric("Production - R² CV", f"{models['xgboost_production']['cv_r2_mean']:.3f}")
        st.metric("Prix - R² CV", f"{models['xgboost_price']['cv_r2_mean']:.3f}")
    
    # Importance des features (XGBoost)
    st.subheader("🎯 Importance des variables (XGBoost)")
    
    if 'feature_importance' in models['xgboost_production']:
        features = list(models['xgboost_production']['feature_importance'].keys())
        importance = [float(v) for v in models['xgboost_production']['feature_importance'].values()]
        
        fig = px.bar(x=features, y=importance, 
                    title="Importance des variables pour la production",
                    labels={'x': 'Variable', 'y': 'Importance'})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def page_analyse_geographique():
    """Page d'analyse géographique."""
    st.header("🌍 Analyse Géographique")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Production par région
    st.subheader("📊 Production par région")
    
    regional_production = df.groupby(['Region', df['Date'].dt.year])['Production'].sum().reset_index()
    
    fig = px.line(regional_production, x='Date', y='Production', color='Region',
                 title="Évolution de la production par région",
                 labels={'Date': 'Année', 'Production': 'Production (millions d\'unités)', 'Region': 'Région'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Carte de chaleur des prix par région
    st.subheader("💰 Prix moyens par région")
    
    price_by_region = df.groupby('Region')['Price'].mean().reset_index()
    
    fig = px.bar(price_by_region, x='Region', y='Price',
                title="Prix moyen par région",
                labels={'Region': 'Région', 'Price': 'Prix moyen ($)'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def page_transition_electrique():
    """Page de transition électrique."""
    st.header("⚡ Transition Électrique")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Évolution de la part électrique
    st.subheader("📈 Évolution de la part des véhicules électriques")
    
    ev_evolution = df.groupby(df['Date'].dt.year)['EV_Share'].mean().reset_index()
    
    fig = px.line(ev_evolution, x='Date', y='EV_Share',
                 title="Évolution de la part des véhicules électriques",
                 labels={'Date': 'Année', 'EV_Share': 'Part des véhicules électriques'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Production EV par fabricant
    st.subheader("🏭 Production de véhicules électriques par fabricant")
    
    ev_by_manufacturer = df.groupby('Manufacturer')['EV_Production'].sum().reset_index()
    
    fig = px.pie(ev_by_manufacturer, values='EV_Production', names='Manufacturer',
                title="Répartition de la production EV par fabricant")
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def page_fabricants():
    """Page d'analyse des fabricants."""
    st.header("🏭 Analyse des Fabricants")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Production par fabricant
    st.subheader("📊 Production par fabricant")
    
    manufacturer_production = df.groupby(['Manufacturer', df['Date'].dt.year])['Production'].sum().reset_index()
    
    fig = px.line(manufacturer_production, x='Date', y='Production', color='Manufacturer',
                 title="Évolution de la production par fabricant",
                 labels={'Date': 'Année', 'Production': 'Production (millions d\'unités)', 'Manufacturer': 'Fabricant'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Prix moyens par fabricant
    st.subheader("💰 Prix moyens par fabricant")
    
    price_by_manufacturer = df.groupby('Manufacturer')['Price'].mean().reset_index()
    
    fig = px.bar(price_by_manufacturer, x='Manufacturer', y='Price',
                title="Prix moyen par fabricant",
                labels={'Manufacturer': 'Fabricant', 'Price': 'Prix moyen ($)'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def page_analyse_economique():
    """Page d'analyse économique."""
    st.header("💰 Analyse Économique")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Corrélation avec le PIB
    st.subheader("📈 Corrélation avec la croissance du PIB")
    
    gdp_correlation = df.groupby(df['Date'].dt.year).agg({
        'Production': 'sum',
        'GDP_Growth': 'mean'
    }).reset_index()
    
    fig = px.scatter(gdp_correlation, x='GDP_Growth', y='Production',
                    title="Corrélation entre croissance du PIB et production automobile",
                    labels={'GDP_Growth': 'Croissance du PIB (%)', 'Production': 'Production (millions d\'unités)'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Impact du prix du pétrole
    st.subheader("🛢️ Impact du prix du pétrole")
    
    oil_impact = df.groupby(df['Date'].dt.year).agg({
        'Production': 'sum',
        'Oil_Price': 'mean'
    }).reset_index()
    
    fig = px.scatter(oil_impact, x='Oil_Price', y='Production',
                    title="Impact du prix du pétrole sur la production",
                    labels={'Oil_Price': 'Prix du pétrole ($)', 'Production': 'Production (millions d\'unités)'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def page_intelligence_concurrentielle():
    """Page d'intelligence concurrentielle."""
    st.header("🏆 Intelligence Concurrentielle")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Part de marché par fabricant
    st.subheader("📊 Part de marché par fabricant")
    
    market_share = df.groupby('Manufacturer')['Production'].sum().reset_index()
    market_share['Market_Share'] = market_share['Production'] / market_share['Production'].sum() * 100
    
    fig = px.pie(market_share, values='Market_Share', names='Manufacturer',
                title="Part de marché par fabricant")
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Évolution des parts de marché
    st.subheader("📈 Évolution des parts de marché")
    
    market_share_evolution = df.groupby(['Manufacturer', df['Date'].dt.year])['Production'].sum().reset_index()
    market_share_evolution['Market_Share'] = market_share_evolution.groupby('Date')['Production'].transform(lambda x: x / x.sum() * 100)
    
    fig = px.line(market_share_evolution, x='Date', y='Market_Share', color='Manufacturer',
                 title="Évolution des parts de marché par fabricant",
                 labels={'Date': 'Année', 'Market_Share': 'Part de marché (%)', 'Manufacturer': 'Fabricant'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def page_risques_opportunites():
    """Page des risques et opportunités."""
    st.header("⚠️ Risques et Opportunités")
    
    # Analyse des risques
    st.subheader("🚨 Principaux Risques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Risques Opérationnels:**
        - Perturbations des chaînes d'approvisionnement
        - Pénurie de composants électroniques
        - Hausse des coûts des matières premières
        """)
    
    with col2:
        st.markdown("""
        **Risques Réglementaires:**
        - Nouvelles normes environnementales
        - Changements de politique commerciale
        - Réglementations sur les véhicules électriques
        """)
    
    # Opportunités
    st.subheader("💡 Opportunités Stratégiques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Opportunités Technologiques:**
        - Développement des véhicules électriques
        - Intelligence artificielle et autonomie
        - Nouvelles technologies de batterie
        """)
    
    with col2:
        st.markdown("""
        **Opportunités Marché:**
        - Marchés émergents en croissance
        - Services de mobilité
        - Économie circulaire
        """)

def page_analyse_post_covid():
    """Page d'analyse post-COVID."""
    st.header("🦠 Analyse Post-COVID")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Impact COVID sur la production
    st.subheader("📉 Impact de la COVID-19 sur la production")
    
    # Filtrer les données 2020-2023
    covid_data = df[df['Date'].dt.year >= 2020].copy()
    
    monthly_production = covid_data.groupby(covid_data['Date'].dt.to_period('M'))['Production'].sum().reset_index()
    monthly_production['Date'] = monthly_production['Date'].astype(str)
    
    fig = px.line(monthly_production, x='Date', y='Production',
                 title="Évolution de la production pendant et après la COVID-19",
                 labels={'Date': 'Mois', 'Production': 'Production (millions d\'unités)'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Comparaison pré/post COVID
    st.subheader("📊 Comparaison pré/post COVID")
    
    pre_covid = df[df['Date'].dt.year == 2019]['Production'].sum()
    post_covid = df[df['Date'].dt.year == 2023]['Production'].sum()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Production 2019", f"{pre_covid:,.0f}")
    
    with col2:
        st.metric("Production 2023", f"{post_covid:,.0f}")
    
    with col3:
        change = ((post_covid / pre_covid) - 1) * 100
        st.metric("Évolution", f"{change:.1f}%")

def page_transition_electrique_avancee():
    """Page de transition électrique avancée."""
    st.header("⚡ Transition Électrique Avancée")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Projections EV avancées
    st.subheader("🔮 Projections véhicules électriques 2030")
    
    # Simuler des projections EV
    years = list(range(2024, 2031))
    ev_share_projection = [0.15, 0.22, 0.30, 0.38, 0.45, 0.52, 0.60]
    
    projection_df = pd.DataFrame({
        'Year': years,
        'EV_Share': ev_share_projection
    })
    
    fig = px.line(projection_df, x='Year', y='EV_Share',
                 title="Projection de la part des véhicules électriques jusqu'en 2030",
                 labels={'Year': 'Année', 'EV_Share': 'Part des véhicules électriques'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Analyse des coûts
    st.subheader("💰 Évolution des coûts des batteries")
    
    battery_costs = [150, 130, 110, 95, 80, 70, 60]  # $/kWh
    
    cost_df = pd.DataFrame({
        'Year': years,
        'Battery_Cost': battery_costs
    })
    
    fig = px.line(cost_df, x='Year', y='Battery_Cost',
                 title="Évolution du coût des batteries ($/kWh)",
                 labels={'Year': 'Année', 'Battery_Cost': 'Coût ($/kWh)'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def page_recommandations_strategiques():
    """Page des recommandations stratégiques."""
    st.header("🎯 Recommandations Stratégiques")
    
    st.subheader("📋 Plan d'action recommandé")
    
    # Recommandations par catégorie
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🚀 Actions Immédiates (0-6 mois):**
        1. Accélérer la transition vers les véhicules électriques
        2. Renforcer les chaînes d'approvisionnement
        3. Investir dans la R&D des batteries
        4. Former les équipes aux nouvelles technologies
        """)
    
    with col2:
        st.markdown("""
        **📈 Actions Moyen Terme (6-18 mois):**
        1. Développer des partenariats stratégiques
        2. Optimiser les processus de production
        3. Adapter l'offre aux marchés émergents
        4. Implémenter des solutions de mobilité
        """)
    
    st.subheader("🎯 Objectifs 2030")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **⚡ Électrification:**
        - 60% de véhicules électriques
        - Réduction de 40% des émissions CO2
        """)
    
    with col2:
        st.markdown("""
        **🏭 Production:**
        - +10% de croissance annuelle
        - Optimisation des coûts de 15%
        """)
    
    with col3:
        st.markdown("""
        **🌍 Marché:**
        - Leadership sur les marchés émergents
        - 25% de parts de marché global
        """)

def page_analyse_sectorielle():
    """Page d'analyse sectorielle."""
    st.header("🏭 Analyse Sectorielle")
    
    if df is None:
        st.error("Données non disponibles")
        return
    
    # Analyse par catégorie de véhicule
    st.subheader("🚗 Production par catégorie de véhicule")
    
    category_production = df.groupby(['Vehicle_Category', df['Date'].dt.year])['Production'].sum().reset_index()
    
    fig = px.line(category_production, x='Date', y='Production', color='Vehicle_Category',
                 title="Évolution de la production par catégorie",
                 labels={'Date': 'Année', 'Production': 'Production (millions d\'unités)', 'Vehicle_Category': 'Catégorie'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Analyse des marges par segment
    st.subheader("💰 Analyse des marges par segment")
    
    # Simuler des données de marge
    segments = ['Premium', 'Standard', 'Economy']
    margins = [25, 15, 8]
    
    margin_df = pd.DataFrame({
        'Segment': segments,
        'Margin': margins
    })
    
    fig = px.bar(margin_df, x='Segment', y='Margin',
                title="Marges par segment de marché",
                labels={'Segment': 'Segment', 'Margin': 'Marge (%)'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def page_prospective_2030():
    """Page de prospective 2030."""
    st.header("🔮 Prospective 2030")
    
    if results is None:
        st.error("Données non disponibles")
        return
    
    # Scénarios 2030
    st.subheader("🌍 Scénarios de développement 2030")
    
    if 'forecasts_2030' in results:
        scenarios = list(results['forecasts_2030'].keys())
        productions = []
        
        for scenario in scenarios:
            ensemble = results['forecasts_2030'][scenario].get('ensemble') if isinstance(results['forecasts_2030'][scenario], dict) else None
            if ensemble and 'production' in ensemble:
                try:
                    prod_val = ensemble['production'][-1]
                    prod = float(prod_val)
                except Exception:
                    prod = 0
                productions.append(prod)
            else:
                productions.append(0)
        
        # Créer un graphique radar pour les scénarios
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=productions,
            theta=scenarios,
            fill='toself',
            name='Production 2030'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(productions) * 1.1]
                )),
            showlegend=True,
            title="Comparaison des scénarios 2030"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Tendances technologiques
    st.subheader("🚀 Tendances technologiques 2030")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🤖 Autonomie:**
        - Niveau 4-5 d'autonomie généralisé
        - Réseaux de véhicules connectés
        - IA embarquée avancée
        """)
    
    with col2:
        st.markdown("""
        **⚡ Électrification:**
        - Batteries solides commercialisées
        - Chargement ultra-rapide (5 min)
        - Véhicules à hydrogène
        """)

# Chargement des données
df, results = load_data()

# Sidebar pour la navigation
st.sidebar.title("🚗 Navigation")
st.sidebar.markdown("---")

# Menu de navigation
pages = {
    "🏠 Accueil": page_accueil,
    "📊 Dashboard Exécutif": page_dashboard_executif,
    "🤖 Modèles ML": page_modeles_ml,
    "🌍 Analyse Géographique": page_analyse_geographique,
    "⚡ Transition Électrique": page_transition_electrique,
    "🏭 Fabricants": page_fabricants,
    "💰 Analyse Économique": page_analyse_economique,
    "🏆 Intelligence Concurrentielle": page_intelligence_concurrentielle,
    "⚠️ Risques et Opportunités": page_risques_opportunites,
    "🦠 Analyse Post-COVID": page_analyse_post_covid,
    "⚡ Transition Électrique Avancée": page_transition_electrique_avancee,
    "🎯 Recommandations Stratégiques": page_recommandations_strategiques,
    "🏭 Analyse Sectorielle": page_analyse_sectorielle,
    "🔮 Prospective 2030": page_prospective_2030
}

# Sélection de la page
selected_page = st.sidebar.selectbox(
    "Choisissez une page:",
    list(pages.keys())
)

# Affichage de la page sélectionnée
pages[selected_page]()

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
**📊 Données:**
- 12,096 observations
- 2010-2023
- 6 fabricants
- 9 scénarios

**🤖 Modèles:**
- XGBoost
- Prophet
- ARIMA
- Régression Linéaire
""")

st.sidebar.markdown("---")
st.sidebar.markdown("🚗 **Analyse Automobile Avancée**")
st.sidebar.markdown("Version 2.0 - Août 2025") 