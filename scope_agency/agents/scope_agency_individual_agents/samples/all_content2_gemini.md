-----------------------------------------------START: 01_project_understanding.md-----------------------------------------------------------

# Project Requirements: 

## Project Requirements: AI-Driven Market Trend Prediction and Optimization for Envirol

**Project Goal:** To develop and implement an AI system that predicts market trends, optimizes grease trap recycling operations, and improves overall efficiency and environmental impact for Envirol.

**Problem Statement:** Envirol currently lacks the ability to accurately predict market trends and optimize its grease trap recycling operations, leading to inefficiencies in collection, scheduling, and resource allocation. This results in potential missed opportunities, increased operational costs, and challenges in assessing environmental impact.

**Stakeholder Needs:**

*   **Envirol Management:**
    *   Gain insights into market trends and future grease collection volumes to make informed business decisions.
    *   Optimize collection routes and scheduling to reduce operational costs and improve efficiency.
    *   Improve understanding of market trends and recycling efficiency.
    *   Assess the reduction of environmental impact through increased proper dumping.
    *   Analyze and highlight revenue fluctuations with reasons.
*   **Collection and Inspection Teams:**
    *   Receive smart schedules for inspections, optimizing their routes and time.
    *   Identify establishments that are likely to miss cleaning schedules.
*   **Environmental Compliance Team:**
    *   Identify potential cases of illegal grease trap waste dumping.
    *   Develop methods to identify non-legal cleanings.

**Project Requirements:**

*   The AI system must predict which restaurants will miss cleaning in the current and next month.
*   The AI system must identify grades for each establishment and implement dynamic scoring.
*   The AI system should forecast grease waste collection volumes for future months.
*   The AI system must generate smart schedules for inspectors.
*   The AI system must identify potential cases of illegal grease trap waste dumping in deserts, valleys, and trash cans.
*   The AI system must analyze and highlight revenue fluctuations with reasons.
*   The AI system must assess the reduction of environmental impact through increased proper dumping.
*   The AI system must develop methods to identify non-legal cleanings.
*   The AI system must leverage 15+ years of plant data.
*   The AI system should potentially integrate external data sources.
*   The AI system must present insights through a user-friendly dashboard.

**Constraints & Assumptions:**

*   The project will utilize existing Envirol plant data.
*   The availability and quality of external data sources may vary.
*   The project will be subject to budget and time constraints.

-----------------------------------------------END: 01_project_understanding.md-----------------------------------------------------------

-----------------------------------------------START: 02_key_objectives.md-----------------------------------------------------------

# Key Objectives: 

 ## Key Objectives

These key objectives outline the essential outcomes the AI system must achieve to optimize Envirol's grease trap recycling operations and improve market understanding. They are focused on delivering measurable improvements in prediction accuracy, operational efficiency, and environmental impact.

- Predict restaurant grease trap cleaning compliance for the current and next month with 90% accuracy.
- Implement a dynamic scoring system for each establishment, categorized by grade.
- Forecast monthly grease waste collection volumes with a Mean Absolute Percentage Error (MAPE) of less than 10%.
- Generate smart schedules for inspectors, optimizing routes to reduce travel time by 15%.
- Identify potential illegal grease trap waste dumping with an accuracy rate of 85%.
- Analyze and highlight revenue fluctuations, identifying root causes with 80% accuracy.
- Assess the reduction of environmental impact through increased proper dumping with an increase of 20% in legal dumping.
- Develop methods to identify non-legal cleanings, achieving a detection rate of 75%.

-----------------------------------------------END: 02_key_objectives.md-----------------------------------------------------------

-----------------------------------------------START: 03_deliverables.md-----------------------------------------------------------

# Deliverables: 

## Deliverables
- AI system for predicting restaurants that will miss cleaning in the current and next month.
- Dynamic scoring system for each establishment.
- Forecasted grease waste collection volumes for future months.
- Smart schedules for inspectors.
- Identification of potential illegal grease trap waste dumping cases.
- Analysis of revenue fluctuations with reasons.
- Assessment of the reduction of environmental impact.
- Methods to identify non-legal cleanings.
- User-friendly dashboard presenting insights.
- Optimized collection routes and scheduling system.
- AI Model for market trend predictions.
- AI Model for grease collection volume predictions.
- Plant data integration.
- Integration of external data sources (if applicable).

