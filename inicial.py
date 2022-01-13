import requests
import sys
import os


def main():

    cep_input = sys.argv[1]
    cep_retorno_file = sys.argv[2]

    if len(cep_input) != 8:
        print('Quantidade de dígitos inválida!')
        exit()

    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if os.path.exists(cep_retorno_file):
        os.remove(cep_retorno_file)

    f = open(cep_retorno_file, "a")

    if 'erro' not in address_data:

        f.write('cep: {}'.format(address_data['cep'])+"\n")
        f.write('logradouro: {}'.format(address_data['logradouro'])+"\n")
        f.write('complemento: {}'.format(address_data['complemento'])+"\n")
        f.write('bairro: {}'.format(address_data['bairro'])+"\n")
        f.write('localidade: {}'.format(address_data['localidade'])+"\n")
        f.write('uf: {}'.format(address_data['uf'])+"\n")
        f.write('ibge: {}'.format(address_data['ibge'])+"\n")
        f.write('gia: {}'.format(address_data['gia'])+"\n")
        f.write('ddd: {}'.format(address_data['ddd'])+"\n")
        f.write('siafi: {}'.format(address_data['siafi']))

    else:
        f.write('error')

    f.close()
    print('Busca finalizada')


if __name__ == '__main__':
    main()
