-----------------------------------------------START: 01_project_understanding.md-----------------------------------------------------------

# Project Requirements: 

# Project Requirements: AI-Powered Market Trend Prediction and Optimization for Envirol's Grease Trap Recycling

**Project Goal:** To develop and implement an AI system that predicts market trends, optimizes grease trap recycling operations, and improves overall efficiency for Envirol.

**Problem Statement:** Envirol currently lacks a data-driven system to accurately predict market trends, optimize collection routes, and identify potential inefficiencies in its grease trap recycling operations, leading to potential revenue loss and operational inefficiencies.

**Stakeholder Needs:**

*   **Envirol Management:**
    *   Improved understanding of market trends to inform strategic decisions.
    *   Increased operational efficiency through optimized collection routes and scheduling.
    *   Enhanced ability to identify and mitigate risks associated with illegal waste disposal.
    *   Data-driven insights to improve recycling efficiency and reduce environmental impact.
    *   A user-friendly dashboard to visualize key performance indicators (KPIs) and insights.
*   **Collection Inspectors:**
    *   Smart schedules to optimize their routes.
*   **Operations Team:**
    *   Accurate predictions of grease waste collection volumes to optimize resource allocation.

**Primary Objectives (Required):**

*   Predict which restaurants will miss cleaning in the current and next month.
*   Identify grades for each establishment and implement dynamic scoring.

**Secondary Objectives (To be estimated separately):**

*   Forecast grease waste collection volumes for future months.
*   Generate smart schedules for inspectors.
*   Identify potential cases of illegal grease trap waste dumping in deserts, valleys, and trash cans.
*   Analyse and highlight revenue fluctuations with reasons.
*   Assess the reduction of environmental impact through increased proper dumping.
*   Develop methods to identify non-legal cleanings.

**Success Metrics:**

*   Accuracy of restaurant cleaning predictions (e.g., percentage of correct predictions).
*   Improved efficiency of collection routes (e.g., reduction in travel time, fuel consumption).
*   Reduction in instances of illegal waste disposal.
*   Accuracy of grease waste collection volume forecasts.
*   Increased recycling efficiency (e.g., percentage of grease collected and processed).
*   User adoption and satisfaction with the dashboard and insights.

**Constraints & Assumptions:**

*   The project will leverage 15+ years of existing plant data.
*   The system may integrate external data sources to enhance prediction accuracy.
*   Data quality and completeness are critical for accurate predictions.
*   The project will be completed within a defined budget and timeline.
*   The user-friendly dashboard will be accessible to relevant stakeholders.

-----------------------------------------------END: 01_project_understanding.md-----------------------------------------------------------

-----------------------------------------------START: 02_key_objectives.md-----------------------------------------------------------

# Key Objectives: 

 ## Key Objectives

These key objectives define the essential outcomes the AI system must achieve to provide value to Envirol, optimizing grease trap recycling operations and improving market trend understanding. They focus on specific, measurable results that align with Envirol's goals.

- Predict restaurants that will miss cleaning in the current and next month with an accuracy of at least 80%.
- Implement a dynamic scoring system for each establishment based on identified grades.
- Forecast grease waste collection volumes for future months with a Mean Absolute Percentage Error (MAPE) of less than 10%.
- Generate smart schedules for inspectors, reducing route optimization time by 15%.
- Identify potential cases of illegal grease trap waste dumping with a detection rate of at least 70%.
- Analyze and highlight revenue fluctuations, providing explanations for at least 80% of significant changes.
- Assess the reduction of environmental impact through increased proper dumping, showing a 5% improvement in recycling efficiency.
- Develop methods to identify non-legal cleanings with an accuracy of at least 75%.

-----------------------------------------------END: 02_key_objectives.md-----------------------------------------------------------

-----------------------------------------------START: 03_deliverables.md-----------------------------------------------------------

# Deliverables: 

## Deliverables
- AI-powered market trend prediction system
- User-friendly dashboard for data visualization
- Predictive model to forecast grease collection volumes
- Collection route optimization module
- Dynamic scoring system for restaurants
- Predictive model to identify restaurants missing cleaning services
- Smart scheduling system for inspectors
- Analysis of revenue fluctuations with reasons
- Environmental impact assessment module
- System to identify non-legal cleaning activities
- Identification of potential illegal grease trap waste dumping locations

-----------------------------------------------END: 03_deliverables.md-----------------------------------------------------------

---------------------------------------------START: Web Chatbot INTERFACE-----------------------------------

# Web Chatbot
Provide immediate support and information to users regarding market trends, recycling efficiency, and other relevant data.


## Information Retrieval

 

*This module provides users with the ability to search for and access relevant information within the system.*

### User
#### Search
##### Actions
- Search for information using keywords.
- View search history.
- View search results.
- Sort search results by relevance.
- Sort search results by date.

