import asyncio
from typing import Literal, Any
import os, shutil
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.types import Command
from pydantic import BaseModel

load_dotenv()
OUTPUT_DIR = 'scope_pipeline'
EXTRA_DIR = 'data'
shutil.rmtree(OUTPUT_DIR)
shutil.rmtree(EXTRA_DIR)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(EXTRA_DIR, exist_ok=True)


# Define shared state schema
class ScopeState(MessagesState):
    query: str
    requirements: str | list
    objectives: str | list
    deliverables: str | list
    panels: str | list
    modules: str | list
    actions: str | list
    verification: str | list


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", google_api_key=os.environ.get('GOOGLE_API_KEY'))

verifier_options = [
    "project_understanding_agent",
    "key_objectives_agent",
    "deliverables_agent",
    "panels_agent",
    "modules_agent",
    "modules_actions_agent",
]


class Router(BaseModel):
    next: Literal[*verifier_options, "FINISH"]
    verification: str

# class Router(BaseModel):
#     agents: dict = None

def project_understanding_agent(state: ScopeState):
    project_understanding_agent_prompt = open("./agent_instructions/project_understanding_agent_instructions.md").read()
    agent = create_react_agent(llm, tools=[],
                               prompt=project_understanding_agent_prompt)
    file_name = 'project_understanding.md'
    if state['verification']:
        identifier = 'verifier_agent'
        msg = [
            {
                "role": "user",
                "content": f"Original user query:\n\n{state['query']}. "
                           f"Previously generated content:\n\n{state['requirements']}"
                           f"Suggestions:\n\n{state['verification']}"
            },
        ]
        print("project understanding: verification")
    else:
        identifier = "key_objectives_agent"
        msg = [state['messages'][0]]
        print("project understanding: state")
    response = agent.invoke({'messages': msg})
    last_message = response['messages'][-1].content
    if last_message:
        if os.path.exists(os.path.join(EXTRA_DIR, file_name)):
            with open(os.path.join(EXTRA_DIR, file_name), 'r+') as f:
                data = f.read()
                new_data = f"{data}\n--------------------------------------------------------------------------------------\n{last_message}"
                f.write(new_data)
        else:
            open(os.path.join(EXTRA_DIR, file_name), 'w').write(last_message)
        open(os.path.join(OUTPUT_DIR, f'01_{file_name}'), 'w').write(last_message)
    else:
        breakpoint()
    return Command(goto=identifier,
                   update={"requirements": last_message, 'messages': response['messages'], 'verification': None})


def key_objectives_agent(state: ScopeState):
    key_objectives_prompt = open("./agent_instructions/key_objectives_agent_instructions.md").read()

    agent = create_react_agent(llm, tools=[],
                               prompt=key_objectives_prompt)
    file_name = 'key_objectives.md'
    if state['verification']:
        msg = [
            {
                "role": "user",
                "content": f"Original user query:\n\n{state['query']}. "
                           f"Previously generated content:\n\n{state['objectives']}"
                           f"Suggestions:\n\n{state['verification']}"
            },
        ]
        print("key objectives: verification")
        identifier = 'verifier_agent'
    else:
        msg = state['messages'][0]
        print("key objectives: state")
        identifier = "deliverables_agent"
    response = agent.invoke({'messages': msg})
    last_message = response['messages'][-1].content
    if last_message:
        if os.path.exists(os.path.join(EXTRA_DIR, file_name)):
            with open(os.path.join(EXTRA_DIR, file_name), 'r+') as f:
                data = f.read()
                new_data = f"{data}\n--------------------------------------------------------------------------------------\n{last_message}"
                f.write(new_data)
        else:
            open(os.path.join(EXTRA_DIR, file_name), 'w').write(last_message)
        open(os.path.join(OUTPUT_DIR, f'02_{file_name}'), 'w').write(last_message)

    else:
        breakpoint()
    return Command(goto=identifier,
                   update={"objectives": last_message, 'messages': response['messages'], 'verification': None})


