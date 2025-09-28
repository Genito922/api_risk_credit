from fastapi import FastAPI, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional

from database import SessionLocal
import query_helpers as helpers
import schemas

# Initialisation FastAPI
app = FastAPI(
    title="Credit Risk API",
    description="API REST lecture seule pour BI & ML (Demandes, Clients, Agences, etc.)",
    version="0.2"
)

# Dépendance pour la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ========================================
# Health check
# ========================================
@app.get("/", summary="Vérifie si l'API fonctionne", tags=["monitoring"])
async def root():
    return {"message": "API Credit Risk opérationnelle"}


# ========================================
# Endpoints Demandes
# ========================================
@app.get(
    "/demandes/{demande_id}",
    summary="Obtenir une demande par son ID",
    response_model=schemas.DemandeDetailed,
    tags=["credits"],
)
def read_demande(demande_id: int = Path(...), db: Session = Depends(get_db)):
    demande = helpers.get_demande(db, demande_id)
    if not demande:
        raise HTTPException(status_code=404, detail=f"Demande {demande_id} non trouvée")
    return demande


@app.get(
    "/demandes",
    summary="Lister les demandes",
    response_model=List[schemas.DemandeSimple],
    tags=["credits"],
)
def list_demandes(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=1000),
    montant_operation: Optional[int] = Query(None),
    duree: Optional[int] = Query(None),
    date_de_demande: Optional[str] = Query(None),
    date_de_cloture: Optional[str] = Query(None),
    numero_client: Optional[int] = Query(None),
    accord: Optional[str] = Query(None),
    numero_agence: Optional[int] = Query(None),
    duree_de_traitement: Optional[int] = Query(None),
    code_accord: Optional[int] = Query(None),
    score_emprunteur: Optional[str] = Query(None),
    montant_prete: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    return helpers.get_demandes(
        db,
        skip=skip,
        limit=limit,
        montant_operation=montant_operation,
        duree=duree,
        date_de_demande=date_de_demande,
        date_de_cloture=date_de_cloture,
        numero_client=numero_client,
        accord=accord,
        numero_agence=numero_agence,
        duree_de_traitement=duree_de_traitement,
        code_accord=code_accord,
        score_emprunteur= score_emprunteur,
        montant_prete=montant_prete
    )


# ========================================
# Endpoints Agences
# ========================================
@app.get(
    "/agences",
    summary="Lister les agences",
    response_model=List[schemas.AgenceSimple],
    tags=["agences"],
)
def list_agences(skip: int = Query(0, ge=0), limit: int = Query(100, le=1000), db: Session = Depends(get_db)):
    return helpers.get_agences(db, skip=skip, limit=limit)


@app.get(
    "/agences/{agence_id}",
    summary="Obtenir une agence par son ID",
    response_model=schemas.AgenceSimple,
    tags=["agences"],
)
def read_agence(agence_id: int = Path(...), db: Session = Depends(get_db)):
    agence = helpers.get_agence(db, agence_id)
    if not agence:
        raise HTTPException(status_code=404, detail=f"Agence {agence_id} non trouvée")
    return agence


# ========================================
# Endpoints Situation Professionnelle
# ========================================
@app.get(
    "/situations_pro",
    summary="Lister les situations professionnelles",
    response_model=List[schemas.SituationProSimple],
    tags=["clients"],
)
def list_situations_pro(skip: int = Query(0, ge=0), limit: int = Query(100, le=1000), db: Session = Depends(get_db)):
    return helpers.get_situations_pro(db, skip=skip, limit=limit)


@app.get(
    "/situations_pro/{client_id}",
    summary="Obtenir une situation professionnelle par client",
    response_model=schemas.SituationProSimple,
    tags=["clients"],
)
def read_situation_pro(client_id: int = Path(...), db: Session = Depends(get_db)):
    sp = helpers.get_situation_pro(db, client_id)
    if not sp:
        raise HTTPException(status_code=404, detail=f"Situation pro du client {client_id} non trouvée")
    return sp


# ========================================
# Endpoints Situation Familiale
# ========================================
@app.get(
    "/situations_famille",
    summary="Lister les situations familiales",
    response_model=List[schemas.SituationFamilialeSimple],
    tags=["clients"],
)
def list_situations_famille(skip: int = Query(0, ge=0), limit: int = Query(100, le=1000), db: Session = Depends(get_db)):
    return helpers.get_situations_famille(db, skip=skip, limit=limit)


@app.get(
    "/situations_famille/{client_id}",
    summary="Obtenir une situation familiale par client",
    response_model=schemas.SituationFamilialeSimple,
    tags=["clients"],
)
def read_situation_famille(client_id: int = Path(...), db: Session = Depends(get_db)):
    sf = helpers.get_situation_famille(db, client_id)
    if not sf:
        raise HTTPException(status_code=404, detail=f"Situation familiale du client {client_id} non trouvée")
    return sf


# ========================================
# Endpoints Apports
# ========================================
@app.get(
    "/apports",
    summary="Lister les apports",
    response_model=List[schemas.ApportSimple],
    tags=["credits"],
)
def list_apports(skip: int = Query(0, ge=0), limit: int = Query(100, le=1000), db: Session = Depends(get_db)):
    return helpers.get_apports(db, skip=skip, limit=limit)


@app.get(
    "/apports/{demande_id}",
    summary="Obtenir un apport lié à une demande",
    response_model=schemas.ApportSimple,
    tags=["credits"],
)
def read_apport(demande_id: int = Path(...), db: Session = Depends(get_db)):
    apport = helpers.get_apport(db, demande_id)
    if not apport:
        raise HTTPException(status_code=404, detail=f"Apport pour demande {demande_id} non trouvé")
    return apport


# ========================================
# Endpoint ML / All demandes
# ========================================
@app.get("/all_demandes/", response_model=list[schemas.AllDBSimple])
def read_demandes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return helpers.get_all_demandes(db, skip=skip, limit=limit)

@app.get("/all_demandes/{numero_demande}", response_model=schemas.AllDBSimple)
def read_demande(numero_demande: int, db: Session = Depends(get_db)):
    db_demande = helpers.get_demande_by_id(db, numero_demande=numero_demande)
    if db_demande is None:
        return {"error": "Demande non trouvée"}
    return db_demande



# ========================================
# Endpoint Analytics
# ========================================
@app.get(
    "/analytics",
    summary="Obtenir les statistiques analytiques",
    response_model=schemas.AnalyticsResponse,
    tags=["analytics"]
)
def get_analytics(db: Session = Depends(get_db)):
    return schemas.AnalyticsResponse(
        demande_count=helpers.get_demande_count(db),
        agence_count=helpers.get_agence_count(db),
        situationpro_count=helpers.get_situationpro_count(db),
        situationfamille_count=helpers.get_situationfamille_count(db),
        apport_count=helpers.get_apport_count(db)
    )
