/*
 PROJET SQL : ANALYSE DE LA PERFORMANCE MARKETING
 Objectif : Analyser les commandes clients pour identifier les segments VIP.
 Base de données : PostgreSQL / MySQL compatible
*/

-- 1. CRÉATION DES TABLES (Pour contexte)
-- Table des clients
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    nom VARCHAR(100),
    date_inscription DATE
);

-- Table des commandes
CREATE TABLE commandes (
    commande_id INT PRIMARY KEY,
    client_id INT,
    montant DECIMAL(10, 2),
    date_commande DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- ============================================================
-- ANALYSE 1 : CALCUL DU PANIER MOYEN GLOBAL
-- ============================================================
SELECT 
    COUNT(commande_id) as total_commandes,
    SUM(montant) as revenus_totaux,
    ROUND(AVG(montant), 2) as panier_moyen
FROM commandes;

-- ============================================================
-- ANALYSE 2 : IDENTIFICATION DES CLIENTS "VIP"
-- Règle métier : Un VIP est un client ayant dépensé plus de 500€
-- ============================================================
SELECT 
    c.nom,
    COUNT(cmd.commande_id) as nombre_achats,
    SUM(cmd.montant) as depense_totale,
    CASE 
        WHEN SUM(cmd.montant) > 500 THEN 'VIP'
        WHEN SUM(cmd.montant) > 200 THEN 'Régulier'
        ELSE 'Nouveau'
    END as segment_client
FROM clients c
JOIN commandes cmd ON c.client_id = cmd.client_id
GROUP BY c.client_id, c.nom
ORDER BY depense_totale DESC;

-- ============================================================
-- ANALYSE 3 : VENTES PAR MOIS (Saisonnalité)
-- ============================================================
SELECT 
    EXTRACT(MONTH FROM date_commande) as mois,
    SUM(montant) as ca_mensuel
FROM commandes
GROUP BY mois
ORDER BY mois ASC;
