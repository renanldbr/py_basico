import os

pasta_principal = str(os.getcwd())
pastas = os.listdir()

#remove os arquivos das pastas
for pasta in pastas:
    if os.path.isdir(pasta) == True:
        os.chdir(pasta_principal+"\\"+f'{pasta}')
        pasta_arquivo = str(os.getcwd())
        arquivos = os.listdir()
        for arquivo in arquivos:
            os.replace(f'{pasta_arquivo}'+"\\"+f'{arquivo}',
                       f'{pasta_principal}'+"\\"+f'{arquivo}')
    os.chdir(pasta_principal)

#exclui as pastas onde os arquivos estavam
for pasta in pastas:
    if os.path.isdir(pasta) == True:
        os.rmdir(f'{os.getcwd()}'+"\\"+f'{pasta}')