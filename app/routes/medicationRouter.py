# app/routes/medicationRouter.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.medication import Medication
from app.controller.auth import get_current_user
from app.database import get_db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class MedicationCreate(BaseModel):
    name: str
    dosage: str
    frequency: str
    start_date: datetime
    end_date: datetime
    notes: str | None = None

@router.post("/add")
async def add_medication(medication: MedicationCreate, current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    db_medication = Medication(**medication.memory_dump(), user_id=current_user.id)
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return {"message": "Medication added successfully"}

@router.get("/list")
async def list_medications(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    medications = db.query(Medication).filter(Medication.user_id == current_user.id).all()
    return medications

@router.delete("/delete/{medication_id}")
async def delete_medication(medication_id: int, current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    db_medication = db.query(Medication).filter(Medication.id == medication_id, Medication.user_id == current_user.id).first()
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(db_medication)
    db.commit()
    return {"message": "Medication deleted successfully"}