#### Knowledge Base
##### Actions
- Browse articles.
- Search articles.
- View articles.

#### Reports
##### Actions
- Generate reports based on search criteria.
- View reports.


## Conversational Interface

 

*This module focuses on enabling the chatbot to understand and respond to user inputs effectively.*

### End User
#### Actions
- Ask questions
- Make requests
- Provide feedback
- Initiate a conversation
- End a conversation

### Administrator
#### Actions
- Define conversation flows
- Configure intent recognition
- Manage chatbot responses
- Test conversation flows
- Monitor conversation logs


## Data Analysis and Presentation

 

### Data Analyst
#### Data Visualization
##### Actions
- Create data visualizations
- Customize visualization parameters
- Export visualizations
- Save visualization templates
- Share visualizations

#### Data Summarization
##### Actions
- Generate data summaries
- Customize summary parameters
- Export data summaries
- Save summary templates
- Share summaries

#### Report Generation
##### Actions
- Generate reports
- Customize report layouts
- Export reports
- Schedule report generation


## User Management

 

*This module manages user accounts, roles, and permissions to control access to the system and its features.*

### Administrator
   *Actions*:
   - Create user account.
   - Update user account details.
   - Delete user account.
   - Assign roles to users.
   - Revoke roles from users.
   - Reset user passwords.
   - View user activity logs.
   - Block user access.
   - Unblock user access.

### End User
   *Actions*:
   - Update profile information.
   - Change password.
   - View account details.


## Web Chatbot

 

*The Web Chatbot module provides a conversational interface for users to access insights, ask questions, and interact with the AI system's data and predictions, enhancing understanding of market trends and recycling efficiency.*

### End User
   **Conversation**
      *Actions*:
         - Ask questions.
         - Make requests.
         - Provide feedback.
         - Initiate a conversation.
         - End a conversation.

### Administrator
   **Chatbot Configuration**
      *Actions*:
         - Define conversation flows.
         - Configure intent recognition.
         - Manage chatbot responses.
         - Test conversation flows.
         - Monitor conversation logs.
   **Data Access Control**
      *Actions*:
         - Grant access to specific data insights.
         - Restrict access to sensitive information.
         - Manage user permissions for chatbot interactions.
   **System Monitoring**
      *Actions*:
         - Monitor chatbot performance.
         - Analyze user interactions.
         - Review chatbot feedback.
         - Update chatbot knowledge base.
----------------------------------END: Web Chatbot INTERFACE--------------------------------------




---------------------------------------------START: Mobile App INTERFACE-----------------------------------

# Mobile App
Enable inspectors to access schedules, update statuses, and report findings in the field.


## Schedule Management

 

*This module enables inspectors to manage and view their inspection schedules, including the ability to accept, reject, or reschedule inspections.*

### Inspector
  #### Schedule Viewing
    *Actions*:
      - View inspection schedule.
      - View inspection details.
      - View client information.
      - View inspection location.
      - View inspection date and time.
      - View associated documentation.
  #### Schedule Management
    *Actions*:
      - Accept an inspection.
      - Reject an inspection.
      - Request to reschedule an inspection.
      - View rescheduled inspection details.


## Status Updates

 

*This module allows inspectors to update the status of inspections, ensuring real-time tracking and management of inspection progress.*

### Inspector
#### Update Inspection Status
*This sub-module allows inspectors to update the status of inspections.*
##### Actions
- Mark inspection as "in progress."
- Mark inspection as "completed."
- Mark inspection as "pending review."


## Findings Reporting

 

*This module enables inspectors to document and report findings, categorize issues, and attach supporting evidence.*

### Inspector
#### Create Finding
##### Actions
- Create a new finding.
- Add a description to the finding.
- Categorize the finding.
- Prioritize the finding.
- Attach supporting evidence to the finding.
- Save the finding.
#### Review Finding
##### Actions
- Review a finding.
- View finding details.
- View supporting evidence.
- Edit finding details.
- Update the finding.
- Delete the finding.


## Data Synchronization

 

*This module facilitates the continuous exchange of data between the mobile application and the central database.*

### Inspector
    **Offline Data Access**
        *Actions*:
          - Inspector can access schedules offline.
          - Inspector can access related data offline.
    **Data Synchronization**
        *Actions*:
          - Inspector can upload changes when a network connection is available.
          - Inspector can view synchronization status.
----------------------------------END: Mobile App INTERFACE--------------------------------------




---------------------------------------------START: Web App INTERFACE-----------------------------------

# Web App
The primary interface for users to access the AI-driven insights and manage the grease trap recycling operations.


## User Authentication

 

*This module manages user access and authentication within the system.*

