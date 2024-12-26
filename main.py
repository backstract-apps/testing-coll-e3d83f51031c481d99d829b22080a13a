from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - testing-coll-e3d83f51031c481d99d829b22080a13a',debug=False,docs_url='/fervent-fermat-dff08c18c1e111ef9b270242ac12000559/docs',openapi_url='/fervent-fermat-dff08c18c1e111ef9b270242ac12000559/openapi.json')

app.include_router(router, prefix='/fervent-fermat-dff08c18c1e111ef9b270242ac12000559/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()