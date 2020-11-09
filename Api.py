import requests
import Consts


def _request(region,api_version,api_url,params={}):
    key = {'api_key' : Consts.api_key}
    response = requests.get(Consts.URL['base'].format(
            region=region,
            api=api_version,
            url=api_url
            ),
            params=key
        )
    print(response.url)
    return response.json()

def get_summoners(tier,division):
    api_url = Consts.URL['summoners_by_rank'].format(
        version = Consts.API_VERSIONS['league'],
        tier=tier,
        division=division
    )
    return _request('EUW1','league', api_url)

def match_lists_by_account(accountid):
    api_url = Consts.URL['match_lists_by_account'].format(
        version=Consts.API_VERSIONS['match'],
        accountid=accountid
    )
    return _request('EUW1', 'match', api_url)
