from balldontlie import BalldontlieAPI

api = BalldontlieAPI(api_key="fa43702b-b869-48a1-a860-e48771ac632b")
teams = api.nba.teams.list()
{
  "data": [
    {
      "id":1,
      "conference":"East",
      "division":"Southeast",
      "city":"Atlanta",
      "name":"Hawks",
      "full_name":"Atlanta Hawks",
      "abbreviation":"ATL"
    },
    ...
  ]
}