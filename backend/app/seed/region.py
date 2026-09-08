from sqlalchemy.orm import Session
from app.models.regions import Region
from app.core.database import sessionlocal
from datetime import datetime

regions=[
    {"name":"Arusha","code":"TZ-1"},
    {"name":"Dar es salaam","code":"TZ-2"},
    {"name":"Dodoma","code":"TZ-3"},
    {"name":"Geita","code":"TZ-27"},
    {"name":"Iringa","code":"TZ-4"},
    {"name":"Kagera","code":"TZ-5"},
    {"name":"Kaskazini pemba","code":"TZ-6"},
    {"name":"kaskazini unguja","code":"TZ-7"},
    {"name":"katavi","code":"TZ-28"},
    {"name":"kigoma","code":"TZ-8"},
    {"name":"kilimanjaro","code":"TZ-9"},
    {"name":"Kusini pemba","code":"TZ-10"},
    {"name":"Kusini unguja","code":"TZ-11"},
    {"name":"Lindi","code":"TZ-12"},
    {"name":"Manyara","code":"TZ-26"},
    {"name":"Mara","code":"TZ-13"},
    {"name":"Mbeya","code":"TZ-14"},
    {"name":"Mjini Mgararibi","code":"TZ-15"},
    {"name":"Morogoro","code":"TZ-16"},
    {"name":"Mtwara","code":"TZ-17"},
    {"name":"Mwanza","code":"TZ-18"},
    {"name":"Njombe","code":"TZ-29"},
    {"name":"Pwani","code":"TZ-19"},
    {"name":"Rukwa","code":"TZ-20"},
    {"name":"Ruvuma","code":"TZ-21"},
    {"name":"Shinyanga","code":"TZ-22"},
    {"name":"Simiyu","code":"TZ-30"},
    {"name":"Singida","code":"TZ-23"},
    {"name":"Songwe","code":"TZ-31"},
    {"name":"Tabora","code":"TZ-24"},
    {"name":"Tanga","code":"TZ-25"},
]

def seed_regions(db:Session):
    for data in regions:
        existing=db.query(Region).filter(Region.code==data["code"]).first()
        if existing:
            existing.code=data["code"],
            existing.name=data["name"],
            existing.created_at=datetime.now()
            
        if not existing:
            region=Region(
                name=data["name"],
                code=data["code"]
            )
            db.add(region)
        
    db.commit()
        
db=sessionlocal()
try:
    seed_regions(db)      
finally:
         db.close()