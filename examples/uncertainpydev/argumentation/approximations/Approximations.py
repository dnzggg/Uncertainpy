class Approximations:
    def __init__(self, ads, time=0, arguments=[], argument_strength=[], attacker=[], supporter=[], name="") -> None:
        self.ads = ads
        self.time = time
        self.arguments = arguments
        self.argument_strength = argument_strength
        self.attacker = attacker
        self.supporter = supporter
        self.name = name

    def initialise_arrays(self):
        argument_set = list(self.ads.BAG.arguments.values())
        arg_to_index = {}

        arguments = []
        argument_strength = []

        for z, a in enumerate(argument_set):
            arguments.append(a)
            argument_strength.append(a.strength)
            arg_to_index[a] = z

        attacker = {}
        supporter = {}

        for z, a in enumerate(argument_set):

            attacker_child = []
            for b in a.attackers:
                attacker_child.append(arg_to_index[b])

            attacker[z] = attacker_child

            supporter_child = []
            for b in a.supporters:
                supporter_child.append(arg_to_index[b])

            supporter[z] = supporter_child

        self.ads.arguments = arguments
        self.ads.argument_strength = argument_strength
        self.ads.attacker = attacker
        self.ads.supporter = supporter

    def rewrite_arrays(self):
        for i in range(len(self.arguments)):
            self.arguments[i].strength = self.argument_strength[i]

    def perform_iteration(delta, epsilon):
        return None

    def approximate_solution(self, delta, epsilon, verbose):
        self.initialise_arrays()

        time = 0
        time_limit = 200
        max_derivative = 0
        while True:
            max_derivative = self.perform_iteration(delta, epsilon)
            time += delta

            if(max_derivative < epsilon or time >= time_limit):
                break

        self.rewrite_arrays()

        if (verbose):
            print_args = '\n'.join([str(x) for x in self.ads.arguments])
            print(f"{self.ads.name}, {self.ads.approximator.name}\nTime: {time}\n{print_args}\n")
        
        return max_derivative