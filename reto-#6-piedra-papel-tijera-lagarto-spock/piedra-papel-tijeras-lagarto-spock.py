def piedra_papel_tijeras_lagarto_spock(games):
    
    reglas = {"✊": ["✌", "🤏"],
                "🤚": ["✊", "🖖"],
                "🖖": ["✊", "✌"],
                "✌": ["🤚", "🤏"],
                "🤏": ["🖖", "🤚"]}
    
    jugador_uno = 0
    jugador_dos = 0
    
    for game in games:
        jugador_uno_jugado = game[0]
        jugador_dos_jugado = game[1]
        if jugador_uno_jugado != jugador_dos_jugado:
            if jugador_dos_jugado in reglas[jugador_uno_jugado]:
                jugador_uno += 1
            else : jugador_dos += 1
            
    
    return  "Empate" if jugador_uno == jugador_dos else "Jugador 1" if jugador_uno > jugador_dos else "Jugador 2" 

print(piedra_papel_tijeras_lagarto_spock([("✌", "✌")]))