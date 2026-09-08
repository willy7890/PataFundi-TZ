from sqlalchemy.orm import Session
from app.core.database import sessionlocal
from app.models.district import District
from app.models.regions import Region

districts = [

    # =========================
    # ARUSHA - TZ-1
    # =========================
    {"name": "Arusha", "region_code": "TZ-1"},
    {"name": "Arusha Urban", "region_code": "TZ-1"},
    {"name": "Karatu", "region_code": "TZ-1"},
    {"name": "Longido", "region_code": "TZ-1"},
    {"name": "Meru", "region_code": "TZ-1"},
    {"name": "Monduli", "region_code": "TZ-1"},
    {"name": "Ngorongoro", "region_code": "TZ-1"},

    # =========================
    # DAR ES SALAAM - TZ-2
    # =========================
    {"name": "Ilala", "region_code": "TZ-2"},
    {"name": "Kinondoni", "region_code": "TZ-2"},
    {"name": "Temeke", "region_code": "TZ-2"},

    # =========================
    # DODOMA - TZ-3
    # =========================
    {"name": "Bahi", "region_code": "TZ-3"},
    {"name": "Chamwino", "region_code": "TZ-3"},
    {"name": "Chemba", "region_code": "TZ-3"},
    {"name": "Dodoma Urban", "region_code": "TZ-3"},
    {"name": "Kondoa", "region_code": "TZ-3"},
    {"name": "Kongwa", "region_code": "TZ-3"},
    {"name": "Mpwapwa", "region_code": "TZ-3"},

    # =========================
    # IRINGA - TZ-4
    # =========================
    {"name": "Iringa", "region_code": "TZ-4"},
    {"name": "Iringa Urban", "region_code": "TZ-4"},
    {"name": "Kilolo", "region_code": "TZ-4"},
    {"name": "Mafinga Township Authority", "region_code": "TZ-4"},
    {"name": "Mufindi", "region_code": "TZ-4"},

    # =========================
    # KAGERA - TZ-5
    # =========================
    {"name": "Biharamulo", "region_code": "TZ-5"},
    {"name": "Bukoba", "region_code": "TZ-5"},
    {"name": "Bukoba Urban", "region_code": "TZ-5"},
    {"name": "Karagwe", "region_code": "TZ-5"},
    {"name": "Kyerwa", "region_code": "TZ-5"},
    {"name": "Missenyi", "region_code": "TZ-5"},
    {"name": "Muleba", "region_code": "TZ-5"},
    {"name": "Ngara", "region_code": "TZ-5"},

    # =========================
    # KASKAZINI PEMBA - TZ-6
    # =========================
    {"name": "Micheweni", "region_code": "TZ-6"},
    {"name": "Wete", "region_code": "TZ-6"},

    # =========================
    # KASKAZINI UNGUJA - TZ-7
    # =========================
    {"name": "Kaskazini A", "region_code": "TZ-7"},
    {"name": "Kaskazini B", "region_code": "TZ-7"},

    # =========================
    # KATAVI - TZ-28
    # =========================
    {"name": "Mlele", "region_code": "TZ-28"},
    {"name": "Mpanda", "region_code": "TZ-28"},
    {"name": "Mpanda Urban", "region_code": "TZ-28"},

    # =========================
    # KIGOMA - TZ-8
    # =========================
    {"name": "Buhigwe", "region_code": "TZ-8"},
    {"name": "Kakonko", "region_code": "TZ-8"},
    {"name": "Kasulu", "region_code": "TZ-8"},
    {"name": "Kasulu Township Authority", "region_code": "TZ-8"},
    {"name": "Kibondo", "region_code": "TZ-8"},
    {"name": "Kigoma", "region_code": "TZ-8"},
    {"name": "Kigoma Urban", "region_code": "TZ-8"},
    {"name": "Uvinza", "region_code": "TZ-8"},

    # =========================
    # KILIMANJARO - TZ-9
    # =========================
    {"name": "Hai", "region_code": "TZ-9"},
    {"name": "Moshi", "region_code": "TZ-9"},
    {"name": "Moshi Urban", "region_code": "TZ-9"},
    {"name": "Mwanga", "region_code": "TZ-9"},
    {"name": "Rombo", "region_code": "TZ-9"},
    {"name": "Same", "region_code": "TZ-9"},
    {"name": "Siha", "region_code": "TZ-9"},

    # =========================
    # KUSINI PEMBA - TZ-10
    # =========================
    {"name": "Chake Chake", "region_code": "TZ-10"},
    {"name": "Mkoani", "region_code": "TZ-10"},

    # =========================
    # KUSINI UNGUJA - TZ-11
    # =========================
    {"name": "Kati", "region_code": "TZ-11"},
    {"name": "Kusini", "region_code": "TZ-11"},

    # =========================
    # LINDI - TZ-12
    # =========================
    {"name": "Kilwa", "region_code": "TZ-12"},
    {"name": "Lindi", "region_code": "TZ-12"},
    {"name": "Lindi Urban", "region_code": "TZ-12"},
    {"name": "Liwale", "region_code": "TZ-12"},
    {"name": "Nachingwea", "region_code": "TZ-12"},
    {"name": "Ruangwa", "region_code": "TZ-12"},

    # =========================
    # MANYARA - TZ-26
    # =========================
    {"name": "Babati", "region_code": "TZ-26"},
    {"name": "Babati Urban", "region_code": "TZ-26"},
    {"name": "Hanang", "region_code": "TZ-26"},
    {"name": "Kiteto", "region_code": "TZ-26"},
    {"name": "Mbulu", "region_code": "TZ-26"},
    {"name": "Simanjiro", "region_code": "TZ-26"},

    # =========================
    # GEITA - TZ-27
    # =========================

    {"name": "Bukombe", "region_code": "TZ-27"},
    {"name": "Chato", "region_code": "TZ-27"},
    {"name": "Geita", "region_code": "TZ-27"},
    {"name": "Geita Town Council", "region_code": "TZ-27"},
    {"name": "Mbogwe", "region_code": "TZ-27"},
    {"name": "Nyang'hwale", "region_code": "TZ-27"},
    # =========================
    # MARA - TZ-13
    # =========================
    {"name": "Bunda", "region_code": "TZ-13"},
    {"name": "Butiama", "region_code": "TZ-13"},
    {"name": "Musoma", "region_code": "TZ-13"},
    {"name": "Musoma Urban", "region_code": "TZ-13"},
    {"name": "Rorya", "region_code": "TZ-13"},
    {"name": "Serengeti", "region_code": "TZ-13"},
    {"name": "Tarime", "region_code": "TZ-13"},

    # =========================
    # MBEYA - TZ-14
    # =========================
    {"name": "Chunya", "region_code": "TZ-14"},
    {"name": "Kyela", "region_code": "TZ-14"},
    {"name": "Mbarali", "region_code": "TZ-14"},
    {"name": "Mbeya", "region_code": "TZ-14"},
    {"name": "Mbeya Urban", "region_code": "TZ-14"},
    {"name": "Rungwe", "region_code": "TZ-14"},

    # =========================
    # MJINI MAGHARIBI - TZ-15
    # =========================
    {"name": "Magharibi", "region_code": "TZ-15"},
    {"name": "Mjini", "region_code": "TZ-15"},

    # =========================
    # MOROGORO - TZ-16
    # =========================
    {"name": "Gairo", "region_code": "TZ-16"},
    {"name": "Kilombero", "region_code": "TZ-16"},
    {"name": "Kilosa", "region_code": "TZ-16"},
    {"name": "Morogoro", "region_code": "TZ-16"},
    {"name": "Morogoro Urban", "region_code": "TZ-16"},
    {"name": "Mvomero", "region_code": "TZ-16"},
    {"name": "Ulanga", "region_code": "TZ-16"},

    # =========================
    # MTWARA - TZ-17
    # =========================
    {"name": "Masasi", "region_code": "TZ-17"},
    {"name": "Masasi Township Authority", "region_code": "TZ-17"},
    {"name": "Mtwara", "region_code": "TZ-17"},
    {"name": "Mtwara Urban", "region_code": "TZ-17"},
    {"name": "Nanyumbu", "region_code": "TZ-17"},
    {"name": "Newala", "region_code": "TZ-17"},
    {"name": "Tandahimba", "region_code": "TZ-17"},

    # =========================
    # MWANZA - TZ-18
    # =========================
    {"name": "Ilemela", "region_code": "TZ-18"},
    {"name": "Kwimba", "region_code": "TZ-18"},
    {"name": "Magu", "region_code": "TZ-18"},
    {"name": "Misungwi", "region_code": "TZ-18"},
    {"name": "Nyamagana", "region_code": "TZ-18"},
    {"name": "Sengerema", "region_code": "TZ-18"},
    {"name": "Ukerewe", "region_code": "TZ-18"},

    # =========================
    # NJOMBE - TZ-29
    # =========================
    {"name": "Ludewa", "region_code": "TZ-29"},
    {"name": "Makambako Township Authority", "region_code": "TZ-29"},
    {"name": "Makete", "region_code": "TZ-29"},
    {"name": "Njombe", "region_code": "TZ-29"},
    {"name": "Njombe Urban", "region_code": "TZ-29"},
    {"name": "Wanging'ombe", "region_code": "TZ-29"},

    # =========================
    # PWANI - TZ-19
    # =========================
    {"name": "Bagamoyo", "region_code": "TZ-19"},
    {"name": "Kibaha", "region_code": "TZ-19"},
    {"name": "Kibaha Urban", "region_code": "TZ-19"},
    {"name": "Kisarawe", "region_code": "TZ-19"},
    {"name": "Mafia", "region_code": "TZ-19"},
    {"name": "Mkuranga", "region_code": "TZ-19"},
    {"name": "Rufiji", "region_code": "TZ-19"},

    # =========================
    # RUKWA - TZ-20
    # =========================
    {"name": "Kalambo", "region_code": "TZ-20"},
    {"name": "Nkasi", "region_code": "TZ-20"},
    {"name": "Sumbawanga", "region_code": "TZ-20"},
    {"name": "Sumbawanga Urban", "region_code": "TZ-20"},

    # =========================
    # RUVUMA - TZ-21
    # =========================
    {"name": "Mbinga", "region_code": "TZ-21"},
    {"name": "Namtumbo", "region_code": "TZ-21"},
    {"name": "Nyasa", "region_code": "TZ-21"},
    {"name": "Songea", "region_code": "TZ-21"},
    {"name": "Songea Urban", "region_code": "TZ-21"},
    {"name": "Tunduru", "region_code": "TZ-21"},

    # =========================
    # SHINYANGA - TZ-22
    # =========================
    {"name": "Kahama", "region_code": "TZ-22"},
    {"name": "Kahama Township Authority", "region_code": "TZ-22"},
    {"name": "Kishapu", "region_code": "TZ-22"},
    {"name": "Shinyanga", "region_code": "TZ-22"},
    {"name": "Shinyanga Urban", "region_code": "TZ-22"},

    # =========================
    # SIMIYU - TZ-30
    # =========================
    {"name": "Bariadi", "region_code": "TZ-30"},
    {"name": "Busega", "region_code": "TZ-30"},
    {"name": "Itilima", "region_code": "TZ-30"},
    {"name": "Maswa", "region_code": "TZ-30"},
    {"name": "Meatu", "region_code": "TZ-30"},

    # =========================
    # SINGIDA - TZ-23
    # =========================
    {"name": "Ikungi", "region_code": "TZ-23"},
    {"name": "Iramba", "region_code": "TZ-23"},
    {"name": "Manyoni", "region_code": "TZ-23"},
    {"name": "Mkalama", "region_code": "TZ-23"},
    {"name": "Singida", "region_code": "TZ-23"},
    {"name": "Singida Urban", "region_code": "TZ-23"},

    # =========================
    # SONGWE - TZ-31
    # =========================
    {"name": "Ileje", "region_code": "TZ-31"},
    {"name": "Mbozi", "region_code": "TZ-31"},
    {"name": "Momba", "region_code": "TZ-31"},
    {"name": "Songwe", "region_code": "TZ-31"},
    {"name": "Tunduma", "region_code": "TZ-31"},

    # =========================
    # TABORA - TZ-24
    # =========================
    {"name": "Igunga", "region_code": "TZ-24"},
    {"name": "Kaliua", "region_code": "TZ-24"},
    {"name": "Nzega", "region_code": "TZ-24"},
    {"name": "Sikonge ", "region_code": "TZ-24"},
    {"name": "Tabora Urban", "region_code": "TZ-24"},
    {"name": "Urambo", "region_code": "TZ-24"},
    {"name": "Uyui", "region_code": "TZ-24"},

    # =========================
    # TANGA - TZ-25
    # =========================
    {"name": "Handeni", "region_code": "TZ-25"},
    {"name": "Handeni Mji", "region_code": "TZ-25"},
    {"name": "Kilindi", "region_code": "TZ-25"},
    {"name": "Korogwe", "region_code": "TZ-25"},
    {"name": "Korogwe Township Authority", "region_code": "TZ-25"},
    {"name": "Lushoto", "region_code": "TZ-25"},
    {"name": "Mkinga", "region_code": "TZ-25"},
    {"name": "Muheza", "region_code": "TZ-25"},
    {"name": "Pangani", "region_code": "TZ-25"},
    {"name": "Tanga Urban", "region_code": "TZ-25"},
]

def seed_district(db: Session):
    for data in districts:

        region = (
            db.query(Region)
            .filter(Region.code == data["region_code"])
            .first()
        )

        if not region:
            print(f'{data["region_code"]} region code not found')
            continue

        existing = (
            db.query(District)
            .filter(
                District.name == data["name"],
                District.region_id == region.id
            )
            .first()
        )

        if not existing:
            district = District(
                name=data["name"],
                region_id=region.id
            )

            db.add(district)

    db.commit()

db= sessionlocal()           
try:
    seed_district(db)
finally:
    db.close()
    
            