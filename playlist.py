import heapq
from random import randrange

def getPlaylist(songsIds, ratings):
  l = len(songsIds)
  modifiedRatings = {}
  for key in ratings.keys():
    rating = ratings[key]
    if rating in modifiedRatings:
      modifiedRatings[rating].append(key)
    else:
      modifiedRatings[rating] = [key]
  # rated songs
  maxHeap = []
  for rating in modifiedRatings.keys():
    songsList = modifiedRatings[rating]
    while songsList:
      n = len(songsList)
      randSongIdx = randrange(n)
      heapq.heappush(maxHeap, (-1 * rating, randrange(l), songsList[randSongIdx]))
      del songsList[randSongIdx]
  unratedSongs = []
  for songId in songsIds:
    if songId not in ratings:
      unratedSongs.append(songId)
  playlist = []
  ratedSongsPicked = 0
  # logic 
  while maxHeap or unratedSongs:
    if maxHeap and ratedSongsPicked < 3:
      playlist.append(heapq.heappop(maxHeap)[1])
      ratedSongsPicked += 1 
    elif unratedSongs and ratedSongsPicked == 2:
      unratedSongsSize = len(unratedSongs)
      randUnratedSongIdx = randrange(unratedSongsSize)
      playlist.append(unratedSongs[randUnratedSongIdx])
      del unratedSongs[randUnratedSongIdx]
      ratedSongsPicked = 0
    elif maxHeap:
      playlist.append(heapq.heappop(maxHeap)[1])
    else:
      unratedSongsSize = len(unratedSongs)
      randUnratedSongIdx = randrange(unratedSongsSize)
      playlist.append(unratedSongs[randUnratedSongIdx])
      del unratedSongs[randUnratedSongIdx]
  return playlist

print(getPlaylist([1,2,3,4,5,6], {1:0.7, 2:0.7, 3:0.3, 4:0.3}))