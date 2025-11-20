import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. CRÉATION D'UN JEU DE DONNÉES FICTIF ---
# Pour cet exemple, je génère des données de ventes simulées
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Produit': np.random.choice(['Laptop', 'Souris', 'Clavier', 'Écran'], 100),
    'Prix_Unitaire': np.random.choice([800, 25, 45, 200], 100),
    'Quantité': np.random.randint(1, 5, 100)
}

df = pd.DataFrame(data)

# Ajustement des prix pour qu'ils correspondent aux produits (Nettoyage simulé)
prix_map = {'Laptop': 800, 'Souris': 25, 'Clavier': 45, 'Écran': 200}
df['Prix_Unitaire'] = df['Produit'].map(prix_map)

# --- 2. ANALYSE EXPLORATOIRE (EDA) ---

# Calcul du Chiffre d'Affaires (CA) par ligne
df['Chiffre_Affaires'] = df['Prix_Unitaire'] * df['Quantité']

print("--- APERÇU DES DONNÉES ---")
print(df.head())

# KPI 1 : Chiffre d'affaires total
total_ca = df['Chiffre_Affaires'].sum()
print(f"\n💰 Chiffre d'Affaires Total : {total_ca} €")

# KPI 2 : Meilleur produit (en termes de CA)
top_produit = df.groupby('Produit')['Chiffre_Affaires'].sum().sort_values(ascending=False)
print("\n🏆 Classement des produits par revenus :")
print(top_produit)

# --- 3. VISUALISATION (Code pour générer un graphique) ---
# Note : Dans un notebook Jupyter, le graphique s'afficherait directement.

plt.figure(figsize=(10, 6))
top_produit.plot(kind='bar', color='skyblue')
plt.title('Chiffre d\'Affaires par Produit')
plt.xlabel('Produit')
plt.ylabel('CA (€)')
plt.xticks(rotation=45)
plt.tight_layout()
print("\n📊 Graphique généré avec succès (voir output).")
# plt.show() # Décommenter pour afficher si exécuté en local
