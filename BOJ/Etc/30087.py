seminar_room = {
    "Algorithm": "204",
    "DataAnalysis": "207",
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": 501,
    "TestStrategy": 105,
}

N = int(input())

for _ in range(N):
    seminar = input().strip()
    print(seminar_room[seminar])