-----------------------------------------------END: 03_deliverables.md-----------------------------------------------------------

---------------------------------------------START: Web Chatbot INTERFACE-----------------------------------

# Web Chatbot
This panel will provide a conversational interface for users to quickly access key information, receive support, and perform basic tasks related to the grease trap recycling operations. The chatbot will be integrated into the web application to enhance user experience.


## Conversational Interface

 

*This module provides a conversational interface for users to interact with the system using natural language.*

### End User
    **Chatbot Interaction**
        *Actions*:
          - Initiate a conversation with the chatbot.
          - Ask questions about system functionalities.
          - Request information from the system.
          - Perform tasks through the chatbot interface.
          - Receive responses and information from the chatbot.
          - Provide feedback on the chatbot's responses.
          - End the conversation with the chatbot.
    **Settings**
        *Actions*:
          - Customize the chatbot's appearance.
          - Adjust notification preferences.
          - View conversation history.
          - Manage chatbot settings.
          - Report an issue with the chatbot.
    **Search**
        *Actions*:
          - Search for specific information using keywords.
          - Filter search results based on relevance.
          - Navigate through search results.
          - Access related information from search results.
          - Refine search queries to improve results.
### Administrator
    **Chatbot Management**
        *Actions*:
          - Monitor chatbot usage and performance.
          - Review user interactions with the chatbot.
          - Update chatbot responses and knowledge base.
          - Troubleshoot chatbot issues.
          - Customize chatbot settings and configurations.
          - Analyze chatbot performance metrics.
          - Manage user access to the chatbot.
    **Training**
        *Actions*:
          - Train the chatbot on new topics and information.
          - Review and correct chatbot responses.
          - Improve chatbot accuracy and relevance.
          - Add new intents and entities to the chatbot.
          - Test chatbot performance after training.
          - Monitor and evaluate the chatbot's training progress.


## Information Retrieval

 

*This module provides users with quick access to essential information regarding grease trap recycling operations, including service areas, pricing, and the recycling process.*

### End User
    **General Information**
        *Actions*:
            - Search for service areas by location.
            - View pricing for various grease trap sizes.
            - Review the grease trap recycling process steps.
            - Access contact information for customer support.
            - Find answers to frequently asked questions (FAQs).
            - View educational resources about grease trap recycling.
    **Account Management**
        *Actions*:
            - View their service history.
            - Review invoices and payment history.
            - Update their account information.
            - Contact customer support for assistance.
### Administrator
    **Content Management**
        *Actions*:
            - Update service area information.
            - Modify pricing details.
            - Edit the FAQs section.
            - Add or remove educational resources.
            - Review user feedback and inquiries.
    **Reporting and Analytics**
        *Actions*:
            - Generate reports on information retrieval usage.
            - Analyze search query trends.
            - Monitor the effectiveness of the information provided.


## Support and Assistance

 

*The Support and Assistance module provides users with resources and methods for resolving issues related to grease trap recycling, fostering user satisfaction through efficient support.*

### End User

**Troubleshooting**
    *Actions*:
        - Access troubleshooting guides for common issues.
        - Follow step-by-step instructions to resolve problems.
        - View FAQs to find answers to common questions.
        - Search for solutions using keywords.

**Submit Support Request**
    *Actions*:
        - Submit a detailed support request describing the issue.
        - Attach relevant files (e.g., photos, documents).
        - Track the status of submitted support requests.
        - Receive updates on the progress of support requests.
        - Provide feedback on the support received.

**Contact Support**
    *Actions*:
        - Initiate a live chat with a support agent.
        - Request a phone call from a support agent.
        - View the contact information for support.

**Knowledge Base**
    *Actions*:
        - Search the knowledge base for relevant articles.
        - Read articles on topics related to grease trap recycling.
        - Browse articles by category.
        - Provide feedback on the helpfulness of articles.


## Task Execution

 

*The Task Execution module streamlines grease trap recycling operations, enabling users to schedule services, view their history, and manage accounts.*

### End User

**Service Scheduling**
     *Actions*:
        - Schedule a new grease trap recycling service.
        - Select a service date and time.
        - Specify the grease trap location.
        - Review and confirm the service details.
        - Cancel a scheduled service.
        - Reschedule a service.
