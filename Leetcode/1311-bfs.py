# Given your id and the level of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest.

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        # BFS to find level-degree friends
        queue = [id]
        count = 0
        seen = set(queue)

        while queue and count < level:
            count += 1
            layer = set()
            
            for ppl in queue:
                for f in friends[ppl]:
                    if f not in seen:
                        layer.add(f)
                        seen.add(f)
            
            queue = layer

        # Count movies to determine frequency
        movies = collections.defaultdict(int)
        for ppl in queue:
            for m in watchedVideos[ppl]:
                movies[m] += 1
        # Sort the movies by the frequency
        return [k for _, k in sorted((v, k) for k, v in movies.items())]