# import os
# OUTPUT_DIR = "scope_pipeline"
#
# def create_combined_markdown(root_dir):
#     combined_output_file = f"{root_dir}/combined_panels.md"
#     for interface in os.listdir(root_dir):
#         print(f"ITEM; {interface}")
#         item_path = os.path.join(root_dir, interface)
#         if os.path.isdir(item_path):
#             combined_md_lines = [f"# {interface}\n"]
#             print(f"CONTENT: {combined_md_lines}")
#
#             # Read description.md
#             description_path = os.path.join(item_path, "description.md")
#             print(f"DESCRIPTION PATH: {description_path}")
#             if os.path.exists(description_path):
#                 with open(description_path, 'r', encoding='utf-8') as f:
#                     combined_md_lines.append(f.read() + "\n")
#                     print(f"DESCRIPTION CONTENT: {combined_md_lines}")
#
#             # Read the module order from modules/modules
#             modules_dir = os.path.join(item_path, "modules")
#             modules_order_path = os.path.join(modules_dir, "modules.md")
#             if os.path.exists(modules_order_path):
#                 with open(modules_order_path, 'r+', encoding='utf-8') as fd:
#                     module_files = [line.strip() for line in fd if line.strip()]
#                 # Read each module in the specified order
#                 for module_file in module_files:
#                     module_path = os.path.join(modules_dir, f"{module_file}.md")
#                     if os.path.exists(module_path):
#                         with open(module_path, 'r', encoding='utf-8') as mf:
#                             combined_md_lines.append("\n\n")
#                             combined_md_lines.append(mf.read() + "\n")
#                     else:
#                         print(f"Warning: Module file '{module_file}' not found in {modules_dir}")
#
#             # Write to output markdown
#             output_path = os.path.join(item_path, f"{interface}.md")
#             with open(output_path, 'w', encoding='utf-8') as outf:
#                 outf.writelines(combined_md_lines)
#             with open(combined_output_file, 'a+') as cfile:
#                 cfile.writelines(combined_md_lines)
#                 cfile.write("\n\n\n")
#
#             print(f"Generated: {output_path}")
#
# def combined_file_data():
#     file_names = ["01_project_understanding.md", "02_key_objectives.md", "03_deliverables.md"]
#     content = []
#     for fname in sorted(os.listdir(OUTPUT_DIR)):
#         if fname in file_names:
#             content.append(open(os.path.join(OUTPUT_DIR, fname)).read())
#     create_combined_markdown(os.path.join(OUTPUT_DIR, "interfaces"))
#     panels_data = open(os.path.join(OUTPUT_DIR, "interfaces", "combined_panels.md")).read()
#     content += panels_data
#     open(os.path.join(OUTPUT_DIR, "all_content.md"), "w").writelines(content)
#
# combined_file_data()
import os

from langchain_community.callbacks import OpenAICallbackHandler
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

load_dotenv()
callback_handler = OpenAICallbackHandler()
llm = ChatOpenAI(model="gpt-4.1-nano", api_key=os.environ.get('OPENAI_API_KEY_INTERNAL_TOOLS'))
# llm_with_reasoning = ChatOpenAI(model="gpt-4.1-nano", api_key=os.environ.get('OPENAI_API_KEY_INTERNAL_TOOLS'), reasoning_effort="low")

def generate_token_usage_str(cb):
    return (f"Tokens Used: {cb.total_tokens}\n"
            f"Prompt Tokens: {cb.prompt_tokens}\n"
            f"Prompt Tokens Cached: {cb.prompt_tokens_cached}\n"
            f"Completion Tokens: {cb.completion_tokens}\n"
            f"Reasoning Tokens: {cb.reasoning_tokens}\n"
            f"Successful Requests: {cb.successful_requests}\n"
            f"Total Cost (USD): ${cb.total_cost}\n")
agent = create_react_agent(model=llm, tools=[])
response = agent.invoke({'messages': "what is 2+2"}, config={"callbacks": [callback_handler]})
token_data = generate_token_usage_str(callback_handler)
print(f"Token Data: {token_data}")
# , config={"callbacks": [callback_handler]}
