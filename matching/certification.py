class Certification:
    """Certification class
    Attributes:
        name (str): name of the certification
        domain (str): domain of the certification
        skills (list[str]): list of skills
        schooling_level (int): schooling level

    Methods:
        __init__: constructor
        __str__: string representation
        __repr__: representation
    """
    def __init__(self, name: str, domain: str, skills: list[str] , schooling_level: int):
        self._name = name
        self._domain = domain
        self._skills = skills
        self._schooling_level = schooling_level
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def domain(self) -> str :
        return self._domain
    
    @property
    def skills(self) -> list[str]:
        return self._skills
    
    @property
    def schooling_level(self) -> int:
        return self._schooling_level
    
    def __str__(self) -> str:
        return f"""Certification: 
            Name :{self.name}
            Domain :{self.domain} 
            Skills :{self.skills}
            Schooling level :{self.schooling_level}"""

    def __repr__(self) -> str:
        return f"Certification({self.name}, {self.domain}, {self.skills}, {self.schooling_level})"