# scheduler
Scheduler to schedule time slots

# Apps

Timeslots, Appointments, Days

User is a preexisting model with associated fields (id,email,role etc)
Timeslots has from_time and to_time just to select the time range
Appointments has manytomany reference to timeslots, and hence can choose multuple timeslots for any day

https://dbdiagram.io/d/604c765cfcdcb6230b23f573

