# See: https://leetcode.com/problems/dota2-senate/
class Solution(object):
    def predictPartyVictory(self, senate):
        return self.soln3(senate)
        # return self.soln2(senate)
        # return self.soln1(senate)

    # soln #1 from 2/11/2025
    # queue approach
    def soln3(self, senate):
        from collections import deque

        r_count, d_count = 0, 0
        queue = deque()
        for char in senate:
            queue.append(char)
            if char == 'R':
                r_count += 1
            else:
                d_count += 1

        r_bans, d_bans = 0, 0
        while queue:
            if r_count == 0:
                return 'Dire'
            if d_count == 0:
                return 'Radiant'

            senator = queue.popleft()
            if senator == 'R' and r_bans == 0:
                d_bans += 1
                queue.append(senator)
            elif senator == 'D' and d_bans == 0:
                r_bans += 1
                queue.append(senator)
            elif senator == 'R' and r_bans > 0:
                r_count -= 1
                r_bans -= 1
            elif senator == 'D' and d_bans > 0:
                d_count -= 1
                d_bans -= 1

    # revolving queue approach, keep moving voters at the front to the back unless they're banned
    def soln2(self, senate):
        from collections import deque
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