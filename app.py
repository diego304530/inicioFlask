from flask import Flask, jsonify
from Config.config import Config
from utils.RespHelper import RespHelper
from Routes import ProductsRoutes

app = Config.getApp()
app.register_blueprint(ProductsRoutes.productRoutes)


@app.route("/")
def home():
    return RespHelper.jsonResp("api Flask funcionando", [], 200), 200


@app.errorhandler(404)
def notFound(error):
    return RespHelper.jsonResp('Ruta no encontrada', [], 404), 404


@app.errorhandler(400)
def routeError(error):
    return RespHelper.jsonResp('Peticion incorrecta', [], 400), 400


@app.errorhandler(405)
def incompleteRoute(error):
    return RespHelper.jsonResp('Faltan elementos en la ruta solicitada', [], 405), 405


if __name__ == "__main__":
    app.run(debug=True, port=Config.getConfigJson()["port"])
