idade = int(input("digite sua idade"))

if 18 <= idade <= 70:
    print("voto Registrado!")
elif (16 <= idade < 18) or (idade > 70):
    print("voto opcional")
else:
    print("voto negado!!!")
  