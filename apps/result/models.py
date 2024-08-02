from django.db import models

from apps.corecode.models import (
    AcademicSession,
    AcademicTerm,
    StudentClass,
    Subject,
)
from apps.students.models import Student




class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    test1 = models.FloatField()
    test2 = models.FloatField()
    test3 = models.FloatField()
    exam = models.FloatField()
    total = models.FloatField(blank=True, null=True)
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        ordering = ["subject"]

    def __str__(self):
        return f"{self.student} {self.session} {self.term} {self.subject}"


    def save(self, *args, **kwargs):
        self.total = self.test1 + self.test2 + self.test3 + self.exam
        self.grade = self.get_grade()
        super().save(*args, **kwargs)
    def grade(self):
        return get_grade(self.total())