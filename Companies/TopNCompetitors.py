import heapq

def topNCompetitors(numCompetitors, topNCompetitors, competitors, 
                    numReviews, reviews):
    if(numCompetitors == 0 or topNCompetitors == 0 or numReviews == 0):
        return 0
    else:
        # convert all the competitors to lowercase
        for i in range(numCompetitors):
            competitors[i] = competitors[i].lower()
        # convert all review to lowercase
        for i in range(numReviews):
            reviews[i] = reviews[i].lower()
        # heap to store the competitors and number of times they are mentioned in 
        # unique reviews
        heap = []
        for i in range(numCompetitors):
            competitor = competitors[i]
            noOfReviewsMentioned = 0
            # see competitor with every review
            for j in range(numReviews):
                review = reviews[j]
                if competitor in review:
                    noOfReviewsMentioned += 1 
            heapq.heappush(heap, (noOfReviewsMentioned, competitor))
        # get the n largest companies 
        topNCompetitorsheap = heapq.nlargest(topNCompetitors, heap  )
        topNCompetitorsList = []
        for i in range(topNCompetitors):
            topNCompetitorsList.append(topNCompetitorsheap[i][1])
        return topNCompetitorsList