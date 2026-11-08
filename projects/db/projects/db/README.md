erDiagram
  PEOPLE ||--o{ PEOPLE : "reports to"
  PEOPLE ||--o{ PROJECT_MEMBERS : "works on"
  PEOPLE ||--o{ TASKS : "assigned to"
  PROJECTS ||--o{ PROJECT_MEMBERS : "has member"
  PROJECTS ||--o{ TASKS : "has task"
  PROJECTS ||--o{ EXPENSES : "has expense"


  PEOPLE {
    int person_id PK
    string first_name
    string last_name
    string work_email UK
    string title
    date start_date
    int manager_id FK
  }
#one row for people is the first and last name of a single individual employee
  PROJECTS {
    int project_id PK
    int client_id FK
    string name
    string client_name
    string category
    decimal budget
    date start_date
    string status
  }
#one row in projects is the project id and project name and the details after that
  PROJECT_MEMBERS {
    int person_id FK
    int project_id FK
    string role
    int hours_per_week
    date joined_date
  }
#project members is the specific person per project and is describing them by their ids
  TASKS {
    int task_id PK
    int project_id FK
    string description
    date created_date
    int assigned_to FK
    date due_date
    date completed_date
  }
#task is describing the specific task per project and is using the ids to identify them because a poroject has multiple tasks
  EXPENSES {
    int expense_id PK
    int project_id FK
    date expense_date
    decimal amount
    string category
    string note
  }
  #expenses is idetifying an individual expense per project by their ids so a project can have multiple expense


for people i used a surrogate person ID key instead of email because the scenario says that a person will change their email when they change their title but an individual id will not

the optional ids managerID is optional becaus ethe two founders report to nobody but there is a lack of a managers table which would help solve that issue
client_name is also optional because for internal projects their is no client
assigned to on tasts is optional because new tasks may be unassigned

The main rules the table cant hold are for total hours worked because it is only allocating time started and completed on individual projects not the total time worked on it so a check would be to aggregate total hours to see who is working more than or less then 40 hours

one thing i changed from the ai result was the work email to the person id so that you can actually identify every individal employee I also added a client id which does not go to a table but i think it is important to denote which clients belong to hich project and if it is an internal project then there wuld also be an internal client id 