#
#
#
def get_sports_key_list(api_key, all='false'):

    sports_key_list = []

    response = requests.get(f'https://api.the-odds-api.com/v4/sports', params={
        'api_key': api_key, 'all': all})

    if response.status_code != 200:
        print(f"Error: Request returned status code {response.status_code}.")
        return sports_key_list

    sports_list = response.json()


    for sport_dict in sports_list:
        sports_key_list.append(sport_dict['key'])

    return sports_key_list
