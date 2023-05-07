'''
Q2 - Safaricom Software dev - 
	Given:
		A = [100, 200, 100]
		B = [50, 100, 100]
		X = 100
		Y = 70
	You function should return 0.
	The tapped point (x, y) | (100, 70) is withing the range of icon 0

	Icon ranes:
			icon0  = (100, 50)
			icon1  = (200, 100)
			icons2 = (100, 100)
'''

# it dosen't pass the case where the (x, y) match up and they are the last values in the arrays


def locate(x, y, X_axis=[100, 200, 100], y_axis=[50, 100, 100]):
    locations = {X_axis.index(val[0]): val for val in zip(X_axis, y_axis)}
    print(locations)
    # locations = [val for val in zip(X_axis, y_axis)]
    # for location in locations:
    #     if (
    #         (location[0] > x or location[0] == x)
    #         and
    #             (location[-1] > y or location[-1] == y)):
    #         return f"icon_{locations.index(location)}"
    #     else:
    #         continue


'''
Q3 - Safaricom dev -

'''


if __name__ == "__main__":
    print(locate(x=100, y=100))
    # locate(x=200, y=70)
