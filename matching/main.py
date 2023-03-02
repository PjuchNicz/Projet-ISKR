from certification import Certification
from school import School
from student import Student
from company import Company
from job_offer import JobOffer

isen = School("ISEN", [Certification("Diplome big data", "Big data",["Python","AI"], 5), Certification("Diplome web", "Web",["HTML","CSS"], 3)])
leo = Student("Leo")
leo.add_school(isen)
leo.add_school_certification(isen, "Diplome big data")
leo.add_school_certification(isen, "Diplome web")
print(leo)

google = Company("Google")
google.add_job_offer(JobOffer("Data scientist", "Big data", ["Python","AI"], ["SQL"], 5))
print(google)
print(google.job_offers[0])