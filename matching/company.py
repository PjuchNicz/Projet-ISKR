class Company:
    def __init__(self, name):
        self._name = name
        self._job_offers = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def job_offers(self):
        return self._job_offers
    
    def add_job_offer(self, job_offer):
        self._job_offers.append(job_offer)
    
    def __str__(self):
        return f"""Company name: {self.name}
Job offers: {self.job_offers}"""

    def __repr__(self):
        return f"Company({self.name}, {self.job_offers})"