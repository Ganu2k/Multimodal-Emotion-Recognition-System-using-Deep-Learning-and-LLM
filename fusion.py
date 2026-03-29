def fuse_emotions(face, text, speech):
    emotions = [face, text, speech]

    count = {}

    for e in emotions:
        if e not in count:
            count[e] = 0
        count[e] += 1

    return max(count, key=count.get)