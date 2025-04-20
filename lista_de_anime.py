
animes = {

    "1" : {

    "nome" : "Black Lagoon",
    "gêneros" : "ação, seinen",
    "autor" : "Rei Hiroe",
    "estúdio de animação": "Madhouse" ,
    "Diretor" : "Sunao Katabuchi"

    },

    "2" : {

    "nome" : "Darker Than Black: Kuro No Keiyakusha",
    "gêneros" : "ação, mistério, superpoder",
    "autor" : "Tensai Okamura",
    "estúdio de animação" : "Bones",
    "Diretor" : "Tensai Okamura"

    },

    "3" : {
        
    "nome" : "Sangatsu no Lion",
    "gêneros" : "Drama, Romance, Slice of Life",
    "autor" : "Chica Umino",
    "estúdio de animação" : "shaft",
    "Diretor" : "Kenjiro Okada, Akiyuki Shinbo"

    },

    "4" : {

    "nome" : "Sword Art Online: Alicization",
    "gêneros" : "Ação, Aventura, Fantasia, Jogos, Romance",
    "autor" : "Reki Kawahara",
    "estúdio de animação" : "A-1 Pictures",
    "Diretor" : "Manabu Ono"

    },

    "5" : {

    "nome" : "Akagami No Shirayuki-hime",
    "gêneros" : "Comédia, Drama, Fantasia, Romance, Shoujo",
    "autor" : "Akizuti Sorata",
    "estúdio de animação" : "Bones",
    "Diretor" : "Masahiro Ando"

    },

    "6" : {

    "nome" : "Akatsuki no Yona",
    "gêneros" : "Ação, Comédia, Fantasia, Romance, Shoujo",
    "autor" : "Mizuho Kusanagi",
    "estúdio de animação" : "Pierrot",
    "Diretor" : "Kazuhiro Yoneda"

    },

    "7" : {

    "nome" : "Clannad",
    "gêneros" : "Comédia, Drama, Harém, Romance, Vida escolar",
    "autor" : "Key (story), Shaa (art)",
    "estúdio de animação" : "Kyoto Animation",
    "Diretor" : "Tatsuya Ishihara"

    }

}

print("Anime List")
print("Escolha um anime para ver as informações:")
print("1 - Black Lagoon")
print("2 - Darker Than Black: Kuro No Keiyakusha")
print("3 - Sangatsu no Lion")   
print("4 - Sword Art Online: Alicization")
print("5 - Akagami No Shirayuki-hime")
print("6 - Akatsuki no Yona")
print("7 - Clannad")
print("0 - Sair")

escolha = input("Digite o número do anime: ")

if escolha == "0":
    print("Saindo...")
elif escolha in animes:
    anime = animes[escolha]
    print(f"Nome: {anime['nome']}")
    print(f"Gêneros: {anime['gêneros']}")
    print(f"Autor: {anime['autor']}")
    print(f"Estúdio de Animação: {anime['estúdio de animação']}")
    print(f"Diretor: {anime['Diretor']}")
else:
    print("Anime não encontrado.")

    