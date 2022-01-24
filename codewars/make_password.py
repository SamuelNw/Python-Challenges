def make_password(phrase):
    # Your code here
    phrase_list = phrase.split()
    firsts = []
    for word in phrase_list:
        firsts.append(word[0])
    s = "".join(firsts)
    q = s.replace("i", "1")
    r = q.replace("I", "1")
    t = r.replace("o", "0")
    u = t.replace("O", "0")
    v = u.replace("s", "5")
    w = v.replace("S", "5")
    return w


print(make_password("Give me liberty or give me death"))