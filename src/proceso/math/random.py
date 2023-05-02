import random as rnd


class Random:
    def random_seed(self, seed: float):
        """Sets the seed value for random().

        By default, random() produces different results each time the program is
        run. Set the seed parameter to a constant to return the same
        pseudo-random numbers each time the software is run.
        """
        rnd.seed(seed)

    def random(self, min: float, max: float | None = None) -> float:
        """Return a random floating-point number.

        Takes either 1 or 2 arguments.

        If one argument is given and it is a number, returns a random number from
        0 up to (but not including) the number.

        If two arguments are given, returns a random number from the first
        argument up to (but not including) the second argument.
        """
        if max:
            return rnd.uniform(min, max)
        else:
            return rnd.uniform(0, min)

    def random_gaussian(
        self, mean: float | None = None, sd: float | None = None
    ) -> float:
        """Returns a random number fitting a Gaussian, or normal, distribution.
        There is theoretically no minimum or maximum value that random_gaussian()
        might return. Rather, there is just a very low probability that values far
        from the mean will be returned; and a higher probability that numbers near
        the mean will be returned. Takes either 0, 1 or 2 arguments.
        If no args, the mean is 0 and the standard deviation is 1.
        If one arg, that arg is the mean and the standard deviation is 1.
        If two args, the first arg is the mean and the second is the standard
        deviation.
        """
        return rnd.gauss(mean, sd)
