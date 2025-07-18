from django import forms
from django.contrib import admin

# Register your models here.
from .models.people import (
    NssUser, Assessment,
    Cohort, NssUserCohort,
    StudentAssessmentStatus,
    StudentAssessment, CohortInfo,
    StudentTag
)
from .models.coursework import (
    Course, ProposalStatus, Capstone, Book,
    CapstoneTimeline, StudentProject, Project,
    CohortCourse, FoundationsLearnerProfile, FoundationsExercise
)

from .models.skill import (
    CoreSkill, CoreSkillRecord,
    LearningRecordEntry, LearningRecord, LearningWeight,
)

class StudentProjectForm(forms.ModelForm):
    class Meta:
        model = StudentProject
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentProjectForm, self).__init__(*args, **kwargs)
        # Assuming Project model has a relation to Book and then to Course
        # Adjust 'project__book__course__active=True' to match your model's relationships
        projects = Project.objects.filter(book__course__active=True)
        self.fields['project'].queryset = projects
        project_choices = [(project.id, f"{project.book.course.name} - {project.name}") for project in projects]
        self.fields['project'].choices = project_choices

class StudentAssessmentForm(forms.ModelForm):
    class Meta:
        model = StudentAssessment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentAssessmentForm, self).__init__(*args, **kwargs)
        # Assuming Project model has a relation to Book and then to Course
        # Adjust 'project__book__course__active=True' to match your model's relationships
        assessments = Assessment.objects.filter(book__course__active=True)
        self.fields['assessment'].queryset = assessments
        assessment_choices = [(assessment.id, f"{assessment.book.course.name} - {assessment.name}") for assessment in assessments]
        self.fields['assessment'].choices = assessment_choices



@admin.register(CohortInfo)
class CohortInfoAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('cohort', )

@admin.register(CohortCourse)
class CohortCourseAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('cohort', 'course', 'active', )

@admin.register(StudentAssessment)
class StudentAssessmentAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    form = StudentAssessmentForm
    list_display = ('student', 'assessment', 'status', )
    search_fields = ["student__user__last_name"]
    search_help_text = "Search by last name"

@admin.register(StudentAssessmentStatus)
class StudentAssessmentStatusAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('status', )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('name', 'implementation_url', 'book' )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('name', 'course',)

@admin.register(StudentProject)
class StudentProjectAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    form = StudentProjectForm
    list_display = ('student', 'project', 'date_created')
    search_fields = ["student__user__last_name"]
    search_help_text = "Search by last name"

@admin.register(CapstoneTimeline)
class CapstoneTimelineAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('capstone', 'status', 'student')
    search_fields = ["capstone__student__user__last_name"]
    search_help_text = "Search by last name"


@admin.register(NssUserCohort)
class NssUserCohortAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('nss_user', 'cohort', 'is_github_org_member')
    search_fields = ["nss_user__user__last_name"]
    ordering = ('-pk',)
    search_help_text = "Search by last name"

@admin.register(StudentTag)
class StudentTagAdmin(admin.ModelAdmin):
    """For assigning students to cohorts"""
    list_display = ('student', 'tag',)
    search_fields = ["student__user__last_name"]
    search_help_text = "Search by last name"

@admin.register(Capstone)
class CapstoneAdmin(admin.ModelAdmin):
    """For managing capstone proposals"""
    list_display = ('student', 'course', 'proposal_url',)
    search_fields = ["student__user__last_name"]
    search_help_text = "Search by last name"


@admin.register(ProposalStatus)
class ProposalStatusAdmin(admin.ModelAdmin):
    """For managing capstone proposals statuses"""
    list_display = ('status',)

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    """For managing cohort information"""
    list_display = ('name', 'start_date', 'end_date', 'active')

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    """Assessment skills"""
    list_display = ('name', 'source_url', 'type',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Course skills"""
    list_display = ('name',)

@admin.register(CoreSkill)
class CoreSkillAdmin(admin.ModelAdmin):
    """Core skills"""
    list_display = ('label',)

@admin.register(CoreSkillRecord)
class CoreSkillRecordAdmin(admin.ModelAdmin):
    """Core skill records"""
    list_display = ('student', 'skill', 'level',)

@admin.register(LearningWeight)
class LearningWeightAdmin(admin.ModelAdmin):
    """Learning weights"""
    list_display = ('label', 'weight',)

@admin.register(LearningRecord)
class LearningRecordAdmin(admin.ModelAdmin):
    """Learning records"""
    list_display = ('student', 'weight',)
    search_fields = ["student__user__last_name"]

@admin.register(LearningRecordEntry)
class LearningRecordEntryAdmin(admin.ModelAdmin):
    """Learning record entries"""
    list_display = ('record', 'instructor', 'note',)
    search_fields = ["record__student__user__last_name"]

@admin.register(NssUser)
class NssUserAdmin(admin.ModelAdmin):
    """Users"""
    list_display = ('full_name', 'slack_handle',)
    ordering = ('-pk',)
    search_fields = ["user__last_name"]
    search_help_text = "Search by last name"

@admin.register(FoundationsLearnerProfile)
class FoundationsLearnerProfileAdmin(admin.ModelAdmin):
    list_display = ('cohort_type', 'cohort_number', 'learner_name')
    ordering = ('-pk',)
    search_fields = ["learner_name"]
    search_help_text = "Search by learner name"

@admin.register(FoundationsExercise)
class FoundationsExerciseAdmin(admin.ModelAdmin):
    list_display = ('learner_name', 'slug', 'attempts', 'complete', 'used_solution', 'completed_code')
    ordering = ('-pk',)
    search_fields = ["learner_name"]
    search_help_text = "Search by learner name"
