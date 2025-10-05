import copy
import random

class Hat:
    def __init__(self, **kwargs):

        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):

        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls


        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
   
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

 
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check if expected balls condition is satisfied
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_counts.get(color, 0) < expected_count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments



if __name__ == "__main__":
 
    hat = Hat(blue=5, red=4, green=2)
    probability = experiment(
        hat=hat,
        expected_balls={"red": 1, "green": 2},
        num_balls_drawn=4,
        num_experiments=2000
    )
    print("Estimated Probability:", round(probability, 4))
