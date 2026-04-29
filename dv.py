def ball(ball_dontlie):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    https://www.balldontlie.io/openapi/nba.yml