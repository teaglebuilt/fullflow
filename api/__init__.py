from fastapi import FastAPI


api = FastAPI()


@api.get('/api/tenants')
def get_tenants():
    pass

@api.post('/api/tenant/deploy')
def deploy():
    pass

@api.put('/api/tenant/update')
def update_deployment():
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8000)
