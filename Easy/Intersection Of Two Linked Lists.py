class Solution(object):
    def getIntersectionNode(self, headA, headB):
        point_a, point_b = headA, headB
        if not point_a or not point_b:
            return None
        while point_a != point_b:
            point_a = point_a.next if point_a is not None else headB
            point_b = point_b.next if point_b is not None else headA
        return point_a