def deliverables_agent(state: ScopeState):
    deliverables_prompt = open("./agent_instructions/deliverables_agent_instructions.md").read()
    agent = create_react_agent(llm, tools=[],
                               prompt=deliverables_prompt)
    file_name = 'deliverables.md'
    if state['verification']:
        msg = [
            {
                "role": "user",
                "content": f"Original user query:\n\n{state['query']}. "
                           f"Previously generated content:\n\n{state['deliverables']}"
                           f"Suggestions:\n\n{state['verification']}"
            },
        ]
        print("deliverables: verification")
        identifier = 'verifier_agent'
    else:
        msg = state['messages'][0]
        print("deliverables: state")
        identifier = "panels_agent"
    response = agent.invoke({'messages': msg})
    last_message = response['messages'][-1].content
    if last_message:
        if os.path.exists(os.path.join(EXTRA_DIR, file_name)):
            with open(os.path.join(EXTRA_DIR, file_name), 'r+') as f:
                data = f.read()
                new_data = f"{data}\n--------------------------------------------------------------------------------------\n{last_message}"
                f.write(new_data)
        else:
            open(os.path.join(EXTRA_DIR, file_name), 'w').write(last_message)
        open(os.path.join(OUTPUT_DIR, f'03_{file_name}'), 'w').write(last_message)

    else:
        breakpoint()
    return Command(goto=identifier,
                   update={"deliverables": last_message, 'messages': response['messages'], 'verification': None})


def panels_agent(state: ScopeState):
    panels_prompt = open("./agent_instructions/panels_agent_instructions.md").read()
    agent = create_react_agent(llm, tools=[],
                               prompt=panels_prompt)
    file_name = 'panels.md'
    if state['verification']:
        msg = [
            {
                "role": "user",
                "content": f"Original user query:\n\n{state['query']}. "
                           f"Previously generated content:\n\n{state['panels']}"
                           f"Suggestions:\n\n{state['verification']}"
            },
        ]
        print("panels: verification")
        identifier = 'verifier_agent'
    else:
        msg = state['messages'][0]
        print("panels: state")
        identifier = "modules_agent"
    response = agent.invoke({'messages': msg})
    last_message = response['messages'][-1].content
    if last_message:
        if os.path.exists(os.path.join(EXTRA_DIR, file_name)):
            with open(os.path.join(EXTRA_DIR, file_name), 'r+') as f:
                data = f.read()
                new_data = f"{data}\n--------------------------------------------------------------------------------------\n{last_message}"
                f.write(new_data)
        else:
            open(os.path.join(EXTRA_DIR, file_name), 'w').write(last_message)
        open(os.path.join(OUTPUT_DIR, f'04_{file_name}'), 'w').write(last_message)
    else:
        breakpoint()
    return Command(goto=identifier,
                   update={"panels": last_message, 'messages': response['messages'], 'verification': None})


def modules_agent(state: ScopeState):
    modules_prompt = open("./agent_instructions/modules_agent_instructions.md").read()
    agent = create_react_agent(llm, tools=[],
                               prompt=modules_prompt)
    file_name = 'modules.md'
    if state['verification']:
        msg = [
            {
                "role": "user",
                "content": f"Original user query:\n\n{state['query']}. "
                           f"Previously generated content:\n\n{state['modules']}"
                           f"Suggestions:\n\n{state['verification']}"
            },
        ]
        print("modules: verification")
        identifier = 'verifier_agent'
    else:
        msg = state['panels']
        print("modules: state")
        identifier = "modules_actions_agent"
    response = agent.invoke({'messages': msg})
    last_message = response['messages'][-1].content
    if last_message:
        if os.path.exists(os.path.join(EXTRA_DIR, file_name)):
            with open(os.path.join(EXTRA_DIR, file_name), 'r+') as f:
                data = f.read()
                new_data = f"{data}\n--------------------------------------------------------------------------------------\n{last_message}"
                f.write(new_data)
        else:
            open(os.path.join(EXTRA_DIR, file_name), 'w').write(last_message)
        open(os.path.join(OUTPUT_DIR, f'05_{file_name}'), 'w').write(last_message)
    else:
        breakpoint()
    return Command(goto=identifier,
                   update={"modules": last_message, 'messages': response['messages'], 'verification': None})


