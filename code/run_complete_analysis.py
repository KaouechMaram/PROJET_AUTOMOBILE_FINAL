#!/usr/bin/env python3
"""
=============================================================================
LANCEUR ANALYSE AUTOMOBILE COMPLÈTE
=============================================================================

Ce script lance l'analyse automobile complète avec toutes les pages
d'analyses demandées par l'utilisateur.

Pages incluses:
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
- Navigation Principale

Auteur: Système d'Analyse Automobile Avancée
Date: Juillet 2025
Version: 2.0 - Version complète
=============================================================================
"""

import os
import sys
import webbrowser
from pathlib import Path

def main():
    """Fonction principale de lancement."""
    
    print("🚗 ANALYSE AUTOMOBILE COMPLÈTE - LANCEMENT")
    print("=" * 60)
    
    # Vérification de l'environnement
    print("📋 Vérification de l'environnement...")
    
    # Changement vers le répertoire du projet
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Vérification des dépendances
    try:
        import pandas as pd
        import numpy as np
        import plotly
        import xgboost
        from prophet import Prophet
        print("✅ Toutes les dépendances sont installées")
    except ImportError as e:
        print(f"❌ Dépendance manquante: {e}")
        print("💡 Installez les dépendances avec: pip install -r requirements.txt")
        return
    
    # Import de l'analyseur complet
    try:
        from automotive_analysis_complete import CompleteAutomotiveAnalysis
        print("✅ Module d'analyse importé avec succès")
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return
    
    # Création du dossier dashboards s'il n'existe pas
    dashboards_dir = Path("../dashboards")
    dashboards_dir.mkdir(exist_ok=True)
    
    # Lancement de l'analyse
    print("\n🚀 Lancement de l'analyse complète...")
    print("⏳ Cette opération peut prendre quelques minutes...")
    
    try:
        analyzer = CompleteAutomotiveAnalysis()
        analyzer.run_complete_analysis()
        
        print("\n🎉 ANALYSE COMPLÈTE TERMINÉE AVEC SUCCÈS!")
        print("=" * 60)
        
        # Affichage des fichiers créés
        print("\n📁 FICHIERS CRÉÉS:")
        dashboard_files = list(dashboards_dir.glob("*.html"))
        
        for i, file in enumerate(dashboard_files, 1):
            print(f"  {i:2d}. {file.name}")
        
        print(f"\n📊 Total: {len(dashboard_files)} dashboards créés")
        
        # Ouverture automatique de la page de navigation
        navigation_file = dashboards_dir / "dashboard_navigation.html"
        if navigation_file.exists():
            print(f"\n🌐 Ouverture de la page de navigation...")
            try:
                webbrowser.open(f"file://{navigation_file.absolute()}")
                print("✅ Page de navigation ouverte dans votre navigateur")
            except Exception as e:
                print(f"⚠️ Impossible d'ouvrir automatiquement: {e}")
                print(f"💡 Ouvrez manuellement: {navigation_file.absolute()}")
        
        # Instructions d'utilisation
        print("\n📖 INSTRUCTIONS D'UTILISATION:")
        print("1. Commencez par la page de navigation (dashboard_navigation.html)")
        print("2. Explorez les 15 pages d'analyses disponibles")
        print("3. Consultez les dashboards existants pour plus de détails")
        print("4. Utilisez les modèles ML pour vos propres analyses")
        
        print("\n🎯 PAGES PRINCIPALES:")
        print("🏠 Accueil: dashboard_accueil.html")
        print("📊 Exécutif: dashboard_executif_direction.html")
        print("🤖 ML: dashboard_modeles_ml.html")
        print("🌍 Géographique: dashboard_analyse_geographique_avancee.html")
        print("⚡ Transition VE: dashboard_transition_electrique.html")
        print("🏭 Fabricants: dashboard_fabricants_automobile.html")
        print("💰 Économique: dashboard_analyse_economique_strategique.html")
        print("🏆 Concurrence: dashboard_intelligence_concurrentielle.html")
        print("⚠️ Risques: dashboard_risques_opportunites.html")
        print("🦠 Post-COVID: dashboard_analyse_post_covid.html")
        print("🔋 VE Avancée: dashboard_transition_electrique_avancee.html")
        print("📋 Recommandations: dashboard_recommandations_strategiques.html")
        print("🏢 Sectorielle: dashboard_analyse_sectorielle.html")
        print("🔮 Prospective 2030: dashboard_prospective_2030.html")
        print("📈 Principal: dashboard_principal_automobile.html")
        
        print("\n✅ PROJET COMPLET ET PRÊT À L'UTILISATION!")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de l'analyse: {e}")
        print("💡 Vérifiez les logs pour plus de détails")
        return

if __name__ == "__main__":
    main() 