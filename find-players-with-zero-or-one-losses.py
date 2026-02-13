class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        players = set()
        
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            
            if loser in losses:
                losses[loser] += 1
            else:
                losses[loser] = 1
        
        zero_losses = []
        one_loss = []
        
        for player in players:
            if player not in losses:
                zero_losses.append(player)
            elif losses[player] == 1:
                one_loss.append(player)
        
        zero_losses.sort()
        one_loss.sort()
        
        return [zero_losses, one_loss]
