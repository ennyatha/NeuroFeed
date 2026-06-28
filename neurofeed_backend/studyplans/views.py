from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import StudyPlan
from groq import Groq
import os

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

class GenerateStudyPlanView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        topic = request.data.get('topic')
        goal = request.data.get('goal')
        duration_days = request.data.get('duration_days', 30)
        user_id = request.data.get('user_id', 1)

        if not topic or not goal:
            return Response(
                {'error': 'topic and goal are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        prompt = f"""
        Create a detailed {duration_days}-day study plan for the following:
        
        Topic: {topic}
        Goal: {goal}
        Duration: {duration_days} days
        
        Format the response as a structured day-by-day plan with:
        - Daily topics to cover
        - Resources to use (free ones)
        - Practice tasks
        - Weekly milestones
        
        Make it realistic and achievable for a college student.
        """

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        plan_content = completion.choices[0].message.content

        plan = StudyPlan.objects.create(
            user_id=user_id,
            topic=topic,
            goal=goal,
            duration_days=duration_days,
            plan_content=plan_content
        )

        return Response({
            'id': plan.id,
            'topic': plan.topic,
            'goal': plan.goal,
            'duration_days': plan.duration_days,
            'plan': plan_content,
            'created_at': plan.created_at
        }, status=status.HTTP_201_CREATED)


class GetStudyPlansView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        plans = StudyPlan.objects.filter(user_id=user_id).order_by('-created_at')
        data = [{
            'id': p.id,
            'topic': p.topic,
            'goal': p.goal,
            'duration_days': p.duration_days,
            'plan': p.plan_content,
            'created_at': p.created_at
        } for p in plans]
        return Response(data)