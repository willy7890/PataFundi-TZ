from fastapi import FastAPI
from app.core.config import settings
from app.routers import auth,customer,region,district,ward,street

app=FastAPI(title=settings.APP_NAME)


app.include_router(auth.router)
app.include_router(customer.router)
app.include_router(region.router)
app.include_router(district.router)
app.include_router(ward.router)
app.include_router(street.router)

@app.get("/health")
def checkhealth():
    return{
        "message":"welcome to pata fundi plaform✅✅💰"
    } 