def modules_actions_agent(state: ScopeState):
    modules_actions_prompt = open("./agent_instructions/modules_actions_agent_instructions.md").read()
    agent = create_react_agent(llm, tools=[],
                               prompt=modules_actions_prompt)
    file_name = 'actions.md'
    if state['verification']:
        msg = [
            {
                "role": "user",
                "content": f"Original user query:\n\n{state['query']}. "
                           f"Previously generated content:\n\n{state['actions']}"
                           f"Suggestions:\n\n{state['verification']}"
            },
        ]
        print("actions: verification")

    else:
        msg = state['modules']
        print("actions: state")
    response = agent.invoke({'messages': msg})
    last_message = response['messages'][-1].content
    if last_message:
        if os.path.exists(os.path.join(EXTRA_DIR, file_name)):
            with open(os.path.join(EXTRA_DIR, file_name), 'a') as f:
                f.write(
                    f"---------------------------------------------------------------------------------------------------\n\n{last_message}")
        else:
            open(os.path.join(EXTRA_DIR, file_name), 'w').write(last_message)
        open(os.path.join(OUTPUT_DIR, f'06_{file_name}'), 'w').write(last_message)
    else:
        breakpoint()
    return Command(goto="verifier_agent",
                   update={"actions": last_message, 'messages': response['messages'], 'verification': None})


# async def run_agent_async(agent_name: str, state: ScopeState) -> dict[str, Any]:
#     """
#     Wrap each agent in an async function that returns its updates.
#     """
#     agent_fn = globals()[agent_name]  # or however you look them up
#     # If they are sync functions, run them in a threadpool
#     loop = asyncio.get_running_loop()
#     cmd: Command = await loop.run_in_executor(None, agent_fn, state)
#     return cmd.update


# async def _verifier_agent_async(state: ScopeState) -> Command[...]:
#     """
#     Supervisor agent to orchestrate task execution by delegating to other agents.
#     """
#     print(
#         "---------------------------------------------------------------------In verifier agent------------------------------------------------------")
#     verifier_agent_prompt = open("./agent_instructions/verifier_agent_instructions.md").read()
#     generated_content = []
#     files = os.listdir(OUTPUT_DIR)
#     files = sorted(files)
#     for file in files:
#         if file == "all_content.md" or file == "feedbacks.md":
#             continue
#         with open(os.path.join(OUTPUT_DIR, file), 'r') as f:
#             generated_content.append(f.read())
#
#     with open(os.path.join(OUTPUT_DIR, 'all_content.md'), 'w') as f:
#         f.write("\n\n\n\n-----------------------------------------------------------------------------\n\n\n\n".join(
#             generated_content))
#     messages = [
#         {"role": "system", "content": verifier_agent_prompt},
#         {"role": "user", "content": f"User query: {state['query']}"},
#         {"role": "assistant", "content": f"Generated Content to be checked: {generated_content}"},
#     ]
#     response = llm.with_structured_output(Router).invoke(messages)
#     router_dict = response.agents
#     print(
#         f"---------------------------------------------------Router dict--------------------------------------------------------\n{router_dict}\n")
#     breakpoint()
#     to_run = {}
#     for agent_name, agent_verification in router_dict.items():
#         if agent_verification:
#             agents_state = state.copy()
#             agents_state.update(verification=agent_verification)
#             to_run[agent_name] = agents_state
#     tasks = [run_agent_async(name, agent_state) for name, agent_state in to_run]
#     results = await asyncio.gather(*tasks)
#
#     aggregate_updates: dict[str, Any] = {}
#     for upd in results:
#         aggregate_updates.update(upd)
#
#     # 4) Combine all verification texts
#     combined_feedback = "\n\n".join(
#         f"{agent}: {info['verification']}"
#         for agent, info in router_dict.items()
#     )
#
#     with open(os.path.join(OUTPUT_DIR, "feedbacks.md"), "a") as f:
#         f.write(combined_feedback + "\n" + "-" * 80 + "\n")
#
#     return Command(
#         goto="verifier_agent",
#         update={**aggregate_updates, "verification": combined_feedback}
#     )
#     #
#     # print(response, "_______++++++_______")
#     # if not response or not response.verification:
#     #     breakpoint()
#     # goto = response.next
#     # if goto == "FINISH":
#     #     goto = END
#     # print(goto, "GOTO")
#     # feedbacks_file = os.path.join(OUTPUT_DIR, 'feedbacks.md')
#     #
#     # file_content = ""
#     # if os.path.exists(feedbacks_file):
#     #     content = open(feedbacks_file, 'r').read()
#     #     file_content = content
#     # with open(feedbacks_file, 'w') as f:
#     #     f.write(f'{file_content}\n------------------------------------------------------------------------------\n {response.verification}\n\n')
#     # return Command(goto=goto, update={"next": goto, "verification": response.verification, 'messages': messages})


