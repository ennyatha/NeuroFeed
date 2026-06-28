from django.db import models

class StudyPlan(models.Model):
    user_id = models.IntegerField()
    topic = models.CharField(max_length=255)
    goal = models.TextField()
    duration_days = models.IntegerField()
    plan_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plan for user {self.user_id} - {self.topic}"