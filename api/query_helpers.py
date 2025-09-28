"""SQLAlchemy Query Functions for Credit Scoring"""
from sqlalchemy.orm import Session, joinedload
from typing import Optional, List
import schemas
import models


# =========================
# Demandes
# =========================
def get_demande(db: Session, demande_id: int):
    """Récupère une demande de prêt par son ID avec ses relations One-to-One."""
    return (
        db.query(models.Demande)
        .options(
            joinedload(models.Demande.agence),
            joinedload(models.Demande.client),
            joinedload(models.Demande.apport)
        )
        .filter(models.Demande.numero_demande == demande_id)
        .first()
    )


def get_demandes(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    montant_operation: Optional[int] = None,
    duree: Optional[int] = None,
    date_de_demande: Optional[str] = None,
    date_de_cloture: Optional[str] = None,
    numero_client: Optional[int] = None,
    accord: Optional[str] = None,
    numero_agence: Optional[int] = None,
    duree_de_traitement: Optional[int] = None,
    code_accord: Optional[int] = None,
    score_emprunteur:Optional[str] = None,
    montant_prete: Optional[int] = None
):
    """Récupère une liste de demandes avec filtres optionnels et relations One-to-One."""
    query = db.query(models.Demande).options(
        joinedload(models.Demande.agence),
        joinedload(models.Demande.client),
        joinedload(models.Demande.apport)
    )

    if montant_operation is not None:
        query = query.filter(models.Demande.montant_operation == montant_operation)
    if duree is not None:
        query = query.filter(models.Demande.duree == duree)
    if date_de_demande is not None:
        query = query.filter(models.Demande.date_de_demande == date_de_demande) 
    if date_de_cloture is not None:
        query = query.filter(models.Demande.date_de_cloture == date_de_cloture)
    if numero_client is not None:
        query = query.filter(models.Demande.numero_client == numero_client)
    if accord is not None:
        query = query.filter(models.Demande.accord.ilike(f"%{accord}%"))
    if numero_agence is not None:
        query = query.filter(models.Demande.numero_agence == numero_agence)
    if duree_de_traitement is not None:
        query = query.filter(models.Demande.duree_de_traitement == duree_de_traitement)
    if code_accord is not None:
        query = query.filter(models.Demande.code_accord == code_accord)
    if score_emprunteur is not None:
        query = query.filter(models.Demande.score_emprunteur == score_emprunteur)        
    if montant_prete is not None:
        query = query.filter(models.Demande.montant_prete == montant_prete)

    return query.offset(skip).limit(limit).all()


# =========================
# Agences
# =========================
def get_agence(db: Session, agence_id: int):
    """Récupère l'information sur une agence par son numero d'agence."""
    return db.query(models.Agence).filter(models.Agence.numero_agence == agence_id).first()


def get_agences(db: Session, skip: int = 0, limit: int = 100):
    """Récupère une liste d'agences."""
    query = db.query(models.Agence)
    return query.offset(skip).limit(limit).all()


# =========================
# Situation Pro
# =========================
def get_situation_pro(db: Session, client_id: int):
    """Récupère l'information sur la situation professionnelle d'un client par son numero client."""
    return db.query(models.SituationPro).filter(models.SituationPro.numero_client == client_id).first()


def get_situations_pro(db: Session, skip: int = 0, limit: int = 100):
    """Récupère une liste de situations professionnelles."""
    query = db.query(models.SituationPro)
    return query.offset(skip).limit(limit).all()


# =========================
# Situation Famille
# =========================
def get_situation_famille(db: Session, client_id: int):
    """Récupère l'information sur la situation familiale d'un client par son numero client."""
    return db.query(models.SituationFamille).filter(models.SituationFamille.numero_client == client_id).first()


def get_situations_famille(db: Session, skip: int = 0, limit: int = 100):
    """Récupère une liste de situations familiales."""
    query = db.query(models.SituationFamille)
    return query.offset(skip).limit(limit).all()


# =========================
# Apports
# =========================
def get_apport(db: Session, demande_id: int):
    """Récupère l'apport lié à une demande (One-to-One)."""
    return db.query(models.Apport).filter(models.Apport.numero_demande == demande_id).first()


def get_apports(db: Session, skip: int = 0, limit: int = 100):
    """Récupère une liste d'apports."""
    query = db.query(models.Apport)
    return query.offset(skip).limit(limit).all()

# =========================
# ML dataset
# =========================

def get_all_demandes(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.AllDBSimple]:
    return db.query(models.AllDB).offset(skip).limit(limit).all()

def get_demande_by_id(db: Session, numero_demande: int) -> schemas.AllDBSimple | None:
    return db.query(models.AllDB).filter(models.AllDB.numero_demande == numero_demande).first()


# =========================
# Analytics
# =========================
def get_agence_count(db: Session):
    return db.query(models.Agence).count()

def get_demande_count(db: Session):
    return db.query(models.Demande).count()

def get_situationpro_count(db: Session):
    return db.query(models.SituationPro).count()

def get_situationfamille_count(db: Session):
    return db.query(models.SituationFamille).count()

def get_apport_count(db: Session):
    return db.query(models.Apport).count()

