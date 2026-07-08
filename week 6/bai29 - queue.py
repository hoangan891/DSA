class HitCounter:
    def __init__(self): self.hits = []
    def record_hit(self, ts):
        self.hits.append(ts); self.clean(ts)
    def get_hits(self, cur_time):
        self.clean(cur_time); return len(self.hits)
    def clean(self, cur_time):
        while self.hits and self.hits[0] <= cur_time - 300: self.hits.pop(0)
hc = HitCounter(); hc.record_hit(10); print(hc.get_hits(305))