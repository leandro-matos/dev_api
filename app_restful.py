from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
         'id':'0',
         'nome':'Leandro',
        'habilidades':['Python', 'Flask','Nginx']
    },
    {
        'id':'1',
        'nome':'Matos',
        'habilidades':['Docker', 'Kubernetes','Terraform']
    },
    {
        'id': '2',
        'nome': 'Pereira',
        'habilidades': ['Ansible', 'Puppet', 'Packer']
    },
]

#######################################################################################################################
# Devolve um desenvolver pelo seu número do seu ID. Altera e também deleta um desenvolvedor.
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

#######################################################################################################################
# Lista todos os desenvolvedores no sistema. Permite registrar um novo desenvolvedor
class listaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(listaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)