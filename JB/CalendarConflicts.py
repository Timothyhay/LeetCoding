
def find_conflict(cal):
    if len(cal) <= 1:
        return []
    conflict = []
    temp_conflict = cal[0]
    end = cal[0][1]
    for i in range(1, len(cal)):
        if cal[i][1] > end: # No conflict
            if len(temp_conflict) > 1:
                conflict.append(temp_conflict)
            temp_conflict = []
        end = max(cal[i][1], end)
        temp_conflict.append(cal[i])
    if len(temp_conflict) > 1:
        conflict.append(temp_conflict)
    return conflict


appt = [ [ 1, 5 ],  [ 2, 6 ], [ 3, 7 ],[ 4, 100 ],  [ 5, 6 ], [ 10, 15 ] ]

print(find_conflict(appt))