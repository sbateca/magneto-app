from mangum import Mangum

from app import web_app

app = web_app.create_app()

aws_lambda_handler = Mangum(app)
