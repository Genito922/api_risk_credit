"""SQLAlchemy models"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Demande(Base):
    __tablename__ = "demandes"

    numero_demande = Column(Integer, primary_key=True, index=True)
    montant_operation = Column(Integer)
    duree = Column(Integer, index=True)
    numero_client = Column(Integer, ForeignKey("situation_pro.numero_client"))
    accord = Column(String)
    numero_agence = Column(Integer, ForeignKey("agences.numero_agence"))
    duree_de_traitement = Column(Integer, index=True)
    code_accord = Column(Integer)

    # Relations
    agence = relationship("Agence", back_populates="demandes")  # One-to-Many: une agence a plusieurs demandes
    client = relationship("SituationPro", back_populates="demandes")  # One-to-Many: un client peut avoir plusieurs demandes
    apport = relationship("Apport", uselist=False, back_populates="demande")  # One-to-One: une demande a un seul apport


class Agence(Base):
    __tablename__ = "agences"

    numero_agence = Column(Integer, primary_key=True, index=True)
    ville = Column(String)
    adresse = Column(String)

    # Relations
    demandes = relationship("Demande", back_populates="agence")  # One-to-Many inverse


class SituationPro(Base):
    __tablename__ = "situation_pro"

    numero_client = Column(Integer, primary_key=True, index=True)
    revenu_mensuel_moyen = Column(Integer)
    code_regularite_revenus = Column(Integer)
    regularite_des_revenus = Column(String)
    code_statut_emploi = Column(Integer)
    regularite_emploi = Column(String)

    # Relations
    demandes = relationship("Demande", back_populates="client")  # One-to-Many inverse
    famille = relationship("SituationFamille", uselist=False, back_populates="client")  # One-to-One: un client a une seule situation familiale


class SituationFamille(Base):
    __tablename__ = "situation_famille"

    numero_client = Column(Integer, ForeignKey("situation_pro.numero_client"), primary_key=True, index=True)
    statut_familliale = Column(String)
    nombre_enfants = Column(Integer)
    age = Column(Integer)
    nom_client = Column(String)
    statut_activite = Column(String)

    # Relation
    client = relationship("SituationPro", back_populates="famille")  # One-to-One inverse


class Apport(Base):
    __tablename__ = "apports"

    numero_demande = Column(Integer, ForeignKey("demandes.numero_demande"), primary_key=True, index=True)
    apport = Column(Integer)

    # Relation
    demande = relationship("Demande", back_populates="apport")  # One-to-One inverse


from sqlalchemy import Column, Integer, String
from .database import Base

class All_demande(Base):
    __tablename__ = "all_demandes"

    numero_demande = Column(Integer, primary_key=True, index=True)
    montant_operation = Column(Integer)
    duree = Column(Integer)
    numero_client = Column(Integer)
    accord = Column(String)
    numero_agence = Column(Integer)
    duree_de_traitement = Column(Integer)
    code_accord = Column(Integer)
    apport = Column(Integer)
    revenu_mensuel_moyen = Column(Integer)
    code_regularite_revenus = Column(Integer)
    regularite_des_revenus = Column(String)
    code_statut_emploi = Column(Integer)
    regularite_emploi = Column(String)
    situation_familliale = Column(String)
    nombre_enfants = Column(Integer)
    age = Column(Integer)
    nom_client = Column(String)
    statut_activite = Column(String)
    ville = Column(String)
    adresse = Column(String)
