from flask import Flask
from flask_cors import CORS
from config import MONGO_URL
from routes.employee_routes import employee_bp
from routes.error_routes import error_bp

app = Flask(__name__)
app.config['MONGO_URL'] = MONGO_URL
CORS(app)

app.register_blueprint(employee_bp)
app.register_blueprint(error_bp)

if __name__ == '__main__':
    app.run(debug=True)
