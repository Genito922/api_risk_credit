from bankingsdk import DemandeClient, BankConfig

# 1. Définir l'URL de l'API (en production ou en local)
config = BankConfig(bank_base_url="https://api-risk-credit.onrender.com")
client = DemandeClient(config=config)

# 2. Health check
print("Health check:", client.health_check())

# 3. Récupérer une demande par son ID
demande = client.get_demande(1)
print("\n Demande ID 1:", demande.numero_demande)

# 4. Lister les 5 premieres demandes (au format pandas)
demandes_df = client.list_demandes(limit=5, output_format="pandas")
print("\n Liste de demandes (DataFrame):")
print(demandes_df)

# 5. Récupérer une agence
agence = client.get_agence(1)
print("\n Agence ID 1:", agence.numero_agence)

# 6. Lister les agences (au format pandas)
agences_df = client.list_agences(limit=100, output_format="pandas")
print("\n Liste des agences (DataFrame):")
print(agences_df)