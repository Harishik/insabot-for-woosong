from dataclasses import dataclass


@dataclass
class Office:
    name: str
    purpose: str
    email: str | None = None
    phone: str | None = None
    location: str | None = None
    source_url: str | None = None


OFFICES = [
    Office("Academic Office", "Classes, grades, registration, graduation", source_url="https://english.wsu.ac.kr/page/index.jsp?code=eng0206"),
    Office("International Affairs", "Visa, ARC, arrival, exchange, international support", phone="+82-42-630-9641~4", source_url="https://engforeign.wsu.ac.kr"),
    Office("Student Welfare Center", "Student ID, welfare, clubs, campus life"),
    Office("IT Help Desk", "Accounts, LMS, Smart Campus, technical issues"),
    Office("Admissions Office", "Admissions, documents, applicant inquiries", source_url="https://english.wsu.ac.kr/page/index.jsp?code=eng0302"),
    Office("Dormitory Office", "Dormitory application, check-in, housing rules", email="dormitory@wsu.ac.kr", phone="042-629-6541~2", source_url="https://dorm.wsu.ac.kr/main/"),
]


def route_office(question: str) -> Office:
    lowered = question.lower()
    if any(term in lowered for term in ["visa", "arc", "immigration", "arrival", "airport"]):
        return OFFICES[1]
    if any(term in lowered for term in ["grade", "class", "attendance", "course", "graduation", "calendar"]):
        return OFFICES[0]
    if any(term in lowered for term in ["id card", "student id", "club", "welfare"]):
        return OFFICES[2]
    if any(term in lowered for term in ["lms", "smart campus", "login", "password"]):
        return OFFICES[3]
    if any(term in lowered for term in ["dorm", "housing", "room"]):
        return OFFICES[5]
    if any(term in lowered for term in ["admission", "apply", "application"]):
        return OFFICES[4]
    return OFFICES[1]
