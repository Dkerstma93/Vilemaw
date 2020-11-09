import Api as api
import time

def main():
    tier_list = ['IRON', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']
    division_list = ['IV','III','II','I']
    summonerids = []

    for i in tier_list:
        for j in division_list:
            data = api.get_summoners(i,j)
            for x in data:
                summonerids.append(x['summonerId'])
            time.sleep(1)

    print(summonerids)

if __name__ == "__main__":
    main()
