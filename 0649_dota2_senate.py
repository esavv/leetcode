# See: https://leetcode.com/problems/dota2-senate/
from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        return self.soln2(senate)
        # return self.soln1(senate)

    # revolving queue approach, keep moving voters at the front to the back unless they're banned
    def soln2(self, senate):
        party     = {'R': 0, 'D': 1}
        pops      = {0: 0, 1: 0}
        live_bans = {0: 0, 1: 0}
        not_party = {0: 1, 1: 0}
        voters    = deque()

        for char in senate:
            chari = party[char]
            pops[chari] += 1
            voters.append(chari)

        while pops[0] > 0 and pops[1] > 0:
            chari = voters.popleft()
            enemy = not_party[chari]
            if live_bans[chari] == 0:
                live_bans[enemy] += 1
                pops[enemy] -= 1
                voters.append(chari)
            else:
                live_bans[chari] -= 1

        if pops[0] == 0:
            return 'Dire'
        return 'Radiant'

    # simulate all voting rounds
    def soln1(self, senate):
        pops = {'R': 0, 'D': 0}
        party = {'R': 'Radiant', 'D': 'Dire'}
        not_party = {'R': 'D', 'D': 'R'}
        curr_senate = []

        # take a census
        for idx, char in enumerate(senate):
            pops[char] += 1
            curr_senate.append(char)

        # loop through each voting round until only one party left
        while pops['R'] > 0 and pops['D'] > 0:
            live_voters = {'R': [], 'D': []}
            next_enemy = [0] * len(curr_senate)

            for idx, char in enumerate(curr_senate):
                live_voters[char].append(idx)
                next_enemy[idx] = len(live_voters[not_party[char]])

            banned = [False] * len(curr_senate)

            for i in range(len(curr_senate)):
                if not banned[i]:
                    enemy = not_party[curr_senate[i]]
                    if pops[enemy] == 0:
                        return party[curr_senate[i]]
                    ban_idx = -1
                    for enm_idx in live_voters[enemy]:
                        if enm_idx > i:
                            ban_idx = enm_idx
                            break
                    if ban_idx != -1:
                        live_voters[enemy].remove(ban_idx)
                    else:
                        ban_idx = live_voters[enemy].pop(0)
                    banned[ban_idx] = True
                    pops[enemy] -= 1

            tmp = []
            for idx, char in enumerate(curr_senate):
                if not banned[idx]:
                    tmp.append(char)
            curr_senate = tmp

        if pops['R'] == 0:
            return party['D']
        return party['R']