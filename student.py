class student:

    def __init__(self):
        pass

    def fromret(self,ret):
        ret = ret[0]
        self.student_id = ret[0]
        self.admission_year = ret[1]
        self.name = ret[2]
        self.gender = ret[3]
        self.exam_number = ret[4]
        self.department_code = ret[5]
        self.department = ret[6]
        self.major_category = ret[7]
        self.major = ret[8]
        self.national_standard_major_code = ret[9]
        self.major_code = ret[10]
        self.major_level = ret[11]
        self.current_grade = ret[12]
        self.class_code = ret[13]
        self.class_name = ret[14]
        self.academic_years = ret[15]
        self.enrollment_status = ret[16]
        self.student_status = ret[17]
        self.campus = ret[18]
        self.id_card_number = ret[19]
        self.ethnicity = ret[20]
        self.hometown_province = ret[21]
        self.high_school = ret[22]
        self.contact_address = ret[23]
        self.contact_person = ret[24]
        self.contact_phone = ret[25]
        self.political_affiliation = ret[26]
        self.postal_code = ret[27]
        self.admission_score = ret[28]
        self.enrollment_season = ret[29]
        self.primary_foreign_language = ret[30]
        self.years_of_study = ret[31]
        self.admitted_major = ret[32]
        self.student_level = ret[33]
        self.school_code = ret[34]
        self.has_reported = ret[35]
