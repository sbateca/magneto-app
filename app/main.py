from mangum import Mangum

from app import web_app

app = web_app.create_app()


@app.get("/")
def health_check() -> dict:
    return {"Message": "MagnetoApp is running!"}


aws_lambda_handler = Mangum(app)
