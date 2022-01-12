class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.next = 1
        self.max = 1

    def visit(self, url: str) -> None:
        if self.next >= len(self.history):
            self.history.append(url)
        else:
            self.history[self.next] = url
        self.next += 1
        self.max = self.next

    def back(self, steps: int) -> str:
        self.next -= steps
        if self.next <= 0:
            self.next = 1
        return self.history[self.next - 1]

    def forward(self, steps: int) -> str:
        self.next = min(self.max, self.next + steps)
        return self.history[self.next - 1]