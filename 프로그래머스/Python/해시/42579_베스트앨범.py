# https://school.programmers.co.kr/learn/courses/30/lessons/42579

TOTAL_PLAY_KEY = "total_play"
IDX_LIST_KEY = "idx_list"
IDX_KEY = "index"
PLAY_KEY = "play_count"

def solution(genres, plays):
    result = []
    genre_dict = {}


    for idx, genre in enumerate(genres):
        play = plays[idx]

        if genre not in genre_dict:
            genre_dict[genre] = {
                TOTAL_PLAY_KEY: 0,
                IDX_LIST_KEY: []
            }

        genre_dict[genre][TOTAL_PLAY_KEY] += play
        genre_dict[genre][IDX_LIST_KEY].append({
            IDX_KEY: idx,
            PLAY_KEY: play
        })

    for genre in sorted(genre_dict.keys(), key=lambda x: genre_dict[x][TOTAL_PLAY_KEY], reverse=True):
        result.extend([x[IDX_KEY] for x in sorted(genre_dict[genre][IDX_LIST_KEY], key=lambda x: x[PLAY_KEY], reverse=True)][:2])
    return result

if __name__ == "__main__":
    param = {
        "genres": ["classic", "pop", "classic", "classic", "pop"],
		"plays": [500, 600, 150, 800, 2500]
    }
    result = [4, 1, 3, 0]
    print(solution(**param), result)