{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04877865-2f63-402b-a4d5-04a0f3968ffc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-------------------- Locadora de Veículos LocAqui --------------------\n",
      "[1] Consultar Portifólio \n",
      "[2] Alugar Carros \n",
      "[3] Devolver Carros \n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Qual operação deseja realizar?  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "[2] Aluguel de Carros: \n",
      "[1] Chevrolet Tracker - R$120/dia\n",
      "[2] Chevrolet Onix - R$90/dia\n",
      "[3] Chevrolet Spin - R$120/dia\n",
      "[4] Hyundai HB20 - R$85/dia\n",
      "[5] Hyundai Tucson - R$120/dia\n",
      "[6] Fiat Uno - R$60/dia\n",
      "[7] Fiat Mobi - R$70/dia\n",
      "[8] Fiat Pulse - R$130/dia\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Selecione o modelo desejado:  3\n",
      "Quantos dias deseja ficar com o carro?  2\n",
      "O aluguel do veículo Chevrolet Spin totalizará R$240 por 2 dias. Deseja confirmar? [S]Sim [N]Não s\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Parabéns, Você alugou o carro Chevrolet Spin por 2 dias\n",
      "\n",
      "-------------------- Locadora de Veículos LocAqui --------------------\n",
      "[1] Consultar Portifólio \n",
      "[2] Alugar Carros \n",
      "[3] Devolver Carros \n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Qual operação deseja realizar?  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "[3] Devolução de Carros: \n",
      "\n",
      "[1] Chevrolet Spin\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Qual carro deseja devolver?  1\n",
      "Tem certeza que deseja devolver o veículo Chevrolet Spin [S]Sim [N]Não s\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Parabéns Você devolveu o carro Chevrolet Spin\n",
      "\n",
      "-------------------- Locadora de Veículos LocAqui --------------------\n",
      "[1] Consultar Portifólio \n",
      "[2] Alugar Carros \n",
      "[3] Devolver Carros \n",
      "\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "carros_disponiveis = [\n",
    "            {'modelo':'Chevrolet Tracker',    'preço':120},\n",
    "            {'modelo':'Chevrolet Onix',       'preço':90},\n",
    "            {'modelo':'Chevrolet Spin',       'preço':120},\n",
    "            {'modelo':'Hyundai HB20',         'preço':85}, \n",
    "            {'modelo':'Hyundai Tucson',       'preço':120},\n",
    "            {'modelo':'Fiat Uno',             'preço':60},\n",
    "            {'modelo':'Fiat Mobi',            'preço':70},\n",
    "            {'modelo':'Fiat Pulse',           'preço':130}\n",
    "                      ]\n",
    "carros_alugados = []\n",
    "\n",
    "while True:\n",
    "  print(20*'-','Locadora de Veículos LocAqui',20*'-')\n",
    "  print('[1] Consultar Portifólio', '\\n'\n",
    "        '[2] Alugar Carros','\\n'\n",
    "        '[3] Devolver Carros','\\n')\n",
    "\n",
    "  op = int(input('Qual operação deseja realizar? '))\n",
    "  os.system('cls')  \n",
    "  if op == 1:\n",
    "      print('\\n'\n",
    "            '[1] Consulta de Portifólio: '\n",
    "            '\\n')\n",
    "      i = 1\n",
    "      for carro in carros_disponiveis:\n",
    "        print(f'[{i}] {carro[\"modelo\"]} - R${carro[\"preço\"]}/dia')\n",
    "        i +=1\n",
    "            \n",
    "  elif op == 2:\n",
    "    confirmaçao = 'S'\n",
    "    while confirmaçao == 'S':\n",
    "      print('\\n'\n",
    "            '[2] Aluguel de Carros: ')\n",
    "      i = 1\n",
    "      for carro in carros_disponiveis:\n",
    "        print(f'[{i}] {carro[\"modelo\"]} - R${carro[\"preço\"]}/dia')\n",
    "        i += 1\n",
    "      escolha = int(input('Selecione o modelo desejado: '))\n",
    "      preço = carros_disponiveis[escolha-1]['preço']\n",
    "      periodo = int(input('Quantos dias deseja ficar com o carro? '))\n",
    "      valor = preço * periodo\n",
    "      confirmaçao = input(f'O aluguel do veículo {carros_disponiveis[escolha-1][\"modelo\"]} totalizará R${valor} por {periodo} dias. Deseja confirmar? [S]Sim [N]Não').upper()\n",
    "      while confirmaçao not in 'SN':\n",
    "        confirmaçao = input(f'O aluguel do veículo {carros_disponiveis[escolha-1][\"modelo\"]} totalizará R${valor} por {periodo} dias. Deseja confirmar? [S]Sim [N]Não').upper()\n",
    "      if confirmaçao == 'S':\n",
    "        print('\\n'\n",
    "            f'Parabéns, Você alugou o carro {carros_disponiveis[escolha-1][\"modelo\"]} por {periodo} dias'\n",
    "             '\\n')\n",
    "        carros_alugados.append(carros_disponiveis[escolha-1].copy())\n",
    "        carros_disponiveis.pop(escolha-1)\n",
    "        confirmaçao = 'N'\n",
    "      else:\n",
    "        confirmaçao = 'N'\n",
    "      \n",
    "  else:\n",
    "    print('\\n'\n",
    "          '[3] Devolução de Carros: \\n')\n",
    "    i = 1\n",
    "    for carro in carros_alugados:\n",
    "        print(f'[{i}] {carro[\"modelo\"]}')\n",
    "        i += 1\n",
    "    devolver = int(input('Qual carro deseja devolver? '))\n",
    "    confirmacao = input(f'Tem certeza que deseja devolver o veículo {carros_alugados[devolver-1][\"modelo\"]} [S]Sim [N]Não').upper()\n",
    "    while confirmacao not in 'SN':\n",
    "        confirmacao = input(f'Tem certeza que deseja devolver o veículo {carros_alugados[devolver-1][\"modelo\"]}? [S]Sim [N]Não').upper()\n",
    "    if confirmacao == 'S':\n",
    "        print('\\n'\n",
    "\t      f'Parabéns Você devolveu o veículo {carros_alugados[devolver-1][\"modelo\"]}'\n",
    "              '\\n')\n",
    "        carros_disponiveis.append(carros_alugados[devolver-1])\n",
    "        carros_alugados.pop(devolver-1)\n",
    "    else:\n",
    "        confirmaçao = 'N'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f129f2eb-53d4-4bb2-8ad6-13fdf97753f9",
   "metadata": {},
   "source": [
    "## "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6515caa3-a533-4337-80ee-70baa92ec0b2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "110cb2b0-6244-47b0-911c-fb823cb367e3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
