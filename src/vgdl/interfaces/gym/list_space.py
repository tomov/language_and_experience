from gymnasium import Space

class list_space(Space):
    def __init__(self, basespace):
        # NOTE: intentionally do NOT call super().__init__ -- this is a
        # placeholder variable-length space; gymnasium's Space.__init__ would
        # require a concrete shape/dtype we don't have.
        self.basespace = basespace
        self.shape_ = [None] + list(self.basespace.shape)

    #def sample(self):
    #    return [space.sample() for space in self.spaces]

    def shape(self):
        return tuple(self.shape_)

    def __repr__(self):
        return "List(%d)" % self.basespace.shape
    def __eq__(self, other):
        return self.basespace == other.basespace
