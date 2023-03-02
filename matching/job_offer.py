class JobOffer:
    def __init__(self, job_title: str, domain: str, required_skills: list[str], extra_skills: list[str], schooling_level: int):
        self._job_title = job_title
        self._domain = domain
        self._required_skills = required_skills
        self._extra_skills = extra_skills
        self._schooling_level = schooling_level

    @property
    def job_title(self):
        return self._job_title

    @property
    def domain(self):
        return self._domain

    @property
    def required_skills(self):
        return self._required_skills

    @property
    def extra_skills(self):
        return self._extra_skills

    @property
    def schooling_level(self):
        return self._schooling_level

    def __str__(self):
        return f"""Job title: {self.job_title}
Domain: {self.domain}
Required skills: {self.required_skills}
Extra skills: {self.extra_skills}
Schooling level: {self.schooling_level}"""

    def __repr__(self):
        return f"JobOffer({self.job_title}, {self.domain}, {self.required_skills}, {self.extra_skills}, {self.schooling_level})"
