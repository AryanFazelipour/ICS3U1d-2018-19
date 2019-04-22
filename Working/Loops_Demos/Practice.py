
def km_to_miles():
    """

    Output a table of km to mile conversions from 1 to 100 km
    :return:
    """

    for i in range(5, 51, 5):
        print(i, " --->", round(i *0.621, 2), "miles")

km_to_miles()