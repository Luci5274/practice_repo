class StopWatch:
    def __init__(self):
        self.running =False
        self.elapsed_time = 0

    def start(self):
        if not self.running:
            self.running =True
            print('Stopwatch Started')


    def stop(self):
        if self.running:
            self.running = False
            print(f'stopwatch stopped at {self.elapsed_time}')

    def reset(self):
        self.elapsed_time = 0
        self.running = False

    def status(self):
        print(f'running state is: {self.running},elapsed time is: {self.elapsed_time}')

    def tick(self):
        if self.running:
            self.elapsed_time += 1