# def verifier_agent(state: ScopeState) -> Command[...]:
#     # run the async version on its own event loop
#     return asyncio.run(_verifier_agent_async(state))

def verifier_agent(state: ScopeState) -> Command[Literal[*verifier_options, "__end__"]]:
    """
    Supervisor agent to orchestrate task execution by delegating to other agents.
    """
    print(
        "---------------------------------------------------------------------In verifier agent------------------------------------------------------")
    verifier_agent_prompt = open("./agent_instructions/verifier_agent_instructions.md").read()
    generated_content = []
    files = os.listdir(OUTPUT_DIR)
    files = sorted(files)
    for file in files:
        if file == "all_content.md" or file == "feedbacks.md":
            continue
        with open(os.path.join(OUTPUT_DIR, file), 'r') as f:
            generated_content.append(f.read())

    with open(os.path.join(OUTPUT_DIR, 'all_content.md'), 'w') as f:
        f.write("\n\n\n\n".join(generated_content))
    messages = [
        {"role": "system", "content": verifier_agent_prompt},
        {"role": "user", "content": state['query']},
        {"role": "assistant", "content": generated_content},
    ]
    response = llm.with_structured_output(Router).invoke(messages)
    print(response, "_______++++++_______")
    if not response or not response.verification:
        breakpoint()
    goto = response.next
    if goto == "FINISH":
        goto = END
    print(goto, "GOTO")
    feedbacks_file = os.path.join(OUTPUT_DIR, 'feedbacks.md')

    file_content = ""
    if os.path.exists(feedbacks_file):
        content = open(feedbacks_file, 'r').read()
        file_content = content
    with open(feedbacks_file, 'w') as f:
        f.write(f'{file_content}\n\n  {response.verification}\n\n')
    return Command(goto=goto, update={"next": goto, "verification": response.verification, 'messages': messages})


memory = MemorySaver()
Graph = StateGraph(ScopeState)

Graph.add_node('project_understanding_agent', project_understanding_agent)
Graph.add_node('key_objectives_agent', key_objectives_agent)
Graph.add_node('deliverables_agent', deliverables_agent)
Graph.add_node('panels_agent', panels_agent)
Graph.add_node('modules_agent', modules_agent)
Graph.add_node('modules_actions_agent', modules_actions_agent)
Graph.add_node('verifier_agent', verifier_agent)

Graph.add_edge(START, 'project_understanding_agent')

graph = Graph.compile()

