from string import punctuation


def name_checker(request, row, broken):
    stop = False
    for char in [x for x in punctuation if x != '-']:
        if char in row[int(request.GET.get('name', '1')) - 1]:
            broken.append(row[int(request.GET.get('name', '1')) - 1])
            stop = True
            break
    return broken, stop
