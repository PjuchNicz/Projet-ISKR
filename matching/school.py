from certification import Certification

class School:
    """School class
    Attributes:
        name (str): name of the school
        certification (list[Certification]): list of certification

    Methods:
        __init__: constructor
        __str__: string representation
        __repr__: representation
        add_certification: add a certification to the school
    """
    def __init__(self, name: str, certifications: list[Certification] = []):
        self._name = name
        self._certification = certifications

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def certification(self) -> list[Certification]:
        return self._certification
    
    def __str__(self) -> str:
        return f"""School: 
            Name :{self.name}
            Certification :{self.certification}"""
    
    def __repr__(self) -> str:
        return f"School({self.name}, {self.certification})"
    
    def add_certification(self, certification: Certification) -> None:
        self.certification.append(certification)