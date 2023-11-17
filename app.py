from flask import Flask, jsonify
from Config.config import Config
from utils.RespHelper import RespHelper
from Routes import ProductsRoutes
from waitress import serve
from flask_cors import CORS

app = Config.getApp()
CORS(app)
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
    # se usa esta forma de correr el servidor mientras se desarrolla ya que este se recarga automaticamente al guardar cambios el otro no
    app.run(port=Config.getConfigJson()["port"], debug=True)
    # print(
    #     f'Servidor iniciado en la ruta {Config.getConfigJson()["url-backend"]}:{Config.getConfigJson()["port"]}')
    # serve(app, host=Config.getConfigJson()[
    #       "url-backend"], port=Config.getConfigJson()["port"], debug=True)
