
"""Graduation day Problem """


class GraduationAttendance():
    """
    To find the number of ways to attend classes over N days and
    the probability that you will miss your graduation ceremony
    """

    def __init__(self, days):
        """
        days -> total days of attendence
        ceremony_absent_combination_count -> last day of the ceramony is absent count for the combinations, inilized as zero
        initial list is for creating the combination of all days
        A -> Absent
        P -> Present
        """

        self.days = int(days)
        self.ceremony_absent_combination_count = 0
        self.initial_list = ['A', 'P']

    def check_consecutive_absent(self, combination_el):
        """ check the combination absent 4 days consecutively"""

        self.update_number_of_absent(combination_el)

        return combination_el[-4:] != 'AAAA'

    def update_number_of_absent(self, combination_el):
        """ update the ceremony_absent_combination_count if the student is absent for the ceremony day"""

        if len(combination_el) == self.days and combination_el[-1] == 'A' and combination_el[-4:] != 'AAAA':
            self.ceremony_absent_combination_count = self.ceremony_absent_combination_count + 1

    def find_all_combinations(self, initial_list, days):
        """ Find all the combinations from the initial list and the number of days """
        if days == 0:
            return ['']
        combinations = [combination_el + intial_el for combination_el in self.find_all_combinations(initial_list, days - 1) for intial_el in  initial_list if self.check_consecutive_absent(combination_el + intial_el)]
        return combinations


n = input("Enter the number of days ")

## get GraduationAttendance class object
graduation_attendance_obj = GraduationAttendance(n)

### find the length of the combinations
combinations_count = len(graduation_attendance_obj.find_all_combinations(graduation_attendance_obj.initial_list, graduation_attendance_obj.days))
print(combinations_count)


### find the probability of miss the ceremony
probability = f'{graduation_attendance_obj.ceremony_absent_combination_count}/{combinations_count}'
print(probability)
