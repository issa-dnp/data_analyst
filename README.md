# 📊 Portfolio Data Analyst

Bienvenue sur mon dépôt de projets ! Ici, je centralise mes travaux d'analyse de données, montrant ma capacité à résoudre des problématiques business avec **Python** et **SQL**.

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## 🚀 Mes Projets

Voici une vue d'ensemble de mes analyses. Cliquez sur le nom du projet pour voir le code.

| Projet | Description | Compétences Clés | Lien Code |
| :--- | :--- | :--- | :---: |
| **1. Analyse des Ventes** | Simulation de ventes produits, calcul de CA et identification des top produits. | `Python` `Pandas` `Cleaning` | [Voir le dossier](./projet_1_python_ventes) |
| **2. Performance Marketing** | Analyse SQL pour segmenter les clients (VIP vs Standard) et suivre les KPI. | `SQL` `Joins` `GROUP BY` | [Voir le dossier](./projet_2_sql_marketing) |

---

## 📂 Détails techniques des projets

### 🐍 Projet 1 : Analyse des Ventes (Python)
*Scénario : Une entreprise souhaite comprendre la répartition de son chiffre d'affaires.*
*   **Données :** Générées via script (Simulation).
*   **Processus :**
    1.  Nettoyage des données (prix incohérents).
    2.  Calcul du Chiffre d'Affaires total.
    3.  Classement des produits.
*   **Extrait de code :**
    ```python
    # Exemple de calcul KPI
    top_produit = df.groupby('Produit')['Chiffre_Affaires'].sum()
    ```

### 🗄️ Projet 2 : Segmentation Client (SQL)
*Scénario : Le département marketing veut cibler les meilleurs clients.*
*   **Processus :**
    1.  Jointure entre tables `Clients` et `Commandes`.
    2.  Création d'une logique conditionnelle (`CASE WHEN`) pour définir le statut VIP.
*   **Extrait de requête :**
    ```sql
    CASE 
        WHEN SUM(amount) > 500 THEN 'VIP'
        ELSE 'Standard'
    END as segment
    ```

---

## 📫 Me Contacter

Je suis ouvert aux opportunités en Data Analysis.

*   💼 **LinkedIn** : [Ton Lien LinkedIn ici](https://www.linkedin.com/)
*   📧 **Email** : [ton-email@exemple.com](mailto:ton-email@exemple.com)

---
*Ce portfolio est hébergé sur GitHub et maintenu par [Ton Nom].*
