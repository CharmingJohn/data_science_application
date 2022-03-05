class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def __repr__(self):
        return 'Temperature({}, {})'.format(self.value, self.scale)

    def __str__(self):
        return 'Temperature is {}, {}'.format(self.value, self.scale)


t = Temperature(25, 'C')


print(repr(t))
print(str(t))
print(t)

