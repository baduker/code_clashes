def chop_it_up(listOfSamples, delimiter):
    return ", ".join(["[{}]".format(delimiter.join(map(str,chunk))) for chunk in [listOfSamples[i:i+2] for i in range(0, len(listOfSamples), 2)]])