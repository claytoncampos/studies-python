import requests 

def retorna_dados_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    print(response.status_code)

    data = response.json()
    print(data)
    input('tete')
    return data


def retorna_response(url):
    response = requests.get(url)
    return response.text
    

if __name__ == '__main__':
    entrada_cep = int(input('Entre com o CEP: '))
    retorna_dados_cep(entrada_cep)
    # response = retorna_response('https://claytoncampos.netlify.app/')
    # print(response)
    input()