query_latam_airline = """
        Write a scope for a WhatsApp bot for Latam Airlines.
        Description: website - https://www.latamairlines.com/br/pt I request QP team to create a WhatsApp Demo on Kevit International number. It should be triggered with keyword "latam".
        You may start scrapping the website and start training the middleware and also create API.
        As of now flow content is only required in English. But I request backend developer to train the bot in English & Portuguese.
        Plus, backend developer should create a single API and an additional parameter of database, so that we can use same API and chatomate flow developer don't need to wait for new API and devops dependency can be eliminated.
        For example: { "input_message": "Any specific dress codes or clothing recommendations?", "user_id": "550e8400-e29b-41d4-a716-446655440000", "thread_id": "thread_rVjCuBeUaCGbtcb0L0NGZtqj", "language": "English", "database": "Latam" }
        Integrate google spreadsheet in the flow Client Open AI account will be used and key will be shared via DM Note: The deadline is for backend ,flow developer and devops
    """

query_al_serkal = """
We aim to develop and implement an AI system to predict market trends and optimize Envirol's grease trap recycling operations. The system will leverage 15+ years of plant data and potentially integrate external sources to:
    • Predict actual market size and future grease collection volumes
    • Identify patterns in outlet-specific data
    • Present insights through a user-friendly dashboard
    • Optimize collection routes and scheduling
    • Improve understanding of market trends and recycling efficiency

. Key Deliverables
The AI model should provide the following insights through predictive modelling:
Primary Objectives (Required)
    1. Predict which restaurants will miss cleaning in the current and next month.
    2. Identify grades for each establishment and implement dynamic scoring.
Secondary Objectives (To be estimated separately)
    3. Forecast grease waste collection volumes for future months.
    4. Generate smart schedules for inspectors.
    5. Identify potential cases of illegal grease trap waste dumping in deserts, valleys, and trash cans.
    6. Analyse and highlight revenue fluctuations with reasons.
    7. Assess the reduction of environmental impact through increased proper dumping.
    8. Develop methods to identify non-legal cleanings.
    """

