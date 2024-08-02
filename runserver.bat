@echo off
   REM Navigate to the project directory
   cd /d "C:\Users\DELL\Desktop\versions_web_apss\xchelon"

   REM Activate the virtual environment
   call xchenv\Scripts\activate

   REM Start the Django development server
   start cmd /k "python manage.py runserver"

   REM Delay to give the server time to start
   timeout /t 5 > nul

   REM Open the web browser 
   start "" "http://127.0.0.1:8000"

   pause
