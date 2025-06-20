mais_tocadas_por_ano = {}
with open('spotify-2023.csv', 'r', encoding='latin-1') as f:
    linhas = f.readlines()
for linha in linhas[1:]:

    if '"' in linha:
        continue

    campos = linha.strip().split(',')

    try:
        track_name = campos[0]
        artist_name = campos[1]
        artist_count = int(campos[2])
        released_year = int(campos[3])
        streams = int(campos[8])  
    except (IndexError, ValueError):
        continue  
    if 2012 <= released_year <= 2022:
        atual = mais_tocadas_por_ano.get(released_year)
        if not atual or streams > atual[3]:
            mais_tocadas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

resultado = [mais_tocadas_por_ano[ano] for ano in sorted(mais_tocadas_por_ano)]

for item in resultado:
    print(item)