query_ij = """
Build an end-to-end system to cover 4 M’s of Construction & Infrastructure Industry.
• Manpower
• Material
• Machinery
• Money
This RFP covers 3 major sections
1. Identifying Data Techniques (POC’s)
2. App & Web Development (MVP & MLP)
3. Support & Maintenance
Vendor can choose to respond to one section, any 2 or all the sections.
Section 1 – Identifying Data Techniques
1.1 Purpose of the Section
Main focus of this section is to conduct POC’s around data collection, making it useful
and executing the onboarding process to identify the data techniques, technology and
infrastructure for building a robust data driven system.
POC’s on below topics:
1. How data can be pulled from different sources and using intelligent data
mining/extraction techniques/technology?
2. How can we implement self-service-based customer registration process?
3. Instead of doing call centre-based effort can we use ChatGPT or any other tool for
onboarding a vendor?
4. Best and cost affective data storage solution/infrastructure?
5. How will the data engine work?
Proprietary & Confidential
Page 7 of 226. How will we get the data if it is not available in our DataBase?
7. Data Backup & Archival Process?
These POC’s have to be future ready, so that it can be used in subsequent phases of the
project.
Further Details
Please Note: Modification on the process mentioned below can be discussed if needed
a. Data needs to be extracted from different sources using AI or Web Scraping
b. Automated system should perform cleansing activity and make data useful
c. Finalized data will be used by call centre or AI Assistant based on the
criteria’s we define e.g., small vendors where Turnover is less then 10L will
be handled by AI Assistant, Medium scale vendors will be handled by both AI
Assistant and human intervention and huge vendors will be majorly call centre
and expert’s task
d. Once the master data is prepared, same cycle will be repeated monthly for
first 6 months to make sure data is thoroughly validated. After 6 months, cycle
will be converted to quarterly cycle
Expected Outputs from Phase 1:
1.
2.
3.
4.
5.
6.
7.
8.
Detailed Architecture Diagram – for each POC and combined structure
Code for each Module/Prototype
Technical Documentation for each module/fields and database
All layer details – Front End, Middle Layer and Backend
User Manuals
Output reports and structure
Data Storage details
Third Party Tools and Integration configurations
Section 2 – App & Web Development
This document is a Request for Proposal (RFP) for a design, development, testing &
implementation of Web and Mobile App (Android & iOS).
This section has 2 phases
1. MVP
2. MLP
2.1 MVP Stage:
1. MVP covering Manpower, Machinery, Money Flows & some products in Material
2. Mobile and Web (device agnostic web design)
3. Phase 1 will be focused only on providing legitimate data to customers & will be
rolled out for Mumbai Region Only
4. AI Assistant & Language Support for English, Hindi & Marathi
Proprietary & Confidential
Page 8 of 225. Matchmaking based on Geolocation, Past Experience, Price selects the most
suitable vendor’s
6. AI Predictive analytics regarding the assessment of market trends for demand
forecasting and enable efficient inventory
7. AI chat bots for real-time experience enhancing user engagement as different tiers of
contractors have different communication pattern
8. AI to analyse the auditable trial of transactions leading to integrity in procurement &
thus reducing pilferage.
Please Note: Sample data will be provided for shortlisted vendors, this is only for analysis
and not complete data.
2.2 MLP Stage:
1.
2.
3.
4.
Enhance MVP to MLP
Material Stream to be Added
Make platform ready for expansion to PAN India
Complete Platform Features (Listed in Appendix A “Platform Features”)
Further Details
Please Note: Modification on the process mentioned below can be discussed if needed
1. High Level Details – Below steps are very high-level idea on app web flow and is
a. User opens web/app
b. Location of device will be auto detected by system else first information
collected is location
c. User selects the category he is searching for, L1 – L2 – L3 – L4(L4 only if
available)
d. Selection will narrow down the user requirement
e. 3rd field will be based on the stream he is selecting (e.g., for Manpower
Stream 3rd field will be by when user needs to start the work)
f. After taking the requirement system should use the matchmaking AI feature
to search for the data within or outside the system and provide hidden result
(e.g., We have 15 contractors matching your requirements)
g. System should also ask if user needs our team to finalize the best contractor
h. If users says yes then the query will be routed to page for collecting further
information and will be routed to our Call Centre.
i. If, No then collect some more information from user like Name, WhatsApp
Number, email ID, Profile type and Price expectation
j. After adding these details, user should be routed to Payment Flow, show
approx. amount and distribution, T&C and request for GST number to make
payment
k. Once the payment is done show unlock first 5 matching records
l. For further records some more amount has to be paid by the user, so same
floe repeats again.
Proprietary & Confidential
Page 9 of 22RFP Response Expectations from Section 2:
1.
2.
3.
4.
5.
6.
7.
Detailed Architecture
UI/UX Designs
Technology Stack
Detailed Project Plan, milestones & timelines
Testing & Roll Out Plans
Detailed Technical Documentation
Training Plan
Section 3 – Support & Maintenance
1. The scope of work under maintenance services includes management & assisted
operations, support services, preventive maintenance and breakdown/curative
maintenance. The underlying philosophy of the maintenance services is to maintain
the operation of Apps/Portal running under all conditions with timely and prompt
attendance to faults so as to maintain the availability of all modules/software
applications in portal and Mobile app.
2. Operational Issues & Bug Fixing: This includes handling of all the minor, major (non-
critical) and critical problems of the Application, their repair and restoration. The
vendor shall extend all the cooperation to the client in identifying & rectification of the
faults in the shortest possible time.
3. Maintenance of existing code, Version control & management of the application
source code
4. Periodic Releases: Update of apps shall be done on need basis and/or on release of
new version of Android/iOS.
5. Application related optimizations shall be done regularly in order to enhance its
performance, as and when necessary, as limited to the scope of this agreement.
6. For backup & recovery purposes, database snapshots will be stored periodically on
cloud for backup and recovery of database and application.
7. Appropriate Measures shall be taken for safeguarding the application software from
security threats: Safety of application software as per CERT-IN norms shall be
assured by Vendor.
8.
Patch management of Application software shall be taken care of along with system
requirements.
Proprietary & Confidential
Page 10 of 229. Review meetings: Periodic review meetings, on agreed date & time, shall be held
during the contract period to review the technical, operational, quality and any other
aspects of the services delivered through the contract. The review meetings shall be
attended by the senior representative of Vendor. The meeting agenda shall inter-alia
include but not limited to the following:
(a) Services related issues.
(b) Issues related to unattended faults/ problems
(c) Upgradation issues.
10. Total Downtime: “Total Downtime” means, out of the Scheduled Hours, the
aggregate number of hours in the reporting period during which applications were
unavailable (fault severity Critical as mentioned in penalty section) for use by the
designated users

Project Background
Current Market has many unethical activities which need to be fixed, this will directly
impact/reduce the cost of construction. Current Problems are:
-
-
-
Unstructured Data: Data for T5 & T6 Contractors is not available online. So, if T2
Vendor wants to search the Contractors then they post a query on some sites like
IndiaMart, JustDial and they start receiving the calls, which becomes a pain and all
these contractors' calls are not even validated to be authentic.
Machinery Utilisation & Liaisoning: Unethical activities due to lack of Technology
Adoption. Liasoning machinery data is not available online.
Unethical activities at every level due to loopholes in the system
● Due to middle man
● Due to data not available
● Due to scammers
● Suppliers’ verification missing
● Exploitation of both Supplier & Vendor
Infrastructure construction industry has 4 major streams & every stream has its own
loopholes and issues. Below are the high-level concerns in all the 4 streams:
Manpower: Skilled Labour Shortage, Safety & Compliance, Training & Development,
Labour Turnover, Workforce Productivity, Unstructured Data, Missing Validation, Unethical
activities.
Material: Procurement Delays, Quality Control, Cost Fluctuations, Inventory Management,
Sustainable Sourcing
Machinery: Underutilization, Maintenance Cost, Technology Adoption, Equipment
Downtime, Obsolescence, TAT & Vendors for repairs
Money: Funding Challenges, Cash Flow Management, Cost Overruns, Contractual
Disputes, Economic Fluctuations
Industry spends a huge amount of effort to pull all these together, and almost all activities
are repeated for new site setup again this results in
Proprietary & Confidential
Page 12 of 221)
2)
3)
4)
5)
Waste of time and effort
Dependency on individual person
Close to zero learning from prior site experience gets applied to next site
Reduced transparency across supplier and vendor
Frictions across all interactions
Vision for InfraJugaad.com
Vision is to provide B2B solutions + legitimate & validated data to end users. Provide end to
end solutions covering all the 4 M’s. Increase awareness in the industry & help in reducing
the hassles / overcome the loopholes & dependencies in the current market. This will in turn
help the entire industry in increasing:

Visibility
Tracking
Availability
Performance
Costing
Scope
Data driven intelligence will be the backbone of the entire project which will help in
providing logical results. Algorithms will make decisions based on Location, Pricing, Rating,
Availability, Response Timings, Eligibility, Past Work, Most Relevant Interactions, Payments,
Last Time Visited etc. Matchmaking is the key, primary scope of the project is to understand
the customer needs, provide end to end solution & to provide legitimate data to the searcher.
Entire system has to be AI driven, details mentioned in Phases description.

Main Streams
1. Manpower
2. Machinery
Proprietary & Confidential
Page 15 of 223. Material
4. Money
Data collection
1) Master Data Preparation for initial setup
a) Scrape the data (this is covered in another document)
b) Data collection from Experience or any references
2) Data while usage of system
a) Customer/Vendor Data
b) Device Connected Data
c) Data from Govt. Bodies
d) Legal predefined dat
"""

initial_state = {
    'messages': [HumanMessage(role="user", content=query_al_serkal)],
    'query': query_al_serkal,
    'requirements': None,
    'objectives': None,
    'deliverables': None,
    'modules': None,
    'actions': None,
    'verification': None,
    'panels': None
}

for i in graph.stream(initial_state, config=RunnableConfig(recursion_limit=90)):
    print("-------")
