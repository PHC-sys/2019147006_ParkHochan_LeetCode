class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('R') - moves.count('L'), moves.count('U')-moves.count('D'))==(0,0)