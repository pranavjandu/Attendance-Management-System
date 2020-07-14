


from django.urls import path
from . import views,adminviews,instructorviews,studentviews

urlpatterns = [
    path('',views.loginpage,name="loginpage"),
    path('adm',adminviews.dash,name="dashboard"),
    path('logout',views.logoutUser,name="logout"),
    path('addInstructor',adminviews.registerInstructor,name="addInstructor"),
    path('addCourse',adminviews.addCourse,name="addCourses"),
    path('addBatch',adminviews.addBatch,name="addBatch"),
    path('addStudent',adminviews.registerStudent,name="addStudent"),
    path('managei',adminviews.manageInstructor,name="managei"),
    path('manages',adminviews.manageStudent,name="manages"),
    path('managec',adminviews.manageCourse,name="managec"),
    path('manageb',adminviews.manageBatch,name="manageb"),
    path('edit_instructor/<str:ins_id>',adminviews.editInstructor,name="editi"),
    path('edit_student/<str:stu_id>',adminviews.editStudent,name='edits'),
    path('edit_course/<str:cou_id>',adminviews.editCourse,name='editc'),
    path('edit_batch/<str:bat_id>',adminviews.editBatch,name='editb'),
    path('createdataset/<str:us_id>',adminviews.registerFace,name='createdataset'),
    path('train',adminviews.trainSet,name="train"),
    #student paths
    path('studashboard',studentviews.studentDashboard,name="studashboard"),
    #instructor paths
    path('insdashboard',instructorviews.instructorDashboard,name="insdashboard"),
    path('insbatch',instructorviews.viewbatch,name="insbatch"),
    path('check_students/<str:bat_id>',instructorviews.viewstudents,name="checkstudents")
]