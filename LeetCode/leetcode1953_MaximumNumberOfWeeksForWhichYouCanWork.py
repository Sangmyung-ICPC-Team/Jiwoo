from sys import stdin

def numberOfWeeks(milestones):
    total_milestones, max_milestone = sum(milestones), max(milestones)

    if total_milestones - max_milestone >= max_milestone:
        return total_milestones

    return 2 * (total_milestones - max_milestone) + 1

arr = [*map(int, stdin.readline().split())]
print(numberOfWeeks(arr))