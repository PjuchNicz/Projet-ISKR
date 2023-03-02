from school import School
from certification import Certification

class Student:
    """Student class
    Attributes:
        name (str): name of the student
        schools (list[School]): list of schools
        certification (list[Certification]): list of certification
        additionnal_skills (list[str]): list of additionnal skills
        exclude_domain (list[str]): list of excluded domains
        
    Methods:
        __init__: constructor
        __str__: string representation
        __repr__: representation
        add_school: add a school to the student
        add_school_certification: add a certification to the student
        add_additionnal_skills: add an additionnal skill to the student
        add_exclude_domain: add an excluded domain to the student
        get_skills: get the list of skills of the student
    """
    def __init__(self, name: str):
        self._name = name
        self._schools = []
        self._certification = []
        self._additionnal_skills = []
        self._exclude_domain = []

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def schools(self) -> list[School]:
        return self._schools
    
    @property
    def certification(self) -> list[Certification]:
        return self._certification
    
    @property
    def additionnal_skills(self) -> list[str]:
        return self._additionnal_skills

    @property
    def exclude_domain(self) -> list[str]:
        return self._exclude_domain
    
    def __str__(self) -> str:
        return f"""Student {self.name}:
        - Schools: {self.schools}
        - Certification: {self.certification}
        - Additionnal skills: {self.additionnal_skills}
        - Exclude domain: {self.exclude_domain}
        """

    def __repr__(self) -> str:
        return self.__str__()

    def add_school(self, school: School) -> None:
        self._schools.append(school)
    
    def add_school_certification(self, school: School, certification_name: str) -> None:
        if school not in self.schools:
            raise ValueError(f"{school.name} not found in {self.name}'s schools")
        for certification in school.certification:
            if certification.name == certification_name:
                self.certification.append(certification)
                break
        else:
            raise ValueError(f"Certification {certification_name} not found in {school.name}")

    def add_additionnal_skills(self, skill: str) -> None:
        self._additionnal_skills.append(skill)
    
    def add_exclude_domain(self, domain: str) -> None:
        self._exclude_domain.append(domain)
    
    def get_skills(self) -> list[str]:
        skills = []
        for certification in self.certification:
            skills.extend(certification.skills)
        skills.extend(self.additionnal_skills)
        return skills
    
