import collections
import heapq

class PriorityQueue:
    @staticmethod
    def simpleOps():
        normal_list = [3, 4, 5, 12, 6]
        # this will by default create a min heap
        # were minimum elements will be at the top
        # it may not be sorted
        # they come first when you pop
        heapq.heapify(normal_list)
        print(normal_list)

        heapq.heappush(normal_list, 2)
        print(normal_list)

        print("N smallest in the list {}".format(heapq.nsmallest(3, normal_list)))
        print("N largest in the list is {}".format(heapq.nlargest(3, normal_list)))

        min_1 = heapq.heappop(normal_list)
        print(min_1)
        print(normal_list)

    @staticmethod
    def otherOps():
        # heap based on criteria
        normal_list = [(1, 2), (4, 5), (7, 1)]
        heapq.heapify(normal_list)
        # this would push based on first value first then second value
        heapq.heappush(normal_list, (10, 1))
        print(normal_list)
        pass


if __name__ == "__main__":
    PriorityQueue.simpleOps()
    PriorityQueue.otherOps()
