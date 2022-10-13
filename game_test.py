import unittest

class BowlingGameTest(unittest.TestCase):
    pass
class Game:
    def __init__(self):
        self.rolls = []
        for i in range(21):
            self.rolls.append(0)
        self.currentRoll = 0

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(10):
            if self.rolls[frame_index] == 10:  # strike
                score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.is_spare(frame_index):
                score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
        return score

    def is_spare(self, frame_index:int):
        return self.rolls[frame_index] + self.rolls[frame_index+1] == 10

    def sum_of_balls_in_frame(self, frame_index: int):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
if __name__ == "__main__":
    unittest.main()