**Service History**
     *Actions*:
        - View the history of completed service.
        - View service details, including date, time, and location.
        - View service status.
        - Download service reports.

**Account Management**
     *Actions*:
        - Update account information.
        - Change password.
        - View payment history.
        - Update payment method.
        - Contact customer support.
----------------------------------END: Web Chatbot INTERFACE--------------------------------------




---------------------------------------------START: Web App INTERFACE-----------------------------------

# Web App
This panel will serve as the primary user interface for accessing and interacting with the AI-driven market trend predictions and operational optimization tools. It will provide a centralized dashboard for visualizing data, managing schedules, and analyzing key performance indicators related to grease trap recycling operations.


## Dashboard

 

*The Dashboard module provides a centralized overview of key performance indicators and market trends. It displays real-time data visualizations, including recycling volumes, market prices, and operational efficiency metrics. This module allows users to monitor overall performance and identify areas for improvement within the grease trap recycling operations.*

### Manager
*Actions*:
    - View real-time data visualizations of key performance indicators.
    - Monitor recycling volumes and market prices.
    - Analyze operational efficiency metrics.
    - Identify areas for improvement based on data insights.
    - Customize dashboard views to display specific metrics.
    - Generate reports on key performance indicators.

### Inspector
    *Actions*:
    - View real-time data visualizations of key performance indicators.
    - Monitor recycling volumes and market prices.
    - Analyze operational efficiency metrics.
    - Identify areas for improvement based on data insights.
    - Customize dashboard views to display specific metrics.
    - Generate reports on key performance indicators.


## Data Visualization

 

*The Data Visualization module transforms raw data into interactive visual representations, enabling users to explore and understand trends in grease trap recycling data.*

### Data Analyst
    **Dashboard**
        *Actions*:
            - Create interactive dashboards displaying key performance indicators (KPIs).
            - Customize dashboard layouts with drag-and-drop functionality.
            - Save and share custom dashboards with other users.
    **Chart Generation**
        *Actions*:
            - Generate various chart types, including bar charts, line graphs, and pie charts.
            - Customize chart appearance, such as colors, labels, and titles.
            - Filter data displayed in charts based on specific criteria.
    **Report Generation**
        *Actions*:
            - Generate reports summarizing data visualizations.
            - Export reports in various formats, such as PDF and CSV.
            - Schedule automated report generation and distribution.
    **Data Exploration**
        *Actions*:
            - Drill down into data points for detailed analysis.
            - Zoom in and out of charts to view data at different levels of granularity.
            - Compare data across different time periods and categories.


## Schedule Management

 

### Administrator
*Actions*:
  - Create a new service schedule.
  - Modify existing service schedules.
  - Delete service schedules.
  - Assign service schedules to technicians.
  - View all service schedules.
  - Generate service schedule reports.
  - Manage service schedule templates.

### Technician
*Actions*:
  - View assigned service schedules.
  - Update service schedule status (e.g., completed, in progress).
  - Report issues encountered during service.
  - Confirm service completion.
  - Access service schedule details, including customer information and service requirements.


## Prediction & Analysis

 

*The Prediction & Analysis module provides AI-driven market trend forecasts and operational optimization recommendations. This module analyzes historical data and current market conditions to predict future trends and suggest improvements. Users can leverage these predictions to make informed decisions about resource allocation and market strategies.*

### Analyst
    **Data Input & Validation**
        *Actions*:
            - Upload historical data for analysis.
            - Validate data for accuracy and completeness.
            - Define data sources and connection parameters.
    **Trend Analysis**
        *Actions*:
            - Generate market trend forecasts based on historical data.
            - Identify key market drivers and their impact.
            - Visualize trend predictions through charts and graphs.
    **Report Generation**
        *Actions*:
            - Create custom reports on market trends.
            - Export reports in various formats.
            - Schedule report generation and distribution.
    **Scenario Planning**
        *Actions*:
            - Simulate different market scenarios.
            - Analyze the impact of various factors on predictions.
            - Compare and contrast different scenarios.
    **Recommendation Engine**
        *Actions*:
            - Receive recommendations for operational optimization.
            - Review the rationale behind each recommendation.
            - Implement recommended changes.
            - Track the performance of implemented recommendations.
----------------------------------END: Web App INTERFACE--------------------------------------




