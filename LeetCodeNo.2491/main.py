# 2491. Divide Players Into Teams of Equal Skill

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Thoughts:
        # sort the skill first.
        # In order for teams of equal skills to exist, we have to combine the first and last skill number. Use this to track
        # If any team's skill sum is not the first team, return -1.

        n = len(skill)

        skill.sort()
        start = 0
        end = n-1
        teams = []
        total_skills = skill[start] + skill[end]
        while start < end:
            if skill[start] + skill[end] == total_skills:
                teams.append([start, end])
            else:
                return -1
            start += 1
            end -= 1
        chem = 0
        for one_team in teams:
            chem += skill[one_team[0]] * skill[one_team[1]]
        return chem