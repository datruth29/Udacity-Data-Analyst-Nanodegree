# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print("requesting {}".format(r.url))

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        print(data)


def _main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    artist_id = results["artists"][1]["id"]
    print("\nARTIST:")
    pretty_print(results["artists"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print("\nONE RELEASE:")
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]

    print("\nALL TITLES:")
    for t in release_titles:
        print(t)


def main():
    q1_result = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    pretty_print("How many bands named 'First Aid Kit'? - {}".format(q1_result))

    q2_result = query_by_name(ARTIST_URL, query_type['simple'], "Queen")
    pretty_print("begin_area name for Queen? - {}".format(q2_result['artists'][0]['begin-area']['name']))

    q3_artist_id = query_by_name(ARTIST_URL, query_type['simple'], 'Beatles')['artists'][0]['id']
    q3_result = query_site(ARTIST_URL, query_type['aliases'], q3_artist_id)['aliases'][5]['name']
    pretty_print("Spanish Alias for the Beatles? - {}".format(q3_result))

    q4_result = query_by_name(ARTIST_URL, query_type['simple'], 'Nirvana')['artists'][0]['disambiguation']
    pretty_print("Nirvana disambiguation? - {}".format(q4_result))

    q5_result = query_by_name(ARTIST_URL, query_type['simple'], 'One Direction')['artists'][0]['life-span']['begin']
    print("When was One Direction formed? - {}".format(q5_result))

if __name__ == '__main__':
    main()