### End User
#### Sign Up
*Actions*:
- User can register with required information.
#### Login
*Actions*:
- User can log in using their credentials.
#### Forgot Password
*Actions*:
- User can reset their password.
#### Profile Management
*Actions*:
- User can view their profile information.
- User can update their profile information.
- User can change their password.

### Administrator
#### User Management
*Actions*:
- Administrator can create user accounts.
- Administrator can modify user roles and permissions.
- Administrator can disable user accounts.
- Administrator can reset user passwords.
#### Authentication Logging
*Actions*:
- Administrator can view authentication logs.
- Administrator can monitor failed login attempts.


## Data Input & Management

 

*This module enables users to input, upload, validate, store, and retrieve data related to grease trap operations.*

### Inspector
#### Data Input
##### Actions
- Input grease trap inspection data.
- Upload inspection reports.
- Validate inspection data.

#### Data Retrieval
##### Actions
- Retrieve inspection data.
- Generate inspection reports.

#### Data Management
##### Actions
- Update inspection data.
- Delete inspection data.

### Administrator
#### Data Input
##### Actions
- Input grease trap operation data.
- Upload data related to grease trap operations.

#### Data Retrieval
##### Actions
- Retrieve data related to grease trap operations.
- Generate reports on grease trap operations.

#### Data Management
##### Actions
- Manage data storage.
- Manage data access permissions.


## Insight Generation & Display

 

*This module focuses on processing data to produce actionable insights and presenting these insights through interactive visualizations.*

### Data Analyst
*Actions*:
   - Upload data for analysis.
   - Select data sources for insight generation.
   - Define parameters for insight generation.
   - Initiate insight generation process.
   - Review generated insights.
   - Customize visualization templates.
   - Generate reports based on insights.
   - Export reports in various formats.
   - Share reports with stakeholders.

### Manager
*Actions*:
   - Review generated insights.
   - View interactive visualizations.
   - Access reports.
   - Share reports with team members.
   - Provide feedback on insights.


## Service Scheduling & Management

 

*This module allows for the scheduling, dispatching, and tracking of grease trap servicing, enabling users to manage service appointments.*

### Service Coordinator
    **Scheduling**
        *Actions*:
          - Schedule a new service appointment.
          - Reschedule an existing service appointment.
          - Cancel a service appointment.
          - View service appointment calendar.
          - Assign a service appointment to a technician.
    **Dispatching**
        *Actions*:
          - Dispatch a technician to a service appointment.
          - View technician's location.
          - Update service appointment status.
    **Reporting**
        *Actions*:
          - Generate service reports.
          - View service history.
          - Export service data.

### Technician
    **Service Execution**
        *Actions*:
          - View assigned service appointments.
          - Update service appointment status.
          - Record service details.
          - Upload service completion documents.
          - Mark service as complete.
    **Communication**
        *Actions*:
          - Communicate with the service coordinator.
          - Notify the customer of arrival.

### Customer
    **Appointment Management**
        *Actions*:
          - Request a service appointment.
          - View scheduled service appointments.
          - Receive service appointment notifications.
          - Approve/Reject service appointment rescheduling requests.


## Reporting & Analytics

 

*This module generates reports and analytics to provide insights into grease trap operations.*

### Manager
#### Service Efficiency
*This sub-module focuses on the efficiency of grease trap services.*
##### Actions
- View service completion rates
- Analyze service time per location
- Identify underperforming service areas
- Track technician performance metrics
- Generate service efficiency reports

#### Cost Analysis
*This sub-module focuses on the costs associated with grease trap services.*
##### Actions
- Review operational costs
- Analyze costs per service
- Generate cost reports
- Identify cost-saving opportunities
- Track vendor expenses

#### Environmental Impact
*This sub-module focuses on the environmental impact of grease trap operations.*
##### Actions
- Monitor waste disposal quantities
- Track environmental compliance metrics
- Generate environmental impact reports
- Identify areas for environmental improvement
- Analyze waste disposal costs

### Administrator
##### Actions
- Configure report generation schedules
- Manage report access permissions
- Customize report templates
- Review report generation logs
- Monitor system performance for reporting


## Notification & Alerting

 

*This module facilitates the timely dissemination of information to users through various channels, ensuring awareness of service schedules, operational issues, and system updates.*

### End User
#### Notifications
*This sub-module focuses on the delivery of notifications to end users.*
##### Actions
- Receive service schedule notifications.
- Receive operational issue alerts.
- Receive system update notifications.
- Manage notification preferences.
- View notification history.

### Administrator
#### Alert Management
*This sub-module allows administrators to manage the alerts.*
##### Actions
- Create alert templates.
- Update alert templates.
- Delete alert templates.
- Schedule alerts.
- Configure notification channels.
- Monitor alert delivery status.
- View alert logs.
----------------------------------END: Web App INTERFACE--------------------------------------




