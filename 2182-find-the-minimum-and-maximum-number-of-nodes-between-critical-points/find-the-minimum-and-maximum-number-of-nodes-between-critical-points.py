class Solution(object):
    def nodesBetweenCriticalPoints(self, head):

        prev = head
        curr = head.next

        index = 1

        first = -1
        last = -1

        min_distance = float('inf')

        while curr.next:

            # Check whether curr is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                # First critical point
                if first == -1:
                    first = index

                # If this isn't the first critical point
                if last != -1:
                    distance = index - last
                    min_distance = min(min_distance, distance)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        max_distance = last - first

        return [min_distance, max_distance]