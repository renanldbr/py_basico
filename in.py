import os

arquivos =[]
pastas = []

itens = os.listdir()

#identifica se é um arquivo ou pasta
for item in itens:
    info = os.path.isfile(item)
    if info == True and item[item.find('.'):] != '.py' :
        arquivos.append(item)
    elif info == False and item[item.find('.'):] != '.py':
        pastas.append(item)

#cria pastas para cada tipo de arquivo
for arquivo in arquivos:
    if arquivo[arquivo.find('.')+1:] not in pastas:
        os.mkdir(arquivo[arquivo.find('.')+1:])
        pastas.append(arquivo[arquivo.find('.')+1:])

#envia cada arquivo para suas respectivas pastas
for arquivo in arquivos:
    org_arquivo = os.getcwd()+"\\"+arquivo
    dst_arquivo = os.getcwd()+"\\"+arquivo[arquivo.find('.')+1:]+"\\"+arquivo
    os.replace(org_arquivo, dst_arquivo)

