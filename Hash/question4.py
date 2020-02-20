"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며,
노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항

genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

"""
from operator import itemgetter

def solution(genres, plays):
    album_dict = {}
    total_genre = {}
    best_album = []

    index = 0
    for genre, play in zip(genres, plays):
        album_dict[genre] = album_dict.get(genre, []) + [(play, -index)]
        total_genre[genre] = total_genre.get(genre, 0) + play
        index += 1

    # sort
    for key in album_dict.keys():
        album_dict[key].sort(key=itemgetter(0, 1), reverse=True)

    total_genre = dict(sorted(total_genre.items(), key=lambda x: x[1], reverse=True))

    # make best_album
    for key in total_genre.keys():
        if len(album_dict[key]) == 1:
            best_album.append(album_dict[key].pop(0)[1])
            continue
        else:
            best_album.append(album_dict[key].pop(0)[1])
            best_album.append(album_dict[key].pop(0)[1])

    # 정렬의 일관화를 위해 - 부호를 붙였던 고유번호를 다시 돌린다
    best_album = [abs(x) for x in best_album]

    return best_album

print(solution(['classic','pop','classic','pop','classic','classic'] , [400,600,150,2500,500,500]))