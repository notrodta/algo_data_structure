import urllib.request


def answer(topic):
    link = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=" + topic
    fp = urllib.request.urlopen(link)
    print(fp)

    mybytes = fp.read()

    mystr = mybytes.decode("utf8").split("\"text\":{\"*\":")[1]
    counter = 0

    for line in mystr.split():
        if topic in line:
            counter += 1
            #print(topic)

    return counter



print(answer("pizza"))