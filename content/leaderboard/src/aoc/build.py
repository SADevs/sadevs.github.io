import os
import json
import sys
import time
import requests
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
requests.packages.urllib3.disable_warnings()

here = os.path.abspath(os.path.dirname(__file__))

if not os.getenv('CI'):
    load_dotenv()

class AOCLoader():
    def __init__(self, aoc_year, aoc_session, aoc_id):
        self.aoc_year = aoc_year
        self.aoc_session = aoc_session
        self.aoc_id = aoc_id
        self.data = []

    def load(self):
        headers = {
            "content-type": "application/json",
            "Cookie": f"session={self.aoc_session}"
        }

        r = requests.post(
             f"https://adventofcode.com/{self.aoc_year}/leaderboard/private/view/{self.aoc_id}.json",
             headers=headers,
             verify=True)

        if r.status_code == 200:
            self.data = r.json()
            # print(json.dumps(self.data, sort_keys=True, indent=2))
        else:
            print (r.status_code)
            print (r.content)
            sys.exit(1)

    # def load_file(self, path):
    #     with open(path) as fh:
    #         self.data = json.load(fh)

    def get_owner_id(self):
        return self.data["owner_id"]

    def get_player(self, player_id):
        return self.data["members"][str(player_id)]

    def __str__(self):
        return json.dumps(self.data, sort_keys=True, indent=2)

    def get_active_players(self):
        return sorted(
            [player["id"] for player in self.data["members"].values() if player["stars"] > 0]
        )

    def get_all_players(self):
        return sorted([player["id"] for player in self.data["members"].values()])

    def get_star_times(self, player_id):
        times = []
        player = self.get_player(player_id)["completion_day_level"]
        for stars in player.values():
            for star in stars.values():
                times.append(star["get_star_ts"] * 1000)
        times.sort()
        return times

    def get_player_series(self):
        data = []
        ids = self.get_active_players()
        owner = self.get_owner_id()
        # print(ids)
        for player_id in ids:
            player = self.get_player(player_id)
            stars = self.get_star_times(player_id)

            name = player["name"] if player["name"] else f'Anon({str(player_id)[0:2]}*)'

            if player_id == owner:
                name = f'🎁 {name} 🎁'

            data.append({
                "name": name,
                "data": [[v, k+1] for k,v in enumerate(stars)],
                "local_score": player["local_score"],
                "total_stars": len(stars)
            })

        return data

    def get_last_star(self):
        times = []
        ids = self.get_active_players()
        for player_id in ids:
            times.append(max(self.get_star_times(player_id)))

        return max(times) if times else 0


def main():

    aoc_session = os.getenv('AOC_SESSION')
    aoc_year = os.getenv('AOC_YEAR')
    aoc_id = os.getenv('AOC_ID')

    if not aoc_session:
        print('Env Missing AOC_SESSION')
        sys.exit(1)

    if not aoc_year:
        print('Env Missing AOC_YEAR')
        sys.exit(1)

    if not aoc_id:
        print('Env Missing AOC_ID')
        sys.exit(1)

    aoc = AOCLoader(aoc_year, aoc_session, aoc_id)

    print(f'Building AoC Leaderboard Event: {aoc_year} Event ID: {aoc_id}')
    aoc.load()

    env = Environment(
        loader=FileSystemLoader(os.path.join(here, 'views')),
        extensions=['pypugjs.ext.jinja.PyPugJSExtension']
    )

    template = env.get_template('index.pug')

    out = template.render(
        title="SADevs AoC",
        title_text="SADevs AoC - Leader Board",
        last_star_found=aoc.get_last_star(),
        player_series_data=json.dumps(aoc.get_player_series()),
        built=time.time() * 1000,
        year=aoc_year,
    )

    artifact = os.path.abspath(os.path.join(here, '../../dist/index.html'))
    print(f'Rendering html template {artifact}')

    with open(artifact, encoding="utf-8", mode='w') as fhw:
        fhw.write(out)


if __name__ == '__main__':
    main()
