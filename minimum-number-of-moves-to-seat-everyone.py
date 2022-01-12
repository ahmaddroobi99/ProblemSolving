class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort(reverse=True), students.sort()
        moves = 0
        for student in students:
            moves += abs(student - seats[-1])
            seats.pop()
        return moves